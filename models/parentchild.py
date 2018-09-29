from models import db


class ParentChild(db.Model):
    __tablename__ = "parentchild"
    child_id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, primary_key=True)
