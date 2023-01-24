class MyError(BaseException):
    pass


# abstract / interface

class Reader:
    def read(self, a, b, c):
        raise NotImplementedError


class XSLXReader(Reader):
    def read(self, a, b, c):
        print('reading...')


class CSVReader(Reader):
    def read(self):
        print('reading csv')


class A:
    def __init__(self, value):
        self._value = value
        self.__private = 13

    def tell_private_value(self):
        print(self.__private)


class B(A):
    def add_three(self):
        return self._value + 3

    def tell_private_value(self):
        print(self._A__private)


class NoDynamicFields:
    __slots__ = ['a', 'b']


class TooShortError(ValueError):
    pass


class TooLongError(ValueError):
    pass


def string_validator(s, min_length=None, max_length=None):
    if (
        min_length is not None
        and max_length is not None
        and min_length > max_length
    ):
        raise ValueError('..')

    if min_length is not None and len(s) < min_length:
        raise TooShortError

    if max_length is not None and len(s) > max_length:
        raise TooLongError

    return s


if __name__ == '__main__':
    # raise MyError('message')
    # b = B(3)
    # assert b._value == 3
    # assert b.add_three() == 6
    # # assert b._A__private == 13
    #
    # a = A(3)
    #
    # assert a._value == 3
    # a.tell_private_value()
    # b.tell_private_value()
    # # assert a._A__private == 13
    # # assert a.add_three() == 6 - not available
    #
    # XSLXReader().read(1, 2, 3)
    # CSVReader().read()

    # assert 'abc' == string_validator('abc')
    # assert 'abc' == string_validator('abc', min_length=0)
    # assert 'abc' == string_validator('abc', max_length=10)

    try:
        result = string_validator('abcd', min_length=10, max_length=1)
    # except (TooShortError, TooLongError):
    #     print('short or long')
    #     raise
    # except ValueError:
    #     print('general value error')
    #     raise
    except:
        print('post-process')
        raise
    else:
        print('no exceptions encountered')
    finally:
        print('here')

    file_handler = None
    try:
        file_handler = open('..', 'w')
        # exception raises
    finally:
        if file_handler is not None:
            file_handler.close()

    print('this is value:', result)
