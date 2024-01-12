#!/usr/bin/python3

"""
Module that creates a Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a review in the Airbnb clone.

    Attributes:
        - place_id: ID of the place being reviewed
        - user_id: ID of the user who created the review
        - text: Review text
    """
    place_id = ""
    user_id = ""
    text = ""
