#!/usr/bin/python3
<<<<<<< HEAD
"""Script that start Flask web app server"""
=======
"""
    Minimal flask app
"""

>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_world():
=======
@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(port=5000, host='0.0.0.0')
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
