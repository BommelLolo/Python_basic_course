import os


class Path:
    def __init__(self, initial_path='.'):
        self._current_path = initial_path

    def __str__(self):
        return self._current_path

    def __add__(self, other):
        assert isinstance(other, (str, Path)), 'message'
        if isinstance(other, Path):
            return self + other._current_path

        return os.path.join(self._current_path, other)

    def __truediv__(self, other):
        return self + other


if __name__ == '__main__':
    path = Path('/Users/mvelykanov')
    path = path + 'PycharmProjects/python_2022-11-22/classes.py'
    # path += '...'
    assert str(path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    new_path = Path('/Users/mvelykanov') + Path('PycharmProjects/python_2022-11-22/classes.py')
    assert str(new_path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    div_path = Path('/Users/mvelykanov') / Path('PycharmProjects/python_2022-11-22/classes.py')
    assert str(div_path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    assert str(Path('a') / 'bcd') == 'a/bcd'
    