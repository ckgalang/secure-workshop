from AtlasConnector import *

# GLOBAL VARIABLES
# Keys to authenticate to the Atlas Project
connection_string = "xxxxxxxxx"
public_key = 'xxxxxxxxx'
private_key = 'xxxxxxxxx'
projectId = 'xxxxxxxxx'

# Name of the cluster and list of the students
cluster_name = "xxxxxxxxx"
user_list = {
# Put the user list here
}

# main method
def main():
    ac = AtlasConnector(connection_string, projectId, public_key, private_key)
    ac.create_dbList(user_list, cluster_name)
    ac.create_userCollection(user_list)

if __name__ == "__main__":
    main()