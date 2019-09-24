import os
from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from apis.user import api as User
from apis.leaves import api as Leave

# Init app
app = Flask(__name__)

# Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# Swagger UI config
app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='REST API',
    description='A simple REST API with user authentication.',
)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# Endpoints
api.add_namespace(User, path='/v1')
api.add_namespace(Leave, path='/v1')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
