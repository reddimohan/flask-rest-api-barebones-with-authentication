# from app import app
from flask_mysqldb import MySQL

class Database(object):
    """docstring for Database."""

    def __init__(self, app):
        super(Database, self).__init__()
        self.app = app
        # MySQL configurations
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = 'mohan'
        self.app.config['MYSQL_DB'] = 'rest_db'
        self.app.config['MYSQL_HOST'] = 'localhost'

        self.conn = self.connect()


    def connect(self):
        mysql = MySQL(self.app)

        with self.app.app_context():
            try:
                conn = mysql.connect
                return conn
            except Exception as e:
                self.app.logging.error("{}, check database details in main/db_config.py file.".format(e.args[1]))
                exit()
