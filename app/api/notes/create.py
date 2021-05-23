from flask import (make_response, abort, request)
from werkzeug.exceptions import (HTTPException, BadRequest, Unauthorized, InternalServerError)

from app.utils.decoator_utils.is_request_valid import is_request_valid


@is_request_valid('post')
def create():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for item information
    """
    payload = request.json['payload']
    text = payload['text']
    
    return make_response({"msg": "Created", "payload": text}, 201)