#!/usr/bin/python3
""" storage file AirBnB
"""
import json
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