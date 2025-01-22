from dotenv import load_dotenv
load_dotenv()

import requests
import os
from  program_settings import verbose

class SpokenDataDB:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def post_document(self, document):
        if verbose: print("posting document to db: ", document)
        response = requests.post(self.url+"/spokenData/document", json=document, headers=self.headers)
        
        return response.json()
    
    def search_document(self, query):
        response = requests.post(self.url+"/spokenData/search", json=query, headers=self.headers)
        
        return response.json()

class RemindersDB:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post_reminder(self, reminder):
        response = requests.post(self.url+"/reminders", json=reminder, headers=self.headers)
        
        return response.json()
    
    def update_reminder(self, id, update_fields):
        response = requests.put(self.url+"/reminders/"+ str(id), json=update_fields, headers=self.headers)
        
        return response.json()
    
    def delete_reminder(self, id):
        response = requests.delete(self.url+"/reminders/" + str(id), headers=self.headers)
        
        return response.json()
    
    def get_all_reminders(self):
        response = requests.get(self.url+"/reminders", headers=self.headers)
        
        return response.json()
    
    def get_reminder(self, id):
        response = requests.get(self.url+"/reminders/" + str(id), headers=self.headers)
        
        return response.json()

class APIHelper:
    def __init__(self, url, api_key):
        self.url = url
        self.api_url= url + "/api"
        self.api_key = api_key

        self.headers = {'Authorization': api_key}

        self.spoken_data_db = SpokenDataDB(url=self.api_url, headers=self.headers)
        self.reminders_db = RemindersDB(url=self.api_url, headers=self.headers)

api_helper = APIHelper(url=os.getenv("INTERNAL_API_URL"), api_key=os.getenv("INTERNAL_API_KEY"))