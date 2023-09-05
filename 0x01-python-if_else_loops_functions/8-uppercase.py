#!/usr/bin/python3
# 8-uppercase.py

def uppercase(characterinsert):
    """Print a string in uppercase."""
    for charac in characterinsert:
        if ord(charac) >= 97 and ord(charac) <= 122:
            charac = chr(ord(charac) - 32)
        print("{}".format(charac), end="")
    print("")
