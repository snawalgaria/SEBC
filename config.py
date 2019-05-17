class Config:

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

        self.database_name = database_name
        self.hash_table = hash_table
        self.anonymized_table = anonymized_table
        self.endpoint = endpoint
        self.region = region
        self.customerkey = customerkey
        self.key = key
        self.cosmos_account_name = cosmos_account_name
        self.scaleup_cosmos = scaleup_cosmos
        self.scaledown_cosmos = scaledown_cosmos

        # write configuration for hashtable
        self.hash_writeConfig = {
            "Endpoint": endpoint,
            "Masterkey": key,
            "Database": database_name,
            "Collection": hash_table,
            "Upsert": "true"
        }

        # read configuration for hashtable
        self.hash_readConfig = {
            "Endpoint": endpoint,
            "Masterkey": key,
            "Database": database_name,
            "Collection": hash_table,
            "preferredRegions": region,
            "SamplingRatio": "1.0",
            "schema_samplesize": "1000000",
            "query_pagesize": "2147483647",
            "query_custom": "SELECT * FROM c"
        }

        # write configuration for anonymization
        self.anonymization_writeConfig = {
            "Endpoint": endpoint,
            "Masterkey": key,
            "Database": database_name,
            "Collection": anonymized_table,
            "Upsert": "true"
        }

        # read configuration for anonymization
        self.anonymization_readConfig = {
            "Endpoint": endpoint,
            "Masterkey": key,
            "Database": database_name,
            "Collection": anonymized_table,
            "preferredRegions": region,
            "query_custom": "SELECT * FROM c"
        }

    def get_dev_config(self):
        """
        Set Dev Parameters of config object and return it
        :return:
        """
        return self

    def get_test_config(self):
        """
        Set Test Parameters of config object and return it
        :return:
        """
        return self

    def get_prod_config(self):
        """
        Set Prod Parameters of config object and return it
        :return:
        """
        return self

    def get_database_name(self):
        return self.database_name

    def get_hash_table(self):
        return self.hash_table

    def get_anonymized_table(self):
        return self.anonymized_table

    def get_endpoint(self):
        return self.endpoint

    def get_region(self):
        return self.region

    def get_customerkey(self):
        return self.customerkey

    def get_key(self):
        return self.key

    def get_cosmos_account(self):
        return self.cosmos_account_name

    def get_scaleup_cosmos(self):
        return self.scaleup_cosmos

    def get_scaledown_cosmos(self):
        return self.scaledown_cosmos

    def get_anonymize_readconfig(self):
        return self.anonymization_readConfig

    def get_anonymize_writeconfig(self):
        return self.anonymization_writeConfig

    def get_hash_readconfig(self):
        return self.hash_readConfig

    def get_hash_writeconfig(self):
        return self.hash_writeConfig
