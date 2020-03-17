from core.utils import Utils

from main.db import MongoDB

class UserService():
    """ doc string for UserService """
    def __init__(self):
        super(UserService, self).__init__()
        self.collection = 'users'
        self.utils = Utils()
        self.mongo = MongoDB()
    
    def add_user(self, user_obj):
        """ user_obj - user object """
        user = self.mongo.find(self.collection, {'email': user_obj['email']})
        if not user:
            return self.mongo.save(self.collection, user_obj)
        else:
            return f'User with {user_obj["email"]} already existed.'

    def login(self, email):
        """ email as input """
        user = self.mongo.find(self.collection, {'email': email})
        if user:
            user = user[0]
            return user
        else:
            return None