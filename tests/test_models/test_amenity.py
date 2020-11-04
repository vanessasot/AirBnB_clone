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

    def testattr(self):
        """ Tests attributes """
        base = Amenity()
        base.name = "Didier"
        self.assertAlmostEqual(base.name, "Didier")
        base.number = 52000
        self.assertAlmostEqual(base.number, 52000)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
