from models import db


class Volunteer(db.Model):
    __tablename__ = "volunteers"
    volunteer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
