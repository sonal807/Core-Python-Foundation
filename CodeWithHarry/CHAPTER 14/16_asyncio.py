#asynchio: asyncio is a Python library for writing concurrent programs using asynchronous programming,
#especially for I/O-bound tasks such as network requests, APIs, and file operations.

import asyncio
# Python ki asyncio library import ki gayi hai
# asynchronous programming ke features use karne ke liye


async def task():
    #An asynchronous function in Python (often called a coroutine) allows your program to perform other tasks
    #while waiting for operations like network requests, database queries, or file I/O to finish
    # async def se ek asynchronous function (coroutine function) create kiya gaya hai
    print("Task Started")

    # 2 seconds ka asynchronous wait create karta hai.
    # Is waiting period mein event loop doosre async tasks ko
    # execute karne ka opportunity de sakta hai.
    await asyncio.sleep(2)

    # Wait complete hone ke baad task yahan se continue hota hai
    print("Task completed")


# asyncio.run() asynchronous function ko execute karne ke liye
# event loop ko start aur manage karta hai.
asyncio.run(task())