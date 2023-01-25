import logging
import sys
import os


logging.basicConfig(
    filename='hw_11.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(levelname)s %(name)s [%(filename)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
)

logger = logging.getLogger()
method = os.environ.get('FUNCTION', 'add')


class MathFunction:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.result = None

    def add(self):
        self.result = self.arg_1 + self.arg_2
        return self.result

    def subtract(self):
        self.result = self.arg_1 - self.arg_2
        return self.result

    def divide(self):
        self.result = self.arg_1 / self.arg_2
        return self.result

    def multiply(self):
        self.result = self.arg_1 * self.arg_2
        return self.result


class InvalidDMethodError(Exception):
    def __init__(self):
        logger.error('Got invalid function name: %s', str(method))
        sys.exit(2)


if __name__ == '__main__':
    # check function name
    function = {'add', 'subtract', 'multiply', 'divide'}
    if method not in function:
        raise InvalidDMethodError()

    logger.info('Function "%s" called with: %s', method, sys.argv[1:])
    #  check quantity of arguments
    try:
        a, b = sys.argv[1:]
    except ValueError:
        logger.exception('Called with: %s', sys.argv[1:])
        sys.exit(2)
    # check type of arguments
    try:
        a_int = int(a)
        b_int = int(b)
    except ValueError:
        logger.exception('Got non-int values: (%s, %s)', a, b)
        sys.exit(2)

    c = MathFunction(a_int, b_int)
    # use function for object
    if method == 'add':
        c.add()
    elif method == 'subtract':
        c.subtract()
    elif method == 'multiply':
        c.multiply()
    elif method == 'divide':
        try:
            c.divide()
        except ZeroDivisionError:
            logger.exception('Tried to divide by 0')
            sys.exit(2)
    # log result
    logger.info('Result: %s', c.result)
