#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename: The name.
        text: The text.
    Returns:
        Num of caracter
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
