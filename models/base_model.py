#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import os

Base = object
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()


class BaseModel:
    """Adding attributes in class"""
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    else:
        id = None
        created_at = None
        updated_at = None

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.utcnow()
            
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary["__class__"] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)