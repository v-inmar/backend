from flask import (make_response, abort)
from app.utils.decoator_utils.is_request_valid import is_request_valid

from app.controllers.notes_controllers.read_controller import read_single_note
from app.controllers.notes_controllers.read_controller import read_all_note


@is_request_valid('get')
def read_single(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for note information
    @param pid String public id of a note
    """
    result = read_single_note(pid.lower())
    if result is None:
        abort(404)
    
    if result is False:
        abort(500)
    
    return make_response({"msg": "OK", "payload": result}, 200)

@is_request_valid('get')
def read_all():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for list of notes and information
    """
    result = read_all_note()
    if result is None:
        abort(404)
    
    if result is False:
        abort(500)

    return make_response({"msg": "OK", "payload": result}, 200)