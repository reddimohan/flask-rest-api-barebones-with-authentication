from flask_restplus import Namespace, Resource, fields

api = Namespace("User", description="User related APIs")
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from main.services.jwt_service import JWTService
from main.services.user_service import UserService

user_model = api.model(
    "UpdateUserModel",
    {
        "name": fields.String(description="Name of the user", required=True),
        "email": fields.String(description="Email address", required=True),
        "password": fields.String(description="password", required=True),
    },
)


@api.route("/user/<user_id>")
class User(Resource):
    """docstring for User."""

    def __init__(self, arg):
        super(User, self).__init__(arg)
        self.jwt_service = JWTService()
        self.user_service = UserService()
        self.arg = arg

    @jwt_required
    def get(self, user_id):
        """ Get user object by _id. ex: 5e87480bb8db9adc3298a2ad """
        current_user = get_jwt_identity()
        msg = "Current user is " + current_user
        status, res, msg, code = self.user_service.get_user(user_id)

        return {"message": status, "res": res}, code

    # @jwt_required
    @api.expect(user_model)
    def put(self, user_id):
        """ Update User profile by _id """
        if not user_id:
            api.abort(400, "User _id is missing.", status="error")

        if "password" in request.json and request.json["password"] != "":
            request.json["password"] = self.jwt_service.hash_password(
                request.json["password"]
            )

        status, obj, msg, code = self.user_service.update_user(user_id, request.json)

        return {"status": status, "data": obj, "message": msg}, code

    @jwt_required
    def delete(self, user_id):
        """ Delete User based on user_id """
        if not user_id:
            api.abort(400, f"User _id is required.", status="error")

        res, msg = self.user_service.delete_user(user_id)

        if res:
            return {"status": "success", "data": res, "message": msg}, 200
        else:
            return api.abort(400, msg, status="error")


@api.route("/users")
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

        return {"status": "success", "res": users}, 200
