import os
from flask import Flask, request, session, redirect, render_template, url_for
from forms import SignupForm, LoginForm
from models import db, User


app = Flask(__name__)

app.config.from_pyfile('config.py')
db.init_app(app)


from routes import *

if __name__ == '__main__':
    app.run()