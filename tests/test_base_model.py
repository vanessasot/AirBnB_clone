#!/usr/bin/python3
from os.path import basename
from models.base_model import BaseModel
import unittest
from models import storage
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """ base model test

    Args:
        unittest (base class)
    """
    def test_doc(self):
        """test for documentation
        """
        base = BaseModel()
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(base.__doc__)
        self.assertIsNotNone(base.__init__.__doc__)
        self.assertIsNotNone(base.save.__doc__)
        self.assertIsNotNone(base.to_dict.__doc__)
        self.assertIsNotNone(base.__str__.__doc__)

    def test_attr(self):
        """create new attributes test
        """
        base = BaseModel()
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
        base = BaseModel()
        a = str(base.updated_at)
        b = str(base.created_at)
        base.name = "Didier"
        base.save()
        self.assertNotEqual(str(base.updated_at), a)
        self.assertEqual(str(base.created_at), b)

    def test_to_dict(self):
        """ Tests the dictionary """
        base = BaseModel()
        base2 = base.to_dict()
        self.assertEqual(base2["updated_at"], base.updated_at.isoformat())
        self.assertEqual(base2["__class__"], "BaseModel")
        self.assertNotIn("__class__", base.__dict__)

    def test_save(self):
        """ Tests the save method """
        base = BaseModel()
        base.save()
        with open("file.json", mode="r", encoding="UTF-8") as f:
            d = json.load(f)
        for item in d:
            if base.id in item:
                d = d[item]
        self.assertDictEqual(d, base.to_dict())

    def test_save_andrew_kali_suggestion(self):
        """
            test save using method provided by peer in Bog
            not our own test
        """
        o = BaseModel()
        n = datetime.datetime.now().replace(microsecond=0)
        o.save()
        self.assertEqual(o.updated_at.replace(microsecond=0), n)

    def test_new_model_from_dict(self):
        """ Tests createion of new model with dictionary """
        base = BaseModel()
        m1_dict = base.to_dict()
        base2 = BaseModel(**m1_dict)
        self.assertFalse(base is base2)
        self.assertDictEqual(base.to_dict(), base2.to_dict())


if __name__ == '__main__':
    unittest.main()
