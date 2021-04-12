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

        project_data = {
            'consumer': 'SYSTEM',
            'projectName': user['Project'],
            'baseURI': user['Project URI'],
            'model': '<http://www.w3.org/2004/02/skos/core>',
            'lexicalizationModel': '<http://www.w3.org/2004/02/skos/core>',
            'historyEnabled': 'false',
            'validationEnabled': 'false',
            'blacklistingEnabled': 'false',
            'repositoryAccess': '{"@type":"CreateRemote","serverURL":"http://rdf4j:8080/rdf4j-server","username":null,"password":null}',
            'coreRepoID': user['Project'] + '_core',
            'supportRepoID': user['Project'] + '_support',
            'coreRepoSailConfigurerSpecification': '{"factoryId":"it.uniroma2.art.semanticturkey.extension.impl.repositoryimplconfigurer.predefined.PredefinedRepositoryConfigurer","configType":"it.uniroma2.art.semanticturkey.extension.impl.repositoryimplconfigurer.predefined.RDF4JPersistentInMemorySailConfiguration","configuration":{"syncDelay":1000,"directTypeInference":false,"inferencer":"none"}}',
            'shaclEnabled': 'false',
            'trivialInferenceEnabled': 'false',
            'openAtStartup': 'true',
            'globallyAccessible': 'true'}
        create_project_response = session.post(f'{host}/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Projects/createProject?', data = project_data)
        print(create_project_response.status_code)
