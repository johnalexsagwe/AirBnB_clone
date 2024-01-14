#!/usr/bin/python3
"""
Unit tests for the User class
Execute: python3 -m unittest discover tests
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class
    """
    def setUp(self):
        """
        Set up an instance of the User class for testing
        """
        self.user = User()

    def test_inheritance(self):
        """
        Test if User inherits from BaseModel
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_default_attributes(self):
        """
        Test the default attribute values of User
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
