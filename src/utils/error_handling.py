"""
Utility functions for demonstrating error handling in Python.
"""

def divide(a, b):
    """
    Safely divide two numbers with error handling.

    Args:
        a (float): The numerator
        b (float): The denominator

    Returns:
        float: The result of a/b, or None if b is 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
        return None