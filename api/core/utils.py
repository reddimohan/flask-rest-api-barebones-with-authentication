import os

import yaml


class Utils:
    def __init__(self):
        pass

    def http_status(self, code):
        return "success" if code == 200 else "error"

    # def get_config(self):
    #     config = yaml.safe_load(open(os.path.join(os.getcwd(), "main/database.yml")))
    #     return config
    
    def validations(self):
        return True
