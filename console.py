#!/usr/bin/python3

"""
Module for Command Line Interpreter
"""

import cmd
import json
import re
import shlex
import ast
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage

# Global variables
class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

function_list = [
    "all",
    "show",
    "create",
    "update",
    "destroy",
    "count"
]


class HBNBCommand(cmd.Cmd):
    """
    This class defines console functions
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Handles an empty line
        """
        return

    def do_create(self, arg):
        """
        Create command to create an instance of a class
        """
        args_list = parse(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif (args_list[0] not in class_dict):
            print("** class doesn't exist **")
        else:
            instance = class_dict[args_list[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance \
        based on the class name and id
        Usage: <class name>.show(<id>)
        Usage: show <class name> <id>
        """
        args_list = parse(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif (args_list[0] not in class_dict):
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif (f"{args_list[0]}.{args_list[1]}"
              ) not in storage.FileStorage_objects:
            print("** no instance found **")
        else:
            print(
                storage.FileStorage_objects[
                    f"{args_list[0]}.{args_list[1]}"])

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance \
        based on the class name and id
        Usage: <class name>.destroy(<id>)
        Usage: destroy <class name> <id>
        """
        args_list = parse(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif (args_list[0] not in class_dict):
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif (f"{args_list[0]}.{args_list[1]}"
              ) not in storage.FileStorage_objects:
            print("** no instance found **")
        else:
            del storage.FileStorage_objects[f"{args_list[0]}.{args_list[1]}"]
            storage.save()

    def do_all(self, arg):
        """
        All command to print all string representation of all instances
        Usage: <class name>.all()
        Usage: all <class name>
        where <class name> is optional
        """
        args_list = parse(arg)
        if len(args_list) > 0 and args_list[0] not in class_dict:
            print("** class doesn't exist **")
        else:
            result_list = []
            for key, value in storage.FileStorage_objects.items():
                if len(args_list) == 0:
                    result_list.append(str(value))
                else:
                    if args_list[0] == value.to_dict()["_class_"]:
                        result_list.append(str(value))
            print(result_list)

    def do_count(self, arg):
        """
        Count command to retrieve the number of instances of a class
        Usage: <class name>.count()
        Usage: count <class name>
        where <class name> is optional
        """
        count = 0
        if arg:
            args_list = parse(arg)
            for key, value in storage.FileStorage_objects.items():
                if value._class.__name__ == args_list[0]:
                    count += 1
        else:
            for key in storage.FileStorage_objects.keys():
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Update command to modify an instance based on the class name
        and id by adding or updating attributes.
        Usage: <class name>.update(<id>, <dictionary representation>)
        Usage: <class name>.update(<id>, <attribute name>, <attribut
        value>)
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args_list = parse(arg)
        if len(args_list) == 0:
            print("** class name missing **")
        elif (args_list[0] not in class_dict):
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif (f"{args_list[0]}.{args_list[1]}"
              ) not in storage.FileStorage_objects:
            print("** no instance found **")
        elif (len(args_list) < 3):
            print("** attribute name missing **")
        elif (len(args_list) < 4):
            print("** value missing **")
        else:
            setattr(
                storage.FileStorage_objects[f"{args_list[0]}.{args_list[1]}"],
                args_list[2], try_eval(args_list[3])
            )
            instance = storage.FileStorage_objects[
                f"{args_list[0]}.{args_list[1]}"]
            instance.save()

    def default(self, arg):
        """
        Function that takes user input and processes information.
        Usage: <class name>.<function()>
        """
        pattern_reg = r"(.*)\.(.*)\((.*?)\)"
        if re.search(pattern_reg, str(arg)):
            str_arg = re.sub(pattern_reg, r"\2 \1 \3", arg)
            list_arg = parse(str_arg)
            if list_arg[0] in function_list:
                if list_arg[0] == "update":
                    dict_reg = r"({.: \w})"
                    if (re.search(dict_reg, str_arg)):
                        arg_str = re.search(dict_reg, str_arg).group(
                            0).replace("'", '"')
                        arg_dict = json.loads(arg_str)
                        for key, value in arg_dict.items():
                            if type(value) is str:
                                value = "\"" + value + "\""
                            self.do_update("{} {} {} {}".format(
                                list_arg[1],
                                list_arg[2].strip(','),
                                key,
                                value
                            ))
                        else:
                            arg_list = []
                        for elt in list_arg:
                            element = elt.strip(',')
                            if type(element) is str:
                                element = "\"" + element + "\""
                            arg_list.append(element)
                        sentence = ""
                        for word in arg_list[1:]:
                            sentence = sentence + " " + str(word)
                        self.do_update(sentence)
                else:
                    str_arg = str_arg.replace(",", " ")
                    arg = str_arg.split(" ", 1)
                    getattr(self, "do_" + list_arg[0])(arg[1])
            else:
                return syntax_error(arg)
        else:
            return syntax_error(arg)


@staticmethod
def parse(arg):
    """
    Convert a series of zero or more numbers to an argument tuple
    """
    return shlex.split(arg)


@staticmethod
def handle_syntax_error(arg):
    """
    Handles unknown syntax errors
    """
    print("*** Unknown syntax: {}".format(arg))
    return False


@staticmethod
def try_evaluate(value):
    """
    Finds the most appropriate type for value and returns the new value
    """
    try:
        value = ast.literal_eval(value)
    except Exception:
        pass
    return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
