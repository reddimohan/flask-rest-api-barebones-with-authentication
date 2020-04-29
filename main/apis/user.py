from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('User', description='User related APIs')
from main.services.user_service import UserService
from core.utils import Utils
from flask import request, jsonify
from main.services.jwt_service import JWTService
from main.services.blacklist_helpers import BlacklistHelper
from flask_jwt_extended import jwt_required

@api.route('/user/<user_id>')
class User(Resource):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__(arg)
        self.user_service = UserService()
        self.arg = arg

    @jwt_required
    def get(self, user_id):
        """ Get user object based on ID 5e86d84da011b26c2082e0c9 """
        current_user = get_jwt_identity()
        msg = "Current user is " + current_user
        status, res, msg, code = self.user_service.get_user(user_id)

        return {'message': status, 'res': res}, code
    
    @jwt_required
    def delete(self, user_id):
        """ Delete User based on user_id """
        return {'msg': 'Working on it.', 'id': user_id}, 200


@api.route('/users')
class UserList(Resource):
    """docstring for UserList."""

    def __init__(self, arg):
        super(UserList, self).__init__(arg)
        self.user_service = UserService()
        self.arg = arg

    @jwt_required
    def get(self):
        """ Get list of users """
        users = self.user_service.user_list()

        return {'status': 'success', 'res': users}, 200