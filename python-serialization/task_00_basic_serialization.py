#!/usr/bin/env python3
"""
Basic JSON serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The name of the file where data will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it
    back into a Python dictionary.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
