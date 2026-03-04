#!/usr/bin/python3
"""Return the dictionary description with simple data structure of an object"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization"""
    return obj.__dict__
