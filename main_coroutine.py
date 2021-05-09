import asyncio
import time

async def say_hello():
    print(f'waiting...')
    await time.sleep(1)
    print(f'Hello!')


async def main():

    