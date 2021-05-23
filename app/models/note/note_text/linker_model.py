import datetime
from app.index import db

from app.utils.model_utils.read_model import read_single
from app.models.note.note_model import NoteModel
from app.models.note.note_text.note_text_model import NoteTextModel


class NoteTextLinkerModel(db.Model):
    """
    Creates a data access object for NoteTextLinkerModel
    This links the NoteModel to the NoteTextModel
    """
    __tablename__ = 'note_text_linker_model'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    note_id = db.Column(db.BigInteger, db.ForeignKey("note_model.id"))
    note_text_id = db.Column(db.BigInteger, db.ForeignKey("note_text_model.id"))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.note_id = kwargs['note_id']
        self.note_text_id = kwargs['note_text_id']
        self.timestamp = datetime.datetime.utcnow()
    

    def get_note(self):
        """
        Return NoteModel object
        """
        return read_single(NoteModel, (NoteModel.id == self.note_id))
    
    def get_text(self):
        """
        Return NoteTextModel object
        """
        return read_single(NoteTextModel, (NoteTextModel.id == self.note_text_id))