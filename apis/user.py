from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('User', description='User related APIs')

from flask import request

user_register_parser = api.parser()
user_register_parser.add_argument('name', type=str, help='Name of the user', location='form')
user_register_parser.add_argument('email', type=str, help='User email address', location='form')
user_register_parser.add_argument('password', type=str, help='Password', location='form')
user_register_parser.add_argument('reporting_to', type=str, help='Reporting to..', location='form')

@api.route('/register')
class UserRegister(Resource):
    """docstring for UserRegister."""

    def __init__(self, arg):
        super(UserRegister, self).__init__(arg)

    @api.doc(parser= user_register_parser)
    def post(self):
        if 'email' not in request.form:
            return api.abort(400, 'Email should not be empty.', status='error')


@api.route('/user/<int:user_id>')
class User(Resource):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__(arg)
        self.arg = arg

    def get(self, user_id: int):
        print(user_id)
        pass
        # user = UserModel.find_by_id(user_id)
        # if not user:
        #     return {"message": "User not found."}, 404
        # return user.json(), 200


user_login_parser = api.parser()
user_login_parser.add_argument('email', type=str, help='', location='form')
user_login_parser.add_argument('password', type=str, help='', location='form')

@api.route('/login')
class UserLogin(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserLogin, self).__init__(arg)
        self.arg = arg

    @api.doc(parser= user_login_parser)
    def post(self):
        pass



@api.route('/users')
class UserList(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserList, self).__init__(arg)
        self.arg = arg

    def get(self):
        print("Get all users")
        pass

@api.route('/logout')
class UserLogout(Resource):
    """docstring for UserLogout."""

    def __init__(self, arg):
        super(UserLogout, self).__init__(arg)
        self.arg = arg

    # @jwt_required
    def post(self):
        # jti = get_raw_jwt()["jti"]
        pass
