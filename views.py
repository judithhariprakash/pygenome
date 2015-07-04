from pygenome import app
from flask import render_template, request
from forms import Loginform
from dbutils import addEntry
from dbutils import validatePassword


@app.route('/')
def hello():
    return render_template("index.html", message="Peedu loves Judo !!!. Message to my love")

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = Loginform(csrf_enabled=False)
    if request.method == 'POST':
        username = str(form.username.data)
        pwd = str(form.password.data)
        query = addEntry(username, pwd)
        if query is not False:
            if validatePassword(query, pwd) is True:
                return "Hello %s" % username
    return render_template("login.html", form=form)
