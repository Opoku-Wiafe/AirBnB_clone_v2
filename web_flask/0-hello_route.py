#!/usr/bin/python3
"""a Model that builds an app framework"""


from flask import Flask

app = Flask(__name__)

@app.route('/',strict_slash=False)
def home():
    """this where the code goes"""
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
