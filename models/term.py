from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Term(db.Model):
    __tablename__ = "terms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
