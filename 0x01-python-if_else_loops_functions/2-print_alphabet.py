#!/usr/bin/python3
# 2-print_alphabet.py

"""Write a program that prints the ASCII alphabet,
in lowercase, not followed by a new line.
"""
for index_i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(index_i), end="")
