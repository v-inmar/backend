from flask import (abort, request)
from functools import wraps

# NOTE: This can also check for JWT token in the future when auth is implemented
# or any API keys, etc

import traceback

def is_request_valid(method):
    """
    Return decorator that allows parameter to be passed in the decorator
    @param method String http verb (get, post, put, delete)
    """
    def decor(func):
        """
        Decorator that checks the request validity
        """
        # wraps the function to be decorated
        wraps(func)

        def wrapper(*args, **kwargs):
            """
            A wrapper function that performs the necessary request checks
            """

            # TODO: Refactor and wrap in a try/except block with matching http exception
            if not request.method:
                abort(400)
        
            if str(request.method).lower() != str(method).lower():
                abort(405)
            
            if not request.headers:
                abort(400)

            if 'accept' not in request.headers:
                abort(400)
            
            if request.headers['accept'].lower() != 'application/json':
                abort(400)
            
            req_method = str(request.method).lower()
            if req_method == 'post' or req_method == 'put':
                if not request.json:
                    abort(400)
                
                if "payload" not in request.json:
                    abort(400)
                
                if not request.json['payload']:
                    abort(400)


            elif req_method == 'get' or req_method == 'delete':
                # No request checks yet for get and delete
                # so just return the wrapped function
                return func(*args, **kwargs)

            else:
                # No other methods are allowed
                abort(405)

            return func(*args, **kwargs)
            
        return wrapper
    return decor

