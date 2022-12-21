import random


def retry(attempts: int = 5, desired_value: any = None):
    """
    Retry function with this decorator "attempts" times
    until "desired_value" will be achieved or attempts will go out.
    """
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for attempt in range(attempts):
                res = func(*args, **kwargs)
                # print("№", attempt+1, "-> func=", res, "equal?", "desired", desired_value)
                func_res = [res]
                if desired_value in func_res:
                    print("The desired value", desired_value,
                          "was achieved in", attempt+1, "attempt(s)")
                    # print("res=", res)
                    return res
            return print("Failure! Desired value wasn't achieved. Out of attempts")
        return inner_wrapper
    return wrapper


# examples of implemented 'retry' decorator
@retry(desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


# @retry(desired_value=[1, 2])
# def get_random_values(choices, size=2):
#     return random.choices(choices, k=size)
#
#
# @retry(attempts=7, desired_value=3)
# def get_random_value():
#     return random.choice((1, 2, 3, 4, 5))

#
# @retry(attempts=2, desired_value=[1, 2, 3])
# def get_random_values(choices, size=2):
#     return random.choices(choices, k=size)


# @retry(50, desired_value=[1, 2, 3, 4])
# def get_random_values(choices, size=2):
#     return random.choices(choices, k=size)


def print_square(n: int, _attempts: int = 0):
    """ Print square with side's length equal to 'n'. """
    _attempts += 1
    if _attempts in (1, n):
        print(' * ' * n)
    else:
        print(' *', ' - ' * (n-2), '* ')
    if _attempts == n:
        return
    print_square(n, _attempts)


if __name__ == "__main__":
    # examples of function usages
    get_random_value()
    print("*" * 50)
    # get_random_values([1, 2, 3, 4])
    # print("*" * 50)
    # get_random_values([1, 2, 3, 4], 3)
    # print("*" * 50)
    # get_random_values([1, 2, 3, 4], size=1)
    # print("*" * 50)
    # get_random_values([1, 2, 3, 4], size=4)

    print_square(4)
