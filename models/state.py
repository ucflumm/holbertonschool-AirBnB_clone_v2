#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """ Return the list of City instances where state_id equals State.id """
            from models.city import City
            city_list = [city for city in storage.all(
                City).values() if city.state_id == self.id]
            return city_list

    def __init__(self, *args, **kwargs):
        """Initialization for the State class."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
