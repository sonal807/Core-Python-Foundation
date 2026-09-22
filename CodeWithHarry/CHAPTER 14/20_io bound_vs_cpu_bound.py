#I/O-bound vs CPU-bound: An I/O-bound task spends most of its time waiting for input/output operations,
#while a CPU-bound task spends most of its time performing computations using the CPU.

# I/O-bound
#     ↓
# Mostly WAITING
#     ↓
# Network, API, file, database, etc.

# CPU-bound
#     ↓
# Mostly CALCULATING
#     ↓
# Mathematical computation, image processing,
# large data processing, etc.

#Example of I/O bound task:
import time

def io_task():
    print("I/O task started")

    time.sleep(2)

    print("I/O task completed")

start = time.time()

io_task()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")

#Example of CPU bound:
import time

def cpu_task():
    print("CPU task started")

    total = 0

    for i in range(10_000_000):
        total += i

    print("CPU task completed")

start = time.time()

cpu_task()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")


#                     CONCURRENCY
#                          │
#           ┌──────────────┼──────────────┐
#           ↓              ↓              ↓
#        Threads        Processes       Async
#           │              │              │
#           ↓              ↓              ↓
#    ThreadPoolExecutor ProcessPool    asyncio
#           │          Executor            │
#           ↓              ↓               ↓
#      I/O-bound       CPU-bound       I/O-bound

#I/O-bound = mostly waiting → async/threading can help.

# CPU-bound = mostly computing → processes can help utilize CPU cores.