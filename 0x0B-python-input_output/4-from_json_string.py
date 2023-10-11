#!/usr/bin/python3
"""JSON  repr function."""
import json


def from_json_string(my_str):
    """Return the obj in json rep"""
    return json.loads(my_str)
