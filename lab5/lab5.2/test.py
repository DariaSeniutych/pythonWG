import pytest
from task import count_words, find_unique, is_palindrome, are_anagrams, combine_dicts


# задача 1 - подсчет слов
def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("Python") == 1
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("  a  b  c  ") == 3


# задача 2 - про уникальные элементы
def test_find_unique():
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
    assert find_unique([1, 1, 2, 2]) == []
    assert find_unique([42]) == [42]
    assert find_unique([]) == []


# задача 3 - палиндром
def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == False  # из-за пробелов не палиндром
    assert is_palindrome("racecar") == True
    assert is_palindrome(121) == True
    assert is_palindrome("hello") == False
    assert is_palindrome("А роза упала на лапу Азора") == False  # из-за регистров
    assert is_palindrome("Madam") == True


# задача 4 - анаграммы
def test_are_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "bello") == False
    assert are_anagrams("Astronomer", "Moon starer") == True
    assert are_anagrams("", "") == True
    assert are_anagrams("evil", "vile") == True


# задача 5 - слияние словарей
def test_combine_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    result = combine_dicts(d1, d2)
    assert result == {"a": 1, "b": 3, "c": 4}

    assert combine_dicts({}, {"x": 1}) == {"x": 1}
    assert combine_dicts({"x": 1}, {}) == {"x": 1}
    assert combine_dicts({"a": 1}, {"a": 1}) == {"a": 1}