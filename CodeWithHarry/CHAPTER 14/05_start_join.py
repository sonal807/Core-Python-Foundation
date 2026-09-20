#start() join(): start() begins the execution of a thread,
#while join() makes the calling thread wait until that thread has finished its execution.

import threading #Threading is a built-in module which is useful in creating, starting, controlling and synchrozation of thread.
import time  #Improted time module, sleep() doesn't stop whole program; the thread where the sleep() is executing that thread will wait

def task():  #we have created a normal python function whose work is to start, wait for two second and get complete, and we have only defined the task() is not executed
    print("Task started")
    time.sleep(2)
    print("Task completed")

thread = threading.Thread(target=task) #created a Thread object, target=task means when this thread start, then execute task in this thread
                                       #targest=task means assinging funtion for thread, target=task() immediately executing task function
thread.start()  #Actual thread starts now, start() internally thread ko start karta hai aur uske target function ko execute karwata hai. we don't need to call task() manually

thread.join()  #Main thread will wait untill the worker thread get completed

print("Main program continues...")  #Main thread is executing, we have used thread.join() which will make this line (main thread) wait untill the worker thread gets completed

#program flow:
# PROGRAM START
#      │
#      ↓
# import threading
#      │
#      ↓
# import time
#      │
#      ↓
# task() function define
#      │
#      ↓
# Thread object create
# target = task
#      │
#      ↓
# thread.start()
#      │
#      ├──────────────→ Worker Thread
#      │                    │
#      │                    ↓
#      │              Task started
#      │                    │
#      │                    ↓
#      │                 sleep(2)
#      │                    │
#      │                    ↓
#      │              Task completed
#      │                    │
#      │                    ↓
#      │              Worker finished
#      │
#      ↓
# thread.join()
#      │
#      ↓
# Wait until worker finishes
#      │
#      ↓
# Main program continues...


#Flow
# Main Thread
#     │
#     ├── thread.start()
#     │
#     ↓
# Worker Thread ───────→ Task started
#                        ↓
#                      wait 2 sec
#                        ↓
#                     Task completed
#                        │
#     ← thread.join() ───┘
#     │
#     ↓
# Main program continues


#what if we remove join(): main thread will not wait for worker thread to get complete, when the worker therad is doing its work for 2 seconds the main thread will get execute, it will not wait for completion of worker thread
import threading
import time


def task():
    print("Task started")
    time.sleep(2)
    print("Task completed")


thread = threading.Thread(target=task)

thread.start()

print("Main program continues...")

#Flow:
# Main Thread                 Worker Thread
#     │                            │
#     │── start() ────────────────→│
#     │                            │
#     │                      Task started
#     │                            │
#     │                      sleep(2)
#     │                            │
#     ↓                            │
# Main program continues...       │
#     │                            │
#     │                      Task completed
#     │                            │
#     └────────────────────────────┘