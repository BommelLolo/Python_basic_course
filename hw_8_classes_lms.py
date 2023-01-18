class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        self.teacher.course = self
        self.students = []
        self.homeworks = []

        self.lectures = []
        for lec in range(self.number_of_lectures):
            lec += 1
            self.lectures.append(Lecture(f"Lecture {lec}", lec, self.teacher))

        for lec in self.lectures:
            lec.course = self

        self.teacher.lectures = self.lectures

    def __str__(self):
        return f"{self.name} ({self.start_date})"

    def enrolled_by(self):
        return self.students

    def get_lecture(self, number):
        number -= 1
        if number in range(self.number_of_lectures):
            return self.lectures[number]
        else:
            raise AssertionError('Invalid lecture number', )

    def get_homeworks(self):
        return self.homeworks


class Lecture:
    def __init__(self, name, number, teacher):
        self.name = name
        self.number = number
        self.teacher = teacher
        self.course = None
        self.homework = None

    def get_homework(self):
        return self.homework

    def set_homework(self, homework):
        self.homework = homework
        self.course.homeworks.append(self.homework)
        for student in self.course.students:
            student.homeworks_to_do.append(self.homework)

    def new_teacher(self, sub_teacher):
        self.teacher.lectures.remove(self)
        self.teacher = sub_teacher
        sub_teacher.lectures.append(self)


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.who_done = {}

    def __str__(self):
        return f"{self.name}: {self.description}"

    def done_by(self):
        return self.who_done


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.course = None
        self.homeworks_to_do = []

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"

    def enroll(self, course):
        self.course = course
        return course.students.append(self)

    @property
    def assigned_homeworks(self):
        return self.homeworks_to_do

    def do_homework(self, homework):
        self.homeworks_to_do.remove(homework)
        homework.who_done.setdefault(self, None)
        self.course.teacher.homeworks_to_check.append(homework)


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.course = None
        self.lectures = []
        self.homeworks_to_check = []

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"

    def teaching_lectures(self):
        return self.lectures

    def check_homework(self, homework, student, mark):
        # check, has the student done this hw
        if student not in homework.who_done:
            raise ValueError('Student never did that homework', )
        else:
            # check, that teacher check hw at first
            if homework.who_done[student] is not None:
                raise ValueError('You already checked that homework', )
            else:
                if mark in range(0, 101):
                    homework.who_done[student] = mark
                    self.homeworks_to_check.remove(homework)
                    return homework.who_done
                else:
                    raise AssertionError('Invalid mark', )


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures

    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by() == students

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        assert student.assigned_homeworks == [functions_homework]

    assert main_teacher.homeworks_to_check == []
    students[0].do_homework(functions_homework)
    assert students[0].assigned_homeworks == []
    assert students[1].assigned_homeworks == [functions_homework]

    assert functions_homework.done_by() == {students[0]: None}
    assert main_teacher.homeworks_to_check == [functions_homework]

    for mark in (-1, 101):
        try:
            main_teacher.check_homework(functions_homework, students[0], mark)
        except AssertionError as error:
            assert error.args == ('Invalid mark',)

    main_teacher.check_homework(functions_homework, students[0], 100)
    assert main_teacher.homeworks_to_check == []
    assert functions_homework.done_by() == {students[0]: 100}

    try:
        main_teacher.check_homework(functions_homework, students[0], 100)
    except ValueError as error:
        assert error.args == ('You already checked that homework',)

    try:
        main_teacher.check_homework(functions_homework, students[1], 100)
    except ValueError as error:
        assert error.args == ('Student never did that homework',)

    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher

    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    assert substitute_teacher.homeworks_to_check == []
