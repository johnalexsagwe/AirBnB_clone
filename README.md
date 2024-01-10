# AirBnB_clone
# AirBnB Clone - The Console

**Group Project**
- **Language:** Python
- **Concepts:** Object-Oriented Programming (OOP), Python packages, AirBnB clone
- **By:** Guillaume
- **Weight:** 5
- **Team:** John Alex Sagwe
- **Project Duration:** Jan 8, 2024, 6:00 AM - Jan 15, 2024, 6:00 AM
- **Checker Release:** Jan 13, 2024, 12:00 PM

## Project Overview
This is the initial stage of the AirBnB clone project. The goal is to build a command interpreter to manage AirBnB objects. The project involves creating Python classes, serialization/deserialization, and implementing a simple storage engine. The tasks cover various aspects of Python programming and web development.

## Learning Objectives
By the end of this project, participants are expected to understand:
- Creating a Python package
- Developing a command interpreter using the cmd module
- Implementing Unit testing in a large project
- Serializing and deserializing a Class
- Writing and reading JSON files
- Managing datetime, UUID, *args, and **kwargs
- Handling named arguments in a function

## Requirements
- Python Scripts
  - Editors: vi, vim, emacs
  - Ubuntu 20.04 LTS, Python 3.8.5
  - pycodestyle (version 2.8.*)
  - Documentation for modules, classes, and functions
- Python Unit Tests
  - unittest module
  - Test files organized in a folder structure
  - Documentation for modules, classes, and functions
- GitHub
  - One project repository per group
  - README.md, AUTHORS file

## Project Structure
1. README, AUTHORS
   - Description of the project
   - Description of the command interpreter
   - How to start and use it
   - Examples
   - Authors listed in the AUTHORS file

2. Be pycodestyle compliant!
   - Write clean code that passes pycodestyle checks.

3. Unittests
   - Test all files, classes, and functions using unittests.

4. BaseModel
   - Define a BaseModel class with common attributes/methods.
   - Implement serialization/deserialization methods.

5. Create BaseModel from dictionary
   - Recreate an instance from a dictionary representation.

6. Store first object
   - Implement FileStorage class for serializing instances to a JSON file.
   - Link BaseModel to FileStorage.

7. Console 0.0.1
   - Implement a command interpreter using the cmd module.
   - Commands: quit, help, custom prompt.

8. Console 0.1
   - Add commands: create, show, destroy, all, update.
   - Handle various scenarios for missing or invalid inputs.

## Execution
Interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
