from flask import (make_response, abort, request)

from app.utils.decoator_utils.is_request_valid import is_request_valid
from app.controllers.notes_controllers.update_controller import update_note


@is_request_valid('put')
def update(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for note information
    @param pid String public id of a note
    """
    payload = request.json['payload']

    if 'text' not in payload:
        abort(400)
    
    text = payload['text']
    if not text or len(text) < 1:
        abort(400)

    result = update_note(pid.lower(), text[:65000])
    if result is None:
        abort(404)
    
    if result is False:
        abort(500)

    return make_response({"msg": "Updated", "payload": result}, 201)