import os, sys
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

import coloredlogs, logging as log
coloredlogs.install()

from main.apis.user import api as User
from main.apis.book import api as Book

from main import create_app
from flask_pymongo import PyMongo

# Init app
app = Flask(__name__)

authorizations = {
    'token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# Swagger UI config
app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


api = Api(app, authorizations=authorizations, version='1.0', title='API docs',
    description='A simple REST API with user authentication.',
    doc='/docs'
)

app.config['jwt']._set_error_handler_callbacks(api)

# @app.before_first_request
# this function is to init the db and realted models
# def create_tables():
    # print("Before first statement")
#     db.create_all()


# Endpoints
api.add_namespace(User, path='/v1')
api.add_namespace(Book, path='/v1')

# Run Server
if __name__ == '__main__':
    app.run()
