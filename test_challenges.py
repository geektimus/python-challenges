import unittest
from challenges import is_palindrome, count_words
from dictionary import contains_key


class TestChallenges(unittest.TestCase):
    def test_is_palindrome(self):
        # Test cases
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("No lemon no melon"))
        self.assertFalse(is_palindrome("Python"))

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), {'hello': 1, 'world': 1})
        self.assertEqual(count_words("Hello world hello"),
                         {'hello': 2, 'world': 1})
        self.assertEqual(count_words("Hello world hello world"), {
                         'hello': 2, 'world': 2})


class TestDictionary(unittest.TestCase):
    def test_contains_key(self):
        d = {'a': 1, 'b': 2}
        self.assertTrue(contains_key(d, 'a'))
        self.assertFalse(contains_key(d, 'c'))
        self.assertTrue(contains_key(d, 'b'))
        self.assertFalse(contains_key(d, 'd'))


if __name__ == '__main__':
    unittest.main()
