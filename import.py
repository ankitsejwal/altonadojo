import csv, os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Member

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


def main():
    f = open('import.csv')
    reader = csv.reader(f)

    for first_name, last_name, member_type, gender, email, phone, school in reader:
        member = Member(first_name=first_name, last_name=last_name,
                        member_type=member_type, gender=gender, email=email,
                        phone=phone, school=school)
        print(f'Adding {first_name} of type: {member_type}')
        db.session.add(member)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        main()
