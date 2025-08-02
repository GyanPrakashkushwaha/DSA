import asyncio

async def main():
    print('hey Hello...')

async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(fn())





# asyncio.run(fn())
