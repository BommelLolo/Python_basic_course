import os
import pytest
from things_to_test_hw import search_in_file

FILENAME = 'for_test.txt'
YOUR_PATH_TO_FILE = ''
path_to_file = os.path.join(YOUR_PATH_TO_FILE, FILENAME)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        search_in_file('not_existing_file', 'pattern')


@pytest.fixture(scope='function')
def temp_file(text):
    with open(path_to_file, 'w', encoding='utf-8') as file:
        file.write(text)
    yield path_to_file
    os.remove(path_to_file)


@pytest.mark.parametrize(
    'text, expected',
    (
            ('', []),
            ('party pattern patient', ['party pattern patient']),
            ('party\n123 pattern \npatient', ['123 pattern \n'])
    ),
)
def test_positive(temp_file, text, expected):
    assert search_in_file(temp_file, 'pattern') == expected


# first try
# def test_file_not_found():
#     with pytest.raises(FileNotFoundError):
#         search_in_file('not_existing_file', 'pattern')
#
#
# @pytest.mark.parametrize(
#     'path, text, expected',
#     (
#             (path_to_file, '', []),
#             (path_to_file, 'party pattern patient', ['party pattern patient']),
#             (path_to_file, 'party\n123 pattern \npatient', ['123 pattern \n'])
#     )
# )
# def test_positive(path, text, expected):
#     with open(path_to_file, 'w', encoding='utf-8') as file:
#         file.write(text)
#     assert search_in_file(path, 'pattern') == expected
#     os.remove(path)
