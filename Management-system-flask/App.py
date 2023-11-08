from flask import Flask,url_for,request
from flask.templating import render_template
import os
from os import system
import psycopg2
from flask import redirect
from flask import Flask
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
def db_conn():
     conn = psycopg2.connect(host='localhost',
                            database='employee',
                            user='academy_inter_mac24',
                            port=5430,
                            password='')
     return conn

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
        conn=db_conn()
        # declaring a cursor
        cur=conn.cursor()
        cur.execute("SELECT * from Employee")
        data=cur.fetchall()

        cur.close()
        conn.close()
        return render_template('dashboard.html',data=data)

@app.route('/dd')
def hello():
    print("hello")
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
       
    if request.method == 'POST':
       
        conn=db_conn()
        cur=conn.cursor()
        id = request.form.get('id')
        full_name = request.form.get('inputfullname')
        email = request.form.get('inputEmail4')
        phone_no= request.form.get('inputphonenumber')
        position= request.form.get('inputposition')
        salary= request.form.get('inputsalary')
        address = request.form.get('inputAddress')

        cur.execute('''INSERT INTO employee(id,full_name,email,phone_no,position,salary,address) VALUES (%s,%s,%s,%s,%s,%s,%s)''',(id,full_name,email,phone_no,position,salary,address))
        conn.commit()
        return render_template('dashboard.html')



if __name__ == '__main__':
 app.run(debug=True, port=3507)

