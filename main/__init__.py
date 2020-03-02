from flask import Flask

# local imports
from config import app_config

# db variable initialization
# db = SQLAlchemy()
from .db import MongoDB

import coloredlogs, logging as log


def create_app(config_name):

    config_name = 'dev' if not config_name else config_name
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["log"] = log

    with app.app_context():
        db = MongoDB()
    # db.init_app(app)
    # print(db)

    @app.route('/')
    def hello_world():
        # render home template
        return 'Hello, World!'

    return app
