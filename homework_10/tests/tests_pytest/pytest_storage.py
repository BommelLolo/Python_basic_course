from dataclasses import dataclass
import pytest
from things_to_test_hw import Storage


@dataclass
class Data1ForStructure:
    id_num: int
    first_name: str
    last_name: str
    age: int
    hobbies: tuple


@dataclass
class Data2ForStructure:
    id_num: int
    first_name: str
    last_name: str
    position: str
    experience: float


@pytest.fixture
def data_1():
    return Data1ForStructure(1293, 'John', 'Doe', 47, ('dogs', 'running'))


@pytest.fixture
def data_11():
    return Data1ForStructure(156, 'John', 'Wick', 47, ('dogs', 'running', 'shooting'))


@pytest.fixture
def data_2():
    return Data2ForStructure(4509, 'Jane', 'Doe', 'nobody_knows', 12.5)


# for working with big DB better to make only one object for the module
@pytest.fixture(scope='module')
def storage():
    temp_storage = Storage()
    yield temp_storage


def test_add_table_tried_overwrite_table(storage, data_1):
    storage.add_table('table1', data_1)
    with pytest.raises(ValueError):
        storage.add_table('table1', data_1)
    storage._data = {}


def test_add_table_positive_add_2_different_tables(storage, data_1, data_2):
    storage.add_table('table1', data_1)
    storage.add_table('table2', data_2)
    assert {'table1': {
        'name': 'table1',
        'structure': Data1ForStructure(1293, 'John', 'Doe', 47, ('dogs', 'running')),
        'data': []
    },
               'table2': {
                   'name': 'table2',
                   'structure': Data2ForStructure(4509, 'Jane', 'Doe', 'nobody_knows', 12.5),
                   'data': []
               }
           } == storage._data
    storage._data = {}


def test_add_table_positive_add_empty_structure(storage):
    storage.add_table('', '')
    assert {'': {'name': '', 'structure': '', 'data': []}} == storage._data
    storage._data = {}


def test_add_table_positive_empty_data_dict(storage):
    assert storage._data == {}


def test_get_from_table_table_not_exist(storage):
    with pytest.raises(ValueError):
        storage.get_from_table('table1')


def test_get_from_table_positive_empty_data_in_table(storage, data_1):
    storage.add_table('table1', data_1)
    res = storage.get_from_table('table1')
    assert res == []
    storage._data = {}


def test_get_from_table_positive_with_data_in_table(storage, data_1, data_2):
    storage.add_table('table1', data_1)
    storage._data['table1']['data'] = data_2
    res = storage.get_from_table('table1')
    assert res == data_2
    storage._data = {}


def test_add_to_table_table_not_exist(storage, data_1):
    with pytest.raises(ValueError):
        storage.add_to_table('table1', data_1)


def test_add_to_table_invalid_data(storage, data_1, data_11, data_2):
    storage.add_table('table1', Data1ForStructure)
    with pytest.raises(ValueError):
        storage.add_to_table('table1', data_1, data_11, data_2)
    storage._data = {}


def test_add_to_table_positive_add_data(storage, data_1, data_11):
    storage.add_table('table1', Data1ForStructure)
    storage.add_to_table('table1', data_1, data_11)
    assert str(storage._data) == "{'table1': {'name': 'table1', 'structure': <class " \
           "'homework_10.tests.tests_pytest.pytest_storage.Data1ForStructure'>, " \
                                 "'data': [Data1ForStructure(" \
           "id_num=1293, first_name='John', last_name='Doe', age=47, " \
                                 "hobbies=('dogs', 'running')), " \
           "Data1ForStructure(" \
           "id_num=156, first_name='John', last_name='Wick', age=47, " \
                                 "hobbies=('dogs', 'running', 'shooting'))]}}"
    storage._data = {}
