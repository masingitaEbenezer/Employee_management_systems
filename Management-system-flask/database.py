from flask import Flask
import psycopg2

# connecting to the database
app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_Port']='3307'
# app.config['MYSQL_DB'] = 'employee_management'
 
# mysql = MySQL(app)
conn = psycopg2.connect(host='localhost',
                            database='employee',
                            user='postgres',
                            port=5430,
                            password='')
#Creating a connection cursor
cursor = conn.cursor()

conn.commit()
cursor.close()

# cursor = mysql.connection.cursor()
 
#Executing SQL Statements
# cursor.execute(''' CREATE TABLE Employee(fullName,ID,Email,Phone_no,Address,Position,Salary) ''')
# mysql.connection.commit()
# cursor.close()