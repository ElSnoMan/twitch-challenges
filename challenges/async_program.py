# synchronous - running things in order
# asynchronous - running things at the same time (concurrently, or parallel)

import asyncio
import time


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print(f'{stop_time - start_time} seconds')
    return wrapper


def synchronous_task():
    time.sleep(1)
    return {'name': 'value'}


@stopwatch
def create_objects(how_many: int):
    for _ in range(how_many):
        print(synchronous_task())


async def asynchronous_task():
    await asyncio.sleep(1)
    return {'name': 'value'}


@stopwatch
def create_async_objects(how_many: int):
    loop = asyncio.new_event_loop()

    # add the tasks the execute
    tasks = [loop.create_task(asynchronous_task()) for _ in range(how_many)]
    loop.run_until_complete(asyncio.wait(tasks))

    # get the results and do something with them
    [print(task.result()) for task in tasks]
    loop.close()


if __name__ == '__main__':
    # create_objects(30)
    create_async_objects(60)
