import os
from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from apis.user import api as UserRegister

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


# Endpoints
api.add_namespace(UserRegister, path='/v1/auth/register')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
