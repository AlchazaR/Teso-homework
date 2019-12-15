from pymongo import MongoClient
from app import db, app, login
from config import Config
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# MongoDB connection
class MngConnect(object):
	def __init__(self):
		client = MongoClient(app.config['MONGO_URI'])
		database = app.config['MONGO_DB']
		mongodb = client.database   #Select the database
		mongodb.authenticate(name=app.config['MONGO_USER'],password=app.config['MONGO_PASS'])
		
		
# Users DB 
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	admin = db.Column(db.Boolean)
	salt = 'S1e1k-t13k_dru5k05'

	def __repr__(self):
		return '<User {}>'.format(self.username) 
    
	def set_password(self, password):
		self.password_hash = generate_password_hash(password + self.salt)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password + self.salt)		

	def add_user(self, username, email, password):
		self.username = username
		self.email = email
		self.set_password(password)
		db.session.add(self)
		db.session.commit()

	def delete_user(self, userid):
		self.id = userid
		db.session.delete(self)
		db.session.commit()


# User login loader
@login.user_loader
def load_user(id):
	return User.query.get(int(id))