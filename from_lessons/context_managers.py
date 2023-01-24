import contextlib


def prepare_data(data):
    return [dict(zip(data['columns'], row)) for row in data['data']]


@contextlib.contextmanager
def prepare_ctx(data):
    print('actions before')
    yield prepare_data(data)
    print('actions after')


def read_from_db():
    response_from_db = {
        'columns': ['a', 'b', 'c'],
        'data': [
            [1, 2, 3],
            [4, 5, 6],
        ],
    }
    print('before ctx')
    with prepare_ctx(response_from_db) as data:
        print('inside ctx')
        assert data == prepare_data(response_from_db)
        # >>> actual function goes here
        result = [row['a'] + row['c'] for row in data]
    print('after ctx')
    return result


if __name__ == '__main__':
    assert read_from_db() == [4, 10]
    