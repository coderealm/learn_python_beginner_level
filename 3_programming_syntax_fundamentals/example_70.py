# file name: example_70.py

import asyncio

async def main():
    await asyncio.sleep(1)
    return "done"

print(asyncio.run(main()))
