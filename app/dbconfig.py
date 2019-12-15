from pymongo import MongoClient
from config import Config
from app import app


class DbConnect(object):
	def __init__(self):
		client = MongoClient(app.config['MONGO_URI'])
		database = app.config['MONGO_DB']
		db = client.database   #Select the database
		#print("DB data 1 - " + str(db))
		db.authenticate(name=app.config['MONGO_USER'],password=app.config['MONGO_PASS'])
		#print("DB data 2 - " + str(db))
		#collections = db.list_collection_names()