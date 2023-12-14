#!/usr/bin/python3
"""
    Minimal flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
    return "Hello HBNB!"
