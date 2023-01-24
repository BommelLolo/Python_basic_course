def gen(n):
    for i in range(n):
        yield i


class Iterator:
    counter = None

    def __init__(self, n):
        self.n = n
        self.counter = None
        self.reset()

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter + 1 == self.n:
            raise StopIteration

        self.counter += 1

        return self.counter

    def reset(self, initial_value=-1):
        if initial_value >= self.n:
            raise ValueError('initial value beyond the range')

        self.counter = initial_value


if __name__ == '__main__':
    g = gen(3)
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 2
    # g.__next__()
    for i in gen(3):
        print(i)

    it = Iterator(3)
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 2
    # assert next(it) == 3

    it = Iterator(5)
    for item in it:
        print(item)
