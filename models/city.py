#!/usr/bin/python3
"""
Module defining the City class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class representing a city in the Airbnb clone.

    Public Attributes:
        - state_id (str): ID of the state to which the city belongs
        - name (str): Name of the city
    """
    state_id = ""
    name = ""
