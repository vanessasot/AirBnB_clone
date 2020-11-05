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
import models


class Test_user(unittest.TestCase):
    """this will test the User class"""

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

    def test_updated_at(self):
        """
            test updated_at
        """
        base = User()
        create = str(base.created_at)
        start = str(base.updated_at)
        base.name = "Didier"
        base.save()
        self.assertNotEqual(str(base.updated_at), start)
        self.assertEqual(str(base.created_at), create)

    def test_to_dict(self):
        """ Tests dict """
        base = User()
        base2 = base.to_dict()
        self.assertEqual(base2["updated_at"], base.updated_at.isoformat())
        self.assertEqual(base2["__class__"], "User")
        self.assertNotIn("__class__", base.__dict__)

    def test_save(self):
        """ Tests save """
        base = User()
        base.save()
        with open("file.json", mode="r", encoding="UTF-8") as f:
            d = json.load(f)
        for item in d:
            if base.id in item:
                d = d[item]
        self.assertDictEqual(d, base.to_dict())

    def test_new_model_dict(self):
        """ Tests new model with dictionary """
        base = User()
        dict1 = base.to_dict()
        base2 = User(**dict1)
        self.assertFalse(base is base2)
        self.assertDictEqual(base.to_dict(), base2.to_dict())

    def test_instace(self):
        """ test instance """
        test1 = User()
        self.assertIsInstance(test1, User)

    def test_permissions(self):
        """ test permissions """
        self.assertTrue(os.access("models/user.py", os.X_OK))
        self.assertTrue(os.access("models/user.py", os.R_OK))
        self.assertTrue(os.access("models/user.py", os.W_OK))
        self.assertTrue(os.access("models/user.py", os.F_OK))

    def test_ids_maker(self):
        """ test to generate unique id """
        user1_id = User()
        user2_id = User()
        self.assertNotEqual(user1_id, user2_id)

if __name__ == '__main__':
    unittest.main()
