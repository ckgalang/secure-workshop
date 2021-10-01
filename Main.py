from AtlasConnector import *
from MongoDBConnector import *

# GLOBAL VARIABLES
# Keys to authenticate to the Atlas Project
# Project Permissions = "Project Owner"
connection_string = "mongodb+srv://admin:admin@cluster0.qx9qh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# Project Permissions = "Project Owner"
public_key = 'bdanaqjk'
private_key = 'b2fa0d4b-55be-458b-a4ab-48aab0e7a671'
projectId = '5f281a8bc4ccb250e2faf829'

# Name of the cluster and list of the students
cluster_name = "Cluster0"
user_list = {
# Put the user list here
# Usernames can only comprise of [A-Z][a-z][0-9]
    "test",
    "test2"
}

database_dict = {
    "sample_analytics": [ # DATABASE
        "customers",      # COLLECTION
        "transactions"
    ],
    "sample_mflix": [
        "movies",
        "comments",
        "theaters"
    ]
}

def create_class(atlas_connector, mongodb_connector):
    atlas_connector.add_users_to_db_list(user_list, cluster_name)
    mongodb_connector.create_user_collections(user_list, database_dict)

def delete_class(atlas_connector, mongodb_connector):
    atlas_connector.delete_users(user_list)
    mongodb_connector.delete_user_collections(user_list)

# main method
def main():
    atlas_connector = AtlasConnector(projectId, public_key, private_key)
    mongodb_connector = MongoDBConnector(connection_string)
    # create_class(atlas_connector, mongodb_connector)
    delete_class(atlas_connector, mongodb_connector)

if __name__ == "__main__":
    main()