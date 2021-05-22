from flask import (make_response, abort, request)
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import Unauthorized
from werkzeug.exceptions import InternalServerError

from app.utils.decoators.is_request_valid import is_request_valid


@is_request_valid('post')
def create():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for item information
    """
    payload = request.json['payload']
    return make_response({"msg": "Created", "payload": payload}, 201)