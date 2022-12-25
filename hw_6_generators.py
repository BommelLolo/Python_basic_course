
def get_even_or_odd_numbers(number: int = 0, even: bool = True) -> list:
    """
    Function returns list of even or odd numbers from 0 to value passed in 1-st arg.
    Choose between even and odd values defines by 2-nd argument (by default - even)
    """
    return list(range(0, number + 1, 2)) if even else list(range(1, number + 1, 2))


def search_words(el: str, items: list) -> list:
    """
    Function defines entering of passed symbols from 1-st arg
    into items in the list of iterable objects from 2-nd arg
    and returns list of suitable items
    """
    return [item for item in items if el in item]


def flatten(seq: list):
    """
    It's a generator, that returns every step one element from the passed sequence of sequences.
    """
    return (el for item in seq for el in item)


if __name__ == '__main__':
    assert get_even_or_odd_numbers(3, True) == [0, 2]
    assert get_even_or_odd_numbers(4, False) == [1, 3]
    assert get_even_or_odd_numbers(7) == [0, 2, 4, 6]
    assert get_even_or_odd_numbers(-1, False) == []

    assert search_words('he', ['hello', 'orange', 'phenomenon']) == ['hello', 'phenomenon']
    assert search_words('abc', ['hello', 'orange', 'phenomenon']) == []
    assert search_words('tea', ['steak', 'meat', 'tea', 'table']) == ['steak', 'tea']
    assert search_words('ea', ['steak', 'meat', 'tea', 'table']) == ['steak', 'meat', 'tea']
    assert search_words('eat', ['steak', 'meat', 'tea', 'table']) == ['meat']
    assert search_words('', ['steak', 'meat', 'tea', 'table']) == ['steak', 'meat', 'tea', 'table']
    assert search_words(' ', ['steak', 'meat', 'tea', 'table']) == []
    assert search_words('f', [[1, 2], [1, 5], '56', '234']) == []

    generator = flatten([[1, 2], [], [3, 4, 5]])
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 4
    assert next(generator) == 5

    generator2 = flatten([[1, 2, 6, 10], ['a', 'e', 3], 'q', []])
    assert next(generator2) == 1
    assert next(generator2) == 2
    assert next(generator2) == 6
    assert next(generator2) == 10
    assert next(generator2) == 'a'
    assert next(generator2) == 'e'
    assert next(generator2) == 3
    assert next(generator2) == 'q'
