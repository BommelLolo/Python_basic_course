import unittest
import os
from things_to_test_hw import search_in_file


class TestSearchInFile(unittest.TestCase):
    FILENAME = 'for_test.txt'
    YOUR_PATH_TO_FILE = ''
    path_to_file = os.path.join(YOUR_PATH_TO_FILE, FILENAME)

    def setUp(self):
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            file.write('')

    def tearDown(self):
        os.remove(self.path_to_file)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            search_in_file('other_file.txt', 'pattern')

    # other variant for test
    # def test_file_not_exist(self):
    #     self.assertEqual(False, os.path.exists('not_existing_file'))

    def test_with_empty_file(self):
        text = ''
        with open(self.path_to_file, 'a', encoding='utf-8') as file:
            file.write(text)
        self.assertEqual([], search_in_file(self.path_to_file, 'pattern'))

    def test_single_line_in_file(self):
        text = 'party pattern patient'
        with open(self.path_to_file, 'a', encoding='utf-8') as file:
            file.write(text)
        self.assertEqual([text], search_in_file(self.path_to_file, 'pattern'))

    def test_multiple_lines_in_file(self):
        text = 'party\n123 pattern \npatient'
        with open(self.path_to_file, 'a', encoding='utf-8') as file:
            file.write(text)
        self.assertEqual(['123 pattern \n'], search_in_file(self.path_to_file, 'pattern'))
