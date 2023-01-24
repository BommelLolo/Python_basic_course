def echo():
    line = 123
    while True:
        line = yield line


if __name__ == '__main__':
    g = echo()
    assert next(g) == 123
    assert g.send('hello') == 'hello'
    assert next(g) is None
    assert g.send('abc') == 'abc'
