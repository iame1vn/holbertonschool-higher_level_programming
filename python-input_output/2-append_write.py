#!/usr/bin/python3
"""Append a string to a UTF-8 text file and return the number of characters"""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
