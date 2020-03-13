from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('User', description='User related APIs')
from main.services.user_service import UserService
from flask import current_app as app

from flask import request, jsonify
from main.services.jwt_service import token_required

user_register_parser = api.parser()
user_register_parser.add_argument('name', type=str, help='Name of the user', location='form')
user_register_parser.add_argument('email', type=str, help='User email address', location='form')
user_register_parser.add_argument('password', type=str, help='Password', location='form')


@api.route('/auth/register')
class UserRegister(Resource):
    """docstring for UserRegister."""

    def __init__(self, arg):
        super(UserRegister, self).__init__(arg)
        self.user_service = UserService()

    @api.doc(parser= user_register_parser, security='token')
    @token_required
    def post(self):
        if 'email' not in request.form:
            return api.abort(400, 'Email should not be empty.', status='error', status_code= 400)
        
        if 'password' not in request.form:
            return api.abort(400, 'Password should not be empty.', status='error', status_code= 400)
        
        if 'name' not in request.form:
            return api.abort(400, 'Name should not be empty.', status='error', status_code= 400)
        
        form_obj = request.form.to_dict()
        
        form_obj['password'] = app.config['flask_bcrypt'].generate_password_hash(form_obj['password'])

        new_user = self.user_service.add_user(form_obj)
        if 'password' in new_user: del new_user['password']

        return {'status': 'success', 'data': new_user}, 200


user_login_parser = api.parser()
user_login_parser.add_argument('email', type=str, help='', location='form')
user_login_parser.add_argument('password', type=str, help='', location='form')
@api.route('/auth/login')
class UserLogin(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserLogin, self).__init__(arg)
        self.arg = arg

    @api.doc(parser= user_login_parser)
    def post(self):
        if 'email' not in request.form:
            return api.abort(400, 'Email should not be empty.', status='error', status_code= 400)
        
        if 'password' not in request.form:
            return api.abort(400, 'Password should not be empty.', status='error', status_code= 400)
        
        form_obj = request.form.to_dict()
        form_obj['password'] = app.config['flask_bcrypt'].generate_password_hash(form_obj['password'])
        print(form_obj)

        return {'t': 't'}, 200


@api.route('/user/<int:user_id>')
class User(Resource):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__(arg)
        self.arg = arg

    @token_required
    def get(self, user_id: int):
        print(user_id)
        pass
        # user = UserModel.find_by_id(user_id)
        # if not user:
        #     return {"message": "User not found."}, 404
        # return user.json(), 200







# @api.route('/users')
# class UserList(Resource):
#     """docstring for UserLogin."""

#     def __init__(self, arg):
#         super(UserList, self).__init__(arg)
#         self.arg = arg

#     def get(self):
#         return "Get all users"


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
