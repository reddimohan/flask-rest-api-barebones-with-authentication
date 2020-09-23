from flask_restplus import Namespace, Resource, fields

api = Namespace("Authentication", description="Authentication related APIs")
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
)

from core.utils import Utils
from main.services.blacklist_helpers import BlacklistHelper
from main.services.jwt_service import JWTService
from main.services.user_service import UserService

user_register_model = api.model(
    "SignupModel",
    {
        "name": fields.String(description="Name of the user", required=True),
        "email": fields.String(description="Email address", required=True),
        "password": fields.String(description="password", required=True),
    },
)


@api.route("/auth/register")
class UserRegister(Resource):
    """docstring for UserRegister."""

    def __init__(self, arg):
        super(UserRegister, self).__init__(arg)
        self.jwt_service = JWTService()
        self.blacklist = BlacklistHelper()
        self.utils = Utils()
        self.user_service = UserService()

    @api.expect(user_register_model)
    # @jwt_required
    def post(self):
        """ Register new User """
        if "email" not in request.json or request.json["email"] == "":
            return api.abort(
                400, "Email should not be empty.", status="error", status_code=400
            )

        if "password" not in request.json or request.json["password"] == "":
            return api.abort(
                400, "Password should not be empty.", status="error", status_code=400
            )

        if "name" not in request.json or request.json["name"] == "":
            return api.abort(
                400, "Name should not be empty.", status="error", status_code=400
            )

        request.json["password"] = self.jwt_service.hash_password(
            request.json["password"]
        )

        res = self.user_service.add_user(request.json)
        if "password" in res:
            del res["password"]

        return {"status": "success", "res": res, "message": "ok"}, 201


user_login_model = api.model(
    "LoginModel",
    {
        "email": fields.String(description="Email address", required=True),
        "password": fields.String(description="Password", required=True),
    },
)


@api.route("/auth/login")
class UserLogin(Resource):
    """docstring for UserLogin."""

    def __init__(self, arg):
        super(UserLogin, self).__init__(arg)
        self.jwt_service = JWTService()
        self.utils = Utils()
        self.user_service = UserService()

    @api.expect(user_login_model)
    def post(self):
        """ User login API """
        if "email" not in request.json or request.json["email"] == "":
            return api.abort(
                400, "Email should not be empty.", status="error", status_code=400
            )

        if "password" not in request.json or request.json["password"] == "":
            return api.abort(
                400, "Password should not be empty.", status="error", status_code=400
            )

        email, password = request.json["email"], request.json["password"]

        request.json["password"] = self.jwt_service.hash_password(password)

        user = self.user_service.login(email)
        if user:
            pass_match = self.jwt_service.check_password(user["password"], password)
        else:
            pass_match = None

        if pass_match:
            del user["password"]
            user["tokens"] = {
                "access": create_access_token(identity=email),
                "refresh": create_refresh_token(identity=email),
            }
            self.user_service.save_tokens(user["tokens"])
            message, status_code = "Login successful.", 200
        else:
            user = []
            message, status_code = "Email or Password is wrong.", 401

        return {"status": "success", "res": user, "message": message}, status_code


@api.route("/logout")
class UserLogout(Resource):
    """docstring for UserLogout."""

    def __init__(self, arg):
        super(UserLogout, self).__init__()
        self.blacklist = BlacklistHelper()

    @jwt_required
    def post(self):
        """ User logout """
        current_user = get_jwt_identity()
        code, msg = self.blacklist.revoke_token(current_user)

        return {"status": "success", "msg": msg}, code


@api.route("/refresh/token")
class TokenRefresh(Resource):
    """docstring for TokenRefresh."""

    def __init__(self, args):
        super(TokenRefresh, self).__init__()

    @jwt_refresh_token_required
    def post(self):
        """ Refresh token - In Progress """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        self.user_service.save_tokens(access_token)

        return {"status": "success", "access_token": access_token}, 200
