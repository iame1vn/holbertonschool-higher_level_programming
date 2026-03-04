#!/usr/bin/env python3
"""
CSV to JSON conversion module
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV file data into JSON format and writes it to data.json.

    Parameters:
    csv_filename (str): The name of the CSV file.

    Returns:
    bool: True if successful, False otherwise.
    """
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        # Write JSON file
        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, PermissionError, OSError):
        return False
