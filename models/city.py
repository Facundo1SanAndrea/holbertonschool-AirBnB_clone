#!/usr/bin/python3
"""class of city"""

import models


from models.base_model import BaseModel

class City(BaseModel):
    """a class for the type of city"""
    state_id = ""
    name = ""