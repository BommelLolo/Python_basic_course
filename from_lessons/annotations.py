from typing import Any, Union


class A:
    def __add__(self, other):
        pass


def add(
    a: Union[int, float, list, str, tuple],
    b: Union[int, float, list, str, tuple],
) -> Union[int, float, list, str, tuple]:
    return a + b


def validate(func):
    def wrapper(*args, **kwargs):
        annots = func.__annotations__
        args_to_kwargs = dict(zip(annots, args))
        kwargs.update(args_to_kwargs)

        for key, type_ in annots.items():
            if key == 'return':
                continue

            assert isinstance(kwargs[key], type_)

        return func(**kwargs)

    return wrapper


@validate
def mul(a: Union[int, str], b: int) -> str:
    return a * b


if __name__ == '__main__':
    assert add(1, 1.5) == 2.5
    # assert add(2, 's') == ???
    assert add(2, 3) == 5
    assert add(3.4, 2.5) == 5.9
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert add('abc', 'def') == 'abcdef'
    assert add((1, 2), (3, 4)) == (1, 2, 3, 4)

    assert add(True, False) == 1

    assert mul('3', 5) == '33333'
    