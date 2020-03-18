from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('User', description='User related APIs')
from main.services.user_service import UserService
from core.utils import Utils

from flask import request, jsonify
from main.services.jwt_service import JWTService

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, get_raw_jwt
)


user_register_model = api.model('SignupModel', {
    'name': fields.String(description="Name of the user", required=True),
    'email': fields.String(description="Email address", required=True),
    'password': fields.String(description="password", required=True)
})

@api.route('/auth/register')
class UserRegister(Resource):
    """docstring for UserRegister."""

    def __init__(self, arg):
        super(UserRegister, self).__init__(arg)
        self.jwt_service = JWTService()
        self.utils = Utils()
        self.user_service = UserService()

    @api.expect(user_register_model)
    # @jwt_required # Enable this after deploying the ap, so that registration for doctor is not open
    def post(self):
        if 'email' not in request.json or request.json['email'] == '':
            return api.abort(400, 'Email should not be empty.', status='error', status_code= 400)
        
        if 'password' not in request.json or request.json['password'] == '':
            return api.abort(400, 'Password should not be empty.', status='error', status_code= 400)
        
        if 'name' not in request.json or request.json['name'] == '':
            return api.abort(400, 'Name should not be empty.', status='error', status_code= 400)
        
        request.json['password'] = self.jwt_service.hash_password(request.json['password'])

        new_user = self.user_service.add_user(request.json)
        if 'password' in new_user: del new_user['password']

        return {'status': 'success', 'data': new_user}, 201


# user_login_parser = api.parser()
# user_login_parser.add_argument('email', type=str, help='', location='form')
# user_login_parser.add_argument('password', type=str, help='', location='form')
user_login_model = api.model('LoginModel', {
    'email': fields.String(description="Email address", required=True),
    'password': fields.String(description="Password", required=True),
})

@api.route('/auth/login')
class UserLogin(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserLogin, self).__init__(arg)
        self.jwt_service = JWTService()
        self.utils = Utils()
        self.user_service = UserService()

    @api.expect(user_login_model)
    def post(self):
        if 'email' not in request.json or request.json['email'] == '':
            return api.abort(400, 'Email should not be empty.', status='error', status_code= 400)
        
        if 'password' not in request.json or request.json['password'] == '':
            return api.abort(400, 'Password should not be empty.', status='error', status_code= 400)
        
        email, password = request.json['email'], request.json['password']

        request.json['password'] = self.jwt_service.hash_password(password)
        
        user = self.user_service.login(email)
        if user:
            pass_match = self.jwt_service.check_password(user['password'], password)
        else:
            pass_match = None

        if pass_match:
            del user['password']
            user['token'] = {
                'access': create_access_token(identity=email),
                'refresh': create_access_token(identity=email)
            }
            message, status_code = 'Login successful.', 200
        else:
            user = ''
            message, status_code = 'Email or Password is wrong.', 401

        return {'status': 'success', 'data': user, 'message': message}, status_code



@api.route('/logout')
class UserLogout(Resource):
    """docstring for UserLogout."""
    def __init__(self, arg):
        super(UserLogout, self).__init__()

    @jwt_required
    def post(self):
        blacklist = set()
        jti = get_raw_jwt()['jti']
        print(jti)
        blacklist.add(jti)
        
        return {'status': 'success', 'msg': 'Successfully logged out.'}, 200

@api.route('/user/<user_id>')
class User(Resource):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__(arg)
        self.arg = arg

    @jwt_required
    def get(self, user_id):
        """ Get user object based on ID """
        current_user = get_jwt_identity()
        msg = "Current user is " + current_user

        return {'msg': 'Working on it.', 'id': user_id}, 200
    
    @jwt_required
    def delete(self, user_id):
        """ Delete User based on user_id """
        return {'msg': 'Working on it.', 'id': user_id}, 200



@api.route('/refresh/token')
class TokenRefresh(Resource):
    """docstring for TokenRefresh."""

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        if current_user:
            access_token = create_access_token(identity=current_user, fresh=False)
        else:
            access_token = 'No user found.'

        return {'status': 'success', 'access_token': access_token}, 200
@api.route('/users')
class UserList(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserList, self).__init__(arg)
        self.arg = arg

    # def get(self):
    #     # you can query to get all the users and return them
    #     return "Get all users"
    


# @api.route('/logout')
# class UserLogout(Resource):
#     """docstring for UserLogout."""

#     def __init__(self, arg):
#         super(UserLogout, self).__init__(arg)
#         self.arg = arg

#     # @jwt_required
#     def post(self):
#         # jti = get_raw_jwt()["jti"]
#         pass
