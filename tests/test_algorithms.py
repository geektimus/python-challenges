from src.challenges.algorithms import is_palindrome, count_words, fibonacci, is_even


class TestAlgorithms:
    def test_is_palindrome(self):
        # Test cases
        assert is_palindrome("A man a plan a canal Panama") == True
        assert is_palindrome("racecar") == True
        assert is_palindrome("hello") == False
        assert is_palindrome("No lemon no melon") == True
        assert is_palindrome("Python") == False

    def test_count_words(self):
        assert count_words("Hello world") == {'hello': 1, 'world': 1}
        assert count_words("Hello world hello") == {'hello': 2, 'world': 1}
        assert count_words("Hello world hello world") == {
            'hello': 2, 'world': 2}

    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(10) == 55

    def test_is_even(self):
        assert is_even(2) == True
        assert is_even(3) == False
        assert is_even(0) == True
        assert is_even(-2) == True
        assert is_even(-3) == False
