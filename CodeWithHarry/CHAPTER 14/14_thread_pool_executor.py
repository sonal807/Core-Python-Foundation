#ThreadPoolExecutor: ThreadPoolExecutor is a high-level tool in Python that manages a pool of worker threads to execute multiple tasks concurrently,
#especially useful for I/O-bound tasks.

# from concurrent.futures import ThreadPoolExecutor
# # Multiple worker threads ko easily manage karne ke liye
# # ThreadPoolExecutor import kiya

# import time
# # sleep() ka use karke task ke execution delay ko simulate karenge


# def task(name):
#     # Ye function ek individual task ko represent karta hai
#     print(f"{name} started")

#     # 2 seconds ka delay add kiya gaya hai taaki
#     # concurrent execution ko easily observe kiya ja sake
#     time.sleep(2)

#     # Task complete hone ke baad message display karta hai
#     print(f"{name} completed")


# if __name__ == "__main__":

#     # Maximum 3 worker threads ka thread pool create karta hai.
#     # Executor in threads ko automatically manage karega.
#     with ThreadPoolExecutor(max_workers=3) as executor:

#         # task() function ko diye gaye har task name ke liye execute karta hai.
#         # Available worker threads tasks ko concurrently execute karenge.
#         executor.map(
#             task,
#             ["Task 1", "Task 2", "Task 3"]
#         )

#     # Executor ke tasks complete hone ke baad final message
#     print("All tasks completed")

#submit(): submit() schedules a function to be executed by a worker thread
#and immediately returns a Future object representing that task.

#Future: A Future is an object that represents the result of a task that has been submitted for execution
#and may complete later.

from concurrent.futures import ThreadPoolExecutor
import time

def square(number):
    time.sleep(2)
    return number * number

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(square, 5)
        print("Is task completed?", future.done())

        print("Task submitted")

        result = future.result()

        print("Result: ", result)

        print("Is task completed?", future.done())