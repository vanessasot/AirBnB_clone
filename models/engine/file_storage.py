#!/usr/bin/python3
""" storage file AirBnB
"""
import json
import models
from models.base_model import BaseModel

class FileStorage():
    """ class command interpreter
    """

    def __init__(self):
        """ initializate filestorage
        """
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """ return dict = objects
        """
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__,
                                      obj.id)] = obj

    def save(self):
        """save(self): serializes __objects
        to the JSON file (path: __file_path)
        """
        object_tf = {}
        for key, val in self.__objects.items():
            object_tf[key] = val.to_dict()


        with open(self.__file_path, 'w', encoding="utf-8") as fd:
                json.dumps(fd)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new = json.load(f)
                for key, obj in new.items():
                    self.__objects[key] = new

        except:
            pass
