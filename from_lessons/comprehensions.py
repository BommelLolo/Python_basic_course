if __name__ == '__main__':
    l = [0, 1, 2, 3, 4]

    assert l == [0, 1, 2, 3, 4]
    assert l == list(range(5))

    l1 = []
    for i in range(5):
        l1.append(i)

    assert l == l1

    l2 = [i for i in range(5)]
    assert l == l1 == l2

    even_only = [0, 2, 4, 6]
    l3 = []
    for i in range(8):
        if i % 2 == 0:
            l3.append(i)

    assert even_only == l3
    assert even_only == [i for i in range(8) if i % 2 == 0]

    l = []
    for i in range(3):
        for j in range(3):
            l.append(i + j)

    assert l == [0, 1, 2, 1, 2, 3, 2, 3, 4]
    assert l == [i + j for i in range(3) for j in range(3)]

    items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = 0
    for item in items:
        for el in item:
            res += el

    assert [el for item in items for el in item] == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    l = [1, 2, '3', 4]
    res = 0
    try:
        for el in l:
            res += el
    except TypeError:
        print('caught type error', el, type(el))

    print(res)
    print('el from loop', el)

    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    d = {}
    for i in range(1, 6):
        d[i] = i * i  # i ** 2

    assert d == squares
    assert squares == {i: i ** 2 for i in range(1, 6)}
    assert {1, 2, 3, 4, 5} == {i for i in range(1, 6)}

    for _ in range(5):
        print('hello')

    l = [0, 0, 0, 0, 0]
    assert [0 for _ in range(5)] == l
    assert [0] * 5 == l  # [[0], [0], ...] - not gonna happen

    t = (i for i in range(1024))
    assert not isinstance(t, tuple)

    l = ['', 123, None, False, True, 'sdfdg', [], {1, 4}]

    assert [123, True, 'sdfdg', {1, 4}] == [item for item in l if bool(item)]
    g = (item for item in l if bool(item))

    assert [123, True, 'sdfdg', {1, 4}] == list(g)
    assert [123, True, 'sdfdg', {1, 4}] == list(filter(None, l))

    assert [123, True, 'sdfdg', {1, 4}] == list(filter(lambda item: bool(item), l))
