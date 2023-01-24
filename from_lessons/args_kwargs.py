def add(a, var):
    return a + var


def subtract(a, b=0):
    return a - b


def subtract_full_default(a=0, b=0):
    return a - b


# mutable - list, set, dict
def add_to_list(val, arr=None):
    if arr is None:
        arr = []

    arr.append(val)

    return arr


def ternary(arr=None):
    arr = [] if arr is None else arr
    arr = arr or []


def add_many(*values, default=0):
    return sum(values, default)


def print_config(**kwargs):
    print(kwargs)


def args_kwargs(*args, **kwargs):
    print(args, kwargs)


def func(a, b, *args, c, d=3, e=2, **kwargs):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'e:', e, 'args:', args, 'kwargs:', kwargs)


def pos_only(a, b, /):
    print(a, b)


def pos_and_kwargs(a, /, b):
    print(a, b)


def kwargs_only(*, a, b):
    print(a, b)


def pos_and_kwargs2(a, *, b):
    print(a, b)


def restricted_call(a, b, /, *, c, d):
    print(a, b, c, d)


def values_to_use(item):
    return item['a'], item['b']


if __name__ == '__main__':
    print(add(2, 3))
    print(add(2, var=3))
    print(add(var=2, a=3))

    t = (1, 2)
    l = [3, -7]
    d = {'key1': 'value', 'key2': 'value'}
    print(add(t[0], t[1]))
    print(add(*t))
    print(add(*(3, 4)))
    print(add(*l))
    print(add(*{1, 0}))
    print(add(*d))

    kwargs = {'a': 4, 'var': 7}
    print(add(**kwargs))  # add(a=3, var=7)
    print(add(a=kwargs['a'], var=kwargs['var']))

    print(add(*(4,), **{'var': 4}))

    print('=' * 50)

    print(subtract(2))
    print(subtract(2, 3))
    print(subtract(a=4))
    print(subtract(1, b=3))

    print(subtract_full_default())
    print(subtract_full_default(b=-1))
    print(subtract_full_default(1))
    print(subtract_full_default(a=1))
    print(subtract_full_default(1, 3))
    print(subtract_full_default(b=1, a=3))

    print('=' * 50)

    print(add_many())
    print(add_many(1))
    print(add_many(1, 2))
    print(add_many(1, 2, 3))
    print(add_many((1, 2, 3), (3, 4, 5), default=()))

    print('=' * 50)

    print_config()
    print_config(lights='on')
    print_config(sound='on')
    print_config(lights='on', sound='on')
    print_config(**{'lights': 'on', 'sound': 'on'})
    print_config(**{'lights': 'on', '1': 'on'})

    print('=' * 50)

    func(1, 2, c=-3)
    func(1, 2, 7, 8, 9, 0, c=-3)
    func(1, 2, c=-3, f=10)
    func(1, 2, d=-173, c=-3, f=10)
    func(a=1, b=2, c=-3, f=10)

    pos_only(1, 2)

    pos_and_kwargs(1, 2)
    pos_and_kwargs(1, b=2)

    kwargs_only(b=1, a=2)

    pos_and_kwargs2(1, b=4)
    pos_and_kwargs2(a=1, b=2)

    restricted_call(1, 2, c=3, d=4)

    print('=' * 50)

    l_func = lambda: True
    print(l_func())

    print(max({'a': 3}, {'a': 4}, key=lambda item: item['a']))
    print(min({'a': 4, 'b': 7}, {'a': 4, 'b': 6}, key=lambda item: (item['a'], item['b'])))

    print(min({'a': 4, 'b': 7}, {'a': 4, 'b': 6}, key=lambda item: values_to_use(item)))
    print(min({'a': 4, 'b': 7}, {'a': 4, 'b': 6}, key=values_to_use))

    a = -12

    if a > 0:
        if a > 5:
            print('big value')
        else:
            print('not that big')
    else:
        print('below zero')

    print('big value' if a > 5 else 'not that big' if a > 0 else 'below zero')
