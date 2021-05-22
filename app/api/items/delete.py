from flask import make_response
from app.utils.decoators.is_request_valid import is_request_valid


@is_request_valid('delete')
def delete(pid):
    """
    Return Response object with empty JSON object and status code
    JSON object is empty
    @param pid String public id of an item
    """
    return make_response({},204)