import unittest
import os
from things_to_test_hw import search_in_file


class TestSearchInFile(unittest.TestCase):

    def test_negative(self):
        filename = 'for_test.txt'
        with self.assertRaises(FileNotFoundError):
            search_in_file(filename, 'pattern')

    def test_positive(self):
        filename = 'for_test.txt'
        text = 'party pattern patient'
        with open(filename, 'w') as file:
            file.write(text)
        self.assertEqual([text], search_in_file(filename, 'pattern'))
        os.remove(filename)

        filename = 'for_test.txt'
        text = "party\n123 pattern \npatient"
        with open(filename, 'w') as file:
            file.write(text)
        self.assertEqual(["123 pattern \n"], search_in_file(filename, 'pattern'))
        os.remove(filename)

        filename = 'for_test.txt'
        text = ""
        with open(filename, 'w') as file:
            file.write(text)
        self.assertEqual([], search_in_file(filename, 'pattern'))
        os.remove(filename)
        