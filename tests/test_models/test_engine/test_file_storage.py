#!/usr/bin/python3
""" Module for testing file storage """
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """Setup the test class"""
        cls.storage = FileStorage()

    def setUp(self):
        """ Set up test environment """
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down test environment """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """ Test if all returns a dict """
        self.assertIs(type(self.storage.all()), dict)

    def test_all_no_class(self):
        """ Test if all returns a dict when no class is passed """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.storage.save()
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        """ Test adding new object to storage """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.assertIn("User.{}".format(new.id), self.storage.all())

    def test_save(self):
        """ Test save method of file storage """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """ Test reload method of file storage """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.storage.save()
        self.storage.reload()
        key = "User.{}".format(new.id)
        self.assertIn(key, self.storage.all())

    def test_save_updates_file(self):
        """ Test if file is updated on save """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            content = json.load(f)
        self.assertIn("User.{}".format(new.id), content.keys())

    def test_delete(self):
        """ Test delete method of file storage """
        new = User(email="test@test.com", password="test")
        self.storage.new(new)
        self.storage.save()
        self.storage.delete(new)
        self.storage.save()
        self.assertNotIn("User.{}".format(new.id), self.storage.all())

    def test_file_storage_instance(self):
        """ Test if storage is an instance of FileStorage """
        self.assertIsInstance(self.storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
