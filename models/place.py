#!/usr/bin/python3
"""
    This module defines the Place class
    *Update 30/11/2023: added code to use db storage and associated imports
    *Update 1/12/2023: added code to use FileStorage and associated imports
        part of question 10
    *Update 2/12/2023: added code to use Amenity class and associated imports
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, null
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import relationship, backref
import os


metadata = MetaData()


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenity = Table(
            "place_amenity",
            Base.metadata,
            Column('place_id', String(60), ForeignKey("places.id"),
                   primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey("amenities.id"),
                   primary_key=True, nullable=False),
            extend_existing=True
            )

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default=null())
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=null())
        longitude = Column(Float, nullable=True, default=null())

        # reworked all of these relationships
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, overlaps="place_amenities")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
                returns list of Review instances base on atrribute place_id
            """
            from models import storage
            review_dict = storage.all(Review)
            review_list = []
            for key, value in review_dict.items():
                if self.id == value.place_id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """
                returns list of Amenity instances base on atrribute amenity_ids
                that contains all Amenity.id linked to Place
            """
            from models import storage
            amenity_values = storage.all(Amenity).values()
            amenity_list = []
            for amenity in amenity_values:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """
                amenities setter
            """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)