from app import db

class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    record_name = db.Column(db.String(64))
    artist_name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    sold_by = db.Column(db.Integer, db.ForeignKey('staff.id'))

    def __repr__(self):
        return f'<User {self.id}: {self.record_name} {self.artist_name}>'

