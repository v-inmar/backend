from app.index import db
from sqlalchemy.exc import SQLAlchemyError
from app.utils.model_utils.read_model import read_single
from app.models.note.note_pid.note_pid_model import NotePIDModel
from app.models.note.note_pid.linker_model import NotePIDLinkerModel
from app.models.note.note_model import NoteModel

def update_note(pid, text):
    """
    Return a dictionary object with the corresponding note details 
    that macthes the pid value that was passed in 
    @param pid String text public id of the note
    @param text New String text to replace old value
    """
    try:
        # Get the pid object
        pid_obj = read_single(NotePIDModel, (NotePIDModel.value==pid))
        if pid_obj is None:
            return None
        
        if pid_obj is False:
            raise ValueError("pid_obj is False: {}".format(pid_obj))
        
        # Get the pid linker object
        linker_obj = read_single(NotePIDLinkerModel, (NotePIDLinkerModel.note_pid_id==pid_obj.id))
        if linker_obj is None:
            return None
        
        if linker_obj is False:
            raise ValueError("linker_obj is False: {}".format(linker_obj))

        # Get the note object using pid linker object
        note_obj = linker_obj.get_note()
        if type(note_obj) is not NoteModel:
            raise TypeError("note_obj is not of type NoteModel: {}".format(note_obj))
        
        # Get the text object using note object
        text_obj = note_obj.get_text()
        if not text_obj:
            raise ValueError("text_obj is None or False: {}".format(text_obj))
        
        text_obj.value = text
        db.session.commit()
        return {
            "pid": pid_obj.value,
            "text": text_obj.value,
            "timestamp": note_obj.timestamp
        }
    except (SQLAlchemyError, TypeError, ValueError):
        db.session.rollback()
        return False