import time
from threading import Thread, Lock

value = 0
lock = Lock()


def adder(amount, repeats):
    global value
    lock.acquire()
    for _ in range(repeats):
        value = value + amount
    lock.release()


def subtractor(amount, repeats):
    global value
    for _ in range(repeats):
        with lock:
            value = value - amount


if __name__ == '__main__':
    adder_thread = Thread(target=adder, args=(100, 100000))
    adder_thread.start()
    subtractor_thread = Thread(target=subtractor, args=(100, 100000))
    subtractor_thread.start()

    print('Waiting for threads to finish...')
    subtractor_thread.join()
    adder_thread.join()

    print(f'Value: {value}')
    