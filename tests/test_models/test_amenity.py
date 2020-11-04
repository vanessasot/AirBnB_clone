#!/usr/bin/python3
"""
    tests amenity
"""
from models.amenity import Amenity
import unittest
import datetime
import time
import os
import json
from models import storage


class Test_Amenity(unittest.TestCase):
    """Create class Test_Amenity"""

    def test_doc(self):
        """ Tests docstring """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
