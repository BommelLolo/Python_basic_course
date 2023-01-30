import asyncio
import time


async def job(n):
    # print(f'start {n}')
    await asyncio.sleep(1)
    # print(f'end {n}')


async def main(num=10):
    jobs = [job(i) for i in range(num)]
    await asyncio.gather(*jobs)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for num in (10, 100, 1000, 10000, 100000, 1000000):
        start = time.time()
        loop.run_until_complete(main(num))
        print('elapsed', time.time() - start)
