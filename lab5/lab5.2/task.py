def count_words(sentence: str) -> int:  #возвращает количество слов в предложении (слова разделены пробелами)
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.split())


def find_unique(lst):  #возвращает список элементов, встречающихся ровно один раз
    from collections import Counter
    counts = Counter(lst)
    return [item for item, count in counts.items() if count == 1]


def is_palindrome(value) -> bool:  #проверяет, является ли строка или число палиндромом (без учёта регистра)
    s = str(value).lower()
    return s == s[::-1]


def are_anagrams(s1: str, s2: str) -> bool:  #проверяет, являются ли две строки анаграммами (игнорируя регистр и пробелы)
    clean1 = s1.replace(" ", "").lower()
    clean2 = s2.replace(" ", "").lower()
    return sorted(clean1) == sorted(clean2)


def combine_dicts(d1: dict, d2: dict) -> dict:  #объединяем два словаря, значения из d2 перезаписывают значения из d1
    result = d1.copy()
    result.update(d2)
    return result