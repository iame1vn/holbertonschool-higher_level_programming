#!/usr/bin/env python3
"""
XML serialization and deserialization module
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format
    and writes it to a file.

    Parameters:
    dictionary (dict): Dictionary to serialize
    filename (str): Output XML filename
    """
    # Root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML from file and deserializes it
    into a Python dictionary.

    Parameters:
    filename (str): Input XML filename

    Returns:
    dict: Deserialized dictionary or None if error
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
