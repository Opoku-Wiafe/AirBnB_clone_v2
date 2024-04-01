#!/usr/bin/python3
""" module doc """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ initial page of the app """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ click here to come home """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display c followed by text """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ display python followed by text"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ get a number and return it"""
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ pass in the number and it will tell you if it is odd or even"""
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
