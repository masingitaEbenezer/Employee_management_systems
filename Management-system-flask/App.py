from flask import Flask,url_for,request,redirect
from flask.templating import render_template
import os
from os import system
import psycopg2


# conn = psycopg2.connect(host='localhost',
#                             database='employee',
#                             user='postgres',
#                             port=5430,
#                             password='')
# cursor = conn.cursor()
# cursor.execute("select * from users " )

# books = cursor.fetchall()
# print(books)

app = Flask(__name__)
def create_app():
 return app


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn



@app.route('/')
def index():
    return render_template('home.html')

# ...

@app.route('/create/', methods=('GET', 'POST'))
def addEmployee():
    if request.method == 'POST':
        Id = request.form['Id']
        full_name = request.form['full_name']
        Email = request.form['email']
        phone_no= request.form['phone_no']
        Address = request.form['address']
        Position= request.form['position']
        Salary= request.form['salary']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO Employees (Id,full_name,Email,phone_no,Address,Position,Salary)'
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (Id,full_name,Email,phone_no,Address,Position,Salary))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('Add_employee.html')
 
@app.route('/form')
def form():
    return render_template('form.html')





# @app.route('/')
# def index():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM books;')
#     books = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('index.html')

# from flask import Flask

# app = Flask(__name__)

# # @app.route("/")
# # An object of Flask class is our WSGI application.
# from flask import Flask
 
# # Flask constructor takes the name of 
# # current module (__name__) as argument.
# app = Flask(__name__)
 
# # The route() function of the Flask class is a decorator, 
# # which tells the application which URL should call 
# # the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
#     # if request.method == 'POST':
#     #     name = request.form['name']
#     #     age = request.form['age']
#         conn = psycopg2.connect(host='localhost',
#                             database='employee',
#                             user=os.environ['postgres'],
#                             port=5430,
#                             password=os.environ[''])
#         cursor = conn.cursor()
#         cursor.execute("select * from users where name=%s", )
#         books = cursor.fetchall()
        
#         conn.commit()
#         cursor.close()
#         return render_template('index.html', books="books")

if __name__ == '__main__':
   app.run(debug=True)
#     # run() method of Flask class runs the application 
#     # on the local development server.
#     app.run()
# # main driver function