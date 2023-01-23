import os
import json
import pytest
from things_to_test_hw import add_from_json

FILENAME = 'test.json'
YOUR_PATH_TO_FILE = ''
path_to_file = os.path.join(YOUR_PATH_TO_FILE, FILENAME)


@pytest.fixture(scope='function')
def temp_json_file():
    data = {"a": 3, "b": -7, "c": 0}
    with open(path_to_file, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    yield path_to_file
    os.unlink(path_to_file)


def test_file_not_exist():
    keys = ['a', 'b']
    with pytest.raises(FileNotFoundError):
        add_from_json('not_existing_file', keys)


def test_wrong_keys(temp_json_file):
    keys = ['a', 'b', 'd']
    with pytest.raises(KeyError):
        add_from_json(temp_json_file, keys)


def test_invalid_data_in_args(temp_json_file):
    data = {'a': 3, 'b': 'asc'}
    with open(temp_json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    with pytest.raises(TypeError):
        add_from_json(temp_json_file, data.keys())


def test_add_from_json_positive(temp_json_file):
    keys = ['a', 'b', 'c']
    res = add_from_json(temp_json_file, keys)
    assert -4 == res
