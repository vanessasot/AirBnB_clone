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
                        and it will be updated every time you change your object
            """

        if len(kwargs) is 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

        else:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        %Y-%m-%dT%H:%M:%S.%f)
                elif "update_at" == key:
                    self.created_at = datetime.strptime(kwargs["update_at"],
                                                        %Y-%m-%dT%H:%M:%S.%f)
                elif key is "__class__":
                    pass
                else:
                    setattr(self, key, val)

    def __str__(self):
        """ Return string
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):

    def to_dict(self):