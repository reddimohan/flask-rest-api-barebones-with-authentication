from core.utils import Utils
from flask import current_app as app
from main.db import MongoDB

class UserService():
    """ doc string for UserService """
    def __init__(self):
        super(UserService, self).__init__()
        self.collection = 'users'
        self.utils = Utils()
        self.mongo = MongoDB()
    
    def user_list(self):
        users = self.mongo.find(self.collection)
        if users:
            for user in users: del user['password']
            return users
        else:
            return []

    def add_user(self, user_obj):
        """ user_obj - user object """
        user = self.mongo.find(self.collection, {'email': user_obj['email']})
        if not user:
            return self.mongo.save(self.collection, user_obj)
        else:
            return f'User with {user_obj["email"]} already existed.'

    def get_user(self, user_id):
        """ Get Doctor profile by id. ex _id:  """
        res = self.mongo.find_by_id(self.collection, user_id)
        if res:
            del res['password']
            return ('success', res, 'ok', 200)
        else:
            return ('error', [], 'Something went wrong.', 400)

    def login(self, email):
        """ email as input """
        user = self.mongo.find(self.collection, {'email': email})
        if user:
            user = user[0]
            return user
        else:
            return None
    
    def save_tokens(self, user_tokens, jwt_service):
        jwt_service.add_token_to_database(user_tokens['access'], app.config['JWT_IDENTITY_CLAIM'])
        jwt_service.add_token_to_database(user_tokens['refresh'], app.config['JWT_IDENTITY_CLAIM'])