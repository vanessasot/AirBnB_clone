#!/usr/bin/python3
from os.path import basename
from models.base_model import BaseModel
import unittest
from models import storage
import datetime
base = BaseModel()



class TestBaseModel(unittest.TestCase):
    """ base model test

    Args:
        unittest (base class)
    """
    def test_doc(self):
        """test for documentation
        """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(base.__doc__)
        self.assertIsNotNone(base.__init__.__doc__)
        self.assertIsNotNone(base.save.__doc__)
        self.assertIsNotNone(base.to_dict.__doc__)
        self.assertIsNotNone(base.__str__.__doc__)

    def test_attr(self):
        """create new attributes test
        """
        base.name = "Vanessa"
        self.assertAlmostEqual(base.name, "Vanessa")
        base.number = 52000
        self.assertEqual(type(base.id), str)
        self.assertAlmostEqual(base.number, 52000)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)

    def test_update(self):
        """properly update
        """
        a = str(base.updated_at)
        b = str(base.created_at)
        base.name = "Didier"
        base.save()
        self.assertNotEqual(str(base.updated_at), a)
        self.assertEqual(str(base.created_at), b)



if __name__ == '__main__':
    unittest.main()
