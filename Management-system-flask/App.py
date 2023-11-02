from flask import Flask,url_for
from flask.templating import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

#creating routes
@app.route('/')
def index():
    return render_template('home.html')


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

