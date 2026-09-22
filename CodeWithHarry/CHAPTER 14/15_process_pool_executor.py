# #ProcessPoolExecutor: It is a high-level Python tool that manages a pool of worker processes to execute multiple tasks concurrently,
# #especially useful for CPU-bound tasks.

# from concurrent.futures import ProcessPoolExecutor
# # Multiple worker processes ko easily manage karne ke liye
# # ProcessPoolExecutor import kiya

# import time
# # sleep() ka use karke task execution delay simulate karenge


# def calculate(number):
#     # Ye function given number ka square calculate karta hai
#     print(f"Calculating {number}")

#     # 2 seconds ka delay add kiya gaya hai taaki
#     # concurrent process execution ko easily observe kiya ja sake
#     time.sleep(2)

#     # Calculated square ko return karta hai
#     return number * number


# if __name__ == "__main__":

#     # Input values jinhe worker processes ke beech distribute kiya jayega
#     numbers = [1, 2, 3, 4, 5]

#     # Maximum 2 worker processes ka process pool create karta hai.
#     # Executor available worker processes ke beech tasks automatically distribute karega.
#     with ProcessPoolExecutor(max_workers=2) as executor:

#         # numbers ke har element par calculate() function execute karta hai.
#         # Tasks worker processes ke through concurrently execute honge.
#         results = executor.map(calculate, numbers)

#     # map() se mile results ko list mein convert karke display karta hai
#     print("Results:", list(results))

# # 	              ThreadPoolExecutor	    ProcessPoolExecutor
# # Worker	      Threads	                Processes
# # Shared memory	  Same process memory	    Separate process memory
# # Typical use	  I/O-bound	CPU-bound
# # Example	      API requests,             Heavy computation
# #                 file/network I/O	         
# # Main advantage  Efficient                 CPU cores ka better use
# #                 waiting/concurrency	

# # Ye absolute rule nahi hai, but practical guideline hai


# #submit() + Future
# from concurrent.futures import ProcessPoolExecutor
# # Multiple worker processes ko easily manage karne ke liye
# # ProcessPoolExecutor import kiya

# import time
# # sleep() ka use karke task execution delay simulate karenge


# def square(number):
#     # Ye function given number ka square calculate karta hai

#     # 2 seconds ka delay add kiya gaya hai taaki
#     # task ke concurrent execution ko observe kiya ja sake
#     time.sleep(2)

#     # Calculated square ko return karta hai
#     return number * number


# if __name__ == "__main__":

#     # Maximum 2 worker processes ka process pool create karta hai.
#     # Executor submitted tasks ko available worker processes
#     # ke through execute karega.
#     with ProcessPoolExecutor(max_workers=2) as executor:

#         # square(5) task ko executor ko submit karta hai.
#         # submit() immediately ek Future object return karta hai,
#         # jo submitted task ke result ko represent karta hai.
#         future = executor.submit(square, 5)

#         # Task executor ko successfully submit hone ke baad
#         # main process apna execution continue kar sakta hai.
#         print("Task submitted")

#         # Future se actual result retrieve karta hai.
#         # Agar task abhi complete nahi hua hai,
#         # result() task complete hone tak wait karega.
#         result = future.result()

#         # Task ka final result display karta hai
#         print("Result:", result)

# done() is a method of a Future object that checks whether the submitted task has finished executing.
from concurrent.futures import ProcessPoolExecutor
# Multiple worker processes ko easily manage karne ke liye
# ProcessPoolExecutor import kiya

import time
# sleep() ka use karke task execution delay simulate karenge


def square(number):
    # Ye function given number ka square calculate karta hai

    # 2 seconds ka delay add kiya gaya hai taaki
    # task ke execution ko observe kiya ja sake
    time.sleep(2)

    # Calculated square ko return karta hai
    return number * number


if __name__ == "__main__":

    # Maximum 2 worker processes ka process pool create karta hai.
    # Executor submitted tasks ko available worker processes
    # ke through execute karega.
    with ProcessPoolExecutor(max_workers=2) as executor:

        # square(5) task ko executor ko submit karta hai.
        # submit() ek Future object return karta hai,
        # jo submitted task ke result ko represent karta hai.
        future = executor.submit(square, 5)

        # Task complete hua hai ya nahi, uska current status check karta hai.
        # Agar task abhi execute ho raha hai to False return hoga.
        print("Task completed:", future.done())

        # Future se actual result retrieve karta hai.
        # Agar task abhi complete nahi hua hai,
        # result() task complete hone tak wait karega.
        result = future.result()

        # Task ka final result display karta hai
        print("Result:", result)

        # Task complete hone ke baad Future ka status dobara check karta hai.
        # Ab task complete ho chuka hai, isliye True return hoga.
        print("Task completed:", future.done())