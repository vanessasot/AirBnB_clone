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

    def test_updated_at(self):
        """
            test updated_at
        """
        base = City()
        create = str(base.created_at)
        start = str(base.updated_at)
        base.name = "Didier"
        base.save()
        self.assertNotEqual(str(base.updated_at), start)
        self.assertEqual(str(base.created_at), create)

    def test_to_dict(self):
        """ Tests dict """
        base = City()
        base2 = base.to_dict()
        self.assertEqual(base2["updated_at"], base.updated_at.isoformat())
        self.assertEqual(base2["__class__"], "City")
        self.assertNotIn("__class__", base.__dict__)

    def test_save(self):
        """ Tests save """
        base = City()
        base.save()
        with open("file.json", mode="r", encoding="UTF-8") as f:
            d = json.load(f)
        for item in d:
            if base.id in item:
                d = d[item]
        self.assertDictEqual(d, base.to_dict())

    def test_new_model_dict(self):
        """ Tests new model with dictionary """
        base = City()
        dict1 = base.to_dict()
        base2 = City(**dict1)
        self.assertFalse(base is base2)
        self.assertDictEqual(base.to_dict(), base2.to_dict())


if __name__ == '__main__':
    unittest.main()