#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models import storage
import os
from models.engine.file_storage import FileStorage
from models.user import User


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_all(self):
        """ __objects is properly returned """
        new = User()  # Use a concrete subclass instead of BaseModel
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_empty(self):
        """ Data is saved to file """
        new = User()  # Use a concrete subclass instead of BaseModel
        thing = new.to_dict()
        new.save()
        new2 = User(**thing)  # Use a concrete subclass instead of BaseModel
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = User()  # Use a concrete subclass instead of BaseModel
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
