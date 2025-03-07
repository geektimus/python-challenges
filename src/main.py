from src.utils.dict_utils import contains_key
from src.challenges.algorithms import is_palindrome, count_words


def main():
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
