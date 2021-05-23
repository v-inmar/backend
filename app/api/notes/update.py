from flask import (make_response, abort, request)

from app.utils.decoator_utils.is_request_valid import is_request_valid


@is_request_valid('put')
def update(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for note information
    @param pid String public id of a note
    """
    payload = request.json['payload']
    return make_response({"msg": "Updated", "payload": payload}, 201)