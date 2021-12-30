import asyncio
import datetime
import math
import time
import requests
import aiohttp


def main():
    t0 = datetime.datetime.now()

    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task( compute_some() ),
        loop.create_task( compute_some() ),
        loop.create_task( compute_some() ),
        loop.create_task( download_some() ),
        loop.create_task( download_some() ),
        loop.create_task( download_some_more() ),
        loop.create_task( download_some_more() ),
        loop.create_task( wait_some() ),
        loop.create_task( wait_some() ),
        loop.create_task( wait_some() ),
        loop.create_task( wait_some() ),
    ]

    loop.run_until_complete(asyncio.gather(*tasks))

    dt = datetime.datetime.now() - t0
    print("Synchronous version done in {:,.2f} seconds.".format(dt.total_seconds()))


# no waiting here, cannot utilize 'async'
async def compute_some():
    print("Computing...")
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)

# waiting here with the get request, can utilize 'async'
async def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    
    
    """
    # sync implementation
    resp = requests.get(url)
    resp.raise_for_status()
    text = resp.text
    print("Downloaded (more) {:,} characters.".format(len(text)))
    """

    """
    # async implementation
    """
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            text = await resp.text()
    
    print("Downloaded (more) {:,} characters.".format(len(text)))
    

# waiting occurs here, but for the sake of an example will not use the aiohttp implementation
# we are imagining that there may not be an async API for these requests
async def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print("Downloaded {:,} characters.".format(len(text)))


async def wait_some():
    print("Waiting...")
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


if __name__ == '__main__':
    main()