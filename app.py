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
    # mystery_details = {
    #     'title': 'Murder At The Palace',
    #     'author': 'by Margaret Dumas',
    #     'description': "Welcome to the Palace movie theater! Now Showing: Philandering husbands, ghostly sidekicks, and a murder or two. When Nora Paige's movie-star leaves her for his latest co-star, she flees Hollywood to take refuge in San Francisco."
    # }
    # mys = execute_sql('SELECT mystery.mys_id, mystery.mys_title, mystery.mys_author, mystery.mys_description FROM mystery')
    # return render_template('mysteries.html', mys=mystery_details)

@app.route('/fiction')
def fiction():
    fic = execute_sql('SELECT fiction.fict_id, fiction.fict_title, fiction.fict_author, fiction.fict_description FROM fiction')
    return render_template('fiction.html', fic=fic)

@app.route('/romance')
def romance():
    rom = execute_sql('SELECT romance.rom_id, romance.rom_title, romance.rom_author, romance.rom_description FROM romance')
    return render_template('romance.html', rom=rom)


if __name__ == '__main__':
    app.run(debug=True)
