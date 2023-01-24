# age = 20
# name = 'Bob'
# print(age == 17)
# a < b
# a <= b
# a > b
# a >= b
# a == b - not (a == b)
# a != b - not (a != b)
# not

def other_func():
    check_age(24, 'abc')


def check_age(age, name):
    if age < 18 and name != 'Alice':
        print(name, 'underage')
    elif age < 21:
        print('illegal to drink in USA', name)
    else:
        print('can drink alcohol', age)


def add(a, b):
    c = a + b

    return c


if __name__ == '__main__':
    check_age(17, 'Alice')
    check_age(17, 'Bob')
    check_age(40, 'anonymous')

    print(add(2, 3))
    print(add(7, add(1, 2)))  # add(7, 3)
    