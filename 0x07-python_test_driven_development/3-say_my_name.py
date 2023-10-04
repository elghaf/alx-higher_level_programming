#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function.

This module contains a function `say_my_name` that takes two arguments, `first_name` and `last_name`, both of which are expected to be strings. The function prints a formatted message containing the provided names.

Functions:
    say_my_name(first_name, last_name="") -- Print a name.

Args:
    first_name (str): The first name to print.
    last_name (str, optional): The last name to print (default is an empty string).

Raises:
    TypeError: If either `first_name` or `last_name` are not strings.

Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Alice")
    My name is Alice
"""
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
