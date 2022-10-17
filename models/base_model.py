#!/usr/bin/python3
"""Class for a base modle"""
import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """A class of a base model """

    def __init__(self, *args, **kwargs):
        """public instance attribute"""
        forma_t = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, forma_t)
                elif key == 'updatedd_at':
                    self.updatedd_at = datetime.strptime(value, forma_t)
                elif key == 'name':
                    self.name = value
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updatedd_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Prints tha name, id and dict"""
        return (f"[{self.__class__.__name__}] ({self.id} {self.__dict__}")

    def save(self):
        """updateds the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updatedd_at"] = self.updatedd_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
