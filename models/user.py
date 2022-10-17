#!/usr/bin/python3
"""A users class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Auser sub class for the base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
