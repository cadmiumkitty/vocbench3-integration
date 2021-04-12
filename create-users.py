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

        user_data = {
            'email': user['Username'],
            'password': user['Password'],
            'givenName': user['First Name'],
            'familyName': user['Last Name'],
            'customProperties': '{}'}
        create_user_response = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Users/registerUser?', data = user_data)
        print(create_user_response.status_code)

        enable_user_data = {
            'email': user['Username'],
            'enabled': 'true'}
        enable_user_response = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Users/enableUser?', data = enable_user_data)
        print(enable_user_response.status_code)
