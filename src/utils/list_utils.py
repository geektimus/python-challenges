"""
Utility functions for working with lists.
"""

def sum_numbers_in_list(numbers):
    """
    Calculate the sum of numbers in a list using Python's built-in sum function.

    Args:
        numbers (list): A list of numbers to sum

    Returns:
        int or float: The sum of all numbers in the list
    """
    return sum(numbers)


def sum_numbers_in_list_without_sum(numbers):
    """
    Calculate the sum of numbers in a list using a manual loop.

    Args:
        numbers (list): A list of numbers to sum

    Returns:
        int or float: The sum of all numbers in the list
    """
    total = 0
    for number in numbers:
        total += number
    return total