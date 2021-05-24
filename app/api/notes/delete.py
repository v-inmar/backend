from flask import (make_response, abort)
from app.utils.decoator_utils.is_request_valid import is_request_valid

from app.controllers.notes_controllers.delete_controller import delete_note


@is_request_valid('delete')
def delete(pid):
    """
    Return Response object with empty JSON object and status code
    JSON object is empty
    @param pid String public id of a note
    """
    result = delete_note(pid.lower())
    if result is None:
        abort(404)
    
    if result is False:
        abort(500)
    
    return make_response({},204)