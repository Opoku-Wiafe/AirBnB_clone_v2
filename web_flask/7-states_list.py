#!/usr/bin/python3
""" This module sets up a Flask web server """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Route for Hello HBNB! """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Route for HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Route for C followed by the value of the text variable """
    return 'c {}'.format(text.replace("_", " "))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Route for Python followed by the value of the text variable """
    return 'Python {}'.format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Route for an integer followed by 'is a number' """
    return '{} is a number'.format(n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Route for determining if a number is odd or even """
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route for listing all states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close(error):
    """ Close the storage on teardown """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
