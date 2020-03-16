import os
import yaml
from flask import current_app as app

class Utils():

    def __init__(self):
        pass

    def hash_password(self, pass_string):
        return app.config['flask_bcrypt'].generate_password_hash(pass_string)
    
    def check_password(self, pass_hash, pass_string):
        return app.config['flask_bcrypt'].check_password_hash(pass_hash, pass_string)

    def get_config(self):
        config = yaml.safe_load(open(os.path.join(os.getcwd(),"main/database.yml")))
        return config