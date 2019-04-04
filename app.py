import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/bookData.db'

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
    mys = execute_sql('SELECT * FROM mysterys')
    return render_template('mysteries.html', mys=mys)
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

#book routes
@app.route('/book1')
def book1():
    return render_template('book1.html')

@app.route('/book2')
def book2():
    return render_template('book2.html')

@app.route('/book3')
def book3():
    return render_template('book3.html')

@app.route('/book4')
def book4():
    return render_template('book4.html')

@app.route('/book5')
def book5():
    return render_template('book5.html')

@app.route('/book6')
def book6():
    return render_template('book6.html')

@app.route('/book7')
def book7():
    return render_template('book7.html')

@app.route('/book8')
def book8():
    return render_template('book8.html')

@app.route('/book9')
def book9():
    return render_template('book9.html')

if __name__ == '__main__':
    app.run(debug=True)
