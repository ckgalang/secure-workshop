import requests, json, pymongo
from requests.auth import HTTPDigestAuth

class AtlasConnector():

    def __init__(self, connection_string, projectId, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.projectId = projectId
        self.client = pymongo.MongoClient(connection_string)

        self.base_url = "https://cloud.mongodb.com/api/atlas/v1.0"
        self.resource_path = "/groups/" + projectId + "/databaseUsers"

        self.REQUEST_URL = self.base_url + self.resource_path
        self.AUTHENTICATION = HTTPDigestAuth(public_key, private_key)


    def create_dbList(self, user_list, cluster_name):
        for user in user_list:

            request_body = json.dumps({
                "databaseName": "admin",
                "username": user,
                "password": user,
                "roles": [{
                "databaseName": user,
                "roleName": "readWrite"
                }],
                "scopes": [{
                "name": cluster_name,
                "type": "CLUSTER"
                }],
                "groupId": self.projectId
            })

            headers = {'Content-Type': 'application/json'}

            r = requests.post(self.REQUEST_URL, auth=self.AUTHENTICATION, data=request_body, headers=headers)

            print("------------------")
            print("Just added " + user)
            print("------------------")

        print("Success: create_dbList()")

    def create_userCollection(self, user_list):
        for user in user_list:
            ############################################
            # This block pushes the data from sample_analytics.customers and
            # sample_analytics.transactions collection into 2 collections for
            # each user in the user_list
            sample_analytics = self.client["sample_analytics"]

            customers = sample_analytics["customers"]
            customers_aggregation = [
                {
                    "$out": {
                        "db": user,
                        "coll": "customers"
                    }
                }
            ]
            customers.aggregate(customers_aggregation)

            transactions = sample_analytics["transactions"]
            transactions_aggregation = [
                {
                    "$out": {
                        "db": user,
                        "coll": "transactions"
                    }
                }
            ]
            transactions.aggregate(transactions_aggregation)
            ############################################
            # This block pushes the data from sample_analytics.customers and
            # sample_analytics.transactions collection into 2 collections for
            # each user in the user_list
            sample_mflix = self.client["sample_mflix"]

            movies = sample_mflix["movies"]
            movies_aggregation = [
                {
                    "$out": {
                        "db": user,
                        "coll": "movies"
                    }
                }
            ]
            movies.aggregate(movies_aggregation)

            comments = sample_mflix["comments"]
            comments_aggregation = [
                {
                    "$out": {
                        "db": user,
                        "coll": "comments"
                    }
                }
            ]
            comments.aggregate(comments_aggregation)
            ############################################

        print("Success: create_userCollection()")


