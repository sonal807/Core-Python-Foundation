#Multiple threading is the use of multiple threads within the same process to handle multiple tasks concurrently.

import threading  # Thread create aur manage karne ke liye threading module import kiya

import time  # sleep() use karne ke liye time module import kiya


def task(name):  # Ek function banaya jo task ka naam argument ke roop mein lega

    print(f"{name} started")  # Task start hone ka message print karega

    time.sleep(2)  # Current thread ko 2 seconds ke liye wait karayega

    print(f"{name} completed")  # 2 seconds ke baad task complete hone ka message


# Thread 1 create kiya; start hone par task("Task 1") execute hoga
thread1 = threading.Thread(target=task, args=("Task 1",))

# Thread 2 create kiya; start hone par task("Task 2") execute hoga
thread2 = threading.Thread(target=task, args=("Task 2",))

# Thread 3 create kiya; start hone par task("Task 3") execute hoga
thread3 = threading.Thread(target=task, args=("Task 3",))


thread1.start()  # Thread 1 ko start kiya

thread2.start()  # Thread 2 ko start kiya

thread3.start()  # Thread 3 ko start kiya


thread1.join()  # Main thread ko Thread 1 ke complete hone tak wait karwaya

thread2.join()  # Main thread ko Thread 2 ke complete hone tak wait karwaya

thread3.join()  # Main thread ko Thread 3 ke complete hone tak wait karwaya


print("All tasks completed")  # Teeno threads complete hone ke baad final message

#Humne ek hi Python process ke andar 3 threads create kiye, unhe concurrently start kiya,
# aur join() ki help se main thread ko teeno ke complete hone tak wait karwaya.