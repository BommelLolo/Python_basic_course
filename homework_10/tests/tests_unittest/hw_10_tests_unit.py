import unittest
import os


def search_in_file(file_path, pattern):
    with open(file_path, 'r') as file:
        return [line for line in file if pattern in line]

search_in_file('path/to/file', 'pattern')

"""
What to test?
Еррор
- немає файлу за адресою
- в паттерн переданий не текст
Негатив
- файл пустий
- файл не пустий, нема збігу
Поз 
файл є, є збіг 
"""

class TestSearchInFile(unittest.TestCase):

    def test_error(self):
        pass

    def test_negative(self):
        pass

    def test_positive(self):
        with open(os.path, )

