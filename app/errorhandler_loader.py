from app.index import app
from flask import make_response


# Create an error handler for 400 error
@app.errorhandler(400)
def bad_request(error):
    """
    Return Response object with a JSON object and status code
    JSON object contains 'msg' key for message
    @param error Error value to be inserted in the logs (not implement here)
    """
    return make_response({"msg": "Bad Request"}, 400)


# Create an error handler for 404 error
@app.errorhandler(404)
def not_found(error):
    """
    Return Response object with a JSON object and status code
    JSON object contains 'msg' key for message
    @param error Error value to be inserted in the logs (not implement here)
    """
    return make_response({"msg": "File Not Found"}, 404)


# Create an error handler for 405 error
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Return Response object with a JSON object and status code
    JSON object contains 'msg' key for message
    @param error Error value to be inserted in the logs (not implement here)
    """
    return make_response({"msg": "Method Not Allowed"}, 405)


# Create an error handler for 500 error
@app.errorhandler(500)
def server_error(error):
    """
    Return Response object with a JSON object and status code
    JSON object contains 'msg' key for message
    @param error Error value to be inserted in the logs (not implement here)
    """
    return make_response({"msg": "Server Error"}, 500)