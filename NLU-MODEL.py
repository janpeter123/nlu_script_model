import json
import csv
from os.path import join, dirname
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "api_key_here"
url = "model_url_here"


authenticator = IAMAuthenticator(apikey)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(url)
print("Successfully connected with the NLU service")

#Put here the data that you want to use
#Necessary format  - text:"..." - labels:["label_1","label_2"]
training_data_filename = 'Data.json'


with open(join(dirname(__file__), './.', training_data_filename),'rb') as file:
    model = natural_language_understanding.create_classifications_model(
    language='pt',
    training_data=file, 
    training_data_content_type='application/json', 
    name='Mymodel', 
    model_version='1.0.1').get_result()
    print("Created a NLU Classifications model:")