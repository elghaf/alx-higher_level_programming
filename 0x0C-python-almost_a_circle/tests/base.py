#!/usr/bin/python3

"""Defines a base class."""

class Base:
    """
    Base class:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id= None)
    
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
    