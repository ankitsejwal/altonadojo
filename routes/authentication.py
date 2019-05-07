from flask import Flask, request, session, redirect, render_template, url_for
from app import app

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        return render_template('asignup.html')
    elif request.method == 'GET':
        return render_template('asignup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return 'True'

    elif request.method == 'GET':
       return render_template('asignin.html')


@app.route('/signout')
def signout():
    session.pop('email', None)
    return redirect('home')
