from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Passowrd', validators=[DataRequired()])
	submit = SubmitField('Sign In')

class ManageForm(FlaskForm):
	newuser = StringField('Username', validators=[DataRequired()])
	passwd = PasswordField('Passowrd', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	user_id = StringField('user_id')
	create = SubmitField('Add user')
	delete = SubmitField('Delete')