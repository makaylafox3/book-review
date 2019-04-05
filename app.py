import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/bookData.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route('/')

@app.route('/index')
def welcome():
    return render_template('index.html')  # render a template

#genre routes
@app.route('/mysteries')
def mysteries():
    mysterys = execute_sql('SELECT * FROM mysterys')
    return render_template('mysteries.html', mysterys=mysterys)

@app.route('/fiction')
def fiction():
    fictions = execute_sql('SELECT * FROM fictions')
    return render_template('fiction.html', fictions=fictions)

@app.route('/romance')
def romance():
    romances = execute_sql('SELECT * FROM romances')
    return render_template('romance.html', romances=romances)


if __name__ == '__main__':
    app.run(debug=True)
