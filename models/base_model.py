#!/usr/bin/python3
"""
The module is the base of all the classes
it defines all common attributes and methods
for other classes
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base model defining shared attributes and methods for other classes.
    """

    def __init__(self, *unused_args, **kwargs):
        """
        Initializes BaseModel.

        Args:
            *unused_args: Unused variable length arguments.
            **kwargs: Attribute names and values.

        Example:
            # Using kwargs to set attributes for an Airbnb-related instance
            airbnb_instance =
            BaseModel
            (location="CBD", price=100, amenities=["Wi-Fi", "Parking"])
        """

        if not kwargs or 'id' not in kwargs:
            """generating random uuid and converting to a string format"""
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                    )
            self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                    )
            for k, v in kwargs.items():
                if k not in ['updated_at', 'created_at', '__class__']:
                    self.__setattr__(k, v)

    def __str__(self):
        """
        Generates a descriptive string summarizing
        the listing or user information.

        Returns:
        A string containing:
        - Class name (e.g., `Listing` or `User`)
        - Key attributes like `title`, `location`, or `username`
        - Relevant IDs (e.g., listing ID or user ID) if applicable

        Example:
        # Assuming a listing with ID 14 and host ID 5678
        str(my_listing)
        # Output: "<Listing> ID: 14
        -Beachfront Studio in Diani (hosted by ID: 5678)"
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        updates the public instance attribute
        This method is responsible for updating
        the 'updated_at' attribute
        with the current datetime and
        saving the object's state.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Return-:
        a dictionary that mirrors the object's attributes,
        including its class name,
        while formatting timestamps as ISO strings.
        """

        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()

        return data_dict
