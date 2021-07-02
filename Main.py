from AtlasConnector import *

# GLOBAL VARIABLES
# Keys to authenticate to the Atlas Project
connection_string = "mongodb+srv://admin:admin@sandbox.qx9qh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
public_key = 'abntiyiw'
private_key = 'cf76369f-de44-4d1b-be9a-ec8d4bf8436d'
projectId = '5f281a8bc4ccb250e2faf829'

# Name of the cluster and list of the students
cluster_name = "sandbox"
user_list = {
    "sample_student"
}

# main method
def main():
    ac = AtlasConnector(connection_string, projectId, public_key, private_key)
    ac.create_dbList(user_list, cluster_name)
    ac.create_userCollection(user_list)

if __name__ == "__main__":
    main()