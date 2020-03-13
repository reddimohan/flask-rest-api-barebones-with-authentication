from flask import request
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
        
        if not token:
            return {'message': 'Bearer Token is missing.'}, 401
        
        print(f'Bearer Token: {token}')

        return f(*args, **kwargs)
    
    return decorated