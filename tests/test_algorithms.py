"""
Tests for the algorithm functions in the challenges module.

This module contains tests for various algorithm implementations including:
- Palindrome checking
- Word counting
- Fibonacci sequence generation
- Even number detection
"""

from src.challenges.algorithms import (
    is_palindrome,
    count_words,
    fibonacci,
    fibonacci_numbers,
    is_even,
)


class TestAlgorithms:
    """Test cases for algorithm functions in the challenges module."""

    def test_is_palindrome(self):
        """Test is_palindrome function with various palindrome and non-palindrome inputs."""
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("racecar") is True
        assert is_palindrome("hello") is False
        assert is_palindrome("No lemon no melon") is True
        assert is_palindrome("Python") is False

    def test_count_words(self):
        """Test count_words function with various text inputs to verify word frequency counting."""
        assert count_words("Hello world") == {'hello': 1, 'world': 1}
        assert count_words("Hello world hello") == {'hello': 2, 'world': 1}
        assert count_words("Hello world hello world") == {
            'hello': 2, 'world': 2}

    def test_fibonacci(self):
        """Test fibonacci function with various inputs to verify sequence calculation."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(10) == 55

    def test_fibonacci_numbers(self):
        """Test fibonacci_numbers function to test the first n Fibonacci numbers."""
        assert fibonacci_numbers(0) == [0]
        assert fibonacci_numbers(1) == [0, 1]
        assert fibonacci_numbers(5) == [0, 1, 1, 2, 3]
        assert fibonacci_numbers(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_is_even(self):
        """Test is_even function with positive, negative, and zero inputs."""
        assert is_even(2) is True
        assert is_even(3) is False
        assert is_even(0) is True
        assert is_even(-2) is True
        assert is_even(-3) is False
