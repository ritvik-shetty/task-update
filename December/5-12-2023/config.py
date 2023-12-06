from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Thought@1234'
app.config['MYSQL_DATABASE_DB'] = 'rest_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost:3306'

mysql.init_app(app)