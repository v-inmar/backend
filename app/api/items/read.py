from flask import make_response

def read_single(pid):
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for item information
    @param pid String public id of an item
    """
    return make_response({"msg": "OK", "payload": {"pid": pid}}, 200)


def read_all():
    """
    Return Response object with JSON object and status code
    JSON object contains 'msg' key for message and 'payload' for list of items and information
    """
    return make_response({"msg": "OK", "payload": [{"pid": 123, "name": "one two three"}, {"pid": 456, "name": "four five six"}]}, 200)