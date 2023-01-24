my_fancy_var = 13
MY_CONST_VALUE = 'Monday'


def my_func_name():
    pass


class MyClass:
    name = 'value'

    def say_hi(self):
        print(self.name)
        print('Hello!')


class Greet:
    def __init__(self, full_name):
        self.full_name = full_name

    def say_hi(self):
        print(f'Hello {self.full_name}!')


class Circle:
    # public - any name not prefixed with _
    # protected - starts with single _
    # private - starts with double _

    # package

    def __init__(self, radius):
        self._radius = radius

    def _protected_method(self):
        pass

    def __private_method(self):
        pass

    def area(self):
        return 2 * 3.14 * self._radius ** 2

    def __gt__(self, other):
        assert isinstance(other, Circle)
        return self._radius > other._radius

    # def __lt__(self, other):
    #     pass

    # def __le__(self, other):
    #     pass

    def __ge__(self, other):
        # assert isinstance(other, Circle)
        # return self._radius >= other._radius

        # or
        return self > other or self == other

    def __eq__(self, other):
        assert isinstance(other, Circle)
        return self._radius == other._radius

    def __str__(self):
        return f'Circle(radius={self._radius})'


class Path:
    def __init__(self, initial_path='.', sep='/'):
        self._current_path = initial_path
        self._sep = sep

    def __str__(self):
        return self._current_path

    def __add__(self, other):
        assert isinstance(other, (str, Path)), 'message'
        if isinstance(other, Path):
            return self + other._current_path

        return self._sep.join((self._current_path, other)).replace(self._sep * 2, self._sep)

    # def __iadd__(self, other):
    #     pass
    #
    # def __radd__(self, other):
    #     pass

    def __truediv__(self, other):
        return self + other


class SafeFileOpen:
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._file_handler = None

    def __enter__(self):
        if self._mode == 'r':
            with open(self._path, 'a'):
                pass

        self._file_handler = open(self._path, self._mode)

        return self._file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file_handler is not None:
            self._file_handler.close()


if __name__ == '__main__':
    my_class_instance = MyClass()
    my_class_instance2 = MyClass()
    assert isinstance(my_class_instance, MyClass)
    assert my_class_instance.name == 'value'
    my_class_instance.say_hi()
    my_class_instance2.say_hi()
    assert my_class_instance2.name == my_class_instance.name

    greet_john = Greet('John')
    greet_john.say_hi()
    greet_jane = Greet('Jane')
    greet_jane.say_hi()

    assert greet_jane.full_name != greet_john.full_name

    small_circle = Circle(2)
    another_small_circle = Circle(2)
    big_circle = Circle(4)

    assert big_circle > small_circle
    assert small_circle < big_circle
    assert big_circle.__gt__(small_circle)
    assert big_circle != small_circle

    assert small_circle == another_small_circle
    assert small_circle <= another_small_circle
    assert small_circle >= another_small_circle

    print(str(small_circle))
    print(big_circle)

    path = Path('/Users/mvelykanov')
    path = path + 'PycharmProjects/python_2022-11-22/classes.py'
    # path += '...'
    assert str(path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    new_path = Path('/Users/mvelykanov') + Path('PycharmProjects/python_2022-11-22/classes.py')
    assert str(new_path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    div_path = Path('/Users/mvelykanov') / Path('PycharmProjects/python_2022-11-22/classes.py')
    assert str(div_path) == '/Users/mvelykanov/PycharmProjects/python_2022-11-22/classes.py'

    assert str(Path('a') / 'bcd') == 'a/bcd'

    with SafeFileOpen('test.txt', 'w') as file:
        file.write('hello, world!')
        # print(file.read())
        