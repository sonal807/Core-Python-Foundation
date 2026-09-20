#Sequential vs Concurrent Execution: Sequential execution means tasks are executed one after another,
#while concurrent execution allows multiple tasks to make progress during the same period of time.

#Sequential Execution:
# Task 1 → finish
#            ↓
# Task 2 → finish
#            ↓
# Task 3 → finish

#Concurrent Execution:
# Task 1 ────────┐
# Task 2 ────────┤ → tasks make progress during overlapping time
# Task 3 ────────┘

#Example:
import time


def task(name, duration):
    print(f"{name} started")
    time.sleep(duration)
    print(f"{name} completed")


start = time.time()

task("Task 1", 2)
task("Task 2", 2)
task("Task 3", 2)

end = time.time()  #time.sleep() is only here to simulate time waiting

print(f"Total time: {end - start:.2f} seconds")