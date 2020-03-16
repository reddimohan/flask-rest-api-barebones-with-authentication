from flask import request
from functools import wraps
from flask import current_app as app


class JWTService():
    """ doc str """
    def __init__(self):
        super(JWTService, self).__init__()
    
    def hash_password(self, pass_string):
        return app.config['flask_bcrypt'].generate_password_hash(pass_string)
    
    def check_password(self, pass_hash, pass_string):
        return app.config['flask_bcrypt'].check_password_hash(pass_hash, pass_string)

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         if 'Bearer' in request.headers:
#             token = request.headers['Bearer']
        
#         if not token:
#             return {'message': 'Bearer Token is missing.'}, 401
        
#         print(f'Bearer Token: {token}')

#         return f(*args, **kwargs)
    
#     return decorated