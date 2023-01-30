class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print('in new')
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class DBConnector(Singleton):
    def __init__(self):
        print('in init')


def singleton(klass):
    instance = None

    def getinstance(*args, **kwargs):
        nonlocal instance
        if not isinstance(instance, klass):
            instance = klass(*args, **kwargs)

        return instance

    return getinstance


@singleton
class B:
    pass


if __name__ == '__main__':
    conn1 = DBConnector()
    conn2 = DBConnector()

    assert conn1 is conn2

    b1 = B()
    b2 = B()

    assert b1 is b2
