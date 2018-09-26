import os
from flask import Flask, request, render_template, redirect, url_for
from random import randint
from models import db, Member


dynamic_url = str(randint(1000000, 9000000))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
db.init_app(app)


@app.route('/')
def home():
    return redirect(url_for('attendance'))


@app.route('/' + dynamic_url, methods=['POST', 'GET'])
def attendance():
    parents = Member.query.filter_by(member_type="parent").all()
    childs = Member.query.filter_by(member_type="child").all()
    print(parents)
    if request.method == 'POST':
        pass
    return render_template('attendance.html', parents=parents, childs=childs)


@app.route('/qr')
def qr():
    url = request.url_root + dynamic_url
    return render_template('qr.html', dynamic_url=url)


debug = os.environ.get('FLASK_DEBUG')
app.run(port=5002, debug=debug)
