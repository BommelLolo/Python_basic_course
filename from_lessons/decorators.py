import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        print('measure_time started')
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print('elapsed time', end - start)

        return result

    return wrapper


def cache(number_of_items):
    def wrapper(func):
        setattr(func, 'storage', {})
        func.storage = {}

        def inner_wrapper(*args):
            if args in func.storage:
                print('result from storage', args)
                return func.storage[args]

            if len(func.storage) == number_of_items:
                key = tuple(func.storage)[0]
                func.storage.pop(key)

            print('function execution', args)
            func.storage[args] = func(*args)

            return func.storage[args]

        return inner_wrapper

    return wrapper


@measure_time
def long_execution(seconds):
    print('long_execution started')
    time.sleep(seconds)
    print('long_execution ended')


@measure_time
def static_long_execution():
    print('static_long_execution started')
    time.sleep(3)
    print('static_long_execution ended')


@cache(2)
def add(a, b):
    return a + b


@cache(2)
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    # long_execution(1)
    # long_execution(seconds=1)
    # static_long_execution()

    print(add(2, 3))
    print(multiply(3, 4))
    print(add(2, 4))
    print(multiply(3, -4))
    print(add(2, 3))
    print(multiply(3, 0))
    print(add(2, 5))
    print(add(2, 3))
