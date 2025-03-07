"""
Utility functions for working with dictionaries.
"""

def contains_key(d, key):
    """
    Check if a dictionary contains a specific key.

    Args:
        d (dict): The dictionary to check
        key: The key to search for

    Returns:
        bool: True if the key exists in the dictionary, False otherwise
    """
    return key in d