import os
from flask import Flask, request, session, redirect, render_template, url_for
# from forms import SignupForm, LoginForm
from models import db, User

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_pyfile('config.py ')

db.init_app(app)

# app.secret_key = 'development-key'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('asignin.html', username=username, password=password)

    elif request.method == 'GET':
        return render_template('asignin.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return 'True'

    elif request.method == 'GET':
       return 'True'


@app.route('/signout')
def signout():
    session.pop('email', None)
    return redirect('term')


# debug = os.environ.get('FLASK_DEBUG')
app.run(debug=DEBUG)
