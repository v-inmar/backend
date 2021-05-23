from flask import make_response
from app.utils.decoator_utils.is_request_valid import is_request_valid


@is_request_valid('delete')
def delete(pid):
    """
    Return Response object with empty JSON object and status code
    JSON object is empty
    @param pid String public id of a note
    """
    return make_response({},204)