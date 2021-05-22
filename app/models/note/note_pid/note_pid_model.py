import datetime
from app import db

class NotePIDModel(db.Model):
    __tablename__ = 'note_pid_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.String(32), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.timestamp = datetime.datetime.utcnow()

