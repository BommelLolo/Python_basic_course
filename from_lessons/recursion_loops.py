def is_prime_number():
    stop_outer_loop = False
    for n in range(2, 10):
        if stop_outer_loop:
            break

        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n / x)
                stop_outer_loop = True
                break

    print('out of loops')


def print_numbers(stop, current=0):
    if stop == current:
        return

    print(current)
    print_numbers(stop, current + 1)


def factorial(n):  # n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
    # if n == 0 or n == 1:
    # if n in (0, 1):  # [0, 1] / {0, 1}
    #     return 1
    #
    # return n * factorial(n - 1)
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


if __name__ == '__main__':
    # range(10)
    # range(0, 10)
    # range(0, 10, 2) -> (0, 2, 4, 6, 8)

    for i in range(10):  # (stop - start) // step
        print(i)

    l = ['item1', 0, None]
    for item in l:
        print(item)

    word = 'hello, world!'
    for char in word:
        print(char)

    # a, b = (1, 2)
    # a == 1
    # b == 2
    # enumerate(word) -> ((0, 'h'), (1, 'e'), ...)
    # enumerate(word, start=3) -> ((3, 'h'), (4, 'e'), ...)
    for idx, char in enumerate(word, start=3):
        print(idx, char)

    for char in word:
        if char == ',':
            break

        print('>>>', char)

    print('after loop')

    for char in word:
        if char in ',!':
            continue

        if char == ' ':
            print('---', '-')
        else:
            print('---', char)

    is_prime_number()

    for i in range(10):
        # break
        var = i
    else:
        print(var)

    while True:
        print('endless loop')
        break

    print('after endless loop')

    flag = True
    i = 0
    while flag:
        print('doing something', i)
        i += 1
        if i == 10:
            flag = False

    print('=' * 50)

    flag = True
    i = 0
    while flag:
        print('doing something', i)
        i += 1
        flag = i != 10

    print('=' * 50)

    i = 0
    while i < 10:
        print('doing something', i)
        i += 1

    print('calling recursion')
    print_numbers(4)

    print('0! =', factorial(0))
    print('1! =', factorial(1))
    print('5! =', factorial(5), '(must be 120)')

    print('1200! =', factorial(1200))
