import logging
import signal
import sys
import time

"""
Необхідно створити файл, що буде:
- реалізовувати 4 функції, що виконують математичні операції (додавання, віднімання, ділення та множення);
- приймати в себе аргументами значення, над якими треба виконати операцію (тобто саме 2 цілих числа);
- вибір функції залежатиме від змінної середовища, що за замовчуванням буде вказувати на функцію add;
- в разі наявності помилок введення (недоступне значення змінної середовища,
некоректна кількість аргументів, аргументи не є цілими числами і тд), завершувати програму з кодом 2.

Приклад виклику файлу:
$ python your_homework.py 1 2
3
$ FUNCTION=multiply python your_homework.py 3 -7
-21
"""


logging.basicConfig(
        filename='test.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(levelname)s %(name)s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO,
    )

logger = logging.getLogger()


def add(a, b):
    pass


def subtract(a, b):
    pass


def divide(a, b):
    pass


def multiply(a, b):
    pass


if __name__ == '__main__':

    x, y = sys.argv[1:3]

