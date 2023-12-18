#!/usr/bin/python3
"""Script that start Flask web app"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Render a filter html page"""
    state_list = storage.all(State)
    city_list = storage.all(City)
    amenity_list = storage.all(Amenity)

    return render_template("10-hbnb_filters.html", cities=city_list,
                           states=state_list, amenities=amenity_list)


@app.teardown_appcontext
def remove_session(exception):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
