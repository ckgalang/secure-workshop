import pymongo

class MongoDBConnector:

    def __init__(self, connection_string):
        self.client = pymongo.MongoClient(connection_string)

    def create_user_collections(self, user_list: list, database_dict: dict) -> None:
        for user in user_list:
            for key, value in database_dict.items():
                database_name = key
                collection_list = value
                database = self.client[database_name]
                for collection_name in collection_list:
                    collection = database[collection_name]
                    aggregation = [
                        {
                            "$out": {
                                "db": user,
                                "coll": collection_name
                            }
                        }
                    ]
                    collection.aggregate(aggregation)

            print("------------------")
            print("CREATED collection: " + user)
            print("------------------")

    def delete_user_collections(self, user_list: list) -> None:
        for user in user_list:
            self.client.drop_database(user)

            print("------------------")
            print("DELETED collection: " + user)
            print("------------------")



