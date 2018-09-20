from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    firstname = StringField('First Name', validators=[DataRequired('Please enter your first name')])
    lastname = StringField('Last Name', validators=[DataRequired('Please enter your last name')])
    email = StringField('Email', validators=[DataRequired('Please enter your email address'), Email('Enter valid email')])
    password = PasswordField('Password', validators=[DataRequired('Password is empty'), Length(min=6, message="your password should be atleast 6 letters long.")])
    submit = SubmitField('Sign up')
