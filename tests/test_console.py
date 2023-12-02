#!/usr/bin/python3
"""
    Unittest for console.py
"""
import unittest
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from io import StringIO
import os
import sys
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Unittest for console.py"""

    @classmethod
    def setUp(self):
        """Set up method"""
        self.cmd = HBNBCommand()

    @classmethod
    def tearDown(self):
        """Tear down method"""
        storage.reload()

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        
    def test_do_create(self):
        """Test create state"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create State name=\"California\"")
            output = f.getvalue().strip()  # Get the actual output and remove leading/trailing spaces
            created_id = output.split()[-1]  # Extract the ID from the output
            self.assertEqual(created_id, output)

    def test_do_create_state_empty(self):
        """Test create state empty"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create State")
            output = f.getvalue().strip()

    def test_create_state(self):
        """Test create state"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create State name=\"San Jose\"")
            output = f.getvalue().strip()
            created_id = output.split()[-1]
            self.assertEqual(created_id, output)

    def test_create_base_model(self):
        """Test create base model"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            output = f.getvalue().strip()
            created_id = output.split()[-1]
            self.assertEqual(created_id, output)



    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("\n")
            self.assertEqual("", f.getvalue()[:-1])


if __name__ == '__main__':
    unittest.main()
