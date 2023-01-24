import signal
import sys
import time


def handler(signum, frame):
    print('finishing process')
    time.sleep(2)
    sys.exit(0)


def endless_loop():
    while True:
        print('in the loop')
        time.sleep(1)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    endless_loop()
