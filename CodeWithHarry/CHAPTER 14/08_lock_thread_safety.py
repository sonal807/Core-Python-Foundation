#A lock is a synchronization mechanism that allows only one thread at a time to access a protected section of shared data.
#Thread safety means that shared data remains correct and consistent when accessed by multiple threads.

#Creating lock: lock = threading.lock()
#Acquiring lock: lock.acquire()
#Releasing lock: lock.release()

#In python we generally use:
#with lock:
#which is used to: Lock acquire
#                      ↓
#               Protected code execute
#                      ↓
#               Lock automatically release
#If any error comes in between, with block help to release lock properly


import threading
import time

counter = 0

lock = threading.Lock()

def increment():
    global counter 

    for _ in range(1000):

        with lock:
            current = counter
            time.sleep(0.0001)
            counter = current + 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter:", counter)

#Lock ensures that only one thread at a time can execute the critical section that accesses shared data,
#preventing race conditions and keeping the data consistent