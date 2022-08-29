from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1598753'
app.config['MYSQL_DATABASE_DB'] = 'world'
app.config['MYSQL_DATABASE_DB'] = 'world'
app.config['MYSQL_DATABASE_DB'] = 'world'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#MySQL.init_app(app)

mysql = MySQL(app)

conn = mysql.connect()
cursor = conn.cursor()

cursor.execute("SELECT * from city")
data = cursor.fetchone()


@app.route('/')
def index():
    return render_template('old/index.html')
