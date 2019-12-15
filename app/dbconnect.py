from pymongo import MongoClient
from app import app 
from config import Config


class DbConnect(object):
    def __init__(self):
        client = MongoClient(app.config['MOGO_URI'])
        db = client.app.config['MONGO_DB']   #Select the database
        db.authenticate(name=app.config['MONGO_USER'],password=app.config['MONGO_PASS'])
    
    def db(self):
        collections = self.db.list_collection_names()
        return collections