#!/usr/bin/python3
"""Test suite for the Amenity class."""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Defines test cases for the Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initializes the test suite."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests that the name attribute of an Amenity instance is a string."""
        new = self.value(name="WiFi")
        self.assertEqual(type(new.name), str)

        self.assertIsNotNone(new.name)
        self.assertNotEqual(new.name, "")
