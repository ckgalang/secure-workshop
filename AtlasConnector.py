import requests, json
from requests.auth import HTTPDigestAuth

class AtlasConnector():

    def __init__(self, projectId: str, public_key: str, private_key: str) -> None:
        self.public_key = public_key
        self.private_key = private_key
        self.projectId = projectId

        self.base_url = "https://cloud.mongodb.com/api/atlas/v1.0"
        self.AUTHENTICATION = HTTPDigestAuth(public_key, private_key)


    def add_users_to_db_list(self, user_list: list, cluster_name: str) -> None:
        resource_path = "/groups/" + self.projectId + "/databaseUsers"
        REQUEST_URL = self.base_url + resource_path

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

            resp = requests.post(REQUEST_URL, auth=self.AUTHENTICATION, data=request_body, headers=headers)

            if resp.status_code == 201:
                print("------------------")
                print("CREATED user " + user)
                print("------------------")

    def delete_users(self, user_list: list) -> None:
        resource_path = "/groups/" + self.projectId + "/databaseUsers/admin/"
        REQUEST_URL = self.base_url + resource_path

        for user in user_list:

            resp = requests.delete(REQUEST_URL + user, auth=self.AUTHENTICATION)

            if resp.status_code == 204:
                print("------------------")
                print("DELETED user " + user)
                print("------------------")