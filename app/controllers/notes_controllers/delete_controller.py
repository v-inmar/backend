from app.index import db
from sqlalchemy.exc import SQLAlchemyError
from app.utils.model_utils.read_model import read_single
from app.models.note.note_pid.note_pid_model import NotePIDModel
from app.models.note.note_pid.linker_model import NotePIDLinkerModel
from app.models.note.note_model import NoteModel
from app.models.note.note_text.linker_model import NoteTextLinkerModel
from app.models.note.note_text.note_text_model import NoteTextModel

def delete_note(pid):
    """
    Return True after successful deletion
    @param pid String text public id of the note
    """
    try:
        # Get the pid object
        pid_obj = read_single(NotePIDModel, (NotePIDModel.value==pid))
        if pid_obj is None:
            return None
        
        if pid_obj is False:
            raise ValueError("pid_obj is False: {}".format(pid_obj))
        
        # Get the pid linker object
        pid_linker_obj = read_single(NotePIDLinkerModel, (NotePIDLinkerModel.note_pid_id==pid_obj.id))
        if pid_linker_obj is None:
            return None
        
        if pid_linker_obj is False:
            raise ValueError("pid_linker_obj is False: {}".format(pid_linker_obj))
        
        # Get the note object using pid linker object
        note_obj = pid_linker_obj.get_note()
        if type(note_obj) is not NoteModel:
            raise TypeError("note_obj is not of type NoteModel: {}".format(note_obj))
        
        # Get the text linker object
        text_linker_obj = note_obj.get_text_linker()
        if type(text_linker_obj) is not NoteTextLinkerModel:
            raise TypeError("text_linker_obj is not of type NoteTextLinkerModel: {}".format(text_linker_obj))
        
        # Get the text object
        text_obj = note_obj.get_text()
        if type(text_obj) is not NoteTextModel:
            raise TypeError("text_obj is not of type NoteTextModel: {}".format(text_obj))

        # Delete from linker objects first
        db.session.delete(pid_linker_obj)
        db.session.delete(text_linker_obj)

        # Delete child objects
        db.session.delete(pid_obj)
        db.session.delete(text_obj)

        # Delete root object
        db.session.delete(note_obj)

        db.session.commit()
        return True
    except (SQLAlchemyError, TypeError, ValueError):
        db.session.rollback()
        return False
