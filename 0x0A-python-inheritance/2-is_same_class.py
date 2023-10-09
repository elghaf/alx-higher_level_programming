#!/usr/bin/python3
"""Method to check class"""


def is_same_class(obj, a_class):
    """Check if the sam obj
    args:
        obj: object import
        a_class: class type
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
