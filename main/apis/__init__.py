from flask_restplus import Api

from .user import api as ns1
from .book import api as ns2
api = Api(
    title='',
    version='1.0',
    description='API description',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
