import pyrebase
import os
from pprint import pprint as pp
import json

firebaseConfig = {
  "apiKey": "GET FROM FIREBASE",
  "authDomain": "GET FROM FIREBASE",
  "databaseURL": "GET FROM FIREBASE",
  "projectId": "GET FROM FIREBASE",
  "storageBucket": "GET FROM FIREBASE",
  "messagingSenderId": "GET FROM FIREBASE",
  "appId": "GET FROM FIREBASE"
}

def get_jsonfiles(file_path = 'C:/Users/drago/scrapyprojects/news/'):
    all_files = os.listdir(file_path) # get all files in directory
    json_files = [file for file in all_files if file[-5:] == '.json'] #get only json files
    return json_files

def upload_to_firebase():
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    for file in get_jsonfiles(): #loops through each json file in current directory
        f = open(file)
        data = json.load(f)
        count = 0
        for key, value in data.items(): #Key is the page name, value is the index of title/link object

            db.child(file.replace('.json','')).child(key).set(value)
            count += 1

upload_to_firebase()
