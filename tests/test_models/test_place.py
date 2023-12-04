#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
storage_engine = os.getenv('HBNB_TYPE_STORAGE')


class test_Place(test_basemodel):
    """ """
    attribs = {
        "city_id": "123455",
        "user_id": "123456",
        "name": "House Cotage",
        "description": "A place",
        "number_rooms": 2,
        "number_bathrooms": 2,
        "max_guest": 2,
        "price_by_night": 120,
        "latitude": -37.813629,
        "longitude": 144.963058
    }

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(storage_engine == "db", "not using FileStorage")
    def test_amenity_ids(self):
        """ """
        new = self.value(**self.attribs)
        self.assertEqual(type(new.amenity_ids), list)
