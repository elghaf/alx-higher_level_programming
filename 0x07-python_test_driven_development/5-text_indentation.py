#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function.

This module contains a function `text_indentation` that takes a string `text` as an argument and prints the text with two new lines after each '.', '?', and ':'. It also handles leading spaces in the text.

Functions:
    text_indentation(text) -- Print text with two new lines after each '.', '?', and ':'.

Args:
    text (str): The text to print.

Raises:
    TypeError: If `text` is not a string.

Example:
    >>> text = "This is a sample text. It contains sentences? With colons: like this."
    >>> text_indentation(text)
    This is a sample text.

    It contains sentences?

    With colons: like this.
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
