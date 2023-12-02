#!/usr/bin/python3
"""
	Unittest for DBStorage
	skip if file_storage is used
"""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
import os


storage = DBStorage()
storage_env = os.getenv("HBNB_TYPE_STORAGE")

@unittest.skipIf(storage_env == "fs", "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
	"""Unittest for DBStorage"""

	def setUp(self):
		"""Set up method"""
		self.storage = DBStorage()
		for key in list(self.storage._DBStorage__session.query(BaseModel).all()):
			self.storage._DBStorage__session.delete(key)
		self.storage._DBStorage__session.commit()
		