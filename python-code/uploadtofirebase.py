import pyrebase
import os
from pprint import pprint as pp
import json

firebaseConfig = {
  "apiKey": "AIzaSyDhQBIppaOuzhTNuA1Jf3TZrN7w0E_-vG4",
  "authDomain": "news-firebase-8a2f0.firebaseapp.com",
  "databaseURL": "https://news-firebase-8a2f0-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "news-firebase-8a2f0",
  "storageBucket": "news-firebase-8a2f0.appspot.com",
  "messagingSenderId": "254798211096",
  "appId": "1:254798211096:web:4b49433df73fbc37a73b6d"
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