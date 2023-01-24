#!/usr/bin/python3
import logging
import os
import sys

logging.basicConfig(
    filename='test.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(levelname)s %(name)s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
)

logger = logging.getLogger()
log_level = os.environ.get('LOG_LEVEL', 'INFO')

logger.setLevel(logging.DEBUG if log_level == 'DEBUG' else logging.INFO)


if __name__ == '__main__':
    logger.debug('Called with: %s', sys.argv[1:])
    try:
        a, b = sys.argv[1:]
    except ValueError:
        logger.exception('Called with: %s', sys.argv[1:])
        exit(1)

    try:
        c = int(a) + int(b)
    except ValueError:
        logger.exception('Got non-int values: (%s, %s)', a, b)
        exit(1)

    print(c)
    logger.info('Result: %s', c)
