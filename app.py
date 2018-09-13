import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/term')
def term():
    return render_template('term.html')


@app.route('/parent')
def parent():
    return render_template('parent.html')


@app.route('/child')
def child():
    return render_template('child.html')


@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')


@app.route('/admission')
def admission():
    return render_template('admission.html')


debug = os.environ.get('FLASK_DEBUG')
app.run(port=5002, debug=debug)
