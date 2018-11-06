from models import db


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    member_type = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    school = db.Column(db.String, nullable=True)
