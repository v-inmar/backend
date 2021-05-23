import datetime
from app.index import db

from app.utils.model_utils.read_model import read_single
from app.models.note.note_model import NoteModel
from app.models.note.note_pid.note_pid_model import NotePIDModel


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
    

    def get_note(self):
        """
        Return NoteModel object
        """
        return read_single(NoteModel, (NoteModel.id == self.note_id))
    
    def get_pid(self):
        """
        Return NotePIDModel object
        """
        return read_single(NotePIDModel, (NotePIDModel.id == self.note_pid_id))