import unittest
from dataclasses import dataclass
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


class TestStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = Storage()
        cls.data1 = Data1ForStructure(
            id_num=1293,
            first_name='John',
            last_name='Doe',
            age=47,
            hobbies=('dogs', 'running')
        )

        cls.data11 = Data1ForStructure(
            id_num=156,
            first_name='John',
            last_name='Wick',
            age=47,
            hobbies=('dogs', 'running', 'shooting')
        )

        cls.data2 = Data2ForStructure(
            id_num=4509,
            first_name='Jane',
            last_name='Doe',
            position='nobody_knows',
            experience=12.5
        )

    def tearDown(self):
        self.storage._data = {}

    def test_add_table_tried_overwrite_table(self):
        self.storage.add_table('table1', self.data1)
        with self.assertRaises(ValueError):
            self.storage.add_table('table1', self.data1)

    def test_add_table_positive_add_2_different_tables(self):
        self.storage.add_table('table1', self.data1)
        self.storage.add_table('table2', self.data2)
        self.assertEqual(
            {'table1': {'name': 'table1',
                        'structure': Data1ForStructure(1293, 'John', 'Doe', 47,
                                                       ('dogs', 'running')),
                        'data': []},
             'table2': {'name': 'table2',
                        'structure': Data2ForStructure(4509, 'Jane', 'Doe', 'nobody_knows', 12.5),
                        'data': []}},
            self.storage._data
        )

    def test_add_table_positive_add_empty_structure(self):
        self.storage.add_table('', '')
        self.assertEqual({'': {'name': '', 'structure': '', 'data': []}}, self.storage._data)

    def test_add_table_positive_empty_data_dict(self):
        self.assertEqual({}, self.storage._data)

    def test_get_from_table_table_not_exist(self):
        with self.assertRaises(ValueError):
            self.storage.get_from_table('table1')

    def test_get_from_table_positive_empty_data_in_table(self):
        self.storage.add_table('table1', self.data1)
        res = self.storage.get_from_table('table1')
        self.assertEqual(res, [])

    def test_get_from_table_positive_with_data_in_table(self):
        self.storage.add_table('table1', self.data1)
        self.storage._data['table1']['data'] = self.data2
        res = self.storage.get_from_table('table1')
        self.assertEqual(res, self.data2)

    def test_add_to_table_table_not_exist(self):
        with self.assertRaises(ValueError):
            self.storage.add_to_table\
                ('table1', Data1ForStructure(1293, 'John', 'Doe', 47, ('dogs', 'running')))

    def test_add_to_table_invalid_data(self):
        self.storage.add_table('table1', Data1ForStructure)
        with self.assertRaises(ValueError):
            self.storage.add_to_table\
                ('table1', self.data1, self.data11, self.data2)

    def test_add_to_table_positive_add_data(self):
        self.storage.add_table('table1', Data1ForStructure)
        self.storage.add_to_table('table1', self.data1, self.data11)
        print(str(self.storage._data))
        self.assertEqual("{"
                         "'table1': "
                         "{"
                         "'name': 'table1', "
                         "'structure': "
                         "<class 'homework_10.tests.tests_unittest."
                         "test_storage.Data1ForStructure'>, "
                         "'data': "
                         "["
                         "Data1ForStructure(id_num=1293, "
                         "first_name='John', last_name='Doe', age=47, "
                         "hobbies=('dogs', 'running')), "
                         "Data1ForStructure(id_num=156, "
                         "first_name='John', last_name='Wick', age=47, "
                         "hobbies=('dogs', 'running', 'shooting'))"
                         "]"
                         "}"
                         "}",
                         str(self.storage._data))
