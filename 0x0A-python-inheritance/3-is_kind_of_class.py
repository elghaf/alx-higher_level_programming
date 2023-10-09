#!/usr/bin/python3
"""Same class or inherit method checker"""


def is_kind_of_class(obj, a_class):
    """Returns True if obbj is instance or sub
    otherwise False."""
    return isinstance(obj, a_class)
