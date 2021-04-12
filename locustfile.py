import time
import random
import csv
from locust import HttpUser, task, between, events

class QuickstartUser(HttpUser):

    email = ''
    project_name = 'SDG'


    # Retrieve list of projects
    @task(1)
    def step_01_retrieve_projects(self):

        post_data_1 = {
            'bagOf': 'category',
            'userDependent': 'true',
            'onlyOpen': 'true'
        }
        self.client.post('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Projects/retrieveProjects', data = post_data_1)

    # Retrieve individual project details for the UI
    @task(1)
    def step_02_access_project(self):

        get_params_1 = {
            'projectName': self.project_name, 
            'ctx_project': self.project_name,
            'email': self.email
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Administration/getProjectUserBinding', params = get_params_1)

        get_params_2 = {
            'projectName': self.project_name, 
            'ctx_project': self.project_name,
            'properties': 'active_schemes,active_lexicon,show_flags,show_instances_number,project_theme,search_languages,search_restrict_lang,search_include_locales,search_use_autocomplete,class_tree_filter,class_tree_root,instance_list_visualization,instance_list_safe_to_go_limit,concept_tree_base_broader_prop,concept_tree_broader_props,concept_tree_narrower_props,concept_tree_include_subprops,concept_tree_sync_inverse,concept_tree_visualization,concept_tree_multischeme_mode,concept_tree_safe_to_go_limit,lex_entry_list_visualization,lex_entry_list_index_lenght,lex_entry_list_safe_to_go_limit,editing_language,filter_value_languages,rv_partition_filter,res_view_default_concept_type,res_view_default_lexentry_type,graph_partition_filter,hide_literal_graph_nodes,notifications_status'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/PreferencesSettings/getPUSettings', params = get_params_2)

        get_params_3 = {
            'projectName': self.project_name, 
            'ctx_project': self.project_name,
            'pluginID': 'it.uniroma2.art.semanticturkey.extension.extpts.rendering.RenderingEngine',
            'properties': 'languages'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/PreferencesSettings/getPUSettings', params = get_params_3)

        get_params_4 = {
            'projectName': self.project_name, 
            'ctx_project': self.project_name,
            'properties': 'languages,label_clash_mode'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/PreferencesSettings/getProjectSettings', params = get_params_4)

        get_params_5 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Collaboration/getCollaborationSystemStatus', params = get_params_5)

        get_params_6 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Users/listUserCapabilities', params = get_params_6)

        get_params_7 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Metadata/getNamespaceMappings', params = get_params_7)

        get_params_8 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Datatypes/getDatatypeRestrictions', params = get_params_8)


    # Retrieve details of sample project
    @task(1)
    def step_03_get_data(self):

        get_params_9 = {
            'ctx_project': self.project_name,
            'classList': '<http://www.w3.org/2002/07/owl#Thing>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Classes/getClassesInfo', params = get_params_9)

        get_params_10 = {
            'ctx_project': self.project_name,
            'schemeFilter': 'or',
            'broaderProps': '',
            'narrowerProps': '',
            'includeSubProperties': 'true',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/countTopConcepts', params = get_params_10)

        get_params_11 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/getAllSchemes', params = get_params_11)

        get_params_12 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Properties/getTopProperties', params = get_params_12)

        get_params_13 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Datatypes/getDeclaredDatatypes', params = get_params_13)

        get_params_14 = {
            'ctx_project': self.project_name,
            'schemeFilter': 'or',
            'broaderProps': '',
            'narrowerProps': '',
            'includeSubProperties': 'true',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/getTopConcepts', params = get_params_14)

        get_params_15 = {
            'ctx_project': self.project_name
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/getRootCollections', params = get_params_15)

        get_params_16 = {
            'ctx_project': self.project_name,
            'superClass': '<http://www.w3.org/2002/07/owl#Thing>',
            'numInst': 'false'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Classes/getSubClasses', params = get_params_16)

        time.sleep(2)


    # Get narrower
    @task(1)
    def step_04_get_narrower(self):

        get_params_17 = {
            'ctx_project': self.project_name,
            'schemeFilter': 'or',
            'broaderProps': '',
            'narrowerProps': '',
            'includeSubProperties': 'true',
            'concept': '<http://metadata.un.org/sdg/5>',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/getNarrowerConcepts', params = get_params_17)

        get_params_18 = {
            'ctx_project': self.project_name,
            'schemeFilter': 'or',
            'broaderProps': '',
            'narrowerProps': '',
            'includeSubProperties': 'true',
            'concept': '<http://metadata.un.org/sdg/5.c>',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/SKOS/getNarrowerConcepts', params = get_params_18)

        get_params_19 = {
            'ctx_project': self.project_name,
            'resource': '<http://metadata.un.org/sdg/5.c>',
            'includeInferred': 'false'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/ResourceView/getResourceView', params = get_params_19)

        post_params_2 = {
            'ctx_project': self.project_name,
        }
        post_data_2 = {
            'resources': '["<http://purl.unep.org/sdg/SDGIO_00020078>"]'
        }
        self.client.post('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Resources/getResourcesPosition', params = post_params_2, data = post_data_2)


    # Search
    @task(1)
    def step_05_search(self):

        get_params_21 = {
            'ctx_project': self.project_name,
            'searchString': 'climate',
            'rolesArray': 'concept',
            'useLocalName': 'true',
            'searchMode': 'startsWith',
            'schemeFilter': 'or',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Search/searchStringList', params = get_params_21)

        get_params_22 = {
            'ctx_project': self.project_name,
            'searchString': 'Climate action',
            'rolesArray': 'concept',
            'useLocalName': 'true',
            'useURI': 'false',
            'useNotes': 'false',
            'searchMode': 'startsWith',
            'schemeFilter': 'or',
            'schemes': '<http://metadata.un.org/sdg>'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Search/searchResource', params = get_params_22)

        get_params_23 = {
            'ctx_project': self.project_name,
            'role': 'concept',
            'resourceURI': '<http://metadata.un.org/sdg/13>',
            'schemesIRI': '<http://metadata.un.org/sdg>',
            'schemeFilter': 'or',
            'broaderProps': '',
            'narrowerProps': '',
            'includeSubProperties': 'true'
        }
        self.client.get('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Search/getPathFromRoot', params = get_params_23)


    # On start pick a random user credentials from the list
    def on_start(self):

        # Pre-read usernames from the same file as used for user creation, etc.
        with open('users.csv') as users_file:

            users = list(csv.DictReader(users_file))
            user = random.choice(users)

            self.email = user['Username']
            self.password = user['Password']

            auth_data = {
                'email': self.email,
                'password': self.password, 
                '_spring_security_remember_me': 'false'}

            with self.client.post('/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Auth/login?', data = auth_data, catch_response=True) as response:
                print(f'Username: {self.email}, Password: {self.password}, Status: {response.status_code}')


    # Simple scenario of wait times averaging 5 seconds between tasks
    wait_time = between(2.5, 7.5)