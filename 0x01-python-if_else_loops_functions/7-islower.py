#!/usr/bin/python3
# 7-islower.py

def islower(characterinsert):
    """lowercase check"""
    if ord(characterinsert) >= 97 and ord(characterinsert) <= 122:
        return True
    else:
        return False
