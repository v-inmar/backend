from flask import (make_response, abort, request)
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import Unauthorized
from werkzeug.exceptions import InternalServerError

from app.utils.decoators.is_request_valid import is_request_valid


@is_request_valid('put')
def update(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for item information
    @param pid String public id of an item
    """
    payload = request.json['payload']
    return make_response({"msg": "Updated", "payload": payload}, 201)