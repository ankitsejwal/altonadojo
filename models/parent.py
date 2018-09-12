from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Parent(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
