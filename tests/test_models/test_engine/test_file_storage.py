#!/usr/bin/python3
""" tests file storage
"""
from os.path import basename
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from models import storage
import datetime
import json
import os


class TestFileStorage(unittest.TestCase):
    """ init the unnittests
    """
    def test_doc(self):
        """ docstring test """
        self.assertIsNotNone(("models.engine.file_storage".__doc__))
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_attr(self):
        """ tests attr
        """
        file = FileStorage()
        self.assertTrue(hasattr(file, "_FileStorage__objects"))
        self.assertTrue(hasattr(file, "_FileStorage__file_path"))

    def test_savel(self):
        """ reload, save test """
        os.remove('file.json')
        base = BaseModel()
        base.save()
        storage.reload()
        new = storage.all()
        self.assertDictEqual(new["BaseModel." + base.id].to_dict(), base.to_dict())

    def test_different_id(self):
        """Method that check if each instance that is created has
        a unique id
        """
        instance1 = FileStorage()
        instance2 = FileStorage()
        self.assertNotEqual(instance1, instance2)

    def test_is_an_instance(self):
        """Method that check if FileStorageInstance is an instance
        of FileStorage()
        """
        FileStorageInstance = FileStorage()
        self.assertIsInstance(FileStorageInstance, FileStorage)

if __name__ == '__main__':
    unittest.main()
