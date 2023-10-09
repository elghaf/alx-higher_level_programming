#!/usr/bin/python3
"""
Attribute lookup
"""


def lookup(obj):
    """Class lookup

    Args:
        obj: object class
    Returns:
        Na
    """
    return [i for i in dir(obj)]
