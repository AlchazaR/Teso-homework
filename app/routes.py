from flask import render_template, flash, redirect, jsonify, request, url_for
from app import app, db #, mongo
from app.forms import LoginForm, ManageForm
from pymongo import MongoClient
from app.models import MngConnect, User

from bson.json_util import dumps
from bson.objectid import ObjectId
#from flask import jsonify, request
from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required


# Log in 
#@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		try:
			user = User.query.filter_by(username=form.username.data).first()
			# check username/password
			if user is None or not user.check_password(form.password.data):
				flash('Wrong username or password')
				return redirect(url_for('login'))
			# sucessfull login
			login_user(user)
			# return user to "next" page
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = url_for('login')
			return redirect(next_page)
		except Exception as e: 
			return e
		return "User " + form.username.data + " authenticated."
	return render_template('login.html', title='Login', form=form)


# Log out
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


# Add user
@app.route('/adduser/<newuser>/<email>/<passwd>')
@login_required
def adduser(newuser, email, passwd):
	curruser = current_user.username
	# SELECT admin FROM user WHERE username = <current user>
	isadmin = User.query.filter_by(username=curruser).first()
	if (isadmin.admin):
		try:
			u = User(username=newuser, email=email)
			u.add_user(newuser, email, passwd)
		except Exception as e: 
			return e
		return "User " + newuser + " added."
	else:
		flash('You are not athorised to add users.')
		return redirect(url_for('login'))


# Manage users (GUI)
@app.route('/manage', methods=['GET', 'POST'])
@login_required
def manage():
	curruser = current_user.username
	# SELECT admin FROM user WHERE username = <current user>
	isadmin = User.query.filter_by(username=curruser).first()
	if (isadmin.admin):
		form = ManageForm()
		users = User.query.all()
		if form.validate_on_submit():
			# Create new user
			try:
				u = User(username=form.newuser.data, email=form.email.data)
				u.add_user(form.newuser.data, form.email.data, form.passwd.data)
				flash('New user created.')
			except Exception as e: 
				return e
		return render_template('manage.html', title='Manage Users', users=users, form=form)
	else:
		flash('You are not athorised view this page.')
		return redirect(url_for('login'))


# Delete user (GUI)
"""@app.route('/deleteuser', methods=['GET', 'POST'])
@login_required
def deleteuser():
	print ("Delete user")
	curruser = current_user.username
	# SELECT admin FROM user WHERE username = <current user>
	print ("Currnet user " + curruser)
	isadmin = User.query.filter_by(username=curruser).first()
	if (isadmin.admin):
		form = ManageForm()
		users = User.query.all()
		print ("Admin")
		#if form.validate_on_submit():
			# Delete user
		print ("Form submit " + form.user_id.data)
		u = User(id=form.user_id.data)
		u.delete_user(form.user_id.data)
		print("User deleted - " + form.user_id.data)
		flash('User deleted.')
		#return render_template('manage.html', title='Manage Users', users=users, form=form)
		redirect(url_for('manage'))
	else:
		flash('You are not athorised view this page.')
		return redirect(url_for('login')) """


# Search by email
@app.route('/search/<id>/')
@login_required
def search(id):	
	frstSymb = id[:1]
	if (frstSymb.isdigit()):
		collection = 'leaks_number'
	else: 
		collection = 'leaks_' + frstSymb
	
	#dbColl = mngDb.collection
	
	#resp = dbColl.find_one({"_id": id})
	"""for collection in collections:
		if frstSymb == collection.split('_')
		print(collection) """
		
	#resp = dumps(dbColl.find_one({"_id": id}))
	resp = replaceMultiple('''
		{
			"_id" : "example@mail.com",
			"lastModified" : ISODate("2019-11-27T13:13:24.052Z"),
			"source1" : {
				"password" : ["sample_password"],
				"ip" : ["1.1.1.1"]
			},
			"example_com" : {
				"ip" : ["1.1.1.1"],
				"password" : ["password2"]
			}
		}''', ['\n', '\p', '\t', '\"'], '')
	return jsonify(resp)
	
	

# Search by emails list
@app.route('/bulksearch/<ids>')
@login_required
def bulksearch(ids):
	"""
	1. split strnig by ,
	2. sort array by first letter
	3. create new arrays basing on first email letter
	4. search in collections by first letter (use several threads?)
	"""
	print (str(ids))
	ids = ids.split(',')
	ids.sort()


	frstList = [ [0]*30 for k in range(1000)] 
	resp = ''
	frstSymb = ids[0][:1]
	
	j = 0
	for i in range(len(ids)):	# i - first letter of email
		print("i = " + str(i))
		print("j = " + str(j))
		print("ids i = " + str(ids[i]))
		print("frtsSymb = " + str(frstSymb))
		print("ids[i][:1] = " + str(ids[i][:1]))
		if (frstSymb == ids[i][:1]):
			frstList[j][i] = ids[i]
			
		else:
			frstSymb = ids[i][:1]
			j = j + 1
			
		frstList[j][i] = ids[i]
		print("email " + str(frstList[j][i]))
		resp += str(frstList[j][i]) + "<br>"

	for m in range(j):
		resp += str(frstList[j]) + "<br>"

	"""frstSymb = id[:1]
	if (frstSymb.isdigit()):
		collection = 'leaks_number'
	"""
	#resp = str(ids)
	#bulksearch = mongo.db.user.find()
	#resp = dumps(bulksearch)
	
	return resp	


#Replace a set of multiple sub strings with a new string in main string.
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString     