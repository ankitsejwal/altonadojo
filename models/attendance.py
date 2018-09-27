from models import db


class Attendance(db.Model):
    __tablename__ = "attendance"
    member_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    day = db.Column(db.String, nullable=False)

    def __init__(self, member_id, date, day):
        self.member_id = member_id
        self.date = date
        self.day = day

    def present(self):
        attendee = Attendance(self.member_id, self.date, self.day)
        db.session.add(attendee)
        db.session.commit()
