#!/usr/bin/python3
"""
Initialize and reload data for FileStorage in the Airbnb clone.

This script creates an instance of the FileStorage class and reloads
data from the JSON file, allowing seamless access to Airbnb-related
objects in the application.
"""

from models.engine import file_storage
"""
Create an instance of FileStorage
"""
storage = file_storage.FileStorage()
"""
Reload data from the JSON file
"""
storage.reload()
