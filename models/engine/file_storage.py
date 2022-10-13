#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON"""

import json
from os import path
import os
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return __class__.__objects

    def new(self, obj):
        """sets in the obj the class name id"""
        __class__.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file_json:
            json.dump(new_dict, file_json)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file_json:
                this_dict = json.loads(file_json)
                for key, value in this_dict.items():

                    self.new(eval(value['__class__'])(**value))
