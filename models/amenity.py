#!/usr/bin/python3
"""
    Amenity Module for HBNB project
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        place_amenities = Table(
            'place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True, nullable=False)
        )

        places = relationship(
            'Place', secondary=place_amenities, back_populates='amenities')
    else:
        name = ""
