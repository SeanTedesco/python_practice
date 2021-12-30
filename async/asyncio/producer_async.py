import datetime
import colorama
import random
import asyncio


"""
To make a python method into an asyncio coroutine
- include 'async' keyowrd before 'def'
- include 'await' inside the method in areas that asyncio is waiting on something, 
    ex: asyncio.Queue.put(), asyncio.sleep()
"""

async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx*idx
        await data.put((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + 
            " -- generated item {}".format(idx), flush=True
        )
        await asyncio.sleep(random.random() + .5)

async def process_data(num: int, data: asyncio.Queue):

    processed = 0
    while processed < num:
        item = await data.get()

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
            " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True
        )
        await asyncio.sleep(.5)

def main():

    # get the main loop going...
    main_loop = asyncio.get_event_loop()

    # print out a header...
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    # get the required data structure to be used in asyncio
    # replaces our previous list, typical FIFO queue
    data = asyncio.Queue()

    # seperate our function calls into different tasks
    task1 = main_loop.create_task( generate_data(20, data) )
    task2 = main_loop.create_task( generate_data(20, data) )
    task3 = main_loop.create_task( process_data(40, data) )

    # gather tasks together, this is required as 'run_until_complete' accepts only one task
    tasks = asyncio.gather(task1, task2, task3)

    # finally run the tasks, this method does the actual execution 
    main_loop.run_until_complete(tasks)

    # print out a footer...
    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


if __name__ == '__main__':
    main()
