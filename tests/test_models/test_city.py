#!/usr/bin/python3
"""
    tests City
"""
from models.city import City
import unittest
import datetime
import time
import os
import json
from models import storage


class Test_city(unittest.TestCase):
    """Create class Test_city"""

    def test_doc(self):
        """ Tests docstring """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def testattr(self):
        """ Tests attributes """
        base = City()
        base.name = "Didier"
        self.assertAlmostEqual(base.name, "Didier")
        base.number = 52000
        self.assertAlmostEqual(base.number, 52000)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

    def testtype(self):
        """ Test type class """
        base = City()
        self.assertAlmostEqual(type(base), City)
