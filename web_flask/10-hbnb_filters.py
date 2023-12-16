#!/usr/bin/python3
"""
    Flask web application
    Routes for managing your web app for the HBNB project.
        /hbnb_filters: display a HTML page like 6-index.html
        State, Cities, Amenities objects must be loaded from storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like 6-index.html"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
