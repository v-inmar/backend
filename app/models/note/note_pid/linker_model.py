import datetime
from app.index import db


class NotePIDLinkerModel(db.Model):
    """
    Creates a data access object for NotePIDLinkerModel
    This links the NoteModel to the NotePIDModel, thus giving every note a unique pid
    """
    __tablename__ = 'note_pid_linker_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    note_id = db.Column(db.BigInteger, db.ForeignKey("note_model.id"))
    note_pid_id = db.Column(db.BigInteger, db.ForeignKey("note_pid_model.id"))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.note_id = kwargs['note_id']
        self.note_pid_id = kwargs['note_pid_id']
        self.timestamp = datetime.datetime.utcnow()