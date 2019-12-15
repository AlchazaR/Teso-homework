import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	MONGO_URI = os.environ.get('MONGO_URI')
	MONGO_USER = os.environ.get('MONGO_USER')
	MONGO_PASS = os.environ.get('MONGO_PASS')
	MONGO_DB = os.environ.get('MONGO_DB')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False	