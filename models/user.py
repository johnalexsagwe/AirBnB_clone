#!/usr/bin/python3

"""
Module defining the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a user in the Airbnb clone.
    Attributes:
    - email: User's email address
    - password: User's password
    - first_name: User's first name
    - last_name: User's last name
    """
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
