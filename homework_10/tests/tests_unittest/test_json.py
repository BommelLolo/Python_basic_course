import unittest
import os
import json
from things_to_test_hw import add_from_json


class TestAddFromJSON(unittest.TestCase):

    def test_negative(self):
        keys = ['a', 'b']
        with self.assertRaises(FileNotFoundError):
            add_from_json("test.json", keys)

        keys = ['a', 'b', 'd']
        with self.assertRaises(KeyError):
            add_from_json("example.json", keys)

        data = {'a': 3, 'b': 'asc'}
        filename = 'test.json'
        with open(filename, 'w') as file:
            json.dump(data, file)
        with self.assertRaises(TypeError):
            add_from_json(filename, data.keys())
        os.unlink(filename)

    def test_positive(self):
        data = {'a': 3, 'b': 4}
        filename = 'test.json'
        with open(filename, 'w') as file:
            json.dump(data, file)
        res = add_from_json(filename, data.keys())
        self.assertEqual(7, res)
        os.unlink(filename)

        keys = ['a', 'b', 'c']
        res = add_from_json("example.json", keys)
        self.assertEqual(-4, res)
