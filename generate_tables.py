import os
import sys
from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create():
    print('\ncreating tables ...')
    db.create_all()


def delete():
    print('\ndeleting tables ...')
    db.drop_all()


if __name__ == '__main__':
    with app.app_context():
        arguments = sys.argv

        if len(arguments) > 1:
            if arguments[1] == "create":
                create()
            elif arguments[1] == "delete":
                delete()
        else:
            create()
