from flask import Flask,url_for,request
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from os import system
from flask_mysqldb import MySQL


app = Flask(__name__)
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

#creating routes
@app.route('/')
def index():
    return render_template('home.html')

 
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login')
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)

   


@app.route('/Add_employee')
def Add_employee():
    return render_template('Add_employee.html')

@app.route('/view_employee')
def view_employee():
    return render_template('view_employee.html')

@app.route('/update_employee')
def update_employee():
    return render_template('delete_employee.html')

@app.route('/delete_employee')
def delete_employee():
    return render_template('delete_employee.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


def logout():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)

