#async defines a coroutine function that can perform asynchronous operations,
#while await pauses that coroutine until an asynchronous operation is ready to continue, allowing other async tasks to make progress.

import asyncio

async def task():
    print("Task started")
    print("Task completed")

asyncio.run(task())

#coroutine:A coroutine is a special Python function defined with async def that can pause its execution with await and later resume from where it paused.
import asyncio


async def task():
    print("Task started")
    await asyncio.sleep(2)
    print("Task completed")


asyncio.run(task())

#async def → coroutine function → calling it produces a coroutine → asyncio event loop executes it.


#await: await pauses the execution of a coroutine until the awaited asynchronous operation completes,
#while allowing the event loop to run other available async tasks.
import asyncio


async def task():
    print("Task started")

    await asyncio.sleep(2)

    print("Task completed")


asyncio.run(task())

# Execution:
# Task started
#       ↓
# await asyncio.sleep(2)
#       ↓
# Current coroutine pauses
#       ↓
# 2 seconds
#       ↓
# Coroutine resumes
#       ↓
# Task completed

#await with Multiple Coroutines
import asyncio

async def task(name):
    print(f"{name} started")

    await asyncio.sleep(2)

    print(f"{name} completed")

async def main():
    await task("Task 1")
    await task("Task 2")

asyncio.run(main())