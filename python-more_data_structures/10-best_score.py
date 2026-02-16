#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the biggest value in a dictionary."""
    if not a_dictionary:
        return None
    best = max(a_dictionary, key=a_dictionary.get)
    return best
