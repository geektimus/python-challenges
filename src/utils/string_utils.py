"""
Utility functions for string manipulation and processing.
"""

def reverse_string(s):
    """
    Reverse a string using Python's slice notation.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string
    """
    return s[::-1]


def reverse_string_without_slicing(s):
    """
    Reverse a string using the built-in reversed function and join.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string
    """
    return ''.join(reversed(s))


def reverse_string_without_slicing_and_join(s):
    """
    Reverse a string using a list comprehension and range.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string
    """
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))