from pygenome import app
from flask import render_template, request
from forms import Loginform

@app.route('/')
def hello():
	return render_template("index.html", message="Peedu loves Judo !!!. Message to my love")

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = Loginform()
    if request.method == 'POST':
        return str(form.email)
    return render_template("login.html", form=form)



