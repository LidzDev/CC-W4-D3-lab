
from app import db

class Staff(db.Model):
    __tablename__ = "staff"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    records_associated = db.relationship('Record', backref='staff')

    def __repr__(self):
        return f'<User {self.id}: {self.first_name} {self.last_name}>'