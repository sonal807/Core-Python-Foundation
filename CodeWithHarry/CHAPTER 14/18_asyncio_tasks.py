#asyncio.create_task(): asyncio.create_task() schedules a coroutine to run concurrently as an asyncio Task
#and returns a Task object representing its execution.

import asyncio
# Asynchronous programming aur asyncio Tasks ko manage karne ke liye
# asyncio library import ki gayi hai


async def task(name):
    # Ye coroutine function ek individual async task ko represent karta hai
    print(f"{name} started")

    # Current task ko 2 seconds ke liye pause karta hai.
    # Is waiting period mein event loop doosre async tasks ko
    # execute karne ka opportunity de sakta hai.
    await asyncio.sleep(2)

    # Wait complete hone ke baad task yahan se resume hota hai
    print(f"{name} completed")


async def main():

    # Task 1 coroutine ko asyncio Task ke roop mein schedule karta hai.
    # create_task() ek Task object return karta hai.
    task1 = asyncio.create_task(task("Task 1"))

    # Task 2 ko bhi independently schedule karta hai.
    # Ab dono tasks event loop ke through concurrently progress kar sakte hain.
    task2 = asyncio.create_task(task("Task 2"))

    # Task 1 ke complete hone tak wait karta hai.
    # Task pehle hi schedule ho chuka hai, isliye wait ke dauran
    # event loop doosre available tasks ko bhi execute kar sakta hai.
    await task1

    # Task 2 ke complete hone tak wait karta hai.
    await task2


# Main coroutine ko execute karne ke liye event loop start karta hai.
asyncio.run(main())

#Task.done(): Task.done() returns True if the asyncio task has finished executing; otherwise, it returns False.
import asyncio

async def task():
    await asyncio.sleep(2)
    return "Task completed"

async def main():

    my_task = asyncio.create_task(task())

    print("Task completed: ", my_task.done())

    result = await my_task

    print("Result: ", result)
    print("Task completed: ", my_task.done())

asyncio.run(main())

#Task.result(): Task.result() returns the value returned by a completed asyncio task.
import asyncio

async def task():
    await asyncio.sleep(2)
    return "Task completed"

async def main():

    my_task = asyncio.create_task(task())

    await my_task

    print("Result: ", my_task.result())

asyncio.run(main())