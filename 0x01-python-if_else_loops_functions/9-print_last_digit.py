#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(numbersinsert):
    """Print the last digit of a number and return it."""
    print(abs(numbersinsert) % 10, end="")
    return (abs(numbersinsert) % 10)
