#!/usr/bin/python3
"""Defines a Student class with filtered JSON serialization"""


class Student:
    """Student class with public attributes and to_json method"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance

        If attrs is a list of strings, only attribute names in this list
        are included. Otherwise, all attributes are returned.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__.copy()
        filtered = {}
        for key in attrs:
            if key in self.__dict__:
                filtered[key] = self.__dict__[key]
        return filtered
