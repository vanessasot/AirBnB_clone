#!/usr/bin/python3
""" storage file AirBnB
"""
import json
import models
from os import path
from models.base_model import BaseModel

class FileStorage():
    """ class command interpreter
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dict = objects
        """
        return self.__objects

    def new(self, obj):
        if obj:
            FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                      obj.id)] = obj

    def save(self):
        """save(self): serializes __objects
        to the JSON file (path: __file_path)
        """
        object_tf = {}
        for key, val in self.__objects.items():
            object_tf[key] = val.to_dict()


        with open(self.__file_path, 'w', encoding="utf-8") as fd:
                json.dump(object_tf, fd)

    def reload(self):
        if not path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new = json.load(f)
            for key, obj in new.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
