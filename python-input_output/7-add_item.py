#!/usr/bin/python3
"""Add all command line arguments to a Python list and save to a JSON file"""

import sys
from python-input_output.save_to_json_file import save_to_json_file
from python-input_output.load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command line arguments (skip the script name)
items.extend(sys.argv[1:])

save_to_json_file(items, filename)
