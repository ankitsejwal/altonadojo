import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome'


@app.route('/term')
def term():
    return 'Term'


@app.route('/parent')
def parent():
    pass


@app.route('/child')
def child():
    pass


@app.route('/admission')
def admission():
    pass


debug = os.environ.get('FLASK_DEBUG')
app.run(port=5001, debug=debug)
