import os
from flask import Flask, request, session, redirect, render_template, url_for
from forms import SignupForm, LoginForm
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = 'development-key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() is False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() is False:
            return render_template('signin.html', form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user is not None and user.check_password(password):
                session['email'] = email
                return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
    session.pop('email', None)
    return redirect('term')


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
