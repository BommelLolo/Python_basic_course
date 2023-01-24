def remove_short_lines(line):
    return len(line) >= 6


def add(a, b):
    return a + b


def strict_map(func, iterable, *iterables):
    length = len(iterable)
    for it in iterables:
        assert length == len(it), 'all iterables must be of length ' + str(length)

    return map(func, iterable, *iterables)


def gen_func():
    i = 0
    while True:
        yield i
        i += 1


def simple_yield():
    yield 1
    yield 2
    yield 3


def simple_return():
    return 1
    return 2
    return 3


def get_one(arr):
    # for item in arr:
    #     yield item
    yield from arr


def yield_from_gen():
    yield from simple_yield()


def g_func():
    yield 1
    yield 2
    return 3


def countdown(n):
    yield n
    if n == 0:
        return

    yield from countdown(n - 1)


if __name__ == '__main__':
    l = ['', 123, None, False, True, 'sdfdg', [], {1, 4}]
    for item in filter(None, l):
        print(item)

    lines = ['abc', 'blablabla', 'orange', 'world', '!@#$%^&*(']
    assert list(filter(lambda line: remove_short_lines(line), lines)) == ['blablabla', 'orange', '!@#$%^&*(']
    assert list(filter(remove_short_lines, lines)) == ['blablabla', 'orange', '!@#$%^&*(']
    assert [line for line in lines if remove_short_lines(line)] == ['blablabla', 'orange', '!@#$%^&*(']

    upper_lines = []
    for line in lines:
        upper_lines.append(line.upper())

    assert upper_lines == ['ABC', 'BLABLABLA', 'ORANGE', 'WORLD', '!@#$%^&*(']
    assert list(map(lambda line: line.upper(), lines)) == upper_lines
    assert list(map(str.upper, lines)) == upper_lines

    assert list(map(lambda args: add(*args), [(1, 2), (3, 4), (5, 6)])) == [3, 7, 11]
    assert list(map(add, [1, 3, 5], [2, 4, 6])) == [3, 7, 11]

    assert list(strict_map(add, [1, 3, 5], [2, 4, 6])) == [3, 7, 11]

    # ([1, 2, 3], [4, 5, 6]) -> ((1, 4), (2, 5), (3, 6))
    assert list(zip([1, 2, 3], [4, 5, 6])) == [(1, 4), (2, 5), (3, 6)]
    assert list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    assert list(zip(keys, values)) == [('a', 1), ('b', 2), ('c', 3)]
    assert dict(zip(keys, values)) == {'a': 1, 'b': 2, 'c': 3}
    assert dict([('a', 1), ('b', 2), ('c', 3)]) == {'a': 1, 'b': 2, 'c': 3}

    response_from_db = {
        'columns': ['a', 'b', 'c'],
        'data': [
            [1, 2, 3],
            [4, 5, 6],
        ],
    }
    assert response_from_db['data'][1][1] == 5

    data = [dict(zip(response_from_db['columns'], row)) for row in response_from_db['data']]
    assert data == [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
    assert data[1]['b'] == 5

    gen_expr = (item for item in range(2))

    assert next(gen_expr) == 0
    assert next(gen_expr) == 1

    gen_expr = (item for item in range(2))
    for item in gen_expr:
        print(item)

    gen_expr = (item for item in range(5))

    assert next(gen_expr) == 0
    assert next(gen_expr) == 1
    assert list(gen_expr) == [2, 3, 4]
    assert next(gen_expr, 'default_value') == 'default_value'
    assert next(gen_expr, 'default_value') == 'default_value'
    assert next(gen_expr, 'default_value') == 'default_value'
    assert next(gen_expr, 'default_value') == 'default_value'

    generator = gen_func()
    assert next(generator) == 0
    assert next(generator) == 1
    assert next(generator) == 2

    print('=' * 80)
    for i in generator:
        print(i)
        if i == 10:
            break

    g = get_one([1, 2, 3])
    assert next(g) == 1
    assert next(g) == 2

    g = yield_from_gen()
    assert next(g) == 1
    assert next(g) == 2
    