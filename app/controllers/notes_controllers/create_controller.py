from app.index import db
from sqlalchemy.exc import SQLAlchemyError
from app.utils.model_utils.create_model import create
from app.utils.model_utils.read_model import read_single
from app.models.note.note_model import NoteModel
from app.models.note.note_pid.note_pid_model import NotePIDModel
from app.models.note.note_pid.linker_model import NotePIDLinkerModel
from app.models.note.note_text.note_text_model import NoteTextModel
from app.models.note.note_text.linker_model import NoteTextLinkerModel
from app.utils.string_utils.get_random_string import get_random_string

def create_note(text):
    """
    Returns a dictionary of the newly created note pid and text that had commited to 
    database with all its auto generated fields i.e. pid 
    @param text The string value to be saved in the database
    """
    try:
        # Create Note object
        note_obj = create(NoteModel)
        if type(note_obj) is not NoteModel:
            raise TypeError("note_obj is not of type NoteModel: {}".format(note_obj))

        # FOR PID
        # Loop to check random string has not been used
        pid = None
        while True:
            pid = get_random_string(16, 32)

            pid_obj = read_single(
                NotePIDModel,
                (NotePIDModel.value == pid)
            )

            if pid_obj is False:
                raise ValueError("pid_obj is False: {}".format(pid_obj))
            
            if pid_obj:
                continue
            break

        if not pid:
            raise ValueError("pid is None or False: {}".format(pid)) 
        
        # Create PID object
        pid_obj = create(NotePIDModel, value=pid)
        if type(pid_obj) is not NotePIDModel:
            raise TypeError("pid_obj is not of type NotePIDModel: {}".format(pid_obj))

        # Create PID Linker object
        pid_linker_obj = create(NotePIDLinkerModel, note_id=note_obj.id, note_pid_id=pid_obj.id)
        if type(pid_linker_obj) is not NotePIDLinkerModel:
            raise TypeError("pid_linker_obj is not of type NotePIDLinkerModel: {}".format(pid_linker_obj))
        
        # Create Text object
        text_obj = create(NoteTextModel, value=text)
        if type(text_obj) is not NoteTextModel:
            raise TypeError("text_obj is not of type NoteTextModel: {}".format(text_obj))
        
        # Create Text Linker object
        text_linker_obj = create(NoteTextLinkerModel, note_id=note_obj.id, note_text_id=text_obj.id)
        if type(text_linker_obj) is not NoteTextLinkerModel:
            raise TypeError("text_linker_obj is not of type NoteTextLinkerModel: {}".format(text_linker_obj))
    

        db.session.commit()
        return {
            "pid":pid,
            "text":text
        }
    except (SQLAlchemyError, ValueError, TypeError):
        db.session.rollback()
        return False