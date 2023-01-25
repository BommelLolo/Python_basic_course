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

    @property
    def add(self):
        self.result = self.arg_1 + self.arg_2
        return self.result

    @property
    def subtract(self):
        self.result = self.arg_1 - self.arg_2
        return self.result

    @property
    def divide(self):
        self.result = self.arg_1 / self.arg_2
        return self.result

    @property
    def multiply(self):
        self.result = self.arg_1 * self.arg_2
        return self.result


if __name__ == '__main__':
    # check function name
    function = {'add', 'subtract', 'multiply', 'divide'}
    if method not in function:
        logger.error('Got invalid function name: %s', str(method))
        sys.exit(2)

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

    try:
        getattr(c, method)
    except ZeroDivisionError:
        logger.exception('Tried to divide by 0')
        sys.exit(2)
    # log result
    logger.info('Result: %s', c.result)
