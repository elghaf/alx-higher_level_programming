#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function.

This module contains a function `matrix_divided` that takes a matrix and a divisor as arguments, and returns a new matrix representing the result of dividing all elements in the original matrix by the divisor. The function performs several checks to ensure the input is valid and handles various exceptions.

Functions:
    matrix_divided(matrix, div) -- Divide all elements of a matrix by a divisor.

Args:
    matrix (list): A list of lists containing integers or floats, representing the matrix.
    div (int/float): The divisor to divide each element of the matrix.

Raises:
    TypeError: If the matrix is not a list of lists of integers or floats.
    TypeError: If the matrix contains rows of different sizes.
    TypeError: If the divisor is not an int or float.
    ZeroDivisionError: If the divisor is 0.

Returns:
    A new matrix representing the result of the division, with elements rounded to two decimal places.
"""
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
