#!/usr/bin/python3
from os.path import basename
from models.base_model import BaseModel
import unittest
from models import storage
import datetime


class TestBaseModel(unittest.TestCase):
    """ base model test

    Args:
        unittest (base class)
    """
    def test_doc(self):
        """test for documentation
        """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

if __name__ == '__main__':
    unittest.main()
