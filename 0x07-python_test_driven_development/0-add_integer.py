#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function for adding integers.

This module contains a function `add_integer` that takes two arguments, `a` and `b`, and returns their integer sum. If either of the arguments is a float, it is typecasted to an integer before the addition is performed.

Functions:
    add_integer(a, b=98) -- Add two integers or typecasted floats and return the result.

Raises:
    TypeError: If either `a` or `b` is not an integer or float.
"""
def add_integer(a, b=98):
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
