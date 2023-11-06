
from flask_mysqldb import MySQL

# connecting to the database
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_Port']='3307'
app.config['MYSQL_DB'] = 'employee_management'
 
mysql = MySQL(app)
#Creating a connection cursor
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE Employee(fullName,ID,Email,Phone_no,Address,Position,Salary) ''')
mysql.connection.commit()
cursor.close()