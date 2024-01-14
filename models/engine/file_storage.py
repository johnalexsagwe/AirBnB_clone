#!/usr/bin/python3
"""
FileStorage class provides methods for storing, retrieving,
and saving objects to/from a JSON file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    The FileStorage class manages the storage of objects to a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects.

    Methods:
        all(self): Return all stored objects.
        new(self, obj): Add a new object to __objects.
        save(self): Serialize objects to JSON file.
        reload(self): Deserialize JSON file and load data into __objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return a dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the objects in __objects to a JSON file.
        """
        dictionary = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=2)

    def reload(self):
        """
        Deserialize the JSON file and load data into __objects.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fd:
                dict_json = json.load(fd)
                for key, value in dict_json.items():
                    class_name = value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
