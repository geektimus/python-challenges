"""
Utility functions for working with sets.
"""

def set_intersection(s1, s2):
    """
    Find the intersection of two sets.

    Args:
        s1 (set): First set
        s2 (set): Second set

    Returns:
        set: A new set containing elements present in both input sets
    """
    return s1 & s2


def get_elements_list(s):
    """
    Convert a set to a list.

    Args:
        s (set): The set to convert

    Returns:
        list: A list containing all elements from the set
    """
    return list(s)