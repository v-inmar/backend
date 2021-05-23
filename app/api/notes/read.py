from flask import (make_response)
from app.utils.decoator_utils.is_request_valid import is_request_valid


@is_request_valid('get')
def read_single(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for note information
    @param pid String public id of a note
    """
    return make_response({"msg": "OK", "payload": {"pid": pid}}, 200)

@is_request_valid('get')
def read_all():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for list of notes and information
    """
    return make_response({"msg": "OK", "payload": [{"pid": 123, "text": "one two three"}, {"pid": 456, "text": "four five six"}]}, 200)