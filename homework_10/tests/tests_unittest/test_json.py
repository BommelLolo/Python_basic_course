import unittest
import os
import json
from things_to_test_hw import add_from_json


class TestAddFromJSON(unittest.TestCase):
    FILENAME = 'test.json'
    YOUR_PATH_TO_FILE = ''
    path_to_file = os.path.join(YOUR_PATH_TO_FILE, FILENAME)

    def setUp(self):
        data = {"a": 3, "b": -7, "c": 0}
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def tearDown(self):
        os.unlink(self.path_to_file)

    def test_file_not_exist(self):
        keys = ['a', 'b']
        with self.assertRaises(FileNotFoundError):
            add_from_json('not_existing_file', keys)

    def test_wrong_keys(self):
        keys = ['a', 'b', 'd']
        with self.assertRaises(KeyError):
            add_from_json(self.path_to_file, keys)

    def test_invalid_data_in_args(self):
        data = {'a': 3, 'b': 'asc'}
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        with self.assertRaises(TypeError):
            add_from_json(self.path_to_file, data.keys())

    def test_add_from_json_positive(self):
        keys = ['a', 'b', 'c']
        res = add_from_json(self.path_to_file, keys)
        self.assertEqual(-4, res)
