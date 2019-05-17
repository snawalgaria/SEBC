import hmac
import hashlib
import base64
import urllib.parse
import requests
import json
from datetime import datetime


class CosmosDb:

    @staticmethod
    def constructAuthHeader(key, verb, resourceType, resourceLink):
        verb = verb.upper()

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
            "x-ms-version": "2017-02-22"
        }
        return headers

    def listOffers(self, key, cosmos_account_name):
        headers = self.constructAuthHeader(key, "GET", "offers", "")

        res = requests.get("https://" + cosmos_account_name +
                           ".documents.azure.com/offers", headers=headers)
        if res.status_code == 200:
            offers = json.loads(res.text)
            return offers["Offers"]
        else:
            print("Error: " + res.text)
            exit(1)

    def getOffer(self, rid, key, cosmos_account_name):
        headers = self.constructAuthHeader(
            key, "GET", "offers", rid.lower())

        res = requests.get("https://" + cosmos_account_name +
                           ".documents.azure.com/offers/" + rid, headers=headers)
        if res.status_code == 200:
            offer = json.loads(res.text)
            return offer
        else:
            print("Error: " + res.text)
            exit(1)

    def updateThroughputOnOffer(self, rid, throughput, key, cosmos_account_name):
        if (throughput % 100) != 0:
            print("Throughput must be multiple of 100")
            exit(1)

        headers = self.constructAuthHeader(key, "PUT", "offers", rid.lower())

        offer = self.getOffer(rid, key, cosmos_account_name)

        offer["content"]["offerThroughput"] = throughput

        res = requests.put("https://" + cosmos_account_name + ".documents.azure.com/offers/" + rid, headers=headers,
                           json=offer)
        if res.status_code == 200:
            print("Throughput successfully updated to " + str(throughput))
        else:
            print("Error: " + res.text)
            exit(1)

    def updateCollectionThroughputWithRID(self, collectionRid, throughput, key, cosmos_account_name):
        offers = self.listOffers(key, cosmos_account_name)
        # search for offer with collectionRid
        offerToUpdate = None
        for offer in offers:
            if offer["resource"] == collectionRid:
                offerToUpdate = offer

        if offerToUpdate is not None:
            orid = offerToUpdate["_rid"]
            self.updateThroughputOnOffer(
                orid, throughput, key, cosmos_account_name)
        else:
            print("No collection with that RID found!")

    def getCollection(self, database_name, collectionName, key, cosmos_account_name):
        resourceLink = "dbs/" + database_name + "/colls/" + collectionName
        headers = self.constructAuthHeader(key, "GET", "colls", resourceLink)

        res = requests.get("https://" + cosmos_account_name +
                           ".documents.azure.com/" + resourceLink, headers=headers)
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            print("Error: " + res.text)
            exit(1)

    def updateCollectionThroughput(self, database_name, collectionName, throughput, key, cosmos_account_name):
        collection = self.getCollection(
            database_name, collectionName, key, cosmos_account_name)
        self.updateCollectionThroughputWithRID(
            collection["_self"], throughput, key, cosmos_account_name)
