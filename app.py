from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def welcome():
    return render_template('index.html')  # render a template

#genre routes
@app.route('/mysteries')
def mysteries():
    return render_template('mysteries.html')

@app.route('/fiction')
def fiction():
    return render_template('fiction.html')

@app.route('/romance')
def romance():
    return render_template('romance.html')

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

if __name__ == '__main__':
    app.run(debug=True)
