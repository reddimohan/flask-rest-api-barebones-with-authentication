from app import app

from flask_mysqldb import MySQL



# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mohan'
app.config['MYSQL_DB'] = 'rest_db'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        conn = mysql.connect
    except Exception as e:
        app.logging.error("{}, check database details in main/db_config.py file.".format(e.args[1]))
        exit()
