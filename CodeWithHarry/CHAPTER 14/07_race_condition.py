#Race Condition: A race condition occurs when multiple threads access and modify shared data at the same time,
#and the final result depends on the timing or order of their execution.

# import threading

# counter = 0

# def increment():
#     global counter

#     for _ in range(100000):
#         counter += 1

# thread1 = threading.Thread(target= increment)
# thread2 = threading.Thread(target= increment)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Final counter: ", counter)

import threading  # Multiple threads create aur manage karne ke liye
import time  # sleep() function use karne ke liye


counter = 0  # Shared variable jise dono threads modify karenge


def increment():
    global counter  # Function ke andar global counter ko modify karne ke liye

    # Counter ko 1000 times increase karne ke liye loop
    for _ in range(1000):

        # Current counter value ko local variable mein read kar rahe hain
        current = counter

        # Thodi der wait kar rahe hain taaki doosre thread ko execute hone ka chance mile
        # Isse race condition ko clearly reproduce karna easier hota hai
        time.sleep(0.0001)

        # Purani current value mein 1 add karke shared counter ko update kar rahe hain
        # Yahin par threads ek doosre ke updates overwrite kar sakte hain
        counter = current + 1


# Thread 1 create kiya; start hone par increment() function execute karega
thread1 = threading.Thread(target=increment)

# Thread 2 create kiya; start hone par increment() function execute karega
thread2 = threading.Thread(target=increment)


# Thread 1 ko start kiya
thread1.start()

# Thread 2 ko start kiya
thread2.start()


# Main thread ko Thread 1 ke complete hone tak wait karwaya
thread1.join()

# Main thread ko Thread 2 ke complete hone tak wait karwaya
thread2.join()


# Dono threads complete hone ke baad final counter value print karenge
print("Final counter:", counter)

#When multiple threads access and modify shared data without proper synchronization,
#their operations can interfere with each other and produce an unexpected result.