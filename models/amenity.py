#!/usr/bin/python3
"""module creates a Amenity class which inherites from base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity in the Airbnb clone.

    Attributes:
        - name (str): Name of the amenity
    """
    name = ""
