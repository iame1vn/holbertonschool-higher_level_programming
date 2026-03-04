#!/usr/bin/env python3
"""
Pickling Custom Classes
"""

import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Returns True if successful, None if an error occurs.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except (FileNotFoundError, PermissionError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file into an instance of CustomObject.

        Returns the object if successful, None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)

            # Ensure the loaded object is actually CustomObject
            if isinstance(obj, cls):
                return obj
            return None

        except (FileNotFoundError, PermissionError,
                pickle.UnpicklingError, EOFError, OSError):
            return None
