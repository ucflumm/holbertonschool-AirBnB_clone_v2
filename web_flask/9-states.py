#!/usr/bin/python3
"""
    10. States and State
    Routes:
        /states: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage
                LI tag: description of one State: <state.id>: <B><state.name></B>
        /states/<id>: display a HTML page: (inside the tag BODY)
            If a State object is found with this id:
                H1 tag: “State: ”
                H3 tag: “Cities:”
                UL tag: with the list of City objects linked to the State
                    LI tag: description of one City: <city.id>: <B><city.name></B>
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