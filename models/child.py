from models import db


class Child(db.Model):
    __tablename__ = "childs"
    child_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
