import os
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
from random import randint
from models import db, Member, Attendance


dynamic_url = str(randint(1000000, 9000000))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# path to home route
@app.route('/')
def home():
    return redirect(url_for('attendance'))


@app.route('/' + dynamic_url, methods=['POST', 'GET'])
def attendance():
    parents = Member.query.filter_by(member_type="parent").all()
    childs = Member.query.filter_by(member_type="child").all()
    if request.method == 'POST':
        date = datetime.now().strftime('%x')
        day = datetime.now().strftime('%A')

        parent_id = request.form.get("selected_parent")
        child_id = request.form.get("selected_child")

        parent = Attendance(parent_id, date, day)
        parent.present()
        child = Attendance(child_id, date, day)
        child.present()

    return render_template('attendance.html', parents=parents, childs=childs)


@app.route('/qr')
def qr():
    url = request.url_root + dynamic_url
    return render_template('qr.html', dynamic_url=url)


debug = os.environ.get('FLASK_DEBUG')
app.run(port=5002, debug=debug)
