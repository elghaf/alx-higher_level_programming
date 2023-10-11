#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename: The name.
        text: The text.
    Returns:
        Num of character.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
