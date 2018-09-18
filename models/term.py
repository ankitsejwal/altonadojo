from models import db


class Term(db.Model):
    __tablename__ = "terms"
    term_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
