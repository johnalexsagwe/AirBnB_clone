#!/usr/bin/python3

"""
Unit tests for the Review class
Execute all tests: python3 -m unittest discover tests*
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
    """

    def setUp(self):
        """
        Create an instance of the Review class
        """
        self.review = Review()

    def test_inheritance(self):
        """
        Test if Review inherits from BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_module_docstring(self):
        """
        Test if there is a docstring for the Review module
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_type_of_attributes(self):
        """
        Test the types of attributes to ensure correctness
        """
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)

    def test_updated_time(self):
        """
        Test the updated time of the review after calling the save method
        """
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(new_updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
