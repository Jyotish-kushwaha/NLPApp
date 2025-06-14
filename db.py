
from pymongo import MongoClient
from urllib.parse import quote_plus
import os
import os

class Database:
    def __init__(self):
        # Get URI from environment (safe for deployment)
       
        
        uri = f"mongodb+srv://jyotish:Jyotish1009@cluster0.r5lch.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        self.client = MongoClient(uri)
        self.db = self.client['nlpapp']
        self.users = self.db['users']
        self.results = self.db['results']

    def insert(self, name, email, password):
        if self.users.find_one({'email': email}):
            return 0
        self.users.insert_one({'name': name, 'email': email, 'password': password})
        return 1

    def login(self, email, password):
        user = self.users.find_one({'email': email})
        return user if user and user['password'] == password else None

    def save_detection_result(self, email, text, lang_code, confidence):
        self.results.insert_one({
            'email': email,
            'text': text,
            'language': lang_code,
            'confidence': confidence
        })
