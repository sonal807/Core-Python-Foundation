#asyncio.gather(): asyncio.gather() runs multiple awaitable objects concurrently and collects their results into a single result sequence.
#Multiple async operations ko ek saath run karo aur unke results ek saath collect karo.

import asyncio
# Asynchronous programming aur asyncio.gather() ko use karne ke liye
# asyncio library import ki gayi hai


async def task(name, delay):
    # Ye coroutine function ek individual asynchronous task ko represent karta hai
    print(f"{name} started")

    # Given delay ke liye current coroutine ko pause karta hai.
    # Is waiting period mein event loop doosre async tasks ko
    # execute karne ka opportunity de sakta hai.
    await asyncio.sleep(delay)

    # Wait complete hone ke baad coroutine yahan se resume hoti hai
    print(f"{name} completed")

    # Task ka result return karta hai
    return f"{name} result"


async def main():

    # Multiple async tasks ko concurrently execute karta hai.
    # gather() sabhi tasks ke complete hone ka wait karta hai
    # aur unke returned results ko collect karta hai.
    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 2),
        task("Task 3", 2)
    )

    # gather() se returned results ko display karta hai.
    # Results arguments ke order mein return hote hain.
    print("Results:", results)


# Main coroutine ko execute karne ke liye event loop start karta hai
asyncio.run(main())


#Error Handling with asyncio.gather(): Error handling with asyncio.gather() allows us to control how exceptions raised by concurrent async tasks are handled.

import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(2)
    raise ValueError("Something went wrong in task 2")

async def task3():
    await asyncio.sleep(2)
    return "Task 3 completed"

async def main():

    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

    print(results)

asyncio.run(main())
#This will show error


#adding return_exceptions=True
import asyncio
# Asynchronous programming aur multiple async tasks ko
# concurrently execute karne ke liye asyncio library import ki


async def task1():
    # Task 1 ko simulate karne ke liye 1 second ka asynchronous wait
    await asyncio.sleep(1)

    # Task successfully complete hone par result return karta hai
    return "Task 1 completed"


async def task2():
    # Task 2 ko simulate karne ke liye 1 second ka asynchronous wait
    await asyncio.sleep(1)

    # Intentionally ValueError raise kar rahe hain
    # taaki asyncio.gather() ka exception handling behavior demonstrate ho
    raise ValueError("Something went wrong in Task 2")


async def task3():
    # Task 3 ko simulate karne ke liye 1 second ka asynchronous wait
    await asyncio.sleep(1)

    # Task successfully complete hone par result return karta hai
    return "Task 3 completed"


async def main():

    # Multiple async tasks ko concurrently execute karta hai.
    # gather() sabhi tasks ke complete hone ka wait karta hai
    # aur unke results ko ek sequence mein collect karta hai.
    #
    # return_exceptions=True hone par agar kisi task mein exception aaye,
    # to exception immediately raise nahi hota.
    # Instead, exception result sequence ke andar return ho jata hai.
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

    # Sabhi tasks ke returned results ko display karta hai.
    # Successful tasks ke results ke saath exception object bhi
    # result sequence mein present ho sakta hai.
    print("Results:", results)


# Main coroutine ko execute karne ke liye asyncio event loop start karta hai
asyncio.run(main())