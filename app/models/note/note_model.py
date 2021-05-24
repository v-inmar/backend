import datetime
from app.index import db

from app.utils.model_utils.read_model import read_single

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
    

    def get_text(self):
        """
        Return NoteTextModel object
        """
        # Import inside function to avoid ciruclar importing
        from app.models.note.note_text.linker_model import NoteTextLinkerModel
        linker_obj = read_single(NoteTextLinkerModel, (NoteTextLinkerModel.note_id==self.id))
        if linker_obj:
            return linker_obj.get_text()
        return None

    def get_pid(self):
        """
        Return NotePIDModel object
        """
        # Import inside function to avoid ciruclar importing
        from app.models.note.note_pid.linker_model import NotePIDLinkerModel
        linker_obj = read_single(NotePIDLinkerModel, (NotePIDLinkerModel.note_id==self.id))
        if linker_obj:
            return linker_obj.get_pid()
        return None


    def get_text_linker(self):
        """
        Return NoteTextLinkerModel object
        """
        # Import inside function to avoid ciruclar importing
        from app.models.note.note_text.linker_model import NoteTextLinkerModel
        return read_single(NoteTextLinkerModel, (NoteTextLinkerModel.note_id==self.id))
    
    def get_pid_linker(self):
        """
        Return NoteTextLinkerModel object
        """
        # Import inside function to avoid ciruclar importing
        from app.models.note.note_pid.linker_model import NotePIDLinkerModel
        return read_single(NotePIDLinkerModel, (NotePIDLinkerModel.note_id==self.id))
