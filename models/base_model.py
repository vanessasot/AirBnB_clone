#!/usr/bin/python3

"""module BaseModel
    is a parent of all class
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """class base of all proyect
    """
    def __init__(self, *args, **kwargs):
        """ initializate class with UUID and
            created_at:
                    datetime - assign with the current\
                    datetime when an instance is created
            updated_at:
                    datetime - assign with the current\
                        datetime when an instance is created
                        and it will be updated every time you\
                        change your object
            """

        if len(kwargs) is 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif not key == "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """ Return string
        """
        name = self.__class__.__name__
        dic = self.__dict__
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ save
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ create a dict
        """
        n_dict = dict(self.__dict__)
        n_dict["__class__"] = self.__class__.__name__
        n_dict["created_at"] = self.created_at.isoformat()
        n_dict["updated_at"] = self.updated_at.isoformat()
        return n_dict
