#!/usr/bin/python3
"""Defines a content reading json function."""
import json


def load_from_json_file(filename):
    """creation obj with json form"""
    with open(filename) as f:
        return json.load(f)