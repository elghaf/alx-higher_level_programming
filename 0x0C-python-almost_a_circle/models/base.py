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
