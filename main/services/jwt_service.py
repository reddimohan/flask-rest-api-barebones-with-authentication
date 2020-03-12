from flask import request
from functools import wraps

class JWTService():
    """ JWTService to perform authentication """
    def __init__(self):
        super(JWTService, self).__init__()
    
    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'token' in request.headers:
                token = request.headers['token']
            
            if not token:
                return {'message': 'Token is missing.'}, 401
            
            print(f'Token: {token}')

            return f(*args, **kwargs)
        
        return decorated