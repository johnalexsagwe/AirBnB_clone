#!/usr/bin/python3
"""
Test cases for City class
"""
from datetime import datetime
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test City class functionality
    """

    def setUp(self):
        """
        Create an instance of the City class and assign it
        to the self.city attribute
        """
        self.city = City()

    def test_attribute_types(self):
        """
        Verify attribute types in the City instance
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inheritance(self):
        """
        Check if City inherits from BaseModel
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        Confirm default attribute values in the City instance
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_updated_at(self):
        """
        Check if the updated_at attribute is set to the current time
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_created_at(self):
        """
        Verify if created_at attribute is set to the current time
        """
        self.assertIsInstance(self.city.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
