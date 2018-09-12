from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Child(db.Model):
    __tablename__ = "childs"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
