from flask import (make_response, abort, request)
from werkzeug.exceptions import (HTTPException, BadRequest, Unauthorized, InternalServerError)

from app.utils.decoator_utils.is_request_valid import is_request_valid
from app.controllers.notes_controllers.create_controller import create_note


@is_request_valid('post')
def create():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for item information
    """
    payload = request.json['payload']
    if 'text' not in payload:
        abort(400)
    
    text = payload['text']
    if not text or len(text) < 1:
        abort(400)
    
    # Create note ensuring text is sliced to the max valid length
    note_dict = create_note(text[:65000])
    if not note_dict:
        abort(500)
    
    return make_response({"msg": "Created", "payload": note_dict}, 201)