from wtforms import StringField, PasswordField
from flask_wtf import Form

class Loginform(Form):
    username = StringField('User Name')
    email = StringField('Email Address')
    password = PasswordField('Password')
