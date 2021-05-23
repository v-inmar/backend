import datetime
from app.index import db

class NotePIDModel(db.Model):
    """
    Creates a data access object for NotePIDModel
    This will hold the public identification of a particular note, hence value is unique
    """
    __tablename__ = 'note_pid_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.String(32), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.timestamp = datetime.datetime.utcnow()

