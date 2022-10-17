#!/usr/bin/python3
"""a clas for the review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a classs for the inhertance of basemodels"""

    place_id = ""
    user_id = ""
    text = ""
