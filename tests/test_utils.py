import pytest
from src.utils.dict_utils import contains_key
from src.utils.list_utils import sum_numbers_in_list, sum_numbers_in_list_without_sum
from src.utils.string_utils import reverse_string
from src.utils.error_handling import divide
from src.utils.set_utils import set_intersection


class TestDictUtils:
    def test_contains_key(self):
        d = {'a': 1, 'b': 2}
        assert contains_key(d, 'a') == True
        assert contains_key(d, 'c') == False
        assert contains_key(d, 'b') == True
        assert contains_key(d, 'd') == False


class TestListUtils:
    def test_sum_numbers_in_list(self):
        assert sum_numbers_in_list([1, 2, 3, 4, 5]) == 15
        assert sum_numbers_in_list([]) == 0
        assert sum_numbers_in_list([-1, -2, 3]) == 0
    
    def test_sum_numbers_in_list_without_sum(self):
        assert sum_numbers_in_list_without_sum([1, 2, 3, 4, 5]) == 15
        assert sum_numbers_in_list_without_sum([]) == 0
        assert sum_numbers_in_list_without_sum([-1, -2, 3]) == 0


class TestStringUtils:
    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"


class TestErrorHandling:
    def test_divide(self, capsys):
        assert divide(10, 2) == 5
        assert divide(10, 0) is None
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out


class TestSetUtils:
    def test_set_intersection(self):
        s1 = {1, 2, 3, 4}
        s2 = {3, 4, 5, 6}
        assert set_intersection(s1, s2) == {3, 4}