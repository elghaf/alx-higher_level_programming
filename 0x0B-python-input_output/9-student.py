#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, ages):
        """Initialize a new Student.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = ages

    def to_json(self):
        """dict get"""
        return self.__dict__
