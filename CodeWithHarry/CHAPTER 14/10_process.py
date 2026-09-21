#Process: A Process is an independent unit of execution that runs separately from the main Python program and 
#can be used to perform tasks concurrently.

import multiprocessing
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task completed")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)
    print("Process created")

    process.start()
    print("Process started")

    process.join()

    print("Process finished")

#Complete flow
# Main Process
#      │
#      ├── Process create
#      │
#      ├── Process start
#      │       │
#      │       └── Child Process
#      │              ├── Task started
#      │              ├── wait 2 sec
#      │              └── Task completed
#      │
#      ├── join() → wait
#      │
#      └── Process finished

#Passing arguments to process: Arguments allow us to pass data from the main process to the function executed by a child process.
import multiprocessing
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

if __name__ == "__main__":
    process = multiprocessing.Process(
        target=task,
        args= ("Process 1",)
    )

    process.start()
    process.join()

    print("Main process finished")

#Multiple process: Multiple processes allow a program to create and run more than one independent process to handle different tasks concurrently.

import multiprocessing
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

if __name__ == "__main__":
    process1 = multiprocessing.Process(
        target=task,
        args=("Process 1",)
    )

    process2 = multiprocessing.Process(
        target=task,
        args=("Process 2",)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes completed")


#is_alive(): is_alive() is a method used to check whether a process is currently running or has already finished.

import multiprocessing
import time

def task():
    print("Task started")
    time.sleep(3)
    print("Task completed")

if __name__ == "__main__":
    process = multiprocessing.Process(target=task)

    print("Before start: ", process.is_alive())

    process.start()

    print("After start: ", process.is_alive())

    process.join()

    print("After join: ", process.is_alive())