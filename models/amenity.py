#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

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
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""