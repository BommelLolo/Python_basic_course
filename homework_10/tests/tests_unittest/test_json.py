import unittest
import os
import json
from things_to_test_hw import add_from_json


class TestAddFromJSON(unittest.TestCase):

    def test_negative_1(self):
        keys = ['a', 'b']
        with self.assertRaises(FileNotFoundError):
            add_from_json("test.json", keys)

    def test_negative_2(self):
        keys = ['a', 'b', 'd']
        with self.assertRaises(KeyError):
            add_from_json("example.json", keys)

    def test_negative_3(self):
        data = {'a': 3, 'b': 'asc'}
        filename = 'test.json'
        with open(filename, 'w') as file:
            json.dump(data, file)
        with self.assertRaises(TypeError):
            add_from_json(filename, data.keys())
        os.unlink(filename)

    def test_positive_1(self):
        data = {'a': 3, 'b': 4}
        filename = 'test.json'
        with open(filename, 'w') as file:
            json.dump(data, file)
        res = add_from_json(filename, data.keys())
        self.assertEqual(7, res)
        os.unlink(filename)

    def test_positive_2(self):
        keys = ['a', 'b', 'c']
        res = add_from_json("example.json", keys)
        self.assertEqual(-4, res)
