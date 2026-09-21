#concurrent.futures: concurrent.futures is a high-level Python module that provides a simple interface for executing tasks concurrently using threads or processes.

#concurrent.futures
    #    │
    #    ├── ThreadPoolExecutor
    #    │
    #    └── ProcessPoolExecutor

#Basic
# from concurrent.futures import ProcessPoolExecutor
# # Process-based concurrent execution ko easily manage karne ke liye
# # ProcessPoolExecutor import kiya


# def square(number):
#     # Ye function given number ka square calculate karke return karta hai
#     return number * number


# if __name__ == "__main__":

#     # Ye input values hain jin par square() function execute hoga
#     numbers = [1, 2, 3, 4, 5]

#     # Maximum 3 worker processes ka executor create kiya.
#     # Executor available workers ke beech tasks distribute karega.
#     with ProcessPoolExecutor(max_workers=3) as executor:

#         # numbers ke har element par square() function apply karta hai.
#         # map() multiple tasks ko worker processes ke through execute karta hai.
#         # Ye directly normal list ke bajay ek iterable result return karta hai.
#         results = executor.map(square, numbers)

#     # Results iterable ko list mein convert karke final results display karta hai
#     print("Results:", list(results))

# #concurrent.futures = concurrency ko simpler/higher-level way mein manage karne ka framework.

# # ProcessPoolExecutor = processes ke liye
# # ThreadPoolExecutor = threads ke liye

# #Future in concurrent.futures: A Future represents the result of a task that has been submitted for execution and may still be running or may complete later.

# from concurrent.futures import ProcessPoolExecutor  # Process-based concurrent execution ke liye
# import time  # Task ko temporarily delay karne ke liye


# def square(number):
#     # Ye function given number ka square calculate karta hai
#     time.sleep(2)  # 2 seconds ka delay; task execution ko observe karne ke liye
#     return number * number  # Calculated square ko return karta hai


# if __name__ == "__main__":

#     print("Program started")

#     # Maximum 3 worker processes ka executor create karta hai.
#     # Executor submitted tasks ko available worker processes mein execute karta hai.
#     with ProcessPoolExecutor(max_workers=3) as executor:

#         # square(5) task ko executor ko submit karta hai.
#         # submit() immediately ek Future object return karta hai,
#         # jo future mein task ke result ko represent karta hai.
#         future = executor.submit(square, 5)

#         # Task submit hone ke baad main process continue kar sakta hai.
#         print("Task submitted")

#         # Future se actual result retrieve karta hai.
#         # Agar task abhi complete nahi hua hai, result() uske complete hone tak wait karega.
#         result = future.result()

#         # Task ka final result display karta hai
#         print("Result:", result)

#     # Executor ka kaam complete hone ke baad program finish hota hai
#     print("Program finished")

#FLow:
# executor create
#       ↓
# submit(square, 5)
#       ↓
# Future object
#       ↓
# Task execute hota hai
#       ↓
# future.result()
#       ↓
# 25

#future.done(): done() is a method of a Future object that checks whether the submitted task has finished executing.

from concurrent.futures import ProcessPoolExecutor
import time

def square(number):
    time.sleep(2)
    return number * number

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=2) as executor:
        future = executor.submit(square, 5)

        print("Task completed: ", future.done())

        result = future.result()

        print("Result: ", result)
        print("Task completed: ", future.done())