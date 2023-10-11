#!/usr/bin/python3
"""Defines a JSON files content function."""
import json


def save_to_json_file(my_obj, filename):
    """write an obj f in the json form"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)