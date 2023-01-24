import enum
import random


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def guess_password(possible_password):
    assert isinstance(possible_password, str)

    real_password = 'abcdef'
    if possible_password == real_password:
        return 'you got it'

    if possible_password in real_password:
        return 'almost there'

    return 'you never guess it'


def random_value():
    result = random.randint(0, 1)
    if result == 0:
        return 'zero value'
    return 'non-zero value'


@enum.unique
class StudentState(enum.Enum):
    READING = 'READING'
    WATCHING_YOUTUBE = 'WATCHING_YOUTUBE'
    DOING_HOMEWORK = 'DOING_HOMEWORK'


class Student:
    _state: StudentState = StudentState.WATCHING_YOUTUBE

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name}'

    def what_are_you_doing(self) -> StudentState:
        return self._state

    def do_homework(self):
        self._state = StudentState.DOING_HOMEWORK

    def slack(self):
        self._state = StudentState.WATCHING_YOUTUBE

    def read(self):
        self._state = StudentState.READING
