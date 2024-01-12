#!/usr/bin/python3

"""
Module containing test cases for the BaseModel class
"""

import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test methods by initializing an instance of BaseModel.
        """
        self.instance = BaseModel()

    def tearDown(self):
        """
        Tear down the test method by deleting the BaseModel instance.
        """
        del self.instance

    def test_init_with_attribute(self):
        """
        Test initializing BaseModel with specific attributes using kwargs.
        """
        kwargs = {
            'name': 'John',
            'age': 35,
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T00:00:00.000000'
        }
        instance = BaseModel(**kwargs)

        # Check if attributes are set correctly
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 35)
        self.assertEqual(
            instance.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(
            instance.updated_at, datetime(2023, 1, 2, 0, 0, 0))

    def test_str_representation(self):
        """
        Test string representation of the BaseModel instance.
        """
        str_repr = str(self.instance)

        expected_str = "[BaseModel] ({}) {}".format(
            self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), expected_str)

    def test_save_method(self):
        """
        Test that the save method updates
        the updated_at attribute and saves the object.
        """
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(new_updated_at, datetime)

    def test_unique_ids(self):
        """
        Test that BaseModel instances have unique ids.
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertIsInstance(base_model_1.id, str)
        self.assertIsInstance(base_model_2.id, str)
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_to_dict(self):
        """
        Test to_dict method to ensure the correct conversion.
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIn('created_at', obj_dict)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_pep8_conformance(self):
        """
        Test that the BaseModel class conforms to PEP 8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style violations found")

    def test_docstring_exists(self):
        """
        Test if docstring exists in BaseModel class.
        """
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
