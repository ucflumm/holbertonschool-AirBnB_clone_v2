#!/usr/bin/python3
<<<<<<< HEAD
"""Script that start Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
=======
"""
    starts a Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and
    storage.all(...)
    To load all cities of a State:
        If your storage engine is DBStorage, you must use cities relationship
        Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /cities_by_states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
            UL tag: with the list of City objects linked to the State sorted by
            name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
    Use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
from models import storage
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
=======
@app.teardown_appcontext
def teardown_db(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
