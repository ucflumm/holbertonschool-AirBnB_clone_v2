#!/usr/bin/python3
<<<<<<< HEAD
"""Script that start Flask web app server"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
=======
"""
    Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0 port 5000
        Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Says HBNB on the /hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Says C followed by the text variable"""
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(port=5000, host='0.0.0.0')
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
