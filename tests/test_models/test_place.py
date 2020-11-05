#!/usr/bin/python3
"""
    tests Place
"""
from models.place import Place
import unittest
import datetime
import time
import os
import json
from models import storage


class Test_place(unittest.TestCase):
    """Create class Test_place"""

    def test_doc(self):
        """ Tests docstring """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def testattr(self):
        """ Tests attributes """
        base = Place()
        base.name = "Didier"
        self.assertAlmostEqual(base.name, "Didier")
        base.number = 52000
        self.assertAlmostEqual(base.number, 52000)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

    def testtype(self):
        """ Test type class """
        base = Place()
        self.assertAlmostEqual(type(base), Place)
