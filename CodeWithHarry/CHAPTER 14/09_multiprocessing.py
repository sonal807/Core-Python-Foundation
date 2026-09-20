#Multiprocessing: Multiprocessing is a Python technique that uses multiple independent processes
#to execute tasks concurrently, allowing CPU-intensive work to use multiple CPU cores.

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


#CPU-bound tasks: CPU-bound tasks are tasks that mainly depend on the CPU's processing power and require significant computation.
#Multiprocessing can execute such tasks using multiple CPU cores.

#Multiprocessing
import multiprocessing
import time

def calculate():
    total = 0

    for i in range(10_000_000):
        total += i

    return total

if __name__ == "__main__":
    start = time.time()

    process1 = multiprocessing.Process(target=calculate)
    process2 = multiprocessing.Process(target=calculate)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")

#Sequential version
import time

def calculate():
    total = 0

    for i in range(10_000_000):
        total += i

    return total


start = time.time()

calculate()
calculate()

end = time.time()

print(f"Total time: {end - start:.2f} seconds")

#Multiprocessing allows CPU-bound tasks to run in separate processes,
#potentially using multiple CPU cores for parallel execution.

