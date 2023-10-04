#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function.

This module contains a function `print_square` that takes an integer `size` as an argument. The function prints a square using the '#' character, with both the height and width of the square equal to the specified `size`.

Functions:
    print_square(size) -- Print a square with the '#' character.

Args:
    size (int): The height and width of the square.

Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than 0.

Example:
    >>> print_square(5)
    #####
    #####
    #####
    #####
    #####
"""
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
