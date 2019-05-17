# encryption libraries
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import ast
import hmac
import hashlib
import base64
import urllib.parse
import requests

import uuid
import json
from datetime import datetime
from random import randint

# importing config and CosmosDb
from config import Config
from cosmosDb import CosmosDb

# spark libraries
from pyspark.sql.functions import col, upper, udf

customerkey = "dl-stronghold-encryption-private-key"
pkey = dbutils.secrets.get(scope="keyvault", key=customerkey)
pkey = pkey.replace("\\n", "\n")


def decrypt(s):
    """
    Function used to decrypt the dataframe columns which needs to be read
    :param s: dataframe columns that needs to be decrypted
    :return: the decrypted columns
    """
    if s is None:
        return None
    else:
        # try:
        enc_value = ast.literal_eval(s)
        private_key = serialization.load_pem_private_key(
            pkey.encode('utf-8'),
            password=None,
            backend=default_backend()
        )

        dec = private_key.decrypt(
            enc_value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return dec.decode()


class Vault:

    def __init__(self, database_name, hash_table, anonymized_table, endpoint, region, customerkey, key,
                 cosmos_account_name, scaleup_cosmos, scaledown_cosmos):
        """
        :param database_name:  name of the database in cosmosDB
        :param hash_table: name of the cosmosDB tabl/container with the hashe
        :param anonymized_table: name of the cosmosDB tabl/container with the anony
        :param endpoint: endpoint of the cosmosDB service
        :param region:  region of the cosmosDB service
        :param customerkey: service name of he key usedd for encryption
        :param key:
        :param cosmos_account_name:
        :param scaleup_cosmos:
        :param scaledown_cosmos:
        """

        self.config = Config(database_name, hash_table, anonymized_table, endpoint, region,
                             customerkey, key, cosmos_account_name, scaleup_cosmos, scaledown_cosmos)
        self.cosmosdb = CosmosDb()
        self.key = dbutils.secrets.get(
            scope='keyvault', key='dl-stronghold-encrytion-public-key')
        self.key = self.key.replace("\\n", "\n")

    def get_config(self):
        """
        :return: returns the config object
        """
        return self.config

    def get_cosmos_db(self):
        """
        :return:Returns the cosmos db object
        """
        return self.cosmosdb

    def deleteDocFromCosmos(self, id, database, collection, partion_key, key):
        """
        Method to delete the records from cosmos db
        @passi
        :param partion_key:
        :param id:
        :param database: name of the database in cosmos db
        :param collection:
        :param key:
        :return: the status whether the deletion was successful
        """

        verb = "DELETE"
        resourceType = "docs"
        resourceLink = "dbs/{}/colls/{}/docs/{}".format(
            database, collection, id)
        date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:00 GMT')

        stringToSign = verb.lower() + '\n' + resourceType.lower() + '\n' + \
                       resourceLink + '\n' + date.lower() + '\n' + '' + '\n'

        payload = bytes(stringToSign, 'utf-8')
        key = base64.b64decode(key.encode('utf-8'))

        signature = base64.b64encode(
            hmac.new(key, msg=payload, digestmod=hashlib.sha256).digest()).decode()

        authStr = urllib.parse.quote(
            'type=master&ver=1.0&sig={}'.format(signature))

        headers = {
            'Authorization': authStr,
            "x-ms-date": date,
            "x-ms-version": "2017-02-22",
            "x-ms-documentdb-partitionkey": "[" + partion_key + "]"
        }

        res = requests.delete(
            "https://" + self.config.get_cosmos_account() + ".documents.azure.com/dbs/{}/colls/{}/docs/{}".format(
                database,
                collection, id),
            headers=headers)
        if res.status_code == 204:
            print("Document has been deleted successfully")
            ok = True
        else:
            print("Error while deleting document: {}".format(
                json.loads(res.text)["message"]))
            ok = False

        return ok

    def readDataFromCosmosDB(self):
        """
        Reading data from cosmos db. First the data is decrypted calling the decrypt udf, The decrypted data is read
        from cosmosDb

        :return: the dataframe to be read is returned
        """
        self.cosmosdb.updateCollectionThroughput(
            self.config.get_database_name(), self.config.get_hash_table(), self.config.get_scaleup_cosmos(),
            self.config.get_key(),
            self.config.get_cosmos_account())

        # read all the data from cosmos DB with encrypted fields and store in a data frame
        df = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(
            **self.config.get_hash_readconfig()).load()

        # iterate over the dataframe and decrypt and replace all fields except the cosmos db system fields strating
        # with "_" and the key --> id field since its hashed not encrypted and also not the partition field
        df = df.repartition(160).cache()
        dec_udf = udf(decrypt)

        for columns in df.columns:
            if columns.startswith('_') or columns.startswith('id') or columns.startswith('partition'):
                print('not to be encrypted field: ' + columns)
            else:
                print('to be encrypted field: ' + columns)
                df = df.withColumn(columns, dec_udf(df[columns]))
        print("succesfully decrypted the fields in spark df data frame")

        # Register the DataFrame as a SQL temporary view
        df = df.repartition(1).cache()
        # df.persist(StorageLevel.DISK_ONLY_2)
        df.createOrReplaceTempView("customer")
        spark.sql("CACHE TABLE customer").collect()

        print("succesfully read " + str(df.count()) +
              " records from CosmosDB and saved in spark df data frame")
        self.cosmosdb.updateCollectionThroughput(
            self.config.get_database_name(), self.config.get_hash_table(), self.config.get_scaledown_cosmos(),
            self.config.get_key(),
            self.config.get_cosmos_account())

        return df

    # decryption function to decrypt a string with the respective key

    # except ValueError:
    #  return s

    def encrypt(self, s):
        """
        @passi
        Function to encrypt the dataframe columns
        :param s: Dataframe columns that will be encrypted
        :return: encrypted dataframe
        """
        public_key = serialization.load_pem_public_key(
            self.key.encode('utf-8'),
            backend=default_backend())

        encrypted = public_key.encrypt(
            s.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        # enc = bytes(encrypted).decode("utf-8")
        return str(encrypted)

    # sha256 for BPID Key
    @staticmethod
    def encrypt_value(mobno):  # encrypt values
        sha_value = hashlib.sha256(str(mobno).encode()).hexdigest()
        return sha_value


def unit_test1():
    """
    Test deletion Unittest 1: find the id over SQL with the unecrypted value lastname4 and delete
    :return:
    """
    global __searchtestSQL, sqlDF, id, partion_key, reason, d, df
    __searchtestSQL = "SELECT id,partition FROM customer where lastname = 'lastName4'"
    sqlDF = spark.sql(__searchtestSQL)
    id = str(sqlDF.collect()[0][0])
    partion_key = str(sqlDF.collect()[0][1])
    sqlDF.show(sqlDF.count(), False)
    reason = "Test deletion Unittest 1: find the id over SQL with the unecrypted value lastname4 and delete"
    d = [{'id': id, 'date': _date, 'user': _user, 'reason': reason}]
    df = sqlContext.createDataFrame(d)
    df.printSchema()
    df.show(df.count(), False)


def unit_test2():
    """
    Test deletion Unittest 2: find the id over SQL with the unecrypted value lastname5 and email5 and delete"
    :return:
    """
    global __searchtestSQL, sqlDF, id, partion_key, reason, d, df
    __searchtestSQL = "SELECT id,partition FROM customer where lastname = 'lastName5' and email = 'email5'"
    sqlDF = spark.sql(__searchtestSQL)
    sqlDF.show()
    id = str(sqlDF.collect()[0][0])
    partion_key = str(sqlDF.collect()[0][1])
    reason = "Test deletion Unittest 2: find the id over SQL with the unecrypted value lastname5 and email5 and delete"
    d = [{'id': id, 'date': _date, 'user': _user, 'reason': reason}]
    df = sqlContext.createDataFrame(d)
    df.printSchema()
    df.show(df.count(), False)


def unit_test3():
    """
    Test deletion Unittest 3: find the id over SQL with the unecrypted value lastname6 or email6 and delete
    :return:
    """

    global __searchtestSQL, sqlDF, id, partion_key, reason, d, df
    __searchtestSQL = "SELECT id,partition FROM customer where lastname = 'lastName6' or email = 'email6'"
    sqlDF = spark.sql(__searchtestSQL)
    sqlDF.show()
    id = str(sqlDF.collect()[0][0])
    partion_key = str(sqlDF.collect()[0][1])
    reason = "Test deletion Unittest 3: find the id over SQL with the unecrypted value lastname6 or email6 and delete"
    d = [{'id': id, 'date': _date, 'user': _user, 'reason': reason}]
    df = sqlContext.createDataFrame(d)
    df.printSchema()
    df.show(df.count(), False)


def unit_test4():
    """
    Test deletion Unittest 4: find the SAME id over SQL with the unecrypted value lastname6 or email6 and " \
             "delete again
    :return:
    """
    global __searchtestSQL, sqlDF, id, partion_key, reason, d, df
    __searchtestSQL = "SELECT id,partition FROM customer where lastname = 'lastName6' or email = 'email6'"
    sqlDF = spark.sql(__searchtestSQL)
    sqlDF.show()
    id = "ed25ae3a72e066d8e8e09d1d428fa165926608fc195eca8471148290b9611eac"
    partion_key = "1"
    reason = "Test deletion Unittest 4: find the SAME id over SQL with the unecrypted value lastname6 or email6 and " \
             "delete again"
    d = [{'id': id, 'date': _date, 'user': _user, 'reason': reason}]
    df = sqlContext.createDataFrame(d)
    df.printSchema()
    df.show(df.count(), False)


if __name__ == "__main__":
    """
    This is the starting point of execution. The Vault object is created here
    """
    """
    database_name = input("Enter Database Name")
    hash_table = input("Enter Hash Table")
    anonymized_table = input("Enter anonymized table name")
    endpoint = input("Enter endpoint name")
    region = input("Enter region name")
    customerkey = input("Enter customer key")
    scaleup_cosmos = input("Enter cosmos scale up value")
    scaledown_cosmos = input("Enter cosmos scale down value")
    """

    database_name = "stronghold"  # name of the database in cosmosDB
    hash_table = "hashingP"  # name of the cosmosDB tabl/container with the hashed values
    anonymized_table = "anonymized"  # name of the cosmosDB tabl/container with the anonymized contacts
    endpoint = "https://dev-dl-cosmosacc-ne.documents.azure.com:443/"  # endpoint of the cosmosDB service
    region = "North Europe;West Europe"  # region of the cosmosDB service
    customerkey = "dl-stronghold-encryption-private-key"
    scaleup_cosmos = 4000
    scaledown_cosmos = 500

    key = dbutils.secrets.get(scope="cosmosdb", key="primarykey")
    cosmos_account_name = "dev-dl-cosmosacc-ne"
    _date = datetime.utcnow().strftime('%Y-%m-%d')
    # _user=str(dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().apply('user'))
    _user = "p.grippo"

    vault = Vault(database_name, hash_table, anonymized_table, endpoint, region,
                  customerkey, key, cosmos_account_name, scaleup_cosmos, scaledown_cosmos)

    _generate_test_records = 500000
    dec_udf = udf(decrypt)
    enc_udf = udf(vault.encrypt)

    try:
        df = vault.readDataFromCosmosDB()
        # variable who decalres this cell has been executed and is mandatory
        check = "environment is ready"
    except NameError:
        print("An error occured please contact operation")
    finally:
        vault.cosmosdb.updateCollectionThroughput(
            database_name, hash_table, scaledown_cosmos, key, cosmos_account_name)

    try:
        print(check)
    except NameError:
        print("You need to execute the previous cell and set all variables")

    df.printSchema()

    id = '8163ed97cc4f24075f461597cf85493d4df3a22fb2547e3846766f6931d81b5e'
    partion_key = "5"
    reason = "Test deletion showcase Skype Meeting"

    _anoy_d = [{'id': id, 'date': _date, 'user': _user, 'reason': reason}]

    df_anoy = sqlContext.createDataFrame(_anoy_d)
    df_anoy.printSchema()
    display(df_anoy)

    if (vault.deleteDocFromCosmos(id, database_name, hash_table, partion_key,
                                  dbutils.secrets.get(scope="cosmosdb", key="primarykey"))):
        df_anoy.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(
            **vault.config.get_anonymize_writeconfig()).save()
        print('deleted id: ' + id +
              ' has been registered in the lkp table: ' + anonymized_table)
    else:
        print('deleted id: ' + id +
              ' has NOT been registered in the lkp table: ' + anonymized_table)

    documents = []

    for i in range(0, _generate_test_records):
        document = {'BPID': str(uuid.uuid4()), 'partition': randint(0, 21)}
        document['id'] = vault.encrypt_value(document['BPID'].encode('utf-8'))
        document['firstName'] = "firstName" + str(i)
        document['lastName'] = "lastName" + str(i)
        document['email2'] = "email" + str(i)
        document['mobilenumber'] = "00000000000" + str(i)
        document['timestamp'] = str(datetime.utcnow())
        document['date'] = str(datetime.utcnow())
        document['address'] = "Somestreet {}, 0000{} SomeContry".format(
            str(i), str(i))
        documents.append(document)
    json_data = json.dumps(documents)
    df = spark.read.json(sc.parallelize([json_data]))

    for columns in df.columns:
        if (columns == "id" or columns == "partition"):
            print(columns)
        else:
            df = df.withColumn(columns, enc_udf(df[columns]))

    df_hash = df.repartition(32)

    vault.cosmosdb.updateCollectionThroughput(
        database_name, hash_table, 20000, key, cosmos_account_name)

    df_hash.write.format("com.microsoft.azure.cosmosdb.spark").mode(
        'append').options(**vault.config.get_hash_writeconfig()).save()

    print("created " + str(_generate_test_records) +
          " test records in the test table: " + hash_table)

    vault.cosmosdb.updateCollectionThroughput(
        database_name, hash_table, scaledown_cosmos, key, cosmos_account_name)

    unit_test1()

    if (vault.deleteDocFromCosmos(id, database_name, hash_table, partion_key,
                                  dbutils.secrets.get(scope="cosmosdb", key="primarykey"))):
        df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(
            **vault.config.get_anonymize_writeconfig()).save()
        print('deleted id: ' + id +
              ' has been registered in the lkp table: ' + anonymized_table)
        # read all the data from cosmos DB from the the anonoymzed LKP table and check if the deletion id has been
        # registered
        DFcheck = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(
            **vault.config.get_anonymize_readconfig()).load()
        DFcheck.filter(DFcheck['id'] == id).show()
    else:
        print('deleted id: ' + id +
              ' has NOT been registered in the lkp table: ' + anonymized_table)

    # In[11]:

    unit_test2()

    if (vault.deleteDocFromCosmos(id, database_name, hash_table, partion_key,
                                  dbutils.secrets.get(scope="cosmosdb", key="primarykey"))):
        df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(
            **vault.config.get_anonymize_writeconfig()).save()
        print('deleted id: ' + id +
              ' has been registered in the lkp table: ' + anonymized_table)
        # read all the data from cosmos DB from the the anonoymzed LKP table and check if the deletion id has been
        # registered
        DFcheck = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(
            **vault.config.get_anonymize_readconfig()).load()
        DFcheck.filter(DFcheck['id'] == id).show()
    else:
        print('deleted id: ' + id +
              ' has NOT been registered in the lkp table: ' + anonymized_table)

    # In[12]:

    unit_test3()

    if (vault.deleteDocFromCosmos(id, database_name, hash_table, partion_key,
                                  dbutils.secrets.get(scope="cosmosdb", key="primarykey"))):
        df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(
            **vault.config.get_anonymize_writeConfig()).save()
        print('deleted id: ' + id +
              ' has been registered in the lkp table: ' + anonymized_table)
        # read all the data from cosmos DB from the the anonoymzed LKP table and check if the deletion id has been
        # registered
        DFcheck = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(
            **vault.config.get_anonymize_readconfig()).load()
        DFcheck.filter(DFcheck['id'] == id).show()
    else:
        print('deleted id: ' + id +
              ' has NOT been registered in the lkp table: ' + anonymized_table)

    # In[13]:

    unit_test4()

    if (vault.deleteDocFromCosmos(id, database_name, hash_table, partion_key,
                                  dbutils.secrets.get(scope="cosmosdb", key="primarykey"))):
        df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(
            **vault.config.get_anonymize_writeconfig()).save()
        print('deleted id: ' + id +
              ' has been registered in the lkp table: ' + anonymized_table)
    else:
        print('deleted id: ' + id +
              ' has NOT been registered in the lkp table: ' + anonymized_table)

    DFcheck = spark.read.format("com.microsoft.azure.cosmosdb.spark").options(
        **vault.config.get_anonymize_readconfig()).load()
    DFcheck.filter(DFcheck['id'] == id).show(DFcheck.count(), False)
