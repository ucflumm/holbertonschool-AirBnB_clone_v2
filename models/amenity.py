#!/usr/bin/python3
"""
    Amenity Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':

        place_amenities = Table(
            'place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True, nullable=False)
        )

        places = relationship(
            'Place', secondary=place_amenities, back_populates='amenities')
