from flask import request, jsonify
from functools import wraps
from flask import current_app as app
from main.db import MongoDB
from flask_jwt_extended import decode_token
from datetime import datetime
# from app.auth.blacklist_helper import is_token_revoked


class JWTService():
    """ doc str """
    def __init__(self):
        super(JWTService, self).__init__()
        self.mongo = MongoDB()
        self.__jwt_init()
    
    def add_token_to_database(self, encoded_access_token, identity_claim):
        """
        Adds a token to the database. It is not revoked when it is aded.
        :param identity_claim: identity_claim is user email here which we set in api/user.py:UserLogin:post
        """
        decoded_token = decode_token(encoded_access_token)
        jti = decoded_token['jti']
        token_type = decoded_token['type']
        user_identity = decoded_token[identity_claim]
        expires = self._epoch_utc_to_datetime(decoded_token['exp'])

        revoked = False

        token_data = {
            'jti': jti,
            'token_type': token_type,
            'user_identity': user_identity,
            'expires': expires,
            'revoked': revoked
        }

        return self.mongo.save('blacklist', token_data)
    
    def hash_password(self, pass_string):
        return app.config['flask_bcrypt'].generate_password_hash(pass_string)
    
    def check_password(self, pass_hash, pass_string):
        return app.config['flask_bcrypt'].check_password_hash(pass_hash, pass_string)
    
    def _epoch_utc_to_datetime(self, epoch_utc):
        """
        Helper function for converting epoch timestamps (as stored in JWTs) into
        python datetime objects (which are easier to use with sqlalchemy).
        """
        return datetime.fromtimestamp(epoch_utc)

    def __jwt_init(self):
        jwt = app.config['jwt']

        # @jwt.token_in_blacklist_loader
        # def check_if_token_revoked(decrypted_token):
        #     return is_token_revoked(decrypted_token)


        @jwt.expired_token_loader
        def expired_token_callback():
            return jsonify({
                'msg': 'The token has expired',
                'error': 'token_expired'
            }), 401


        @jwt.invalid_token_loader
        def invalid_token_callback(error):
            return jsonify({
                'msg': 'Signature verification failed',
                'error': 'invalid_token'
            }), 401


        @jwt.unauthorized_loader
        def missing_token_callback(error):
            return jsonify({
                'msg': 'Request does not contain an access token',
                'error': 'authorization_required'
            }), 401


        @jwt.needs_fresh_token_loader
        def token_not_fresh_callback():
            return jsonify({
                'msg': 'The token is not fresh',
                'error': 'fresh_token_required'
            }), 401


        @jwt.revoked_token_loader
        def revoked_token_callback():
            return jsonify({
                'msg': 'The token has been revoked',
                'error': 'token_revoked'
            }), 401

# class UserInJWT():
#     def __init__(self, user_obj, args=None):
#         self.user = user_obj
#         self.args = args
    
#     @jwt.user_claims_loader
#     def add_claims_to_access_token(user):
#         """
#         # Create a function that will be called whenever create_access_token
#         # is used. It will take whatever object is passed into the
#         # create_access_token method, and lets us define what custom claims
#         # should be added to the access token.
#         """
#         return {'roles': user.roles}
    
#     @jwt.user_identity_loader
#     def user_identity_lookup(user):
#         """
#         # Create a function that will be called whenever create_access_token
#         # is used. It will take whatever object is passed into the
#         # create_access_token method, and lets us define what the identity
#         # of the access token should be.
#         """
#         return user.name