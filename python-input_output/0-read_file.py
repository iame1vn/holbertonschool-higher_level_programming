#!/usr/bin/python3
"""Read a UTF-8 file and print its content"""

def read_file(filename=""):
    """Reads a file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
