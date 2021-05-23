import datetime
from app import db

class NoteTextModel(db.Model):
    """
    Creates a data access object for NoteTextModel
    This will hold the text value of a particular note
    """
    __tablename__ = 'note_text_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.value = kwargs['value']
        self.timestamp = datetime.datetime.utcnow()