from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qwerty21'
app.config['MYSQL_DATABASE_DB'] = 'todolist_flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)