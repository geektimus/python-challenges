from collections import defaultdict
from collections import Counter

import re


def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail_recursive(n-1, n*accumulator)


def square_lambda(n):
    return lambda x: x**n


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


def fibonacci_tail_recursive(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursive(n-1, b, a+b)


def is_palindrome(s):
    # Remove whitespace and lowercase input string
    input = s.lower().replace(" ", "")

    for i in range(len(input)):
        j = len(input)-i-1
        if (input[i] != input[j]):
            return False
    return True


def count_words(sentence):
    input = sentence.lower()

    # Split the input string into an array of words using whitespace as a delimiter removing any punctuation from the sentence
    arr = re.sub(r"[,.;@#?!&$]+\ *", " ", input).split()

    counters = defaultdict(lambda: 0)

    for word in arr:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1

    return counters