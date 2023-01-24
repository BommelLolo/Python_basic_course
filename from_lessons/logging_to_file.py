import logging


if __name__ == '__main__':
    logging.basicConfig(
        filename='test.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(levelname)s %(name)s [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO,
    )

    logger = logging.getLogger('abc')
    logger.info('Hello')
    logger.setLevel(logging.DEBUG)
    logger.debug('Debug message')
    # print('Debug message', file=open('test.log', 'a'))
    logger.setLevel(logging.WARNING)
    logger.log(logging.INFO, 'Info message')

    logger.error('Got an error here: %s %s %s', 1, 2, 3)

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception('Tried to divide by 0')
        logger.error('Tried to divide by 0', exc_info=True)
        