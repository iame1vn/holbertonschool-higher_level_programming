#!/usr/bin/python3
"""Defines a Student class with JSON serialization"""


class Student:
    """Student class with public attributes and to_json method"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the Student"""
        return self.__dict__
