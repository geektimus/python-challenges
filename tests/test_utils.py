"""
Tests for utility functions in the utils package.

This module tests various utility functions from different modules:
- Dictionary utilities
- List utilities
- String utilities
- Error handling utilities
- Set utilities
"""

from src.utils.dict_utils import contains_key
from src.utils.list_utils import sum_numbers_in_list, sum_numbers_in_list_without_sum
from src.utils.string_utils import reverse_string
from src.utils.error_handling import divide
from src.utils.set_utils import set_intersection


class TestDictUtils:
    """Test cases for dictionary utility functions."""

    def test_contains_key(self):
        """Test contains_key function with various keys to check if they exist in a dictionary."""
        d = {'a': 1, 'b': 2}
        assert contains_key(d, 'a') is True
        assert contains_key(d, 'c') is False
        assert contains_key(d, 'b') is True
        assert contains_key(d, 'd') is False


class TestListUtils:
    """Test cases for list utility functions."""

    def test_sum_numbers_in_list(self):
        """Test sum_numbers_in_list function with various list inputs."""
        assert sum_numbers_in_list([1, 2, 3, 4, 5]) == 15
        assert sum_numbers_in_list([]) == 0
        assert sum_numbers_in_list([-1, -2, 3]) == 0

    def test_sum_numbers_in_list_without_sum(self):
        """Test sum_numbers_in_list_without_sum function with various list inputs."""
        assert sum_numbers_in_list_without_sum([1, 2, 3, 4, 5]) == 15
        assert sum_numbers_in_list_without_sum([]) == 0
        assert sum_numbers_in_list_without_sum([-1, -2, 3]) == 0


class TestStringUtils:
    """Test cases for string utility functions."""

    def test_reverse_string(self):
        """Test reverse_string function with different string inputs."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"


class TestErrorHandling:
    """Test cases for error handling utility functions."""

    def test_divide(self, capsys):
        """Test divide function with valid division and division by zero."""
        assert divide(10, 2) == 5
        assert divide(10, 0) is None
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out


class TestSetUtils:
    """Test cases for set utility functions."""

    def test_set_intersection(self):
        """Test set_intersection function to verify it returns the intersection of two sets."""
        s1 = {1, 2, 3, 4}
        s2 = {3, 4, 5, 6}
        assert set_intersection(s1, s2) == {3, 4}
