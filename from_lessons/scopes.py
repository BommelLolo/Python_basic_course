from constants import CONST1
from constants import CONST2

CURRENT_DOW = 'Friday'
a = 5


def func():
    # a += 7  # a = a + 7
    global a
    a += 7
    print(CURRENT_DOW, a)
    print(a)
    print(CONST1)


def func_with_inner():
    b = 6

    def inner():
        nonlocal b

        print(a, b)
        b += 10
        print(b)

    inner()
    print(b)


if __name__ == '__main__':
    # print('before', a)
    # func()
    # print('after', a)

    func_with_inner()
