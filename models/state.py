#!/usr/bin/python3

"""
Module defining the State class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a geographical state in the Airbnb clone.

    Attributes:
        - name: Name of the state
    """
    name = ""
