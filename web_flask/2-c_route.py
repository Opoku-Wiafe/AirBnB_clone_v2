#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """returns the value Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """shows HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """show “C ” followed by user input"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
