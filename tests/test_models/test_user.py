#!/usr/bin/python3
"""
    tests User
"""
from models.user import User
import unittest
import datetime
import time
import os
import json
from models import storage


class Test_user(unittest.TestCase):

    def test_doc(self):
        """ Tests docstring """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def testattr(self):
        """ Tests attributes """
        base = User()
        base.name = "Didier"
        self.assertAlmostEqual(base.name, "Didier")
        base.number = 52000
        self.assertAlmostEqual(base.number, 52000)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

    def testtype(self):
        """ Test type class """
        base = User()
        self.assertAlmostEqual(type(base), User)
