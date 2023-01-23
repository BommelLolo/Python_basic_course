import unittest
import os
from things_to_test_hw import search_in_file


class TestSearchInFile(unittest.TestCase):
    filename = 'for_test.txt'

    def setUp(self):
        with open(self.filename, 'w') as file:
            file.write('')

    def tearDown(self):
        os.remove(self.filename)

    def test_negative(self):
        other_filename = 'other_file.txt'
        with self.assertRaises(FileNotFoundError):
            search_in_file(other_filename, 'pattern')

    def test_positive_1(self):
        text = ""
        with open(self.filename, 'a') as file:
            file.write(text)
        self.assertEqual([], search_in_file(self.filename, 'pattern'))

    def test_positive_2(self):
        text = 'party pattern patient'
        with open(self.filename, 'a') as file:
            file.write(text)
        self.assertEqual([text], search_in_file(self.filename, 'pattern'))

    def test_positive_3(self):
        text = "party\n123 pattern \npatient"
        with open(self.filename, 'a') as file:
            file.write(text)
        self.assertEqual(["123 pattern \n"], search_in_file(self.filename, 'pattern'))
