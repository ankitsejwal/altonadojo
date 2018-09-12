import os
from flask import Flask
from models import db, term, user, child, parent, volunteer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('ALTONADOJO_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def main():
    term.db.create_all()
    user.db.create_all()
    child.db.create_all()
    parent.db.create_all()
    volunteer.db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()
