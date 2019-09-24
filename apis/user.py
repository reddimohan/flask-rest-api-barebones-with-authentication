from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('API Endpoints', description='')

from flask import request

user_register_parser = api.parser()
user_register_parser.add_argument('name', type=str, help='Name of the user', location='form')
user_register_parser.add_argument('email', type=str, help='User email address', location='form')
user_register_parser.add_argument('password', type=str, help='Password', location='form')

@api.route('/')
class UserRegister(Resource):
    """docstring for UserRegister."""

    def __init__(self, arg):
        super(UserRegister, self).__init__(arg)

    @api.doc(parser= user_register_parser)
    def post(self):
        if 'email' not in request.form:
            return api.abort(400, 'Email should not be empty.', status='error')


# class User(Resource):
#     """docstring for User."""
#
#     def __init__(self, arg):
#         super(User, self).__init__(arg)
#         self.arg = arg
#
#
# user_login_parser = api.parser()
# user_login_parser.add_argument('email', type=str, help='', location='form')
# user_login_parser.add_argument('password', type=str, help='', location='form')
# # @api.route('/')
# class UserLogin(Resource):
#     """docstring for UserLogin."""
#
#     def __init__(self, arg):
#         super(UserLogin, self).__init__(arg)
#         self.arg = arg
#
#     @api.doc(parser= user_login_parser)
#     def post(self):
#         pass
#
#
# class UserLogout(Resource):
#     """docstring for UserLogout."""
#
#     def __init__(self, arg):
#         super(UserLogout, self).__init__(arg)
#         self.arg = arg
