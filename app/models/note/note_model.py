import datetime
from app import db

class NoteModel(db.Model):
    """
    Creates a data access object for NoteModel
    This will serve as the root model that will link all other models related to note
    """
    __tablename__ = 'note_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self):
        self.timestamp = datetime.datetime.utcnow()
