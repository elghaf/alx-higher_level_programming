#!/usr/bin/python3

"""method module"""

def inherits_from(obj, a_class):
    """Returns True if obj is sub or instance,
    otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
