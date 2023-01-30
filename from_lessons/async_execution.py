import asyncio
import time


class Ctx:
    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


async def awith():
    async with Ctx():
        pass


def func():
    pass


async def another_func():
    func()


async def job():
    # func()
    # await another_func()
    await asyncio.sleep(1)


async def task(s):
    await asyncio.sleep(s)
    print('slept', s, 'seconds')
    return s


async def main(num=10):
    tasks = [asyncio.create_task(job()) for _ in range(num)]
    await asyncio.gather(*tasks)


async def get_value(value):
    await asyncio.sleep(value)
    return value


async def run_get_values():
    start = time.time()
    print(await asyncio.gather(get_value(1), get_value(2)))
    print(time.time() - start)


async def wait_for_all(tasks):
    if not tasks:
        return

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for done_task in done:
        yield done_task

    async for t in wait_for_all(pending):
        yield t


async def sleep_tasks():
    tasks = [
        task(4),
        task(1),
        task(3),
    ]
    # while True:
    #     done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #     print(done)
    #     for done_task in done:
    #         print(done_task.result())
    #
    #     if pending:
    #         tasks = pending
    #     else:
    #         break
    async for t in wait_for_all(tasks):
        print(t.result())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(sleep_tasks())
    print('elapsed', time.time() - start)
