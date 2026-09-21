#Pool: A process pool is a collection of worker processes that can execute multiple tasks concurrently,
#allowing us to efficiently distribute work without manually creating each process.

#Basic pool
import multiprocessing  # Multiple worker processes create aur manage karne ke liye
import time  # sleep() use karke task ko temporarily delay karne ke liye


def square(number):
    # Current worker kis number par calculation kar raha hai, ye show karta hai
    print(f"Calculating square of {number}")

    # 1 second wait; concurrency ko clearly observe karne ke liye
    time.sleep(1)

    # Number ka square calculate karke result return karta hai
    return number * number


if __name__ == "__main__":

    # Ye input values hain jin par square() function apply hoga
    numbers = [1, 2, 3, 4, 5]

    # 3 worker processes ka pool create kiya.
    # Pool available workers ke beech tasks distribute karega.
    with multiprocessing.Pool(3) as pool:

        # numbers ke har element par square() function apply karta hai.
        # Pool worker processes ke through tasks execute karta hai
        # aur saare returned values ko results list mein collect karta hai.
        results = pool.map(square, numbers)

    # Pool se milne wale final results print karta hai
    print("Results:", results)

#pool.map is convinient when we have to give only one argument to the function.
#But what if we have to give multiple arguments to function, so there starmap() is useful.

#starmap(): starmap() applies a function to multiple argument tuples, allowing each task to receive more than one argument.

import multiprocessing

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    tasks = [
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9)
    ]

    with multiprocessing.Pool(3) as pool:
        results = pool.starmap(multiply, tasks)

    print("Results: ", results)

# map_async(): map_async() applies a function to multiple inputs asynchronously,
# allowing the main process to continue working without immediately waiting for all tasks to finish.

import multiprocessing
import time


def square(number):
    # Show which number is currently being processed by a worker
    print(f"Calculating square of {number}")

    # Delay added only to make concurrent execution easier to observe
    time.sleep(1)

    # Calculate and return the square of the given number
    return number * number


if __name__ == "__main__":

    # Input data that will be distributed among the worker processes
    numbers = [1, 2, 3, 4, 5]

    # Create a pool containing 3 worker processes.
    # The pool automatically distributes tasks among available workers.
    with multiprocessing.Pool(3) as pool:

        # Apply square() to every number using the worker processes.
        # map() waits for all tasks to finish and returns their results.
        results = pool.map(square, numbers)

    # Display the results returned by the worker processes
    print("Results:", results)