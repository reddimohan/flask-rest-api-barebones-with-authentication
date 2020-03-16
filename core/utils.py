import os
import yaml
from flask import current_app as app

class Utils():

    def __init__(self):
        pass

    def get_config(self):
        config = yaml.safe_load(open(os.path.join(os.getcwd(),"main/database.yml")))
        return config