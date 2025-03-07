"""
Algorithm implementations for solving common programming challenges.

This module contains a collection of functions implementing various algorithms
and solutions to common programming problems and exercises.
"""

from collections import defaultdict

import re


def is_even(n):
    """
    Check if a number is even.

    Args:
        n: A number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return n % 2 == 0


def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
        n: A non-negative integer

    Returns:
        int: The factorial of n (n!)
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial_tail_recursive(n, accumulator=1):
    """
    Calculate the factorial of a number using tail recursion.

    Args:
        n: A non-negative integer
        accumulator: The accumulated result (default=1)

    Returns:
        int: The factorial of n (n!)
    """
    if n == 0:
        return accumulator
    return factorial_tail_recursive(n-1, n*accumulator)


def square_lambda(n):
    """
    Create a lambda function that raises a value to the power of n.

    Args:
        n: The exponent to use in the lambda function

    Returns:
        function: A lambda function that takes x and returns x**n
    """
    return lambda x: x**n


def fibonacci(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoization.

    Args:
        n: A non-negative integer representing the position in the Fibonacci sequence
        memo: A dictionary for memoization to avoid recalculating values (default=None)

    Returns:
        int: The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


def fibonacci_tail_recursive(n, a=0, b=1):
    """
    Calculate the nth Fibonacci number using tail recursion.

    Args:
        n: A non-negative integer representing the position in the Fibonacci sequence
        a: First Fibonacci value (default=0)
        b: Second Fibonacci value (default=1)

    Returns:
        int: The nth Fibonacci number
    """
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursive(n-1, b, a+b)


def is_palindrome(s):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).

    Args:
        s: The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove whitespace and lowercase input string
    txt = s.lower().replace(" ", "")

    for i, char in enumerate(txt[:len(txt) // 2]):
        if char != txt[-(i + 1)]:
            return False
    return True


def count_words(sentence):
    """
    Count the frequency of each word in a sentence.

    Args:
        sentence: A string containing words to count

    Returns:
        defaultdict: A dictionary with words as keys and their frequency as values
    """
    txt = sentence.lower()

    # Split the sentence string into an array of words using whitespace as a delimiter
    # removing any punctuation from the sentence
    arr = re.sub(r"[,.;@#?!&$]+\ *", " ", txt).split()

    counters = defaultdict(lambda: 0)

    for word in arr:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1

    return counters


def fibonacci_numbers(n):
    """
    Generate the first n Fibonacci numbers.

    Args:
        n: The number of Fibonacci numbers to generate

    Returns:
        list: A list of the first n Fibonacci numbers
    """
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
