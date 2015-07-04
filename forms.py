from wtforms import Form, TextField, PasswordField, validators

class Loginform(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.Required()])
