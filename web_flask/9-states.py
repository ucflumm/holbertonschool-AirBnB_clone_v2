#!/usr/bin/python3
<<<<<<< HEAD
"""Script that start Flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Render html page of state list"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """Render html page of state with given id and its city list"""
    states = storage.all(State)

    state_found = None
    for state in states.values():
        if state.id == id:
            state_found = state
            break
    if state_found:
        return render_template("9-states.html", state_found=state_found)
    else:
        return render_template("9-states.html", state_found=None)


@app.teardown_appcontext
def remove_session(exception):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""
    10. States and State
    Routes:
        /states: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage
                LI tag: description of one State: <state.id>: <B><state.name>
        /states/<id>: display a HTML page: (inside the tag BODY)
            If a State object is found with this id:
                H1 tag: “State: ”
                H3 tag: “Cities:”
                UL tag: with the list of City objects linked to the State
                    LI tag: description of one City: <city.id>: <B><city.name>
            Otherwise:
                H1 tag: “Not found!”
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page"""
    all_states = storage.all("State")
    return render_template("9-states.html", state=all_states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display a HTML page"""
    state = storage.all("State")
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> be533091ada1ea270d72f5479c785acad30cc928
