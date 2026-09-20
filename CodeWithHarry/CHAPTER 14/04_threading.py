#Threading: Threading is a Python technique that allows multiple threads to run within the same process,
#which is especially useful for handling I/O-bound tasks concurrently.

#For making thread there is a built-in modeule in python which is threading module.

#For creting a simple thread: thread = threading.Thread(target=function_name)
#For starting thread: thread.start()

#Exmaple:
import threading
import time

def task():
    print("Task started")
    time.sleep(2)   #when the thread is waiting on time.sleep(2), main program can continue it's work
    print("Task completed")

thread = threading.Thread(target= task) #we have created a thread object, target=task means that when this thread will run task() function will execute

thread.start()  #Thread will get started actually

print("Main program continues...")