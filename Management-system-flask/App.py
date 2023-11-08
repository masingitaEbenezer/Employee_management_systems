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
        full_name = request.form.get('fullname')
        email = request.form.get('email')
        phone_no= request.form.get('phonenor')
        position= request.form.get('position')
        salary= request.form.get('salary')
        address = request.form.get('address')

        cur.execute('''INSERT INTO employee(id,full_name,email,phone_no,position,salary,address) VALUES (%s,%s,%s,%s,%s,%s,%s)''',(id,full_name,email,phone_no,position,salary,address))
        conn.commit()
        return render_template('dashboard.html')
    
@app.route('/update',methods=['POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()
    id = request.form.get('id')
    full_name = request.form.get('fullname')
    email = request.form.get('email')
    phone_no= request.form.get('phonenor')
    position= request.form.get('position')
    salary= request.form.get('salary')
    address = request.form.get('address')
    cur.execute('''UPDATE employee SET full_name=%s,email=%s,phone_no=%s,position=%s,salary=%s,address=%s WHERE id=%s''',(id,full_name,email,phone_no,position,salary,address))
    conn.commit()
    cur.close()
    conn.close()

@app.route('/delete')
def delete():
  conn=db_conn()
  cur=conn.cursor()

#   get data from the form
  id=request.form.get[id]
#   delete data from the table
  cur.execute('''DELETE FROM employee WHERE id=%s''',(id))
if __name__ == '__main__':
 app.run(debug=True, port=3507)

