#!/usr/bin/python3
"""Class for a base modle"""
from datetime import datetime

import uuid

import models

import json

class BaseModel:
    """A class of a base modle"""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for i in kwargs:
                if i == 'id':
                    self.id = str(kwargs[i])
                if i == 'created_at':
                    time_now = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = time_now
                if i == 'updated_at':
                    update_time = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    self.update_at = update_time
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.update_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Prints tha name, id and dict"""
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        self.created_at = self.created_at.isoformat()
        self.update_at = self.update_at.isoformat()
        new_dict = self.__dict__
        new_dict["__class__"] = __class__.__name__
        return new_dict
