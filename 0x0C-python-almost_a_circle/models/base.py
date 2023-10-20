#!/usr/bin/python3

"""Defines a base class."""

import json

class Base:
    """
    Base class:
    Private class attributes:
        __nb_objects (int): Number of how many time instantiate class Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        filename = f"{cls.__name__}.json"
        json_list = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w") as file:
            file.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string to a list"""
        return json.loads(json_string) if json_string else []
