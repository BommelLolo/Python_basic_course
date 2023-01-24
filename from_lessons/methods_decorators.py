def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator
def f():
    pass


def shape_from_string(s):
    # shape_name:value
    shape_name, value = s.split(':')
    if shape_name == 'circle':
        return Circle(int(value))

    return Square(int(value))


class ShapeBuilder:
    @staticmethod
    def from_string(s):
        shape_name, value = s.split(':')
        if shape_name == 'circle':
            return Circle(int(value))

        return Square(int(value))


class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius


class Square(Shape):
    def __init__(self, side):
        self._side = side

    @staticmethod
    def from_string(s):
        _, value = s.split(':')
        return Square(int(value))

    def area(self):
        return self._side ** 2


class WithClassMethod:
    var = 13

    @classmethod
    def method(cls):
        print('in class method', cls.var)


class Student:
    def __init__(self, full_name):
        self._full_name = full_name
        self._grades = []

    def get_full_name(self):
        return self._full_name

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    def set_full_name(self, new_full_name):
        self._full_name = new_full_name

    def get_grades(self):
        return self._grades

    def add_grade(self, grade):
        self._grades.append(grade)


class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @property
    def uah(self):
        uah = self._balance // 100
        coins = self._balance % 100

        return f'{uah} UAH {coins} cops'

    @balance.setter
    def balance(self, value):
        # if value < 0:
        #     raise ValueError('balance below 0')
        assert value >= 0, 'balance below 0'
        self._balance = value


if __name__ == '__main__':
    square = Square(4)
    assert square.area() == 16
    # Shape.area(square)

    circle = shape_from_string('circle:3')
    assert isinstance(circle, Circle)

    another_circle = ShapeBuilder.from_string('circle:3')
    assert isinstance(another_circle, Circle)

    shape = Square.from_string('circle:4')
    assert isinstance(shape, Square)

    w = WithClassMethod()
    assert w.var == 13
    w.method()
    WithClassMethod.method()

    student = Student('Jane Doe')
    assert student.get_full_name() == 'Jane Doe'
    assert student.full_name == 'Jane Doe'
    student.set_full_name('John Doe')
    assert student.get_full_name() == 'John Doe'
    assert student.full_name == 'John Doe'

    student.full_name = 'Jane Doe'
    assert student.full_name == 'Jane Doe'

    account = BankAccount()
    account.balance = 130
    assert account.balance == 130
    assert account.uah == '1 UAH 30 cops'

    try:
        account.balance = -10
    except AssertionError:
        print('got assertion error')
        