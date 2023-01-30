import time
from threading import Thread


def job(n):
    # print(f'start {n}')
    time.sleep(1)
    # print(f'end {n}')


def main(num=10):
    threads = []
    for i in range(num):
        threads.append(Thread(target=job, args=(i,)))

    for thread in threads:
        # print('before start')
        thread.start()
        # print('thread started')

    # print('before joins')
    for thread in threads:
        # print('waiting for thread', thread)
        thread.join()
    # print('after joins')


if __name__ == '__main__':
    for num in (10, 100, 1000, 5000, 10000, 100000):
        start = time.time()
        main(num=num)
        print(f'number of threads {num}; elapsed', time.time() - start)
