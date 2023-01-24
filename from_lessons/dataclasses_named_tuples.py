from collections import namedtuple
from dataclasses import dataclass, asdict


@dataclass
class Student:
    first_name: str
    last_name: str
    age: int
    grades: list[int] = None

    @staticmethod
    def from_dict(data):
        return Student(**data)

    def __post_init__(self):
        if self.grades is None:
            self.grades = []

    def method(self):
        print(self.first_name)


class RegularStudent:
    def __init__(self, first_name: str, last_name: str, age: int, grades: list[int] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades or []


if __name__ == '__main__':

    student = Student('John', 'Doe', age=27)
    assert student.first_name == 'John'
    assert student.last_name == 'Doe'
    assert student.age == 27
    assert student.grades is None

    regular_student = RegularStudent('John', 'Doe', 27)
    assert regular_student.first_name == 'John'
    assert regular_student.last_name == 'Doe'
    assert regular_student.age == 27
    assert regular_student.grades == []

    StudentNamedTuple = namedtuple('Student', ['first_name', 'last_name', 'age', 'grades'], defaults=[1, None])
    nt_student = StudentNamedTuple('John', 'Doe', 27)
    assert nt_student.first_name == nt_student[0] == 'John'
    assert nt_student.last_name == nt_student[1] == 'Doe'
    assert nt_student.age == nt_student[2] == 27
    assert nt_student.grades is nt_student[3] is None
    