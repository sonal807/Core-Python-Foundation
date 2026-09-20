#Process vs Thread: A process is an independent running program with its own memory space,
#while a thread is a smaller unit of execution within a process that shares the process's memory.

import os
import threading

print("Process ID: ", os.getpid())  #It shows that python program is running inside a process
print("Main Thread ID: ", threading.get_ident()) #And in that process main thread is executing