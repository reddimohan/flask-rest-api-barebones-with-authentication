import os
import datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# local imports
from config import app_config

from .db import MongoDB

import coloredlogs, logging as log

def create_app(config_name):
    config_name = 'dev' if not config_name else config_name
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["log"] = log

    app.config['JWT_SECRET_KEY'] = '9MZbGqQHaC47SSKyKaTK'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
    app.config['jwt'] = JWTManager(app)
    app.config['flask_bcrypt'] = Bcrypt(app)
    jwt = app.config['jwt']

    with app.app_context():
        db = MongoDB()
    

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        blacklist = set()
        jti = decrypted_token['jti']
        return jti in blacklist

    @app.route('/')
    def hello_world():
        # render home template
        return 'Hello, World!'

    return app
