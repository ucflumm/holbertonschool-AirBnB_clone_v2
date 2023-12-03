
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
    def setUpClass(cls):
        """Set up class method"""
        os.environ['HBNB_TYPE_STORAGE'] = 'db'

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        if 'HBNB_TYPE_STORAGE' in os.environ:
            del os.environ['HBNB_TYPE_STORAGE']

    def setUp(self):
        """Set up test environment"""
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage.reload()

    def test_do_create(self):
        """Test create state"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create State name=\"California\"")
            output = f.getvalue().strip()
            created_id = output.split()[-1]
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

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("\n")
            self.assertEqual("", f.getvalue()[:-1])

    def test_name3(self):
        """ Test State.name is a string """
        new = State(name="California")
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
