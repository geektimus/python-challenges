"""
Main entry point for the Python Challenges application.

This module demonstrates the usage of various utility functions and algorithms
implemented in the project.
"""

from src.utils.dict_utils import contains_key
from src.challenges.algorithms import is_palindrome, count_words


def main():
    """
    Execute demonstration code for Python Challenges.
    
    This function shows examples of using the various functions and utilities
    provided by the Python Challenges package.
    
    Returns:
        None
    """
    print("Python Challenges")
    print("----------------")

    # Example usage
    print(f"'racecar' is a palindrome: {is_palindrome('racecar')}")
    print(f"'hello' is a palindrome: {is_palindrome('hello')}")

    word_count = count_words("Hello world hello")
    print(f"Word count: {word_count}")

    test_dict = {'a': 1, 'b': 2}
    print(f"Dictionary contains key 'a': {contains_key(test_dict, 'a')}")
    print(f"Dictionary contains key 'c': {contains_key(test_dict, 'c')}")


if __name__ == "__main__":
    main()
