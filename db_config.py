from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# Configurações de conexão com o MySQL

app.config['MYSQL_DATABASE_USER'] = 'Tizl'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ninja1234@'
app.config['MYSQL_DATABASE_DB'] = 'sistemateste'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
