from flask_restplus import Api

from .auth import api as ns3
from .book import api as ns2
from .user import api as ns1

api = Api(
    title="",
    version="1.0",
    description="API description",
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
