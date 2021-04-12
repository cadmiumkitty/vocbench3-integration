import csv
import requests
import sys

api_username = sys.argv[1]
api_password = sys.argv[2]
host = sys.argv[3]
users_file_name = sys.argv[4]

session = requests.Session()

auth_data = {
    'email': api_username, 
    'password': api_password, 
    '_spring_security_remember_me': 'false'}
auth_response = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Auth/login?', data = auth_data)
print(auth_response.status_code)

with open(users_file_name) as users_file:
    users = csv.DictReader(users_file)
    for user in users:
        print(user)

        print(user['Project'])

        add_roles_to_user_data_projectmanager = {
            'projectName': user['Project'],
            'email': user['Username'],
            'roles': 'projectmanager'}
        add_roles_to_user_response_projectmanager = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Administration/addRolesToUser?', data = add_roles_to_user_data_projectmanager)
        print(add_roles_to_user_response_projectmanager.status_code)

        for project in ['SDG']:

            print(project)

            add_roles_to_user_data_lurker = {
                'projectName': project,
                'email': user['Username'],
                'roles': 'lurker'}
            add_roles_to_user_response_lurker = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Administration/addRolesToUser?', data = add_roles_to_user_data_lurker)
            print(add_roles_to_user_response_lurker.status_code)
