import json


if __name__ == '__main__':
    filename = 'my_test.txt'

    file = open(filename, 'w')
    file.write(' ' * 8 + '\tnew\tli\nne here\n')
    file.write('he\nllo, wo\nrld!\n')
    lines = ['first line', 'second line', 'third line']
    file.writelines([f'{line}\n' for line in lines])
    file.close()

    file = open(filename, 'a')
    file.write('hello, world!')
    assert not file.closed
    file.close()
    assert file.closed

    file1 = open(filename, 'r')
    print(file1.read())
    file1.close()

    with open(filename, 'r') as new_file:
        assert not new_file.closed
        print('in context manager')
        print(new_file.read())
        print(new_file.tell())
        new_file.seek(30)
        print(new_file.tell())
        print(new_file.read(10))
        print(new_file.tell())
        assert not new_file.closed

    with open(filename, 'r') as new_file:
        for line in new_file:
            print('>>>', line.rstrip('\n'))

        new_file.seek(0)
        print(new_file.readlines())

    student = {
        'full_name': 'John Doe',
        'age': 30,
        'hobbies': ('sport', 'TV'),
        'married': False,
        "relatives": [
            {
                'full_name': "\u0123Jane D\'oe\"",
                'age': 28,
                'status': 'SISTER',
            },
        ],
    }
    print(json.dumps(student, ensure_ascii=False))

    with open('student.json', 'w') as json_file:
        json.dump(student, json_file)

    with open('student.json', 'r') as json_file:
        data = json.load(json_file)
        assert isinstance(data['hobbies'], list)
        assert isinstance(student['hobbies'], tuple)
        json_file.seek(0)
        data2 = json.loads(json_file.read())
        assert data == data2
