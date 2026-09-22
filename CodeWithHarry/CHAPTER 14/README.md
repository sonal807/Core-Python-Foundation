# 📘 Chapter 14 - Python Concurrency & Asynchronous Programming

## 🎯 Objective

This chapter introduces **Concurrency and Asynchronous Programming in Python**, which are important concepts for building efficient, responsive, and scalable applications.

In a basic Python program, instructions are generally executed one after another. However, real-world applications often need to handle multiple tasks at the same time or manage several operations whose execution may overlap.

For example, an application may need to:

- Call multiple APIs
- Read data from databases
- Download files
- Perform web requests
- Process background tasks
- Communicate with external services
- Handle multiple user requests

If these operations are performed strictly one after another, the program may spend a significant amount of time simply waiting.

Concurrency provides techniques that allow a program to **make progress on multiple tasks during overlapping periods of time**.

This chapter covers Python's major concurrency mechanisms, including:

- Threading
- Multiprocessing
- Process Pools
- Thread Pools
- `concurrent.futures`
- Futures
- Asynchronous Programming
- `asyncio`
- Coroutines
- `async` and `await`
- Asyncio Tasks
- `asyncio.gather()`

The chapter also focuses on understanding **when to use each technique**, especially for **I/O-bound and CPU-bound tasks**, and how these concepts are applied in **AI Engineering**.

---

# 📌 Topics Covered

This chapter covers the following topics:

1. Introduction to Concurrency
2. Sequential vs Concurrent Execution
3. Process vs Thread
4. Threading
5. `start()` and `join()`
6. Multiple Threads
7. Race Conditions
8. Lock and Thread Safety
9. Multiprocessing
10. `Process`
11. Process Pool
12. Multiprocessing Queue
13. `concurrent.futures`
14. `ThreadPoolExecutor`
15. `ProcessPoolExecutor`
16. `asyncio`
17. `async` / `await`
18. Asyncio Tasks
19. `asyncio.gather()`
20. I/O-bound vs CPU-bound Tasks
21. Concurrency in AI Engineering

---

# 1️⃣ Introduction to Concurrency

## 🧩 What is Concurrency?

**Concurrency is the ability of a program to make progress on multiple tasks during overlapping periods of time.**

In simple words, concurrency allows a program to manage multiple tasks without requiring every task to completely finish before another task can make progress.

Suppose a program has three tasks:

    Task 1 → Download Data
    Task 2 → Read Database
    Task 3 → Call API

A purely sequential program may execute them like this:

    Task 1
       ↓
    Task 2
       ↓
    Task 3

The program waits for Task 1 to finish before Task 2 starts, and waits for Task 2 to finish before Task 3 starts.

With concurrency, these tasks may overlap:

    Task 1 ───────────────
    Task 2 ─────────────
    Task 3 ───────────────

The exact way this happens depends on the concurrency mechanism being used.

The important idea is:

> **Concurrency allows multiple tasks to make progress during overlapping periods of time.**

---

# 🧠 Understanding Concurrency with a Real-World Example

Imagine that you are cooking three different dishes.

A sequential approach would be:

    Start Dish A
        ↓
    Finish Dish A
        ↓
    Start Dish B
        ↓
    Finish Dish B
        ↓
    Start Dish C
        ↓
    Finish Dish C

This can waste time if a dish needs to cook or wait.

A more efficient approach may be:

    Start Dish A
        ↓
    Dish A is cooking
        ↓
    Prepare Dish B
        ↓
    Dish B is cooking
        ↓
    Prepare Dish C
        ↓
    Check Dish A
        ↓
    Check Dish B
        ↓
    Finish everything

You are making progress on multiple activities during overlapping periods.

This is similar to how concurrency works in software.

For example:

    Start API Request
          ↓
    API is processing request
          ↓
    Perform another task
          ↓
    Check API response
          ↓
    Continue processing

Instead of remaining completely idle while waiting, the program can potentially use that time to make progress on another task.

---

# ❓ Why Do We Need Concurrency?

Many real-world programs spend a considerable amount of time waiting for external operations.

Examples include:

- Network responses
- API responses
- Database queries
- File operations
- Web requests
- External services
- User input
- Cloud services

Consider an application that needs to make three independent API requests.

Suppose each request takes approximately 2 seconds.

A sequential approach may look like:

    API Request 1 → 2 seconds
          ↓
    API Request 2 → 2 seconds
          ↓
    API Request 3 → 2 seconds

Approximate total:

    2 + 2 + 2 = 6 seconds

If the requests can safely run concurrently, they may overlap:

    API Request 1 ─────────────── 2 sec
    API Request 2 ─────────────── 2 sec
    API Request 3 ─────────────── 2 sec

The total waiting time can then be closer to the duration of the slowest request rather than the sum of all requests.

In this simplified example:

    Sequential  → approximately 6 seconds
    Concurrent  → approximately 2 seconds

The actual time depends on many factors, including:

- Network latency
- Server response time
- Number of workers
- System resources
- Scheduling overhead
- Connection limits
- Implementation details

Therefore, concurrency should be understood as a way of **efficiently managing overlapping work**, not as a guarantee that every program will become faster.

---

# ⭐ Advantages of Concurrency

Concurrency provides several benefits when applied to suitable workloads.

## 1. Better Utilization of Waiting Time

When one task is waiting for an external operation, another task can potentially make progress.

For example:

    API Request
        ↓
    Waiting...
        ↓
    Perform another task
        ↓
    API response received
        ↓
    Continue processing

Instead of wasting the waiting period, the program can use that time for other work.

---

## 2. Improved Responsiveness

Concurrency can help applications remain responsive while background operations are running.

For example, an application may have:

    User Interface
          │
          ├── User Interaction
          │
          └── Background API Request

The application can continue handling user interaction while the API request is in progress.

---

## 3. Efficient I/O Handling

Concurrency is particularly useful for operations involving I/O.

Examples:

- API requests
- Database queries
- Network requests
- File operations
- Web scraping
- Cloud services

These operations often involve waiting rather than continuous CPU computation.

---

## 4. Handling Multiple Independent Tasks

If multiple tasks are independent, they may be good candidates for concurrent execution.

For example:

    Task A ───────────────
    Task B ───────────────
    Task C ───────────────

Instead of:

    Task A → Task B → Task C

The tasks can potentially make progress during overlapping periods.

---

## 5. Better Throughput

For suitable workloads, concurrency can allow an application to handle more operations within a given period.

This can be useful in:

- Web servers
- API services
- AI assistants
- Data-processing systems
- Network applications
- Agentic AI systems

---

# ⚠️ Concurrency Does Not Automatically Mean Faster

An important concept is:

> **Concurrency is not automatically faster for every workload.**

Concurrency introduces additional management overhead.

For example, if a task is extremely small:

    Task 1
    Task 2
    Task 3

the overhead of creating and managing threads, processes, or asynchronous tasks may be greater than the performance benefit.

Concurrency may also provide little benefit when:

- Tasks are heavily dependent on each other
- Tasks are extremely small
- Synchronization overhead is high
- Shared data causes contention
- The wrong concurrency technique is selected
- The workload is CPU-bound but threads are used in an unsuitable way

Therefore, the correct process is:

    Understand the workload
            ↓
    Identify the task type
            ↓
    Identify dependencies
            ↓
    Choose the appropriate technique
            ↓
    Measure the result

This idea will become especially important when studying:

- Threading
- Multiprocessing
- Thread Pools
- Process Pools
- `asyncio`
- I/O-bound vs CPU-bound tasks

---

# 🔹 Common Examples of Concurrent Tasks

Concurrency can be useful in many practical situations.

## 🌐 Multiple API Requests

    Weather API
    News API
    Search API

These requests may be independent and can potentially be performed concurrently.

---

## 🗄️ Multiple Database Queries

    Database Query A
    Database Query B
    Database Query C

If the queries are independent, concurrent execution may reduce unnecessary waiting.

---

## 📁 Multiple File Operations

    Read File A
    Read File B
    Read File C

When the operations involve waiting for storage I/O, concurrency may be useful.

---

## 🔎 Multiple Web Searches

    Search Website A
    Search Website B
    Search Website C

A search system may need to communicate with multiple external services.

---

## 🤖 AI Applications

An AI application may need to perform:

    Web Search
    Database Retrieval
    Vector Search
    API Call
    LLM Request

Several of these operations may be independent and I/O-bound.

---

# 2️⃣ Sequential vs Concurrent Execution

## 🐢 What is Sequential Execution?

**Sequential execution means that tasks are executed one after another in a specific order.**

Suppose a program has three tasks:

    Task 1
    Task 2
    Task 3

Sequential execution follows:

    Task 1
       ↓
    Task 2
       ↓
    Task 3

Task 2 starts only after Task 1 finishes.

Task 3 starts only after Task 2 finishes.

---

# 💻 Sequential Execution Example

    import time

    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")


    start = time.time()

    task("Task 1")
    task("Task 2")
    task("Task 3")

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

### Expected Output

    Task 1 started
    Task 1 completed
    Task 2 started
    Task 2 completed
    Task 3 started
    Task 3 completed
    Time taken: approximately 6.00 seconds

The exact execution time may vary slightly depending on the system.

---

# 🧠 How Sequential Execution Works

The execution flow is:

    Program Starts
          ↓
    Task 1 Starts
          ↓
    Task 1 Waits
          ↓
    Task 1 Completes
          ↓
    Task 2 Starts
          ↓
    Task 2 Waits
          ↓
    Task 2 Completes
          ↓
    Task 3 Starts
          ↓
    Task 3 Waits
          ↓
    Task 3 Completes
          ↓
    Program Ends

Only one task is being handled at each stage.

---

# 🔀 What is Concurrent Execution?

**Concurrent execution allows multiple tasks to make progress during overlapping periods of time.**

Instead of completely waiting for one task to finish before another task can make progress, the program can manage multiple tasks concurrently.

Conceptually:

    Time →

    Task 1 ───────────────
    Task 2 ───────────────
    Task 3 ───────────────

The execution periods overlap.

However, overlapping execution does not necessarily mean that all tasks are physically executing at exactly the same moment.

That distinction leads to the concept of **parallelism**.

---

# 💻 Simple Concurrent Execution Concept

Suppose we have:

    Task 1 → Waiting for API
    Task 2 → Processing data
    Task 3 → Reading a file

A concurrent system can organize the work like:

    Task 1 → Waiting
                ↓
            Task 2 runs
                ↓
            Task 3 runs
                ↓
            Task 1 continues

The exact behavior depends on whether we use:

- Threads
- Processes
- Thread pools
- Process pools
- Asynchronous programming

---

# 📊 Sequential vs Concurrent Execution

| Feature | Sequential Execution | Concurrent Execution |
|---|---|---|
| Task handling | One task after another | Multiple tasks can make progress |
| Execution overlap | No | Yes |
| Waiting time | Can block subsequent tasks | Can be overlapped with other work |
| Complexity | Relatively simple | More complex |
| I/O-heavy workloads | Can waste waiting time | Often useful |
| Independent tasks | Executed one by one | Can overlap |
| Synchronization | Usually simpler | May be required |
| Common Python tools | Normal function calls | Threads, processes, `asyncio` |

---

# 📈 Visual Comparison

## Sequential Execution

    Time →

    Task 1: ██████████
    Task 2:           ██████████
    Task 3:                     ██████████

Task 2 begins after Task 1 finishes.

Task 3 begins after Task 2 finishes.

---

## Concurrent Execution

    Time →

    Task 1: █████████████████
    Task 2:   █████████████
    Task 3:      ███████████████

The tasks have overlapping execution periods.

---

# 🧠 Concurrency vs Parallelism

Concurrency and parallelism are related concepts, but they are not identical.

---

# 🔹 What is Concurrency?

**Concurrency is the ability of a system to manage multiple tasks whose execution can overlap in time.**

A system may switch between tasks or allow different tasks to progress while others are waiting.

For example:

    Task A → Running
    Task A → Waiting
    Task B → Running
    Task B → Waiting
    Task A → Continues
    Task C → Running

The tasks are making progress during overlapping periods.

---

# 🔹 What is Parallelism?

**Parallelism is the execution of multiple tasks at the same time, typically by using multiple CPU cores.**

For example:

    CPU Core 1 → Task A
    CPU Core 2 → Task B
    CPU Core 3 → Task C

Different tasks can physically execute simultaneously.

---

# 📊 Concurrency vs Parallelism

| Feature | Concurrency | Parallelism |
|---|---|---|
| Meaning | Multiple tasks make progress during overlapping periods | Multiple tasks execute simultaneously |
| Multiple CPU cores required? | No | Usually beneficial |
| Main concept | Managing overlapping work | Simultaneous execution |
| Common use | I/O-bound workloads | CPU-bound workloads |
| Example | Multiple API requests | Multiple heavy calculations |
| Python examples | `asyncio`, threading | Multiprocessing |

---

# 🧠 Real-World Analogy

Imagine one chef preparing multiple dishes.

The chef may:

    Start Dish A
        ↓
    Dish A is cooking
        ↓
    Prepare Dish B
        ↓
    Dish B is cooking
        ↓
    Prepare Dish C
        ↓
    Check Dish A
        ↓
    Check Dish B

The chef is managing multiple activities during overlapping periods.

This is similar to **concurrency**.

Now imagine three chefs:

    Chef 1 → Dish A
    Chef 2 → Dish B
    Chef 3 → Dish C

The three chefs can actually work on different dishes simultaneously.

This is similar to **parallelism**.

Therefore:

    Concurrency → Multiple tasks can make progress
    Parallelism  → Multiple tasks execute simultaneously

---

# 🔗 Relationship Between Concurrency and Parallelism

Concurrency and parallelism can also exist together.

For example, an application may have multiple processes:

    Multiple Processes
            │
            ├── Process 1
            │      ├── Task A
            │      └── Task B
            │
            └── Process 2
                   ├── Task C
                   └── Task D

Different processes may execute in parallel on different CPU cores.

At the same time, each process may manage multiple tasks concurrently.

Therefore, concurrency and parallelism should be viewed as related concepts rather than mutually exclusive concepts.

---

# 🌐 Real-World Example: Multiple API Requests

Suppose an AI assistant needs information from three independent services:

    User Query
        │
        ├── Weather API
        ├── News API
        └── Search API

## Sequential Approach

The program may execute:

    Weather API
         ↓
    Wait for response
         ↓
    News API
         ↓
    Wait for response
         ↓
    Search API
         ↓
    Wait for response
         ↓
    Combine Results

If every API takes approximately 2 seconds:

    2 + 2 + 2 ≈ 6 seconds

---

## Concurrent Approach

The application may start the independent operations so that they can overlap:

              ┌── Weather API ──┐
              │                 │
    User ─────┼── News API ─────┼──→ Combine Results
    Query     │                 │
              └── Search API ───┘

If all three requests take approximately 2 seconds and can safely run concurrently, the total waiting time can be closer to:

    ≈ 2 seconds

This is a simplified example. Real applications have network latency, server processing time, connection limits, scheduling overhead, and other factors.

---

# 🤖 Why Concurrency Matters in AI Engineering

Modern AI applications often perform several operations to answer a single user request.

For example:

    Receive User Query
            ↓
    Understand Request
            ↓
      ┌─────┼──────────────┐
      ↓     ↓              ↓
    Search  Database      External API
      ↓     ↓              ↓
    Web     Documents     Service
      └─────┼──────────────┘
            ↓
      Combine Information
            ↓
           LLM
            ↓
      Final Response

Several of these operations may be independent and involve waiting for external services.

Concurrency can therefore be useful for:

- Web searches
- API calls
- Database queries
- Vector database retrieval
- File operations
- External tool calls
- LLM requests
- Multiple data-source retrieval
- AI agent tool execution
- Backend AI services

---

# 🧩 Example: Concurrent AI Workflow

Imagine an AI assistant receives:

    "What is today's weather and what are the latest news updates?"

The assistant may need:

    Weather API
          │
          │
          ├─────────────┐
          │             │
    News API             │
          │             │
          └──────┬──────┘
                 ↓
          Combine Results
                 ↓
            LLM Response

If the weather request and news request are independent, the application does not necessarily need to wait for one request to finish before starting the other.

They can potentially make progress concurrently.

This can reduce unnecessary waiting and improve the responsiveness of the AI application.

---

# 🧭 Major Python Concurrency Techniques

Python provides several mechanisms for implementing concurrent programs.

The major techniques covered in this chapter are:

    Python Concurrency
            │
            ├── Threading
            │
            ├── Multiprocessing
            │
            ├── concurrent.futures
            │       │
            │       ├── ThreadPoolExecutor
            │       └── ProcessPoolExecutor
            │
            └── asyncio
                    │
                    ├── async
                    ├── await
                    ├── Tasks
                    └── gather()

Each technique has a different purpose and should be selected according to the workload.

---

# 📌 High-Level Overview

| Technique | Main Idea | Common Use |
|---|---|---|
| `threading` | Multiple threads inside a process | I/O-bound work |
| `multiprocessing` | Multiple independent processes | CPU-bound work |
| `ThreadPoolExecutor` | Managed pool of worker threads | Multiple I/O tasks |
| `ProcessPoolExecutor` | Managed pool of worker processes | Multiple CPU tasks |
| `asyncio` | Asynchronous event-driven execution | Async I/O |
| `async` / `await` | Syntax for asynchronous programming | Coroutines |
| `create_task()` | Schedule asynchronous work | Multiple async tasks |
| `gather()` | Run multiple awaitables and collect results | Concurrent async operations |

These are practical guidelines rather than strict rules. The correct choice depends on the workload, libraries, architecture, and application requirements.

---

# ⚠️ Important Concepts to Remember

Before moving deeper into Python's concurrency tools, keep the following ideas in mind:

### 1. Concurrency is not the same as parallelism.

    Concurrency → Overlapping progress
    Parallelism  → Simultaneous execution

### 2. Concurrency is especially useful when tasks spend time waiting.

Examples:

    API
    Database
    Network
    File
    Web Request

### 3. Not every task should be concurrent.

Sometimes sequential execution is simpler and completely sufficient.

### 4. Independent tasks are good candidates for concurrency.

If Task B cannot start until Task A finishes, concurrency may provide little benefit.

### 5. The workload type matters.

Later in this chapter we will distinguish:

    I/O-bound
        ↓
    Mostly waiting

    CPU-bound
        ↓
    Mostly computing

This distinction will help determine whether techniques such as:

    Threading
    Multiprocessing
    ThreadPoolExecutor
    ProcessPoolExecutor
    asyncio

are appropriate.

---

# 🧠 Key Takeaways

- **Concurrency** allows multiple tasks to make progress during overlapping periods of time.
- **Sequential execution** performs tasks one after another.
- **Concurrent execution** allows independent tasks to overlap in execution.
- **Parallelism** means multiple tasks can execute simultaneously, typically using multiple CPU cores.
- Concurrency and parallelism are related but different concepts.
- Concurrency is particularly useful for I/O-bound operations.
- API calls, database queries, web requests, and file operations are common examples of tasks that can benefit from concurrency.
- Concurrency does not automatically make every program faster.
- Independent tasks are generally better candidates for concurrent execution.
- Python provides several concurrency mechanisms, including:
  - `threading`
  - `multiprocessing`
  - `concurrent.futures`
  - `asyncio`
- The appropriate concurrency technique depends on the workload and application requirements.
- Concurrency is particularly important in AI Engineering because modern AI applications frequently communicate with multiple external services.

---

# 🔚 Part 1 Summary

The fundamental idea of this chapter can be summarized as:

    Sequential Execution
            ↓
    One task after another
            ↓
    Waiting can block later tasks

                VS

    Concurrent Execution
            ↓
    Multiple tasks can make progress
            ↓
    Waiting time can overlap
            ↓
    Useful for suitable workloads

The broader structure of Python concurrency is:

    Python Concurrency
            │
            ├── Threading
            │
            ├── Multiprocessing
            │
            ├── Thread Pools
            │
            ├── Process Pools
            │
            └── Asynchronous Programming
                    │
                    └── asyncio


# 2️⃣ Process vs Thread

## 🧩 Introduction

Before working with Python's concurrency tools, it is important to understand two fundamental concepts:

- **Process**
- **Thread**

Both can be used to perform multiple tasks concurrently, but they work differently and have different use cases.

A useful way to remember the basic relationship is:

    Process
       │
       ├── Thread
       ├── Thread
       └── Thread

A **process** is an independent execution environment, while a **thread** is a smaller unit of execution that exists inside a process.

---

# 🔹 What is a Process?

**A process is an independent instance of a running program with its own memory space and system resources.**

Whenever a program starts, the operating system creates a process to execute that program.

For example, when we run:

    python program.py

the operating system starts a process for that Python program.

Conceptually:

    Operating System
          │
          ├── Process 1
          │
          ├── Process 2
          │
          └── Process 3

Each process is generally isolated from the others and has its own memory space.

---

# 🧠 Process Example

Suppose we have a Python program:

    program.py

When it runs:

    Operating System
           │
           ↓
       Python Process
           │
           └── program.py

The process contains the resources required to execute the program.

A process can also create additional processes.

For example:

    Main Process
         │
         ├── Process 1
         ├── Process 2
         └── Process 3

This concept forms the foundation of **multiprocessing**, which we will study later.

---

# 🔹 What is a Thread?

**A thread is a lightweight unit of execution that runs inside a process.**

A single process can contain multiple threads.

For example:

    Process
       │
       ├── Thread 1
       ├── Thread 2
       └── Thread 3

All these threads belong to the same process.

Threads can be used to perform multiple tasks concurrently within the same process.

---

# 🧠 Thread Example

Suppose an application needs to perform three operations:

    Process
       │
       ├── Thread 1 → Download File
       ├── Thread 2 → Read Database
       └── Thread 3 → Handle Network Request

The threads belong to the same process but can work on different tasks.

This is the basic idea behind **multithreading**.

---

# 🏗️ Process and Thread Relationship

The relationship can be visualized as:

    Operating System
           │
           ↓
        Process
           │
     ┌─────┼─────┐
     ↓     ↓     ↓
   Thread Thread Thread

A process can contain one or more threads.

The thread is therefore not an independent program.

It is an execution unit inside a process.

---

# 📊 Process vs Thread

| Feature | Process | Thread |
|---|---|---|
| Definition | Independent execution environment | Unit of execution inside a process |
| Memory | Has its own memory space | Shares memory with threads of the same process |
| Isolation | Higher | Lower |
| Creation cost | Generally higher | Generally lower |
| Communication | More expensive | Easier because memory is shared |
| Resource usage | Higher | Lower |
| Failure isolation | Better | Lower |
| Suitable for | CPU-bound workloads and isolation | Often useful for I/O-bound workloads |
| Python tool | `multiprocessing` | `threading` |

---

# 🧠 Understanding Memory

One of the most important differences between processes and threads is **memory**.

## Process Memory

Different processes normally have separate memory spaces.

Conceptually:

    Process 1
    ┌──────────────────┐
    │ Memory            │
    │ variable = 100    │
    └──────────────────┘

    Process 2
    ┌──────────────────┐
    │ Memory            │
    │ variable = 200    │
    └──────────────────┘

The variables are not automatically shared between the processes.

This separation provides stronger isolation.

---

## Thread Memory

Threads inside the same process share the process's memory.

Conceptually:

    Process
    ┌─────────────────────────────┐
    │ Shared Memory               │
    │                             │
    │ variable = 100              │
    │                             │
    │ ┌────────┐ ┌────────┐       │
    │ │Thread 1│ │Thread 2│       │
    │ └────────┘ └────────┘       │
    └─────────────────────────────┘

Because threads share memory, communication can be easier.

However, shared memory also introduces risks.

For example, if multiple threads modify the same variable at the same time, a **race condition** can occur.

Race conditions and thread safety will be discussed later in this chapter.

---

# 🔄 Process Communication vs Thread Communication

Because processes have separate memory spaces, exchanging information between processes usually requires explicit communication mechanisms.

Examples include:

- Queues
- Pipes
- Shared memory
- Files
- Other inter-process communication mechanisms

Threads within the same process can often communicate through shared variables and objects.

However, shared data must be accessed carefully.

Conceptually:

    Threads
       │
       ├── Shared Memory
       │
       ├── Shared Objects
       │
       └── Shared Variables

This makes thread communication relatively convenient but also creates synchronization challenges.

---

# ⚠️ Shared Memory and Race Conditions

Consider a shared variable:

    counter = 0

Suppose two threads both execute:

    counter = counter + 1

At first glance, it may look like:

    Thread 1 → +1
    Thread 2 → +1

Therefore:

    0 + 1 + 1 = 2

But when multiple threads access shared data concurrently, the actual operations can interleave in unexpected ways.

Conceptually:

    Thread 1 → Read counter
    Thread 2 → Read counter
    Thread 1 → Modify counter
    Thread 2 → Modify counter

This can produce an incorrect final value.

This situation is called a **race condition**.

Later in this chapter we will study:

- Race conditions
- Locks
- Critical sections
- Thread safety

in detail.

---

# 🔹 Threading in Python

Python provides the built-in `threading` module for working with threads.

The module allows us to create and manage threads.

Basic structure:

    import threading

    thread = threading.Thread(target=function)

    thread.start()

    thread.join()

The important concepts are:

- `Thread`
- `target`
- `args`
- `start()`
- `join()`

These will be studied in detail in the next topics.

---

# 💻 Basic Thread Example

    import threading
    import time


    def task():
        print("Task started")
        time.sleep(2)
        print("Task completed")


    thread = threading.Thread(target=task)

    thread.start()
    thread.join()

    print("Main program completed")

### Output

    Task started
    Task completed
    Main program completed

The thread executes the `task()` function.

The `join()` method makes the main program wait until the thread finishes.

---

# 🔹 Multiprocessing in Python

Python provides the `multiprocessing` module for creating and managing multiple processes.

Basic structure:

    import multiprocessing

    process = multiprocessing.Process(target=function)

    process.start()

    process.join()

Each process has its own execution environment.

Multiprocessing is particularly useful for workloads that are computationally intensive.

We will study multiprocessing in detail later in this chapter.

---

# 💻 Basic Multiprocessing Example

    import multiprocessing
    import time


    def task():
        print("Process started")
        time.sleep(2)
        print("Process completed")


    if __name__ == "__main__":
        process = multiprocessing.Process(target=task)

        process.start()
        process.join()

        print("Main program completed")

### Output

    Process started
    Process completed
    Main program completed

The `if __name__ == "__main__":` guard is especially important when using multiprocessing, particularly on platforms that use the `spawn` start method.

---

# ⚙️ Why Does Multiprocessing Help with CPU-bound Work?

CPU-bound tasks spend most of their time performing computation.

Examples:

- Large mathematical calculations
- Data processing
- Image processing
- Video processing
- Complex simulations
- Machine learning computations

Multiple processes can execute independently and can make use of multiple CPU cores.

Conceptually:

    CPU
    ├── Core 1 → Process 1
    ├── Core 2 → Process 2
    ├── Core 3 → Process 3
    └── Core 4 → Process 4

This allows computational work to be distributed across CPU cores.

However, actual performance depends on:

- Number of CPU cores
- Workload size
- Process creation overhead
- Data transfer overhead
- Operating system
- Python implementation
- Libraries being used

---

# 🧠 Python's GIL and Threads

In standard CPython, the **Global Interpreter Lock (GIL)** is an important factor when discussing threads.

**The GIL is a lock used by CPython that ensures only one thread executes Python bytecode at a time within a given interpreter process.**

This means that Python threads do not generally provide CPU-bound parallel execution of pure Python bytecode in the traditional CPython implementation.

For example:

    Thread 1 → CPU-heavy Python code
    Thread 2 → CPU-heavy Python code

Using threads does not necessarily mean both pieces of pure Python bytecode will execute simultaneously on separate CPU cores.

This is one reason multiprocessing is commonly used for CPU-bound workloads.

---

# 🌐 Why Are Threads Still Useful in Python?

The presence of the GIL does not make threads useless.

Threads are often useful for **I/O-bound tasks**.

For example:

    Thread 1 → Waiting for API
    Thread 2 → Waiting for Database
    Thread 3 → Waiting for File

While one thread is waiting for I/O, another thread can make progress.

This makes threading useful for many applications involving:

- Network requests
- API calls
- File operations
- Database operations
- Web requests

Additionally, some libraries perform work outside Python bytecode or release the GIL during certain operations, so the practical behavior can depend on the library and workload.

---

# 📊 Threading vs Multiprocessing

| Feature | Threading | Multiprocessing |
|---|---|---|
| Unit | Thread | Process |
| Memory | Shared within process | Separate memory spaces |
| Creation overhead | Generally lower | Generally higher |
| Communication | Relatively easier | Requires IPC mechanisms |
| Isolation | Lower | Higher |
| CPU-bound pure Python | Limited by GIL in standard CPython | Often suitable |
| I/O-bound | Often useful | Can also be useful |
| Main module | `threading` | `multiprocessing` |
| Example | Multiple API requests | Heavy computations |

---

# 🧠 When Should We Use Threads?

Threads are often a good choice when:

- Tasks are I/O-bound
- Tasks spend significant time waiting
- Shared memory is useful
- Tasks are relatively lightweight
- You want to perform multiple blocking I/O operations concurrently

Examples:

    Download multiple files
    Make multiple HTTP requests
    Perform multiple database operations
    Read multiple sources

A simplified rule is:

    I/O-bound
        ↓
    Threading can be useful

This is a guideline, not an absolute rule.

---

# 🧠 When Should We Use Processes?

Processes are often useful when:

- Tasks are CPU-bound
- Tasks require significant computation
- Work can be divided into independent units
- Multiple CPU cores can be utilized

Examples:

    Heavy mathematical calculations
    Image processing
    Video processing
    Large data processing
    CPU-intensive algorithms

A simplified guideline is:

    CPU-bound
        ↓
    Multiprocessing can be useful

Again, the actual choice depends on the workload.

---

# 🌍 Real-World Example

Suppose an AI application needs to perform two types of work.

### Task A

Download information from multiple APIs.

This is primarily:

    Waiting for network responses

Therefore:

    I/O-bound
        ↓
    Threading / asyncio
        ↓
    Can be useful

---

### Task B

Perform a large computational transformation on a dataset.

This is primarily:

    CPU computation
        ↓
    CPU-bound
        ↓
    Multiprocessing / ProcessPoolExecutor
        ↓
    Can be useful

This shows why understanding the nature of the workload is more important than simply choosing a concurrency technique.

---

# 🤖 AI Engineering Relevance

Processes and threads are useful concepts for AI Engineers because modern AI systems frequently perform both I/O-bound and CPU-bound operations.

For example:

    AI Application
          │
          ├── Web Search
          │       ↓
          │     I/O-bound
          │
          ├── Database Query
          │       ↓
          │     I/O-bound
          │
          ├── LLM API Request
          │       ↓
          │     I/O-bound
          │
          └── Data Processing
                  ↓
                CPU-bound

Different parts of the same application may therefore require different concurrency strategies.

A practical AI Engineer may use:

    Threading
        ↓
    Blocking I/O tasks

    asyncio
        ↓
    Asynchronous I/O

    Multiprocessing
        ↓
    CPU-intensive tasks

    ThreadPoolExecutor
        ↓
    Managed I/O workers

    ProcessPoolExecutor
        ↓
    Managed CPU workers

Understanding these differences is important when designing efficient AI backends and AI agent systems.

---

# 📌 Key Takeaways

- A **process** is an independent execution environment.
- A **thread** is a lightweight execution unit inside a process.
- A process can contain multiple threads.
- Processes generally have separate memory spaces.
- Threads within the same process share memory.
- Shared memory makes communication easier but can introduce synchronization problems.
- Race conditions can occur when multiple threads access shared data incorrectly.
- Python provides the `threading` module for working with threads.
- Python provides the `multiprocessing` module for working with processes.
- In standard CPython, the GIL limits simultaneous execution of Python bytecode by multiple threads.
- Threads are commonly useful for I/O-bound workloads.
- Processes are commonly useful for CPU-bound workloads.
- Multiprocessing can use multiple CPU cores.
- The choice between threads and processes should be based on the workload rather than a fixed rule.

---

# 📝 Quick Revision

    Process
        ↓
    Independent execution environment
        ↓
    Separate memory space

    Thread
        ↓
    Execution unit inside a process
        ↓
    Shares process memory

    Threading
        ↓
    Often useful for I/O-bound tasks

    Multiprocessing
        ↓
    Often useful for CPU-bound tasks

    GIL
        ↓
    Important limitation for CPU-bound pure Python
    threading in standard CPython

---

# 🔚 Part 2 Summary

The fundamental relationship can be remembered as:

    Operating System
          │
          ├── Process 1
          │      ├── Thread 1
          │      ├── Thread 2
          │      └── Thread 3
          │
          └── Process 2
                 ├── Thread 1
                 └── Thread 2

The key difference is:

    Process → Independent execution environment
    Thread  → Execution unit inside a process

And the practical guideline is:

    I/O-bound
        ↓
    Threading can be useful

    CPU-bound
        ↓
    Multiprocessing can be useful

The next part will move from theory to implementation and cover:

- Creating threads
- `threading.Thread`
- `target`
- `args`
- `start()`
- `join()`
- Multiple threads
- Thread execution order

# 3️⃣ Threading

## 🧩 Introduction to Threading

**Threading is a concurrency technique in Python that allows multiple threads to execute tasks within the same process.**

A thread is a lightweight unit of execution.

A single process can contain multiple threads:

    Process
       │
       ├── Thread 1
       ├── Thread 2
       └── Thread 3

Each thread can be responsible for a different task.

For example:

    Main Process
         │
         ├── Thread 1 → Download File
         ├── Thread 2 → API Request
         └── Thread 3 → Database Operation

Threading is particularly useful when tasks are **I/O-bound**, meaning they spend significant time waiting for external operations.

---

# 📚 Python's `threading` Module

Python provides the built-in `threading` module for creating and managing threads.

The module provides classes and functions that allow us to:

- Create threads
- Start threads
- Wait for threads
- Pass arguments to threads
- Manage multiple threads
- Synchronize threads
- Protect shared data

To use threading, we first import the module:

    import threading

The main class used to create a thread is:

    threading.Thread

---

# 🧩 What is `threading.Thread`?

**`threading.Thread` is a Python class used to create a new thread of execution.**

Basic syntax:

    thread = threading.Thread(target=function)

Here:

- `thread` → Thread object
- `threading.Thread` → Thread class
- `target` → Function that the thread will execute
- `function` → Function assigned to the thread

The thread does not start immediately when the object is created.

We need to explicitly start it using:

    thread.start()

---

# 🔹 Understanding `target`

The `target` parameter specifies the function that the thread should execute.

Example:

    import threading


    def task():
        print("Task is running")


    thread = threading.Thread(target=task)

Here:

    target=task

means:

> Execute the `task()` function inside this thread.

An important point is that we write:

    target=task

and not:

    target=task()

Why?

Because:

    target=task

passes the function itself to the thread.

Whereas:

    target=task()

calls the function immediately while creating the thread.

---

# ⚠️ `target=function` vs `target=function()`

Consider:

    thread = threading.Thread(target=task)

This means:

    Thread
      ↓
    Will execute task later

But:

    thread = threading.Thread(target=task())

means:

    task()
      ↓
    Executes immediately
      ↓
    Its return value becomes target

Therefore, when passing a function as a target, we normally use:

    target=task

not:

    target=task()

---

# 💻 Basic Thread Example

File:

    04_threading.py

Code:

    import threading


    def task():
        print("Task started")
        print("Task completed")


    thread = threading.Thread(target=task)

    thread.start()

### Output

    Task started
    Task completed

The thread executes the `task()` function.

---

# 🧠 How the Basic Thread Example Works

The execution flow is:

    Program Starts
          ↓
    Define task()
          ↓
    Create Thread Object
          ↓
    thread.start()
          ↓
    New Thread Starts
          ↓
    task() Executes
          ↓
    Task Completes

The important part is:

    thread = threading.Thread(target=task)

This creates the thread object.

Then:

    thread.start()

starts the thread.

---

# 🔹 What Does `start()` Do?

**`start()` starts the thread and schedules the target function to execute in that thread.**

Syntax:

    thread.start()

After calling:

    thread.start()

the thread begins execution.

Important:

> `start()` should normally be called only once for a particular thread object.

A thread cannot be restarted after it has already completed.

---

# 🔹 What Does `join()` Do?

**`join()` makes the calling thread wait until the target thread finishes its execution.**

Syntax:

    thread.join()

Suppose:

    thread.start()
    thread.join()

The sequence becomes:

    Main Thread
        │
        ├── Start Worker Thread
        │
        └── Wait
              │
              ↓
        Worker Thread
              │
              ↓
        Task Completes
              │
              ↓
        Main Thread Continues

This is important when the main program must wait for a thread before continuing.

---

# 💻 `start()` and `join()` Example

    import threading
    import time


    def task():
        print("Task started")

        time.sleep(2)

        print("Task completed")


    thread = threading.Thread(target=task)

    thread.start()
    thread.join()

    print("Main program completed")

### Output

    Task started
    Task completed
    Main program completed

---

# 🧠 Why is `join()` Important?

Consider:

    thread.start()

    print("Main program completed")

Without `join()`, the main thread does not explicitly wait for the worker thread.

Depending on the program and timing, output from the main thread and worker thread may appear in an unexpected order.

With:

    thread.join()

the main thread waits for the worker thread to finish.

Therefore:

    thread.start()
        ↓
    Start thread

    thread.join()
        ↓
    Wait for thread

---

# 🔹 Passing Arguments to a Thread

Sometimes the target function needs arguments.

For example:

    def task(name):
        print(f"{name} started")

We can pass arguments using the `args` parameter.

Syntax:

    threading.Thread(
        target=function,
        args=(argument,)
    )

Example:

    import threading


    def task(name):
        print(f"{name} is running")


    thread = threading.Thread(
        target=task,
        args=("Task 1",)
    )

    thread.start()
    thread.join()

### Output

    Task 1 is running

---

# ⚠️ Why is There a Comma in `args=("Task 1",)`?

This is an important Python detail.

In Python, a one-element tuple requires a trailing comma.

Correct:

    args=("Task 1",)

Without the comma:

    args=("Task 1")

this is simply a string enclosed in parentheses, not a tuple.

Therefore:

    ("Task 1",)

is a tuple containing one element.

---

# 🧠 Passing Multiple Arguments

Suppose the function is:

    def calculate(a, b):
        print(a + b)

We can pass two arguments:

    thread = threading.Thread(
        target=calculate,
        args=(10, 20)
    )

Then:

    thread.start()
    thread.join()

Output:

    30

The tuple:

    (10, 20)

contains the two arguments.

---

# 💻 Thread with Multiple Arguments

    import threading


    def calculate(a, b):
        result = a + b
        print("Result:", result)


    thread = threading.Thread(
        target=calculate,
        args=(10, 20)
    )

    thread.start()
    thread.join()

### Output

    Result: 30

---

# 🔄 Thread Execution Flow

A simple thread lifecycle can be visualized as:

    Thread Object Created
            ↓
       thread.start()
            ↓
        Thread Running
            ↓
       Target Function
            ↓
       Task Completed
            ↓
        Thread Finished

If `join()` is used:

    Thread Started
         ↓
    Main Thread Waits
         ↓
    Thread Finishes
         ↓
    Main Thread Continues

---

# 🧩 Main Thread

When a Python program starts, it already has a thread known as the **main thread**.

Conceptually:

    Python Process
          │
          └── Main Thread

When we create another thread:

    Python Process
          │
          ├── Main Thread
          │
          └── Worker Thread

The main thread is responsible for executing the main flow of the program.

The additional thread is often called a **worker thread** because it performs a specific task.

---

# 🧠 Main Thread vs Worker Thread

| Main Thread | Worker Thread |
|---|---|
| Starts when the program begins | Created by the program |
| Executes the main program flow | Performs assigned task |
| Can create worker threads | Executes its target function |
| Can wait for worker threads | Eventually finishes its task |

Example:

    Main Thread
         │
         ├── Create Worker Thread
         │
         ├── Start Worker Thread
         │
         └── Wait using join()
                    │
                    ↓
              Worker Thread
                    │
                    ↓
                 Complete

---

# 4️⃣ Multiple Threads

## 🧩 What are Multiple Threads?

**Multiple threading means using more than one thread within the same process to execute multiple tasks concurrently.**

Instead of creating only one worker thread:

    Process
       │
       ├── Main Thread
       └── Worker Thread

we can create multiple worker threads:

    Process
       │
       ├── Main Thread
       ├── Thread 1
       ├── Thread 2
       └── Thread 3

Each worker can execute a different task.

---

# 💻 Multiple Threads Example

    import threading
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")


    thread1 = threading.Thread(
        target=task,
        args=("Task 1",)
    )

    thread2 = threading.Thread(
        target=task,
        args=("Task 2",)
    )

    thread3 = threading.Thread(
        target=task,
        args=("Task 3",)
    )


    thread1.start()
    thread2.start()
    thread3.start()


    thread1.join()
    thread2.join()
    thread3.join()


    print("All tasks completed")

### Possible Output

    Task 1 started
    Task 2 started
    Task 3 started
    Task 1 completed
    Task 3 completed
    Task 2 completed
    All tasks completed

The exact completion order may vary.

---

# 🧠 Why Can the Completion Order Change?

When multiple threads are running, the operating system and Python runtime determine when each thread gets execution time.

Therefore, we should not assume that:

    Thread 1
    Thread 2
    Thread 3

will always complete in exactly that order.

For example, one execution may produce:

    Task 1 completed
    Task 2 completed
    Task 3 completed

Another execution may produce:

    Task 2 completed
    Task 3 completed
    Task 1 completed

This is normal.

The order depends on factors such as:

- Scheduling
- System load
- Timing
- I/O delays
- Operating system behavior
- Task duration

---

# ⏱️ Thread Start Order vs Completion Order

An important distinction is:

> **The order in which threads are started does not guarantee the order in which they finish.**

Suppose:

    thread1.start()
    thread2.start()
    thread3.start()

This starts the threads in that order.

But completion may be:

    Thread 3
    Thread 1
    Thread 2

because each thread may experience different execution and waiting conditions.

---

# 📊 Single Thread vs Multiple Threads

| Single Thread | Multiple Threads |
|---|---|
| One worker task at a time | Multiple worker tasks |
| Simpler | More complex |
| Limited concurrency | Greater concurrency |
| Easier synchronization | Synchronization may be required |
| Useful for simple tasks | Useful for multiple independent tasks |

---

# 🔄 Thread Execution Model

With multiple threads:

    Main Thread
         │
         ├──────────────→ Thread 1
         │
         ├──────────────→ Thread 2
         │
         └──────────────→ Thread 3

The main thread creates and starts the worker threads.

Then it can wait for them:

    Thread 1 ────────────┐
    Thread 2 ────────────┤
    Thread 3 ────────────┤
                         ↓
                  All Threads Complete
                         ↓
                   Main Continues

This is why we commonly call:

    thread1.join()
    thread2.join()
    thread3.join()

---

# 💻 Measuring Execution Time

We can compare sequential and threaded execution using `time.time()`.

## Sequential Version

    import time


    def task():
        time.sleep(2)


    start = time.time()

    task()
    task()
    task()

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

Approximate result:

    Time taken: 6.00 seconds

---

## Threaded Version

    import threading
    import time


    def task():
        time.sleep(2)


    start = time.time()


    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    thread3 = threading.Thread(target=task)


    thread1.start()
    thread2.start()
    thread3.start()


    thread1.join()
    thread2.join()
    thread3.join()


    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

The result may be closer to:

    Time taken: approximately 2.00 seconds

because the waiting periods overlap.

The exact timing depends on the system.

---

# 🧠 Important: `time.sleep()` is Only Simulating Waiting

In the examples above:

    time.sleep(2)

does not represent a real API request or database operation.

It simply pauses the current thread for approximately two seconds.

It is useful for demonstrating concurrency because it simulates a task that spends time waiting.

Real-world examples could instead involve:

- HTTP requests
- Database queries
- File operations
- Network communication

---

# ⚠️ Threads Are Not Automatically Better

Using multiple threads does not guarantee faster execution.

Threading is most useful when the workload benefits from overlapping waiting time.

For example:

    API Request
        ↓
    Waiting for Response
        ↓
    Continue

is a good candidate for concurrency.

But:

    Small Calculation
        ↓
    Small Calculation
        ↓
    Small Calculation

may not benefit significantly from creating multiple threads.

For CPU-heavy pure Python work in standard CPython, the GIL is also an important limitation.

---

# 🤖 Threading in AI Engineering

Threading can be useful in AI applications when multiple operations involve blocking I/O.

For example:

    AI Assistant
         │
         ├── Web Request
         ├── Database Query
         ├── File Read
         └── External API

A threaded architecture may allow these operations to make progress without requiring one blocking operation to finish before another starts.

Examples include:

### 🌐 Web Requests

    Thread 1 → Search Website A
    Thread 2 → Search Website B
    Thread 3 → Search Website C

### 🗄️ Database Operations

    Thread 1 → Query Database A
    Thread 2 → Query Database B

### 📁 File Operations

    Thread 1 → Read Document A
    Thread 2 → Read Document B

### 🔌 External APIs

    Thread 1 → Weather API
    Thread 2 → News API
    Thread 3 → Search API

Later in this chapter, we will also learn `ThreadPoolExecutor`, which provides a higher-level way to manage worker threads.

---

# 📌 Important Threading Methods and Parameters

| Method / Parameter | Purpose |
|---|---|
| `threading.Thread` | Creates a thread |
| `target` | Specifies the function to execute |
| `args` | Passes positional arguments |
| `start()` | Starts the thread |
| `join()` | Waits for the thread to finish |
| `is_alive()` | Checks whether a thread is currently alive |

The first five will be used extensively throughout the threading section.

---

# 🧠 Key Takeaways

- **Threading** allows multiple threads to execute tasks within the same process.
- Python provides the `threading` module for thread management.
- `threading.Thread` is used to create a thread.
- `target` specifies the function executed by the thread.
- `args` is used to pass arguments to the target function.
- `start()` starts the thread.
- `join()` makes the calling thread wait for another thread to finish.
- A process contains at least one thread of execution.
- The program's initial thread is commonly called the main thread.
- Additional threads are often called worker threads.
- Multiple threads can execute tasks concurrently.
- Thread completion order is not guaranteed.
- `time.sleep()` can be used to simulate waiting in demonstrations.
- Threading is commonly useful for I/O-bound tasks.
- In standard CPython, the GIL limits parallel execution of pure Python bytecode across threads.
- Shared data between threads can create synchronization problems.
- Race conditions can occur when multiple threads access shared data incorrectly.
- Locks can be used to protect critical sections, which will be covered next.

---

# 🔚 Part 3 Summary

The basic threading workflow is:

    Import threading
          ↓
    Define target function
          ↓
    Create Thread object
          ↓
    Pass target and arguments
          ↓
    Call start()
          ↓
    Thread executes task
          ↓
    Call join()
          ↓
    Wait for thread completion
          ↓
    Continue main program

For multiple threads:

    Main Thread
         │
         ├── Thread 1
         ├── Thread 2
         └── Thread 3
                ↓
         Concurrent Execution
                ↓
        join() for each thread
                ↓
        All Tasks Completed


# 5️⃣ Race Conditions

## 🧩 What is a Race Condition?

**A race condition occurs when multiple threads access and modify shared data concurrently, and the final result depends on the timing or order of their execution.**

Race conditions are one of the most important problems in multithreaded programs.

They usually occur when:

1. Multiple threads share the same data.
2. More than one thread can modify that data.
3. The operations are not properly synchronized.

For example:

    Shared Variable
          │
     ┌────┴────┐
     ↓         ↓
 Thread 1   Thread 2
     │         │
     └────┬────┘
          ↓
     Shared Data

If both threads modify the same data at approximately the same time, the final result may become incorrect.

---

# 🧠 Understanding Shared Data

Consider a shared variable:

    counter = 0

Suppose two threads each need to increment it 1000 times.

The expected result would be:

    Thread 1 → 1000 increments
    Thread 2 → 1000 increments

Therefore:

    Expected counter = 2000

However, without proper synchronization, the actual result may be smaller.

For example:

    Final counter = 1000

or another unexpected value.

The reason is that the operation:

    counter = counter + 1

is not conceptually just one indivisible action.

It involves several steps:

    Read current value
          ↓
    Calculate new value
          ↓
    Write new value

Multiple threads can interfere with each other during these steps.

---

# 🔍 How a Race Condition Happens

Suppose:

    counter = 0

Two threads want to increment it.

A simplified execution could be:

    Thread 1 → Reads counter = 0
    Thread 2 → Reads counter = 0
    Thread 1 → Calculates 0 + 1
    Thread 2 → Calculates 0 + 1
    Thread 1 → Writes 1
    Thread 2 → Writes 1

The expected result after two increments is:

    2

But the actual result becomes:

    1

One increment has effectively been lost.

This is called a **lost update**.

---

# 📊 Race Condition Visualization

Without synchronization:

    Shared counter = 0

    Thread 1                 Thread 2
       │                        │
       │── Read 0 ──────────────│
       │                        │
       │                        │── Read 0
       │                        │
       │── Write 1              │
       │                        │
       │                        │── Write 1
       │                        │
       └────────────────────────┘

Final value:

    1

Expected value:

    2

The second thread overwrote the result produced by the first thread.

---

# 💻 Race Condition Example

File:

    07_race_condition.py

    import threading
    import time


    counter = 0


    def increment():
        global counter

        for _ in range(1000):
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

---

# 📤 Possible Output

A possible output is:

    Final counter: 1000

The expected result is:

    Final counter: 2000

The exact incorrect result can vary depending on timing and system behavior.

---

# 🧠 Why Did We Add `time.sleep()`?

This line:

    time.sleep(0.0001)

is intentionally added between reading and writing the shared variable.

It creates a larger opportunity for the two threads to overlap during the critical operation.

The purpose is to make the race condition easier to reproduce and understand.

It does not represent a real requirement for race conditions.

Real race conditions can occur without an explicit `sleep()`.

---

# 🔬 Breaking Down the Critical Operation

The code:

    current = counter
    counter = current + 1

can be understood conceptually as:

    Step 1 → Read counter
    Step 2 → Store current value
    Step 3 → Calculate current + 1
    Step 4 → Write new value

If another thread modifies `counter` between these operations, the first thread may overwrite the other thread's update.

Therefore, this section of code is a **critical section**.

---

# 🔐 What is a Critical Section?

**A critical section is a part of a program where shared data or shared resources are accessed or modified and therefore requires controlled access when multiple threads are involved.**

For example:

    current = counter
    counter = current + 1

This operation accesses shared data.

Therefore, it should be protected when multiple threads can execute it concurrently.

---

# ⚠️ Why Race Conditions Are Dangerous

Race conditions can cause:

- Incorrect results
- Lost updates
- Inconsistent state
- Difficult-to-reproduce bugs
- Data corruption
- Unexpected application behavior

The most difficult part is that the program may sometimes work correctly and sometimes fail.

For example:

    Run 1 → Correct
    Run 2 → Incorrect
    Run 3 → Correct
    Run 4 → Incorrect

This makes race conditions particularly difficult to debug.

---

# 🧠 Why Are Race Conditions Difficult to Debug?

Race conditions depend on timing.

Small changes can affect whether the problem appears:

- Different CPU load
- Different operating system scheduling
- Different thread timing
- Additional logging
- Different machine performance
- Network delays
- Different workload sizes

For example:

    Code works on Developer Machine
              ↓
        Deploy to Server
              ↓
        Timing changes
              ↓
      Race condition appears

Therefore, concurrent programs require careful synchronization.

---

# 🔒 6️⃣ Lock and Thread Safety

## 🧩 What is a Lock?

**A lock is a synchronization mechanism that allows only one thread at a time to access a protected section of shared data.**

Python provides locks through the `threading` module.

Basic syntax:

    lock = threading.Lock()

A lock can then protect a critical section:

    with lock:
        # critical section

This ensures that only one thread at a time can enter the protected section using that lock.

---

# 🧠 Why Do We Need a Lock?

Consider two threads:

    Thread 1
       │
       ↓
    Shared Data
       ↑
       │
    Thread 2

Both threads can attempt to modify the same data.

A lock changes the access pattern:

    Thread 1 ──→ Lock ──→ Critical Section ──→ Unlock
                       │
                       X
                  Thread 2 waits
                       │
                       ↓
                  Lock available
                       │
                       ↓
                  Critical Section

Only one thread can execute the protected section at a time.

---

# 🔹 Creating a Lock

    import threading

    lock = threading.Lock()

Here:

    threading.Lock()

creates a lock object.

The lock can then be shared by multiple threads.

---

# 🔹 Using `with lock:`

The recommended simple pattern is:

    with lock:
        # protected code

This automatically handles acquiring and releasing the lock.

Conceptually:

    with lock:
        critical_section()

is similar to:

    lock.acquire()

    try:
        critical_section()

    finally:
        lock.release()

Using `with` is generally safer because the lock is released automatically even if an exception occurs inside the protected block.

---

# 🧠 What is Thread Safety?

**Thread safety means that shared data and operations remain correct and consistent when accessed by multiple threads concurrently.**

A thread-safe design prevents concurrent execution from producing invalid state.

For example:

    Multiple Threads
           │
           ↓
      Shared Data
           │
           ↓
      Protected Access
           │
           ↓
      Correct State

Thread safety can be achieved using techniques such as:

- Locks
- Proper synchronization
- Thread-safe data structures
- Avoiding unnecessary shared mutable state
- Designing operations carefully

---

# 💻 Fixing the Race Condition with a Lock

File:

    08_lock_thread_safety.py

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

---

# 📤 Output

    Final counter: 2000

Now the result matches the expected value.

---

# 🧠 How the Lock Fixed the Problem

Without a lock:

    Thread 1 → Read
    Thread 2 → Read
    Thread 1 → Write
    Thread 2 → Write

Both threads could enter the critical section at the same time.

With a lock:

    Thread 1 → Acquire Lock
              ↓
           Read Data
              ↓
           Modify Data
              ↓
          Release Lock
              ↓
    Thread 2 → Acquire Lock
              ↓
           Read Data
              ↓
           Modify Data
              ↓
          Release Lock

The critical section is executed by only one thread at a time.

---

# 🔐 Lock Execution Flow

The execution can be visualized as:

    Thread 1
       │
       ↓
    Acquire Lock
       │
       ↓
    Critical Section
       │
       ↓
    Release Lock
       │
       ↓
    Thread 1 Continues


    Thread 2
       │
       ↓
    Tries to Acquire Lock
       │
       ↓
    Waits
       │
       ↓
    Lock Available
       │
       ↓
    Acquire Lock
       │
       ↓
    Critical Section
       │
       ↓
    Release Lock

---

# ⚠️ Important: Lock Does Not Make Everything Thread-Safe

Using a lock does not automatically make an entire program thread-safe.

The lock must protect the correct shared state and be used consistently by all relevant threads.

For example:

    Thread 1:
        with lock:
            modify shared_data

    Thread 2:
        modify shared_data

The second thread is not protected.

Therefore, synchronization must be designed carefully.

---

# 🧩 Lock and Critical Section

A good design usually keeps the critical section as small as reasonably possible.

For example:

    with lock:
        shared_counter += 1

This is preferable to unnecessarily protecting unrelated operations:

    with lock:
        perform_unrelated_work()
        make_network_request()
        process_large_file()
        shared_counter += 1
        perform_more_work()

Holding a lock for a long time can cause other threads to wait unnecessarily.

Therefore:

> **Protect shared state, but avoid holding locks longer than necessary.**

---

# ⚠️ Lock Contention

**Lock contention occurs when multiple threads frequently compete for the same lock.**

For example:

    Thread 1 ──┐
    Thread 2 ──┼──→ Same Lock
    Thread 3 ──┘

Only one thread can enter the critical section at a time.

The others must wait.

If the critical section is large or accessed very frequently, contention can reduce the benefits of concurrency.

Therefore, synchronization should be used carefully.

---

# 🔄 Race Condition vs Thread Safety

| Race Condition | Thread Safety |
|---|---|
| A bug/problem caused by unsafe concurrent access | Property of code that behaves correctly under concurrent access |
| Can produce inconsistent results | Attempts to maintain correct state |
| Often caused by shared mutable data | Achieved using synchronization and safe design |
| Example: lost update | Example: protecting shared counter with a lock |

A race condition is a problem.

Thread safety is the goal of designing concurrent code correctly.

---

# 🧠 Common Synchronization Problems

Locks solve many race conditions, but concurrent programs can have other problems too.

Examples include:

- Deadlocks
- Lock contention
- Starvation
- Excessive synchronization
- Incorrect locking order

These concepts are important in advanced concurrent programming.

---

# ⚠️ What is a Deadlock?

**A deadlock occurs when two or more threads wait indefinitely for resources or locks held by each other.**

For example:

    Thread 1
       │
       ├── Holds Lock A
       │
       └── Waits for Lock B


    Thread 2
       │
       ├── Holds Lock B
       │
       └── Waits for Lock A

The result is:

    Thread 1 → Waiting for Thread 2
    Thread 2 → Waiting for Thread 1

Neither can continue.

Conceptually:

    Thread 1
       ↓
    Lock A
       ↓
    Waiting for Lock B
       ↑
    Lock B
       ↑
    Thread 2

This creates a circular dependency.

---

# 🛡️ Avoiding Deadlocks

Some general practices include:

- Keep locking simple
- Acquire multiple locks in a consistent order
- Avoid unnecessary locks
- Keep critical sections short
- Release resources reliably
- Avoid waiting for unrelated operations while holding a lock

Deadlocks are an important reason why concurrent programs require careful design.

---

# 🤖 Locks in AI Engineering

Locks can become relevant when AI applications use multiple threads that share mutable state.

For example:

    AI Application
          │
          ├── Thread 1 → Update Cache
          ├── Thread 2 → Update Cache
          └── Thread 3 → Update Cache
                         │
                         ↓
                    Shared Cache

Without synchronization, simultaneous updates may produce inconsistent state.

A lock can protect the critical update:

    with lock:
        update_shared_cache()

Other examples include:

- Shared counters
- In-memory caches
- Shared queues
- Application state
- Logging systems
- Resource management

However, not every AI application needs explicit locks.

A better design may sometimes be to avoid shared mutable state altogether or use appropriate thread-safe abstractions.

---

# 📌 Important Lock Methods

Python's `Lock` object provides methods such as:

| Method | Purpose |
|---|---|
| `acquire()` | Acquires the lock |
| `release()` | Releases the lock |
| `locked()` | Checks whether the lock is currently locked |

Example:

    lock.acquire()

    try:
        # Critical section
        pass

    finally:
        lock.release()

However, for ordinary use, the context manager is generally cleaner:

    with lock:
        # Critical section

---

# 🧠 Manual Lock vs Context Manager

### Manual Approach

    lock.acquire()

    try:
        shared_data += 1

    finally:
        lock.release()

### Context Manager

    with lock:
        shared_data += 1

The second approach is generally easier to read and safer because the lock is automatically released when leaving the block.

---

# 📊 Race Condition vs Lock

| Without Lock | With Lock |
|---|---|
| Multiple threads can enter critical section | One thread enters protected section at a time |
| Shared data may become inconsistent | Shared update can be protected |
| Race condition possible | Race condition can be prevented for that protected operation |
| Synchronization absent | Synchronization provided |

---

# 🧠 Key Takeaways

- A **race condition** occurs when multiple threads access shared data concurrently and the final result depends on execution timing.
- Shared mutable state is a common source of race conditions.
- Operations such as `counter = counter + 1` can involve multiple conceptual steps.
- A **critical section** is a part of the program that accesses or modifies shared resources and requires controlled access.
- A **lock** allows only one thread at a time to enter a protected section using that lock.
- Python provides locks using `threading.Lock()`.
- `with lock:` is a convenient and safe way to protect a critical section.
- **Thread safety** means that concurrent access does not produce incorrect or inconsistent program state.
- Locks can prevent race conditions when used correctly.
- Locks should protect the correct shared data.
- Critical sections should generally be kept reasonably small.
- Excessive locking can cause lock contention.
- Poor lock design can cause deadlocks.
- Avoiding unnecessary shared mutable state can simplify concurrent programs.

---

# 🔚 Part 4 Summary

The relationship between the concepts can be remembered as:

    Multiple Threads
           ↓
    Shared Mutable Data
           ↓
    Concurrent Access
           ↓
    Race Condition
           ↓
    Incorrect / Inconsistent Result
           ↓
    Synchronization
           ↓
          Lock
           ↓
    Protected Critical Section
           ↓
       Thread Safety

The key idea is:

    Race Condition
        ↓
    Problem

    Lock
        ↓
    Synchronization Mechanism

    Thread Safety
        ↓
    Desired Correct Behaviour


# 7️⃣ Multiprocessing

## 🧩 What is Multiprocessing?

**Multiprocessing is a Python technique that uses multiple independent processes to execute tasks concurrently, allowing CPU-intensive work to make use of multiple CPU cores.**

Unlike threading, where multiple threads operate inside the same process and share its memory, multiprocessing creates separate processes.

Conceptually:

    Single Process

        ┌─────────────────────┐
        │      Process        │
        │                     │
        │ Thread 1            │
        │ Thread 2            │
        │ Thread 3            │
        └─────────────────────┘


    Multiprocessing

        ┌─────────────┐
        │  Process 1  │
        └─────────────┘

        ┌─────────────┐
        │  Process 2  │
        └─────────────┘

        ┌─────────────┐
        │  Process 3  │
        └─────────────┘

Each process has its own memory space and execution environment.

---

# 🧠 Why Do We Need Multiprocessing?

Some tasks are not primarily waiting for external resources.

Instead, they spend most of their time performing computations.

Examples:

- Large mathematical calculations
- Image processing
- Video processing
- Data processing
- Scientific calculations
- Simulations
- CPU-intensive algorithms

These are known as **CPU-bound tasks**.

For such workloads, using multiple processes can allow work to be distributed across multiple CPU cores.

Conceptually:

    CPU
    ├── Core 1 → Process 1
    ├── Core 2 → Process 2
    ├── Core 3 → Process 3
    └── Core 4 → Process 4

This is different from simply creating multiple threads.

---

# 🔄 Threading vs Multiprocessing

Threading:

    Process
       │
       ├── Thread 1
       ├── Thread 2
       └── Thread 3

Multiprocessing:

    Process 1

    Process 2

    Process 3

The key difference is that threads exist inside a process, while processes are separate execution environments.

---

# 📊 Multiprocessing vs Threading

| Feature | Threading | Multiprocessing |
|---|---|---|
| Unit of execution | Thread | Process |
| Memory | Shared within process | Separate process memory |
| Creation overhead | Generally lower | Generally higher |
| Communication | Easier through shared memory | Requires explicit IPC mechanisms |
| Isolation | Lower | Higher |
| CPU-bound pure Python | Limited by GIL in standard CPython | Often suitable |
| I/O-bound | Often useful | Can also be used |
| CPU cores | Threads do not generally provide pure-Python CPU parallelism in standard CPython | Can utilize multiple cores |
| Python module | `threading` | `multiprocessing` |

---

# 🔹 Python's `multiprocessing` Module

Python provides the built-in `multiprocessing` module for creating and managing processes.

To use it:

    import multiprocessing

The module provides several useful tools, including:

- `Process`
- `Pool`
- `Queue`
- `Pipe`
- Shared memory mechanisms
- Synchronization primitives

In this chapter, we will focus on:

    multiprocessing
        │
        ├── Process
        ├── Pool
        └── Queue

---

# 💻 Basic Multiprocessing Example

File:

    09_multiprocessing.py

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

---

# 📤 Possible Output

    Process 1 started
    Process 2 started
    Process 1 completed
    Process 2 completed
    All processes completed

The order of the output may vary.

For example:

    Process 2 started
    Process 1 started
    Process 2 completed
    Process 1 completed
    All processes completed

The exact order depends on process scheduling and system conditions.

---

# 🧠 How the Multiprocessing Example Works

The program follows these steps:

    Program Starts
          ↓
    Define task()
          ↓
    Create Process 1
          ↓
    Create Process 2
          ↓
    Start Process 1
          ↓
    Start Process 2
          ↓
    Both Processes Execute
          ↓
    join() waits for Process 1
          ↓
    join() waits for Process 2
          ↓
    All Processes Complete
          ↓
    Main Program Continues

---

# 🔹 Why Do We Use `if __name__ == "__main__":`?

When using multiprocessing, especially with the `spawn` start method, the main module may be imported in a new process.

Therefore, process creation should generally be protected with:

    if __name__ == "__main__":

Example:

    if __name__ == "__main__":
        process = multiprocessing.Process(target=task)
        process.start()
        process.join()

This prevents process creation code from executing unintentionally when the module is imported by a child process.

It is especially important for portable multiprocessing programs.

---

# 🧩 Understanding `__name__ == "__main__"`

When a Python file is executed directly, Python sets:

    __name__ = "__main__"

Therefore:

    if __name__ == "__main__":

becomes true.

If the same file is imported as a module, `__name__` contains the module's name instead.

This allows us to distinguish between:

    Direct execution

and:

    Module import

This pattern is common in Python programs and especially important when working with multiprocessing.

---

# 🔹 Creating a Process

The basic syntax is:

    process = multiprocessing.Process(
        target=function,
        args=(arguments,)
    )

Here:

- `multiprocessing.Process` → Creates a process object
- `target` → Function the process will execute
- `args` → Arguments passed to the target function

The process does not begin execution until:

    process.start()

is called.

---

# 🔹 Starting a Process

**`start()` starts the process and schedules the target function for execution in that process.**

Example:

    process.start()

After calling `start()`, the new process begins execution.

The main process can continue executing as well.

Conceptually:

    Main Process
         │
         ├── start()
         │
         └──────────────→ Child Process
                              │
                              ↓
                           task()

---

# 🔹 Waiting for a Process

**`join()` makes the calling process wait until the target process has finished.**

Example:

    process.start()
    process.join()

The flow becomes:

    Main Process
         │
         ├── Start Child Process
         │
         └── Wait
               │
               ↓
         Child Process
               │
               ↓
           Task Complete
               │
               ↓
         Main Continues

Without `join()`, the main process does not explicitly wait at that point.

---

# 🧠 Process Lifecycle

A simplified process lifecycle is:

    Process Created
          ↓
    Process Started
          ↓
    Process Running
          ↓
    Target Function Executes
          ↓
    Target Function Completes
          ↓
    Process Terminates

The main process can monitor or wait for the child process.

---

# ⚙️ CPU-bound Tasks

## 🧩 What is a CPU-bound Task?

**A CPU-bound task spends most of its execution time performing computations rather than waiting for external resources.**

Examples include:

- Large mathematical calculations
- Numerical simulations
- Image transformations
- Video processing
- Complex data processing
- CPU-heavy algorithms

Conceptually:

    CPU-bound Task
          ↓
    Heavy Computation
          ↓
    CPU remains busy
          ↓
    Task completes

---

# 💻 CPU-bound Example

Consider a computational task:

    def calculate():
        total = 0

        for i in range(10_000_000):
            total += i

        return total

This task spends most of its time performing calculations.

It is therefore CPU-bound.

Multiple independent CPU-bound tasks may benefit from multiprocessing.

---

# 🚀 Multiprocessing and CPU Cores

Suppose a computer has four CPU cores:

    CPU
    ┌───────────────────────────┐
    │                           │
    │ Core 1 → Process 1        │
    │ Core 2 → Process 2        │
    │ Core 3 → Process 3        │
    │ Core 4 → Process 4        │
    │                           │
    └───────────────────────────┘

Independent processes can potentially execute on different cores.

This is one of the main reasons multiprocessing is useful for CPU-bound work.

---

# ⚠️ Multiprocessing Has Overhead

Multiprocessing is not free.

Creating and managing processes requires resources.

There can be overhead from:

- Creating processes
- Starting processes
- Communication
- Data serialization
- Transferring data between processes
- Process management
- Memory usage

Therefore, multiprocessing is generally more useful when the work performed by each process is large enough to justify this overhead.

---

# 🧠 When Multiprocessing May Not Help

Suppose we have tiny tasks:

    Task 1 → Very small
    Task 2 → Very small
    Task 3 → Very small

Creating separate processes may take more time than simply performing the tasks sequentially.

Therefore:

    Small Task
        ↓
    Multiprocessing overhead
        ↓
    Little or no benefit

A good rule is:

> **Use multiprocessing when the amount of CPU work is large enough to justify process-management overhead.**

---

# 📊 CPU-bound vs I/O-bound

| CPU-bound | I/O-bound |
|---|---|
| Mostly computation | Mostly waiting |
| CPU is heavily used | CPU may remain idle during waits |
| Mathematical calculations | API requests |
| Image processing | Database queries |
| Video processing | Network requests |
| Large data processing | File operations |
| Multiprocessing often useful | Threading/asyncio often useful |

This distinction is one of the most important concepts in concurrency.

---

# 🔐 Process Memory Isolation

Each process normally has its own memory space.

For example:

    Process 1
    ┌──────────────────┐
    │ counter = 100    │
    └──────────────────┘

    Process 2
    ┌──────────────────┐
    │ counter = 200    │
    └──────────────────┘

Changing `counter` in Process 1 does not automatically change the `counter` in Process 2.

This is different from threads, which share memory within the same process.

---

# 🧩 Why Separate Memory Matters

Separate memory provides stronger isolation.

If one process modifies:

    variable = 100

another process does not automatically see that modification.

This improves isolation but makes communication more complicated.

Processes therefore require explicit mechanisms when they need to exchange data.

Examples include:

- Queue
- Pipe
- Shared memory
- Manager objects
- Files
- Other IPC mechanisms

These concepts will be explored later in this chapter.

---

# 🔄 Inter-Process Communication

**Inter-Process Communication (IPC) refers to mechanisms that allow separate processes to exchange data or coordinate their activities.**

Conceptually:

    Process 1
        │
        │
        ↓
      IPC
        │
        ↓
    Process 2

Python provides several IPC mechanisms.

Examples:

    multiprocessing.Queue
    multiprocessing.Pipe
    Shared Memory
    Manager

In this chapter, `Queue` will be studied as an important process communication mechanism.

---

# 🧠 Multiprocessing and the GIL

One important reason multiprocessing is useful in standard CPython is the Global Interpreter Lock.

The GIL restricts simultaneous execution of Python bytecode by multiple threads within a single CPython interpreter process.

With multiprocessing:

    Process 1 → Interpreter
    Process 2 → Interpreter
    Process 3 → Interpreter

Each process has its own Python interpreter and memory space.

Therefore, CPU-bound work can be distributed across processes and potentially across multiple CPU cores.

This makes multiprocessing a common strategy for CPU-bound Python workloads.

---

# ⚠️ Important GIL Clarification

The GIL should not be interpreted as:

> "Python cannot run things in parallel."

That statement is too broad.

Python programs can achieve parallelism through:

- Multiple processes
- Native libraries that release the GIL
- Certain implementations and execution models

The important practical point for this chapter is:

> **In standard CPython, multiprocessing is a common way to achieve CPU parallelism for CPU-bound pure-Python workloads.**

---

# 💻 Comparing Sequential and Multiprocessing Execution

Consider multiple CPU-heavy tasks.

### Sequential

    Task 1
       ↓
    Task 2
       ↓
    Task 3
       ↓
    Task 4

Only one task is being executed at a time.

---

### Multiprocessing

    Process 1 → Task 1
    Process 2 → Task 2
    Process 3 → Task 3
    Process 4 → Task 4

If sufficient CPU resources are available, these tasks can execute in parallel.

---

# ⏱️ Practical Timing Example

A simple CPU-bound demonstration can compare sequential execution with multiprocessing.

Sequential version:

    import time


    def calculate(number):
        total = 0

        for i in range(10_000_000):
            total += i * number

        return total


    start = time.time()

    calculate(1)
    calculate(2)
    calculate(3)
    calculate(4)

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

A multiprocessing implementation can distribute these calculations across processes.

However, timing results should not be treated as universal benchmarks.

Performance depends on:

- CPU
- Number of cores
- Operating system
- Python version
- Process startup cost
- Workload size
- System load

---

# 🤖 Multiprocessing in AI Engineering

Multiprocessing can be useful in AI Engineering for CPU-heavy workloads that can be divided into independent tasks.

Examples include:

### 🖼️ Image Processing

    Image 1 → Process 1
    Image 2 → Process 2
    Image 3 → Process 3
    Image 4 → Process 4

### 📊 Data Processing

    Dataset Chunk 1 → Process 1
    Dataset Chunk 2 → Process 2
    Dataset Chunk 3 → Process 3

### 🔢 Numerical Computation

    Calculation 1 → Process 1
    Calculation 2 → Process 2
    Calculation 3 → Process 3

### 🧹 Data Preprocessing

Large datasets may sometimes be divided into independent chunks that can be processed separately.

For example:

    Large Dataset
          │
          ├── Chunk 1 → Process 1
          ├── Chunk 2 → Process 2
          ├── Chunk 3 → Process 3
          └── Chunk 4 → Process 4
                    ↓
              Combined Results

The exact approach depends on the libraries and workload.

---

# ⚠️ Multiprocessing in AI Systems

Not every AI workload should use multiprocessing.

For example, if an AI application mainly waits for:

    LLM API
    Web Search
    Database
    Vector Database

then multiprocessing may be unnecessary.

These operations are often I/O-bound.

In such cases, approaches such as:

    asyncio
    ThreadPoolExecutor

may be more appropriate.

On the other hand, CPU-heavy preprocessing may benefit from:

    multiprocessing
    ProcessPoolExecutor

Therefore, understanding the workload is more important than simply using the most powerful-looking concurrency technique.

---

# 📌 Multiprocessing Workflow

The basic workflow can be remembered as:

    Import multiprocessing
            ↓
    Define target function
            ↓
    Create Process
            ↓
    Pass target and arguments
            ↓
    start()
            ↓
    Process executes task
            ↓
    join()
            ↓
    Main process continues

---

# 🧠 Important Concepts

| Concept | Meaning |
|---|---|
| Process | Independent execution environment |
| `multiprocessing` | Python module for process-based concurrency |
| `Process` | Class used to create a process |
| `target` | Function executed by the process |
| `args` | Arguments passed to the target |
| `start()` | Starts the process |
| `join()` | Waits for the process to finish |
| IPC | Communication between processes |
| CPU-bound | Work dominated by computation |

---

# 📊 Threading vs Multiprocessing: Quick Decision Guide

    Is the task mostly waiting?
            │
           YES
            ↓
       I/O-bound
            ↓
    Threading / asyncio
            │
            │
           NO
            ↓
    Is the task computationally heavy?
            │
           YES
            ↓
       CPU-bound
            ↓
    Multiprocessing / ProcessPoolExecutor

This is a practical guideline, not an absolute rule.

---

# 🧠 Key Takeaways

- **Multiprocessing** uses multiple independent processes for concurrent or parallel work.
- Each process has its own memory space.
- Multiprocessing is commonly useful for CPU-bound workloads.
- Multiple processes can potentially use multiple CPU cores.
- Python provides multiprocessing through the built-in `multiprocessing` module.
- `multiprocessing.Process` is used to create an individual process.
- `start()` starts a process.
- `join()` waits for a process to finish.
- The `if __name__ == "__main__":` guard is important for safe and portable multiprocessing code.
- Processes have stronger memory isolation than threads.
- Separate process memory means communication usually requires explicit IPC mechanisms.
- `multiprocessing.Queue` is one such mechanism and will be covered later.
- Multiprocessing introduces overhead, so it is not automatically beneficial for very small tasks.
- In standard CPython, multiprocessing is commonly used for CPU-bound pure-Python work because separate processes have separate interpreter instances.
- AI Engineering applications can use multiprocessing for CPU-heavy preprocessing, data processing, image processing, and other computational workloads.

---

# 🔚 Part 5 Summary

The fundamental difference can be remembered as:

    Threading

    Process
       │
       ├── Thread 1
       ├── Thread 2
       └── Thread 3


    Multiprocessing

    Process 1
    Process 2
    Process 3

Threads:

    Shared Process Memory
          ↓
    Lower isolation
          ↓
    Often useful for I/O-bound work

Processes:

    Separate Memory Spaces
          ↓
    Higher isolation
          ↓
    Can utilize multiple CPU cores
          ↓
    Often useful for CPU-bound work

The basic multiprocessing flow is:

    Create Process
         ↓
    start()
         ↓
    Process Runs
         ↓
    join()
         ↓
    Process Completes

The next topics will go deeper into individual multiprocessing tools, beginning with the **`Process` class**, followed by **Process Pools** and **Multiprocessing Queues**.


# 8️⃣ `Process` Class

## 🧩 What is `Process`?

**`Process` is a class from Python's `multiprocessing` module that is used to create and manage an independent process.**

It allows us to execute a function in a separate process instead of executing it directly inside the main process.

Basic structure:

    Main Process
         │
         ├── Process 1
         │      └── task()
         │
         └── Process 2
                └── task()

The `Process` class gives us control over these child processes.

---

# 📦 Importing `Process`

We can import the complete module:

    import multiprocessing

and then use:

    multiprocessing.Process

Or we can directly import the class:

    from multiprocessing import Process

Both approaches are valid.

For this chapter, we will use:

    from multiprocessing import Process

when we want to work directly with the `Process` class.

---

# 💻 Basic `Process` Example

File:

    10_process.py

    from multiprocessing import Process
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")


    if __name__ == "__main__":
        process1 = Process(
            target=task,
            args=("Process 1",)
        )

        process2 = Process(
            target=task,
            args=("Process 2",)
        )

        process1.start()
        process2.start()

        process1.join()
        process2.join()

        print("All processes completed")

---

# 🔍 Understanding the `Process` Object

When we write:

    process1 = Process(
        target=task,
        args=("Process 1",)
    )

we are creating a `Process` object.

At this point, the process has been created as an object, but its target function has not started executing yet.

The actual execution begins when we call:

    process1.start()

---

# 🔹 `target`

**`target` specifies the function that the new process should execute.**

Example:

    def task():
        print("Task running")


    process = Process(target=task)

Here:

    target=task

means:

> When the process starts, execute the `task()` function.

---

# ⚠️ `target=function` vs `target=function()`

This is an important concept.

Correct:

    Process(target=task)

Incorrect:

    Process(target=task())

Why?

Because:

    target=task

passes the function itself.

But:

    target=task()

calls the function immediately and passes its returned value.

Think of it as:

    target=task
          ↓
    "Run this function later"

while:

    target=task()
          ↓
    "Run this function right now"

This same concept also applies to threading.

---

# 🔹 `args`

**`args` is used to pass positional arguments to the target function.**

Suppose:

    def task(name):
        print(name)

We can pass the argument using:

    process = Process(
        target=task,
        args=("Process 1",)
    )

The process will effectively execute:

    task("Process 1")

---

# ⚠️ Why Is There a Comma?

This:

    args=("Process 1",)

is a tuple containing one element.

The comma is important.

Without the comma:

    args=("Process 1")

this is simply a string enclosed in parentheses, not a one-element tuple.

For multiple arguments:

    args=("Process 1", 10, "AI")

No special trailing comma is required because there are already multiple elements.

---

# 🔹 `start()`

**`start()` starts a new process and begins execution of its target function.**

Example:

    process.start()

Before `start()`:

    Process Object Created

After `start()`:

    Process Starts Running

Important:

`start()` should normally be called only once for a process object.

---

# 🔹 `join()`

**`join()` makes the calling process wait until the target process finishes execution.**

Example:

    process.start()
    process.join()

Flow:

    Main Process
         │
         ├── start()
         │
         ↓
    Child Process
         │
         ├── Execute task
         │
         ↓
       Finish
         │
         ↓
    Main Process continues

This is useful when the main program needs to wait for a child process before continuing.

---

# 🔹 `is_alive()`

**`is_alive()` checks whether a process is currently running.**

It returns:

    True

if the process is still active.

It returns:

    False

if the process has finished.

Example:

    from multiprocessing import Process
    import time


    def task():
        time.sleep(2)


    if __name__ == "__main__":
        process = Process(target=task)

        print("Before start:", process.is_alive())

        process.start()

        print("After start:", process.is_alive())

        process.join()

        print("After completion:", process.is_alive())

Possible output:

    Before start: False
    After start: True
    After completion: False

---

# 🧠 Understanding `is_alive()`

The process lifecycle can be visualized as:

    Process Created
          │
          ↓
    is_alive() → False
          │
          ↓
       start()
          │
          ↓
    Process Running
          │
          ↓
    is_alive() → True
          │
          ↓
    Task Completed
          │
          ↓
    is_alive() → False

Therefore, `is_alive()` is useful when we need to check the current execution state of a process.

---

# 🔹 `terminate()`

**`terminate()` stops a running process forcefully.**

Example:

    process.terminate()

This can be useful when a process needs to be stopped before it naturally finishes.

Example:

    from multiprocessing import Process
    import time


    def task():
        while True:
            print("Process running...")
            time.sleep(1)


    if __name__ == "__main__":
        process = Process(target=task)

        process.start()

        time.sleep(3)

        process.terminate()
        process.join()

        print("Process terminated")

Here, the process would normally continue indefinitely, but `terminate()` stops it.

### ⚠️ Important

`terminate()` should be used carefully.

If a process is terminated while it is:

- Writing data
- Holding resources
- Updating shared state
- Performing an important operation

the operation may not complete cleanly.

For graceful program design, it is often better to allow a process to finish naturally whenever possible.

---

# 🔹 `kill()`

**`kill()` forcefully terminates a process using the operating system's stronger termination mechanism.**

Example:

    process.kill()

It is similar in purpose to `terminate()`, but the exact behavior depends on the operating system.

For normal application logic, prefer designing processes so they can finish or shut down gracefully instead of relying on forceful termination.

---

# 🔹 `close()`

**`close()` releases resources associated with a process object after the process has finished.**

Example:

    process.start()
    process.join()
    process.close()

The process should no longer be running when `close()` is called.

Conceptually:

    Start
      ↓
    Run
      ↓
    Join
      ↓
    Finished
      ↓
    Close

This is useful when explicitly managing process resources.

---

# 🧠 `Process` Methods Quick Reference

| Method | Purpose |
|---|---|
| `start()` | Starts the process |
| `join()` | Waits for the process to finish |
| `is_alive()` | Checks whether the process is running |
| `terminate()` | Forcefully terminates the process |
| `kill()` | Forcefully kills the process |
| `close()` | Releases resources after process completion |

---

# 🔄 Complete Process Lifecycle

A typical process lifecycle looks like:

    ┌──────────────────────┐
    │ Create Process Object│
    └──────────┬───────────┘
               ↓
          process.start()
               ↓
    ┌──────────────────────┐
    │   Process Running    │
    └──────────┬───────────┘
               ↓
       Target Function
          Executes
               ↓
    ┌──────────────────────┐
    │ Process Completes    │
    └──────────┬───────────┘
               ↓
          process.join()
               ↓
          process.close()

A process can also be terminated before naturally completing:

    start()
      ↓
    Running
      ↓
    terminate()
      ↓
    Process Stopped

---

# 🧩 Multiple Processes

We can create multiple `Process` objects.

Example:

    from multiprocessing import Process
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")


    if __name__ == "__main__":
        process1 = Process(
            target=task,
            args=("Process 1",)
        )

        process2 = Process(
            target=task,
            args=("Process 2",)
        )

        process3 = Process(
            target=task,
            args=("Process 3",)
        )

        process1.start()
        process2.start()
        process3.start()

        process1.join()
        process2.join()
        process3.join()

        print("All processes completed")

Possible output:

    Process 1 started
    Process 2 started
    Process 3 started
    Process 2 completed
    Process 1 completed
    Process 3 completed
    All processes completed

The completion order is not guaranteed.

---

# ⚠️ Process Execution Order

If we write:

    process1.start()
    process2.start()
    process3.start()

we should not assume:

    Process 1 completes first
    Process 2 completes second
    Process 3 completes third

The operating system decides when each process gets CPU time.

Therefore, output may vary between executions.

This is an important characteristic of concurrent programming.

---

# 🧠 `start()` vs `join()`

These two methods are frequently used together.

### `start()`

Starts the process.

    process.start()

### `join()`

Waits for the process to finish.

    process.join()

Together:

    process.start()
    process.join()

means:

> Start this process and wait until it finishes.

For multiple processes:

    process1.start()
    process2.start()

    process1.join()
    process2.join()

Both processes can start before the main process waits for them.

This is different from:

    process1.start()
    process1.join()

    process2.start()
    process2.join()

which makes the execution much more sequential.

---

# 🚀 Concurrent vs Sequential Process Starting

### Sequential waiting

    process1.start()
    process1.join()

    process2.start()
    process2.join()

Conceptually:

    Process 1
       ↓
    Complete
       ↓
    Process 2
       ↓
    Complete

---

### Concurrent starting

    process1.start()
    process2.start()

    process1.join()
    process2.join()

Conceptually:

    Process 1 ────────────→ Complete
    Process 2 ────────────→ Complete

Both processes are allowed to execute before the main process waits for completion.

This pattern is generally what we want when the tasks are independent.

---

# 🧠 Process Identity

Every process has an operating-system-level process identity.

Python allows us to access the process ID using:

    process.pid

Example:

    from multiprocessing import Process
    import os


    def task():
        print("Child PID:", os.getpid())


    if __name__ == "__main__":
        process = Process(target=task)

        process.start()

        print("Child Process ID:", process.pid)

        process.join()

Possible output:

    Child Process ID: 12345
    Child PID: 12345

The exact number will vary between executions.

---

# 🔹 Parent Process ID

A process can also identify its parent process.

Using:

    os.getppid()

we can obtain the parent process ID.

Example:

    import os

    print("Current Process ID:", os.getpid())
    print("Parent Process ID:", os.getppid())

This can help when learning how processes are related at the operating-system level.

---

# 🤖 `Process` in AI Engineering

The `Process` class is useful when an AI application has independent CPU-heavy tasks.

For example:

    AI Pipeline
        │
        ├── Image preprocessing → Process 1
        ├── Data preprocessing  → Process 2
        ├── Feature calculation → Process 3
        └── File processing      → Process 4

Each process can perform an independent computation.

Another example:

    Dataset
       │
       ├── Chunk 1 → Process 1
       ├── Chunk 2 → Process 2
       ├── Chunk 3 → Process 3
       └── Chunk 4 → Process 4
                       ↓
                 Combined Output

This can be useful in preprocessing pipelines where tasks are independent and CPU-intensive.

---

# ⚠️ When NOT to Use `Process`

Do not automatically create a process for every task.

For example, an AI assistant might need to perform:

    Web Search
    ↓
    API Request
    ↓
    Database Query

These tasks spend significant time waiting for external systems.

For such workloads, asynchronous programming or thread-based concurrency may be more appropriate.

Use the workload characteristics to choose the approach.

---

# 📊 `Process` vs `Thread`

| Feature | `Thread` | `Process` |
|---|---|---|
| Created using | `threading.Thread` | `multiprocessing.Process` |
| Runs inside | Process | Separate process |
| Memory | Shared within process | Separate |
| Isolation | Lower | Higher |
| Communication | Shared memory possible | IPC mechanisms commonly required |
| CPU-bound pure Python | Limited by GIL | Often suitable |
| I/O-bound | Often useful | Possible, but usually heavier |
| Startup overhead | Lower | Higher |

---

# 🧠 Key Takeaways

- `Process` is a class from the `multiprocessing` module.
- It creates an independent process.
- `target` specifies the function executed by the process.
- `args` passes positional arguments to the target function.
- `start()` starts the process.
- `join()` waits for the process to finish.
- `is_alive()` checks whether a process is currently running.
- `terminate()` forcefully stops a process.
- `kill()` provides another forceful termination mechanism.
- `close()` releases resources after the process has finished.
- Process completion order is not guaranteed.
- Multiple processes can be started before waiting for them.
- `if __name__ == "__main__":` is important for safe multiprocessing programs.
- `pid` can be used to identify a process.
- Processes are especially useful for CPU-bound workloads.
- In AI Engineering, processes can be useful for CPU-heavy preprocessing and independent computational tasks.

---

# 🔚 Summary

The most important `Process` workflow is:

    from multiprocessing import Process

            ↓

    Create Process

            ↓

    Process(
        target=function,
        args=(...)
    )

            ↓

    start()

            ↓

    Process Executes

            ↓

    join()

            ↓

    Process Completes

Useful process-control methods:

    start()
    join()
    is_alive()
    terminate()
    kill()
    close()

The `Process` class is useful when we need direct control over individual processes.

However, manually creating many processes can become repetitive:

    Process 1
    Process 2
    Process 3
    Process 4
    Process 5
    ...

For handling many similar tasks efficiently, Python provides a higher-level abstraction called a **Process Pool**.

That is the next topic.


# 9️⃣ Process Pool

## 🧩 What is a Process Pool?

**A process pool is a collection of worker processes that can execute multiple tasks concurrently, allowing us to distribute work without manually creating each process.**

Instead of manually creating:

    Process 1
    Process 2
    Process 3
    Process 4
    Process 5

we can create a pool:

    Process Pool
    ┌──────────────────────────────┐
    │ Worker 1                    │
    │ Worker 2                    │
    │ Worker 3                    │
    └──────────────────────────────┘
              ↓
          Task Queue
              ↓
    ┌──────┬──────┬──────┬──────┐
    │Task 1│Task 2│Task 3│Task 4│
    └──────┴──────┴──────┴──────┘

The pool automatically distributes tasks among the available worker processes.

---

# 📌 Why Do We Need a Process Pool?

Suppose we have 100 independent CPU-bound tasks.

Creating every process manually would be repetitive:

    process1 = Process(...)
    process2 = Process(...)
    process3 = Process(...)
    ...
    process100 = Process(...)

It would also make the program difficult to manage.

A process pool allows us to specify the number of workers:

    Pool(4)

and then give the pool a collection of tasks.

The pool manages the workers for us.

---

# 🧠 Basic Process Pool Architecture

Suppose we create:

    Pool(3)

The pool contains three worker processes:

    ┌──────────────────────────┐
    │       Process Pool       │
    │                          │
    │  Worker 1                │
    │  Worker 2                │
    │  Worker 3                │
    └────────────┬─────────────┘
                 │
                 ↓
            Task Queue

If there are six tasks:

    Task 1
    Task 2
    Task 3
    Task 4
    Task 5
    Task 6

the workers can process them in batches:

    Worker 1 → Task 1
    Worker 2 → Task 2
    Worker 3 → Task 3

              ↓

    Worker 1 → Task 4
    Worker 2 → Task 5
    Worker 3 → Task 6

The exact scheduling behavior is managed by the pool.

---

# 📦 Importing `Pool`

`Pool` is available inside Python's `multiprocessing` module.

We can write:

    import multiprocessing

and then:

    multiprocessing.Pool

Or directly import it:

    from multiprocessing import Pool

For our examples:

    import multiprocessing

will be used so that the relationship with the `multiprocessing` module remains clear.

---

# 💻 Basic Process Pool Example

File:

    11_pool.py

    import multiprocessing
    import time


    def square(number):
        print(f"Calculating square of {number}")

        time.sleep(1)

        return number * number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]

        with multiprocessing.Pool(3) as pool:
            results = pool.map(square, numbers)

        print("Results:", results)

---

# 📤 Possible Output

    Calculating square of 1
    Calculating square of 2
    Calculating square of 3
    Calculating square of 4
    Calculating square of 5
    Results: [1, 4, 9, 16, 25]

The exact order of the `Calculating...` messages may vary.

However, the result returned by `map()` is ordered according to the input sequence.

---

# 🔍 Understanding `Pool(3)`

This line:

    multiprocessing.Pool(3)

creates a process pool containing up to three worker processes.

Conceptually:

    Pool(3)

        ┌──────────────┐
        │   Worker 1   │
        ├──────────────┤
        │   Worker 2   │
        ├──────────────┤
        │   Worker 3   │
        └──────────────┘

The number `3` represents the number of worker processes.

---

# 🔹 What Does `map()` Do?

**`map()` applies a function to every item in an iterable and distributes the work among the available worker processes.**

Example:

    numbers = [1, 2, 3, 4, 5]

    results = pool.map(square, numbers)

Conceptually:

    square(1)
    square(2)
    square(3)
    square(4)
    square(5)

The pool manages how these function calls are distributed among its workers.

---

# 🧠 Process Pool `map()` Flow

    Input:

    [1, 2, 3, 4, 5]

            ↓

       Process Pool

       ┌───────────┐
       │ Worker 1  │ → square(1)
       │ Worker 2  │ → square(2)
       │ Worker 3  │ → square(3)
       └───────────┘

            ↓

       More tasks become available

            ↓

       Worker processes execute them

            ↓

    Results:

    [1, 4, 9, 16, 25]

---

# 🔄 `map()` and Result Order

One important property of `pool.map()` is that the results are returned in the same order as the input iterable.

Input:

    [1, 2, 3, 4, 5]

Output:

    [1, 4, 9, 16, 25]

Even if:

    square(5)

finishes before:

    square(2)

the result sequence remains aligned with the original input.

Conceptually:

    Input          Result

      1     →       1
      2     →       4
      3     →       9
      4     →      16
      5     →      25

---

# ⚠️ Completion Order vs Result Order

These are two different things.

### Completion order

Determined by:

- Scheduling
- Task duration
- CPU availability
- System load

Therefore, it can vary.

### Result order

With `map()`, results correspond to the input order.

For example:

    Input:
    [1, 2, 3]

Possible completion order:

    2 → 3 → 1

But returned result:

    [square(1), square(2), square(3)]

which becomes:

    [1, 4, 9]

This distinction is important when working with concurrent programs.

---

# 🔹 `with multiprocessing.Pool(...)`

The recommended pattern is:

    with multiprocessing.Pool(3) as pool:
        results = pool.map(square, numbers)

The `with` statement manages the pool lifecycle.

Conceptually:

    Create Pool
        ↓
    Use Pool
        ↓
    Tasks Execute
        ↓
    Leave `with` block
        ↓
    Pool Cleanup

This reduces the need to manually manage the pool's resources.

---

# 🧠 Why Use `with`?

Without a context manager, we may need to manually manage the pool.

For example:

    pool = multiprocessing.Pool(3)

    results = pool.map(square, numbers)

    pool.close()
    pool.join()

Using:

    with multiprocessing.Pool(3) as pool:
        results = pool.map(square, numbers)

makes the lifecycle easier to manage.

The context manager handles cleanup when execution leaves the block.

---

# 🔹 `close()`

**`close()` prevents any more tasks from being submitted to the pool.**

Example:

    pool.close()

After closing the pool, new work should not be submitted to it.

The worker processes can finish tasks that were already submitted.

---

# 🔹 `join()`

**`join()` waits for the worker processes in the pool to finish.**

A traditional lifecycle can look like:

    pool = multiprocessing.Pool(3)

    pool.map(square, numbers)

    pool.close()
    pool.join()

The order is important:

    close()
       ↓
    join()

`close()` indicates that no more work will be submitted.

`join()` waits for the workers to finish.

When using the `with` pattern, explicit cleanup is normally handled automatically.

---

# 🔹 `terminate()`

**`terminate()` stops the worker processes immediately.**

Example:

    pool.terminate()

This is useful when the remaining tasks should not continue.

However, forcefully stopping workers should be used carefully because tasks may not complete cleanly.

---

# 📊 Pool Lifecycle

A simplified lifecycle is:

    Create Pool
        ↓
    Add / Submit Tasks
        ↓
    Workers Execute Tasks
        ↓
    Finish Task Processing
        ↓
    Close / Cleanup
        ↓
    Pool Ends

With a context manager:

    with Pool(...) as pool:
        work
    ↓
    Cleanup

---

# 🧩 Pool with Multiple Tasks

Example:

    import multiprocessing


    def cube(number):
        return number ** 3


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5, 6]

        with multiprocessing.Pool(3) as pool:
            results = pool.map(cube, numbers)

        print("Results:", results)

Output:

    Results: [1, 8, 27, 64, 125, 216]

The pool automatically distributes the six tasks among the available workers.

---

# 🔹 `starmap()`

**`starmap()` is used when the target function requires multiple arguments for each task.**

Suppose we have:

    def multiply(a, b):
        return a * b

Our input can be:

    values = [
        (2, 3),
        (4, 5),
        (6, 7)
    ]

We can use:

    results = pool.starmap(multiply, values)

Output:

    [6, 20, 42]

Conceptually:

    (2, 3) → multiply(2, 3) → 6
    (4, 5) → multiply(4, 5) → 20
    (6, 7) → multiply(6, 7) → 42

---

# 💻 `starmap()` Example

    import multiprocessing


    def multiply(a, b):
        return a * b


    if __name__ == "__main__":
        values = [
            (2, 3),
            (4, 5),
            (6, 7)
        ]

        with multiprocessing.Pool(3) as pool:
            results = pool.starmap(multiply, values)

        print("Results:", results)

Output:

    Results: [6, 20, 42]

---

# 🧠 `map()` vs `starmap()`

| Method | Use |
|---|---|
| `map()` | Function receives one item at a time |
| `starmap()` | Function receives multiple arguments unpacked from tuples |

Example:

    map()

    square(number)

    [1, 2, 3, 4]


    starmap()

    multiply(a, b)

    [(2, 3), (4, 5), (6, 7)]

---

# 🔹 `map_async()`

**`map_async()` performs a pool mapping operation asynchronously and returns an `AsyncResult` object instead of immediately waiting for all results.**

Example:

    import multiprocessing
    import time


    def square(number):
        time.sleep(1)
        return number * number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]

        with multiprocessing.Pool(3) as pool:
            result = pool.map_async(square, numbers)

            print("Tasks submitted")

            results = result.get()

        print("Results:", results)

Possible output:

    Tasks submitted
    Results: [1, 4, 9, 16, 25]

The important difference is that `map_async()` returns immediately with an asynchronous result object.

---

# 🧩 `AsyncResult`

The object returned by asynchronous pool methods is an `AsyncResult`.

Example:

    result = pool.map_async(square, numbers)

We can later retrieve the results:

    results = result.get()

`get()` waits until the computation is complete if the results are not ready yet.

---

# 🔹 `get()`

**`get()` retrieves the result of an asynchronous pool operation, waiting if necessary until the operation completes.**

Example:

    result = pool.map_async(square, numbers)

    print("Work submitted")

    results = result.get()

The flow is:

    Submit Task
        ↓
    Continue Program
        ↓
    AsyncResult
        ↓
    get()
        ↓
    Wait if necessary
        ↓
    Receive Results

---

# 🔹 `ready()`

**`ready()` checks whether an asynchronous pool operation has finished.**

Example:

    result = pool.map_async(square, numbers)

    print(result.ready())

    results = result.get()

Before completion, it may return:

    False

After completion:

    True

---

# 🔹 `successful()`

**`successful()` checks whether an asynchronous pool operation completed successfully without raising an exception.**

Example:

    result = pool.map_async(square, numbers)

    results = result.get()

    print(result.successful())

Possible output:

    True

It should be checked only after the asynchronous operation has completed.

---

# 📊 Synchronous vs Asynchronous Pool Methods

| Method | Behavior |
|---|---|
| `map()` | Waits for results |
| `map_async()` | Returns immediately with `AsyncResult` |
| `AsyncResult.get()` | Retrieves results |
| `AsyncResult.ready()` | Checks completion |
| `AsyncResult.successful()` | Checks successful completion |

---

# 🧠 Why Use `map_async()`?

Suppose we have other work to perform while the worker processes are calculating.

With:

    pool.map()

the calling code waits for the mapping operation.

With:

    pool.map_async()

we can submit the work and continue executing other code.

Conceptually:

    Main Process
         │
         ├── Submit tasks
         │
         ├── Continue other work
         │
         ├── Continue other work
         │
         └── get()
                ↓
           Receive results

This can be useful when the application has other work that can proceed while the processes are busy.

---

# 🧠 Process Pool vs Individual `Process`

| Feature | `Process` | `Pool` |
|---|---|---|
| Main purpose | Individual process control | Manage multiple worker processes |
| Best for | Specific independent process | Many similar tasks |
| Manual process creation | Yes | No |
| Worker management | Manual | Pool manages workers |
| Task distribution | Manual | Automatic |
| Scaling repeated tasks | More repetitive | Easier |
| Common methods | `start()`, `join()` | `map()`, `starmap()`, `map_async()` |

A simple way to remember:

    Process
       ↓
    "I want to control this process."


    Pool
       ↓
    "I have many tasks and want workers to handle them."

---

# 🚀 Pool Example with AI/Data Processing

Suppose an AI preprocessing pipeline has many images.

    images = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpg",
        "image4.jpg",
        "image5.jpg"
    ]

A CPU-heavy preprocessing function could be:

    def preprocess(image):
        # CPU-heavy image processing
        return processed_image

A process pool could distribute the images:

    with multiprocessing.Pool(4) as pool:
        results = pool.map(preprocess, images)

Conceptually:

    Images
       │
       ├── image1 → Worker 1
       ├── image2 → Worker 2
       ├── image3 → Worker 3
       ├── image4 → Worker 4
       │
       └── image5 → Worker becomes available

This type of architecture can be useful for independent preprocessing tasks.

---

# 🤖 Process Pool in AI Engineering

Process pools can be useful in AI Engineering when many independent CPU-heavy operations need to be performed.

Examples:

### 🖼️ Image Preprocessing

    Images
       ↓
    Process Pool
       ↓
    Resize / Transform / Normalize
       ↓
    Processed Images

### 📊 Dataset Processing

    Large Dataset
          ↓
    Split into chunks
          ↓
    Process Pool
          ↓
    Parallel preprocessing
          ↓
    Combined Dataset

### 📝 Text Preprocessing

For CPU-heavy preprocessing operations:

    Documents
        ↓
    Worker Processes
        ↓
    Clean / Transform / Process
        ↓
    Results

The exact benefit depends on the workload and the libraries being used.

---

# ⚠️ Important AI Engineering Note

Modern AI libraries such as:

- NumPy
- PyTorch
- TensorFlow
- OpenCV

may internally use optimized native code, multithreading, multiprocessing, or other parallelization mechanisms.

Therefore, we should not automatically wrap every AI operation in a Python process pool.

Sometimes the underlying library is already optimized for parallel execution.

The correct approach depends on the workload and library behavior.

---

# 🧠 Pool Size

Suppose:

    Pool(4)

This creates a pool with four worker processes.

The ideal number of workers depends on:

- Number of CPU cores
- Task complexity
- Memory usage
- Process overhead
- Other workloads running on the system

More workers do not automatically mean more performance.

For example:

    Pool(100)

could create unnecessary overhead on a system with limited CPU and memory resources.

---

# ⚠️ More Workers ≠ Always Faster

Suppose a system has limited CPU resources.

Creating too many processes can cause:

    Too many processes
          ↓
    More scheduling overhead
          ↓
    More memory usage
          ↓
    More context switching
          ↓
    Reduced efficiency

Therefore, the number of workers should be chosen based on the workload and system.

---

# 🧠 Important Pool Concepts

| Concept | Meaning |
|---|---|
| `Pool(n)` | Creates a pool with `n` worker processes |
| `map()` | Applies a function to every item |
| `starmap()` | Applies a function using multiple arguments |
| `map_async()` | Performs mapping asynchronously |
| `AsyncResult` | Represents the asynchronous operation |
| `get()` | Retrieves the asynchronous result |
| `ready()` | Checks whether operation is complete |
| `successful()` | Checks whether operation completed successfully |
| `close()` | Prevents new tasks from being submitted |
| `join()` | Waits for workers to finish |
| `terminate()` | Stops worker processes |

---

# 📌 Pool Workflow

The basic synchronous workflow is:

    Create Pool
        ↓
    Submit Tasks
        ↓
    Workers Execute
        ↓
    Results Returned
        ↓
    Pool Cleanup

Using `map()`:

    pool.map(function, data)
            ↓
       Process Tasks
            ↓
        Return List

Using `map_async()`:

    pool.map_async(function, data)
            ↓
       AsyncResult
            ↓
       Other Work
            ↓
       get()
            ↓
        Results

---

# 🧠 Key Takeaways

- A **Process Pool** is a collection of worker processes.
- It avoids manually creating every process.
- `Pool(n)` specifies the number of worker processes.
- `map()` distributes a function across an iterable.
- `map()` returns results in input order.
- Completion order and result order are different concepts.
- `starmap()` is useful when each task requires multiple arguments.
- `map_async()` performs pool mapping asynchronously.
- `AsyncResult` represents the asynchronous operation.
- `get()` retrieves the result.
- `ready()` checks whether the operation is complete.
- `successful()` checks whether the operation completed successfully.
- `close()` prevents new tasks from being submitted.
- `join()` waits for worker processes to finish.
- `terminate()` forcefully stops the pool.
- A context manager (`with Pool(...)`) simplifies resource management.
- Process pools are especially useful for many independent CPU-bound tasks.
- The number of workers should be chosen according to the workload and available system resources.
- In AI Engineering, process pools can be useful for CPU-heavy preprocessing and independent data-processing tasks.

---

# 🔚 Summary

The most important concept is:

    Individual Process

        Process 1
        Process 2
        Process 3


    Process Pool

        ┌─────────────────────────┐
        │       Worker Pool       │
        │                         │
        │ Worker 1                │
        │ Worker 2                │
        │ Worker 3                │
        └────────────┬────────────┘
                     ↓
                  Tasks

Instead of manually controlling every process, the pool manages a group of worker processes for us.

The most commonly used methods are:

    pool.map()
    pool.starmap()
    pool.map_async()

And for asynchronous results:

    result.get()
    result.ready()
    result.successful()

The next topic will focus on **`Queue`**, which is important for communication between separate processes.


# 🔟 Queue & Inter-Process Communication

## 🧩 What is a Multiprocessing Queue?

**A multiprocessing Queue is a process-safe data structure used to exchange data between multiple processes.**

Since separate processes normally have separate memory spaces, one process cannot simply access another process's ordinary variables.

A `Queue` provides a safe way for processes to send and receive data.

Conceptually:

    Process 1
        │
        │ put(data)
        ↓
    ┌───────────────┐
    │     Queue     │
    │               │
    │  Data 1       │
    │  Data 2       │
    │  Data 3       │
    └───────┬───────┘
            │
            │ get()
            ↓
       Process 2

This makes Queue an important **Inter-Process Communication (IPC)** mechanism.

---

# 📌 What is IPC?

**Inter-Process Communication (IPC) is a mechanism that allows separate processes to exchange data and coordinate their activities.**

Because processes have separate memory:

    Process 1
    ┌──────────────┐
    │ memory       │
    │ data = 100   │
    └──────────────┘

    Process 2
    ┌──────────────┐
    │ memory       │
    │ data = 200   │
    └──────────────┘

Changing `data` inside Process 1 does not automatically change `data` inside Process 2.

Therefore, processes need explicit communication mechanisms.

Examples of IPC include:

- Queue
- Pipe
- Shared memory
- Manager objects
- Files
- Other operating-system communication mechanisms

In this chapter, we focus primarily on **Queue**.

---

# 📦 Importing Queue

`Queue` is available inside Python's `multiprocessing` module.

We can write:

    import multiprocessing

and then:

    multiprocessing.Queue()

Or directly:

    from multiprocessing import Queue

For this chapter, we will use:

    from multiprocessing import Process, Queue

---

# 💻 Basic Queue Example

File:

    12_queue.py

    from multiprocessing import Process, Queue


    def producer(queue):
        queue.put("Hello from Process 1")


    def consumer(queue):
        message = queue.get()
        print("Received:", message)


    if __name__ == "__main__":
        queue = Queue()

        process1 = Process(
            target=producer,
            args=(queue,)
        )

        process2 = Process(
            target=consumer,
            args=(queue,)
        )

        process1.start()
        process2.start()

        process1.join()
        process2.join()

        print("Communication completed")

---

# 📤 Output

    Received: Hello from Process 1
    Communication completed

The producer process puts data into the queue:

    queue.put("Hello from Process 1")

The consumer process retrieves it:

    queue.get()

---

# 🧠 Producer and Consumer

The Queue pattern is commonly described using two roles.

### Producer

**A producer is a process that creates or sends data into a queue.**

Example:

    queue.put(data)

### Consumer

**A consumer is a process that retrieves and processes data from a queue.**

Example:

    data = queue.get()

Conceptually:

    Producer
       │
       │ put()
       ↓
    ┌─────────┐
    │  Queue  │
    └────┬────┘
         │
         │ get()
         ↓
    Consumer

This pattern is called the **Producer-Consumer Pattern**.

---

# 🔹 `put()`

**`put()` adds an item to the queue.**

Example:

    queue.put("Hello")

The value is placed into the queue so another process can retrieve it.

We can put different types of Python objects into the queue, provided they can be transferred between processes.

Examples:

    queue.put(100)

    queue.put("Python")

    queue.put([1, 2, 3])

    queue.put({"name": "Sonal"})

The object is transferred between processes using multiprocessing's underlying communication and serialization mechanisms.

---

# 🔹 `get()`

**`get()` retrieves an item from the queue.**

Example:

    data = queue.get()

If data is currently available, it is returned.

Example:

    queue.put("Hello")

    data = queue.get()

Now:

    data == "Hello"

---

# 🧠 FIFO Behavior

A standard Queue follows the **FIFO principle**.

FIFO means:

> **First In, First Out**

Suppose we add:

    queue.put("A")
    queue.put("B")
    queue.put("C")

The queue conceptually contains:

    ┌─────────────┐
    │ A           │ ← First
    │ B           │
    │ C           │ ← Last
    └─────────────┘

Retrieving values gives:

    get() → A
    get() → B
    get() → C

Therefore:

    First inserted
          ↓
       First out

This is similar to a real-world queue.

---

# 💻 FIFO Example

    from multiprocessing import Queue


    if __name__ == "__main__":
        queue = Queue()

        queue.put("Task 1")
        queue.put("Task 2")
        queue.put("Task 3")

        print(queue.get())
        print(queue.get())
        print(queue.get())

Output:

    Task 1
    Task 2
    Task 3

---

# 🔄 Queue Flow

The basic data flow is:

    Producer
       │
       │ put()
       ↓
    Queue
       │
       │ get()
       ↓
    Consumer

For multiple items:

    Producer
       │
       ├── put(Task 1)
       ├── put(Task 2)
       ├── put(Task 3)
       └── put(Task 4)
                ↓
            ┌─────────┐
            │  Queue  │
            └────┬────┘
                 ↓
            Consumer
                 │
                 ├── get() → Task 1
                 ├── get() → Task 2
                 ├── get() → Task 3
                 └── get() → Task 4

---

# 🧩 Multiple Items in a Queue

File:

    12_queue.py

Example:

    from multiprocessing import Process, Queue


    def producer(queue):
        for number in range(1, 6):
            queue.put(number)


    def consumer(queue):
        for _ in range(5):
            number = queue.get()
            print("Received:", number)


    if __name__ == "__main__":
        queue = Queue()

        process1 = Process(
            target=producer,
            args=(queue,)
        )

        process2 = Process(
            target=consumer,
            args=(queue,)
        )

        process1.start()
        process2.start()

        process1.join()
        process2.join()

        print("Communication completed")

Possible output:

    Received: 1
    Received: 2
    Received: 3
    Received: 4
    Received: 5
    Communication completed

The producer generates values and places them into the queue.

The consumer retrieves them one by one.

---

# 🧠 Why Does Queue Work Between Processes?

Normally:

    Process 1
       ↓
    Own Memory

    Process 2
       ↓
    Own Memory

They cannot simply share ordinary Python variables.

A multiprocessing Queue provides a communication channel managed by the multiprocessing system.

Conceptually:

    Process 1
        │
        │ Data
        ↓
    Queue Mechanism
        │
        │ Data
        ↓
    Process 2

The actual implementation involves inter-process communication and serialization behind the scenes.

---

# 🔐 Queue is Process-Safe

**A process-safe data structure is designed so that multiple processes can safely use it for communication without manually implementing low-level synchronization for every operation.**

`multiprocessing.Queue` is designed for communication between processes.

This means multiple processes can use the Queue without us manually protecting every `put()` and `get()` operation with a normal `threading.Lock`.

This is one of the main reasons Queue is useful for multiprocessing.

---

# 🔹 Blocking Behavior of `get()`

By default:

    queue.get()

can wait if there is currently no item available.

For example:

    data = queue.get()

If the producer has not yet placed anything into the queue, the consumer can wait until an item becomes available.

Conceptually:

    Consumer
       │
       ↓
    get()
       │
       ↓
    No data available
       │
       ↓
    Wait
       │
       ↓
    Producer puts data
       │
       ↓
    Consumer receives data

This behavior is useful in producer-consumer systems.

---

# 🔹 `get(timeout=...)`

We can specify a timeout.

Example:

    data = queue.get(timeout=2)

This means the operation can wait for up to approximately two seconds for an item.

If an item does not become available within the timeout period, an exception can be raised.

Example:

    from queue import Empty


    try:
        data = queue.get(timeout=2)
        print("Received:", data)

    except Empty:
        print("No data received")

This allows a consumer to avoid waiting indefinitely.

---

# 🔹 `put(timeout=...)`

A Queue can also have a limited capacity.

For example:

    queue = Queue(maxsize=2)

This means the queue can hold a limited number of items at a time.

A producer can use:

    queue.put(data, timeout=2)

If the queue is full, the producer may wait for space to become available.

---

# 🧠 Queue `maxsize`

Example:

    queue = Queue(maxsize=2)

Conceptually:

    ┌───────────────┐
    │ Queue         │
    │               │
    │ Item 1        │
    │ Item 2        │
    └───────────────┘

The queue is currently full.

A producer trying to add another item may need to wait until the consumer removes an item.

Flow:

    Queue Full
       ↓
    Producer waits
       ↓
    Consumer gets item
       ↓
    Space available
       ↓
    Producer puts new item

This provides a form of **backpressure**.

---

# 🧩 What is Backpressure?

**Backpressure is a mechanism where a producer slows down or waits when the consumer or communication system cannot process data quickly enough.**

Example:

    Producer
       │
       │ Fast
       ↓
    Queue
       │
       ↓
    Consumer
       │
       │ Slow
       ↓

If the producer keeps generating data faster than the consumer can process it, the queue can grow.

A bounded queue can prevent unlimited growth:

    Fast Producer
         ↓
    Limited Queue
         ↓
    Slow Consumer

When the queue becomes full, the producer may need to wait.

---

# 🔹 `empty()`

`empty()` can be used to check whether the queue appears to be empty.

Example:

    if queue.empty():
        print("Queue is empty")

However, there is an important concurrency warning.

In a multi-process environment, `empty()` should **not** be relied upon as a precise synchronization mechanism.

Why?

Because another process may change the queue immediately after the check.

For example:

    if not queue.empty():
        data = queue.get()

Between these two operations:

    empty()
       ↓
    get()

another process could consume the item.

Therefore, blocking `get()`, `get(timeout=...)`, or another explicit coordination mechanism is generally safer.

---

# ⚠️ Important `empty()` Lesson

Avoid relying on:

    if not queue.empty():
        data = queue.get()

for correctness in concurrent systems.

Prefer patterns such as:

    try:
        data = queue.get(timeout=2)

    except Empty:
        print("No data available")

This directly attempts to retrieve the item and handles the case where no item arrives.

---

# 🔹 `full()`

`full()` can indicate whether a queue appears to be full.

Example:

    if queue.full():
        print("Queue is full")

However, similar to `empty()`, its state can change immediately in a concurrent program.

Therefore, it should not be treated as a guaranteed synchronization mechanism.

---

# 📊 Important Queue Methods

| Method | Purpose |
|---|---|
| `put()` | Adds an item to the queue |
| `get()` | Retrieves an item |
| `empty()` | Checks whether queue appears empty |
| `full()` | Checks whether queue appears full |
| `close()` | Closes the queue's underlying resources |
| `join_thread()` | Waits for the queue's background thread to finish |

For normal producer-consumer programs, the most important methods are:

    put()
    get()

---

# 🔄 Multiple Producers and Consumers

A Queue can be used with multiple producers and consumers.

Conceptually:

    Producer 1 ──┐
                  │
    Producer 2 ──┼──→ Queue ──→ Consumer 1
                  │
    Producer 3 ──┘            └→ Consumer 2

This can be useful when:

- Multiple processes generate work
- Multiple workers process results
- Tasks arrive dynamically
- Work needs to be distributed

---

# 💻 Multiple Producers and Consumers

    from multiprocessing import Process, Queue
    import time


    def producer(queue, name):
        for number in range(3):
            item = f"{name} - Task {number}"
            queue.put(item)
            print("Produced:", item)
            time.sleep(0.5)


    def consumer(queue, name):
        for _ in range(3):
            item = queue.get()
            print(f"{name} received:", item)


    if __name__ == "__main__":
        queue = Queue()

        producer1 = Process(
            target=producer,
            args=(queue, "Producer 1")
        )

        producer2 = Process(
            target=producer,
            args=(queue, "Producer 2")
        )

        consumer1 = Process(
            target=consumer,
            args=(queue, "Consumer 1")
        )

        consumer2 = Process(
            target=consumer,
            args=(queue, "Consumer 2")
        )

        producer1.start()
        producer2.start()

        consumer1.start()
        consumer2.start()

        producer1.join()
        producer2.join()

        consumer1.join()
        consumer2.join()

        print("All processes completed")

The exact output order can vary because multiple processes are executing concurrently.

---

# 🧠 Sentinel Values

When a consumer waits for work indefinitely, we need a way to tell it:

> "There is no more work."

A common technique is a **sentinel value**.

A sentinel is a special value that represents a control message rather than normal data.

For example:

    None

can be used as a sentinel.

Conceptually:

    Task 1
    Task 2
    Task 3
    None
      ↑
    Stop signal

The consumer can do:

    while True:
        item = queue.get()

        if item is None:
            break

        process(item)

---

# 💻 Sentinel Example

    from multiprocessing import Process, Queue


    def producer(queue):
        for number in range(5):
            queue.put(number)

        queue.put(None)


    def consumer(queue):
        while True:
            item = queue.get()

            if item is None:
                break

            print("Processing:", item)


    if __name__ == "__main__":
        queue = Queue()

        producer_process = Process(
            target=producer,
            args=(queue,)
        )

        consumer_process = Process(
            target=consumer,
            args=(queue,)
        )

        producer_process.start()
        consumer_process.start()

        producer_process.join()
        consumer_process.join()

        print("Processing completed")

Possible output:

    Processing: 0
    Processing: 1
    Processing: 2
    Processing: 3
    Processing: 4
    Processing completed

The `None` value tells the consumer that the producer has finished sending tasks.

---

# ⚠️ Multiple Consumers and Sentinels

If multiple consumers are waiting for work, one sentinel may not be enough.

Suppose:

    Consumer 1
    Consumer 2
    Consumer 3

are all waiting.

If we send:

    None

only one consumer may receive it.

Therefore, a common pattern is to send one sentinel for each consumer:

    None
    None
    None

This allows every consumer to receive a stop signal.

---

# 🤖 Queue in AI Engineering

Queues are highly useful in AI systems where tasks need to be passed between workers.

For example:

    User Requests
          │
          ↓
       Queue
          │
     ┌────┼────┐
     ↓    ↓    ↓
   Worker Worker Worker
     │    │    │
     └────┼────┘
          ↓
       Results

This can be useful for:

- Image processing
- Document processing
- Data preprocessing
- Batch inference
- Background jobs
- AI pipelines
- CPU-heavy preprocessing

---

# 🖼️ Example: Image Processing Pipeline

Suppose users upload images.

A producer can add image paths to a queue:

    queue.put("image1.jpg")
    queue.put("image2.jpg")
    queue.put("image3.jpg")

Workers can retrieve them:

    image = queue.get()

and perform processing:

    Load Image
        ↓
    Resize
        ↓
    Normalize
        ↓
    Feature Processing
        ↓
    Store Result

Conceptually:

    Uploaded Images
          │
          ↓
        Queue
          │
     ┌────┼────┐
     ↓    ↓    ↓
   Worker Worker Worker
     │    │    │
     └────┼────┘
          ↓
       Results

---

# 🤖 Example: AI Data Processing Pipeline

A larger AI pipeline could look like:

    Raw Data
       │
       ↓
    Producer
       │
       ↓
    ┌─────────────┐
    │    Queue    │
    └──────┬──────┘
           │
       ┌───┼───┐
       ↓   ↓   ↓
     CPU  CPU  CPU
    Worker Worker Worker
       │   │   │
       └───┼───┘
           ↓
      Processed Data
           ↓
      Model Pipeline

The Queue acts as a communication and work-distribution mechanism.

---

# 🧠 Queue vs Shared Variables

### Shared Variable Approach

Processes have separate memory:

    Process 1
    counter = 100

    Process 2
    counter = 100

Changing one does not automatically change the other.

---

### Queue Approach

    Process 1
        │
        │ put(200)
        ↓
      Queue
        │
        │ get()
        ↓
    Process 2

The data is explicitly transferred.

This makes the communication model clearer and safer than pretending separate processes share ordinary variables.

---

# 🔄 Queue vs Threading Queue

Python has multiple Queue implementations.

For example:

    queue.Queue

is commonly used for communication between threads.

While:

    multiprocessing.Queue

is designed for communication between processes.

Conceptually:

    Threads
       ↓
    queue.Queue


    Processes
       ↓
    multiprocessing.Queue

Choosing the correct Queue implementation is important.

---

# 📊 Thread Queue vs Multiprocessing Queue

| Feature | `queue.Queue` | `multiprocessing.Queue` |
|---|---|---|
| Designed for | Threads | Processes |
| Shared memory context | Same process | Separate processes |
| Main purpose | Thread communication | Process communication |
| Common use | Thread worker pools | Multiprocessing workers |
| IPC | Not designed as process IPC | Yes |

---

# ⚠️ Queue and Serialization

When data moves between processes, it generally needs to be serialized so it can be transferred.

For many Python objects, multiprocessing uses **pickle** internally.

Conceptually:

    Python Object
         ↓
    Serialization
         ↓
    Transfer
         ↓
    Deserialization
         ↓
    Python Object

This means passing very large objects through a Queue can have significant overhead.

For example:

    Huge NumPy Array
          ↓
    Serialize
          ↓
    Transfer
          ↓
    Deserialize

This may become expensive.

Therefore, multiprocessing designs should consider the amount of data being transferred between processes.

---

# 🧠 Important Design Principle

Multiprocessing is most effective when:

    Large CPU Work
          ↓
    Separate Processes
          ↓
    Small / Reasonable Communication
          ↓
    Good Parallelism

If processes constantly exchange huge amounts of data:

    Process 1
       ↕
    Huge Data Transfer
       ↕
    Process 2

communication overhead may reduce the benefits of multiprocessing.

---

# 📌 Producer-Consumer Pattern

The Producer-Consumer pattern can be summarized as:

    ┌──────────────┐
    │   Producer   │
    └──────┬───────┘
           │
           │ put()
           ↓
    ┌──────────────┐
    │    Queue     │
    └──────┬───────┘
           │
           │ get()
           ↓
    ┌──────────────┐
    │   Consumer   │
    └──────────────┘

The producer creates work.

The queue stores and transfers work.

The consumer processes work.

This pattern appears in many real-world systems.

---

# 🧠 Real-World Analogy

Imagine a restaurant.

    Customer Orders
          ↓
       Queue
          ↓
       Kitchen
          ↓
       Workers

Customers generate orders.

The queue stores orders.

Workers process them.

The same basic architecture can be used in software:

    Requests
       ↓
    Task Queue
       ↓
    Worker Processes
       ↓
    Results

This is a fundamental pattern in backend and AI systems.

---

# 📊 Important Queue Concepts

| Concept | Meaning |
|---|---|
| Queue | Communication mechanism between processes |
| `put()` | Adds data |
| `get()` | Retrieves data |
| FIFO | First In, First Out |
| Producer | Creates/sends data |
| Consumer | Receives/processes data |
| `maxsize` | Limits queue capacity |
| Blocking | Operation waits until it can proceed |
| Timeout | Limits how long an operation waits |
| Sentinel | Special value used as a control signal |
| IPC | Communication between separate processes |
| Backpressure | Producer slows/waits when consumers cannot keep up |

---

# 🧠 Key Takeaways

- A multiprocessing Queue allows processes to communicate safely.
- Processes normally have separate memory spaces.
- Queue provides an explicit communication mechanism.
- `put()` adds an item.
- `get()` retrieves an item.
- Queue follows FIFO behavior.
- A producer puts data into a queue.
- A consumer retrieves data from a queue.
- `Queue(maxsize=n)` can limit queue capacity.
- Blocking operations can wait until space or data becomes available.
- `timeout` can prevent indefinite waiting.
- `empty()` and `full()` should not be treated as precise synchronization mechanisms in concurrent systems.
- Sentinel values can be used to tell consumers to stop.
- Multiple consumers may require multiple sentinel values.
- Multiprocessing Queue is different from `queue.Queue`, which is commonly used for threads.
- Moving large objects between processes can introduce serialization and communication overhead.
- Queues are useful for AI pipelines, data processing, image processing, background jobs, and worker architectures.

---

# 🔚 Summary

The central idea is:

    Separate Processes
          │
          │ Cannot directly share
          │ ordinary variables
          ↓
    Inter-Process Communication
          │
          ↓
        Queue
          │
     ┌────┴────┐
     ↓         ↓
   put()      get()
     ↓         ↓
  Producer → Consumer

The most important Queue operations are:

    queue.put(data)

    queue.get()

The Producer-Consumer pattern is:

    Producer
       ↓
     Queue
       ↓
    Consumer

And in AI Engineering:

    Requests / Data
          ↓
        Queue
          ↓
    Worker Processes
          ↓
      Processing
          ↓
       Results

With `Process`, `Pool`, and `Queue`, we now have the basic building blocks of Python's process-based concurrency.

The next section moves to **`concurrent.futures`**, which provides a higher-level and often simpler interface for working with threads and processes.


# 1️⃣1️⃣ `concurrent.futures`

## 🧩 What is `concurrent.futures`?

**`concurrent.futures` is a high-level Python module that provides a simple interface for executing tasks concurrently using threads or processes.**

It makes concurrent programming easier by providing ready-made executor classes instead of requiring us to manually manage every thread or process.

The two main executors are:

    concurrent.futures
          │
          ├── ThreadPoolExecutor
          │       ↓
          │     Threads
          │
          └── ProcessPoolExecutor
                  ↓
                Processes

---

# 🎯 Why Do We Need `concurrent.futures`?

Earlier, we learned how to manually create processes:

    Process(...)
        ↓
    start()
        ↓
    join()

For multiple tasks, this can become repetitive.

For example:

    process1 = Process(...)
    process2 = Process(...)
    process3 = Process(...)
    process4 = Process(...)

Then:

    process1.start()
    process2.start()
    process3.start()
    process4.start()

And finally:

    process1.join()
    process2.join()
    process3.join()
    process4.join()

`concurrent.futures` provides a higher-level abstraction.

Instead of manually managing every worker, we can create an **Executor**.

Conceptually:

    Executor
       │
       ├── Worker 1
       ├── Worker 2
       └── Worker 3
              ↓
            Tasks

The executor manages the workers and task scheduling for us.

---

# 🧠 What is an Executor?

**An Executor is an object that manages a pool of workers and schedules submitted tasks for execution.**

Python provides two major executor implementations:

    Executor
       │
       ├── ThreadPoolExecutor
       │
       └── ProcessPoolExecutor

The main idea is:

    Submit Task
         ↓
      Executor
         ↓
    Worker Executes
         ↓
      Get Result

---

# 📦 Importing `concurrent.futures`

We can import the required executor directly:

    from concurrent.futures import ProcessPoolExecutor

or:

    from concurrent.futures import ThreadPoolExecutor

We can also import both:

    from concurrent.futures import (
        ThreadPoolExecutor,
        ProcessPoolExecutor
    )

---

# 🔹 `ProcessPoolExecutor`

**`ProcessPoolExecutor` is a high-level executor that manages a pool of worker processes for executing tasks concurrently.**

It is commonly useful for CPU-bound workloads.

Conceptually:

    ProcessPoolExecutor
          │
          ├── Process 1
          ├── Process 2
          └── Process 3
                  ↓
                Tasks

It provides a simpler interface compared with manually creating multiple `multiprocessing.Process` objects.

---

# 💻 Basic `ProcessPoolExecutor` Example

File:

    13_concurrent_futures.py

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        print(f"Calculating {number}")

        time.sleep(1)

        return number * number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]

        with ProcessPoolExecutor(max_workers=3) as executor:
            results = executor.map(calculate, numbers)

        print("Results:", list(results))

---

# 📤 Output

Possible output:

    Calculating 1
    Calculating 2
    Calculating 3
    Calculating 4
    Calculating 5
    Results: [1, 4, 9, 16, 25]

The order of the `Calculating...` messages may vary.

However, `executor.map()` returns results according to the input order.

---

# 🔍 Understanding `ProcessPoolExecutor`

This line:

    ProcessPoolExecutor(max_workers=3)

creates an executor that manages up to three worker processes.

Conceptually:

    ProcessPoolExecutor
          │
          ├── Worker Process 1
          ├── Worker Process 2
          └── Worker Process 3

Tasks are submitted to the executor.

The executor decides how those tasks are distributed among workers.

---

# 🔹 `max_workers`

**`max_workers` specifies the maximum number of worker threads or processes that the executor can use.**

Example:

    ProcessPoolExecutor(max_workers=3)

means that up to three worker processes can execute tasks concurrently.

Suppose we have:

    numbers = [1, 2, 3, 4, 5]

and:

    max_workers=3

Conceptually:

    Worker 1 → Task 1
    Worker 2 → Task 2
    Worker 3 → Task 3

When a worker becomes available:

    Worker 1 → Task 4
    Worker 2 → Task 5

The executor manages this scheduling automatically.

---

# 🧠 Why Use `with`?

We commonly write:

    with ProcessPoolExecutor(max_workers=3) as executor:
        ...

The `with` statement automatically manages the executor's lifecycle.

Conceptually:

    Create Executor
          ↓
    Submit Tasks
          ↓
    Execute Tasks
          ↓
    Finish Work
          ↓
    Executor Cleanup

This is safer and cleaner than manually managing the executor's shutdown.

---

# 🔹 `executor.map()`

**`executor.map()` applies a function to each item in an iterable and schedules those tasks using the executor's workers.**

Example:

    numbers = [1, 2, 3, 4, 5]

    results = executor.map(calculate, numbers)

Conceptually:

    calculate(1)
    calculate(2)
    calculate(3)
    calculate(4)
    calculate(5)

The executor manages the worker processes.

---

# 🧠 `map()` Result Order

Like `multiprocessing.Pool.map()`, `executor.map()` returns results corresponding to the input order.

Input:

    [1, 2, 3, 4, 5]

Output:

    [1, 4, 9, 16, 25]

Even if the actual tasks finish in a different order, the results are yielded according to their input ordering.

This is important when processing multiple tasks concurrently.

---

# 🔄 Completion Order vs Result Order

Suppose:

    Task 1 → takes 3 seconds
    Task 2 → takes 1 second
    Task 3 → takes 2 seconds

Actual completion may be:

    Task 2
       ↓
    Task 3
       ↓
    Task 1

But `executor.map()` can still provide results according to:

    Task 1
    Task 2
    Task 3

Therefore:

    Execution order ≠ Result order

This is an important concurrency concept.

---

# 🧩 `ThreadPoolExecutor`

**`ThreadPoolExecutor` is a high-level executor that manages a pool of worker threads for executing tasks concurrently.**

It is especially useful for I/O-bound workloads.

Conceptually:

    ThreadPoolExecutor
          │
          ├── Thread 1
          ├── Thread 2
          └── Thread 3
                  ↓
                Tasks

Example use cases:

- API requests
- Network operations
- File operations
- Database operations
- Web requests

---

# 💻 Basic `ThreadPoolExecutor` Example

    from concurrent.futures import ThreadPoolExecutor
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")

        return f"{name} result"


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:
            results = executor.map(
                task,
                ["Task 1", "Task 2", "Task 3"]
            )

        print("Results:", list(results))

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 1 completed
    Task 3 completed
    Task 2 completed
    Results: ['Task 1 result', 'Task 2 result', 'Task 3 result']

The completion order may vary.

---

# 📊 `ThreadPoolExecutor` vs `ProcessPoolExecutor`

| Feature | `ThreadPoolExecutor` | `ProcessPoolExecutor` |
|---|---|---|
| Worker type | Threads | Processes |
| Memory | Shared within process | Separate |
| Common workload | I/O-bound | CPU-bound |
| GIL impact | Relevant for pure-Python CPU work | Separate processes avoid single-process GIL limitation |
| Communication | Easier through shared memory | Requires process communication mechanisms |
| Overhead | Generally lower | Generally higher |
| Isolation | Lower | Higher |

A practical rule:

    I/O-bound
       ↓
    ThreadPoolExecutor


    CPU-bound
       ↓
    ProcessPoolExecutor

This is a guideline rather than an absolute rule.

---

# 🧠 One Interface, Two Execution Models

One major advantage of `concurrent.futures` is that the overall programming style is similar.

Thread version:

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(function, data)

Process version:

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(function, data)

The main difference is the type of worker.

    ThreadPoolExecutor
          ↓
       Threads


    ProcessPoolExecutor
          ↓
       Processes

This makes it easier to switch concurrency strategies when the workload changes.

---

# 🔹 `submit()`

**`submit()` schedules a single callable for execution and immediately returns a `Future` object representing that task.**

Example:

    future = executor.submit(calculate, 5)

Here:

    calculate(5)

is submitted to the executor.

The executor can execute it using one of its workers.

Instead of immediately receiving:

    25

we receive:

    Future

The Future represents the eventual result.

---

# 🧠 What is a `Future`?

**A `Future` represents the result of a task that has been submitted for execution and may still be running or may complete later.**

Conceptually:

    submit(task)
         ↓
       Future
         │
         ├── Task Running
         │
         ├── Task Completed
         │
         └── Result Available

The Future acts as a handle through which we can inspect or retrieve the task's result.

---

# 💻 `submit()` Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=2) as executor:

            future = executor.submit(calculate, 5)

            print("Task submitted")

            result = future.result()

            print("Result:", result)

Possible output:

    Task submitted
    Result: 25

The important point is that:

    executor.submit(...)

returns immediately with a Future.

---

# 🔹 `future.result()`

**`Future.result()` returns the result of the submitted task, waiting for the task to finish if necessary.**

Example:

    future = executor.submit(calculate, 5)

    result = future.result()

If the calculation has already completed:

    result = 25

If it is still running:

    future.result()

waits until the result becomes available.

Conceptually:

    Future
      │
      ↓
    result()
      │
      ├── Result ready → return result
      │
      └── Still running → wait
                         ↓
                       result

---

# 🔹 `future.done()`

**`Future.done()` checks whether the submitted task has finished executing.**

Example:

    future = executor.submit(calculate, 5)

    print("Task completed:", future.done())

Possible output:

    Task completed: False

After waiting for the result:

    result = future.result()

    print("Task completed:", future.done())

Output:

    Task completed: True

Therefore:

    done() → Status check

while:

    result() → Retrieve result

---

# 🧠 `done()` vs `result()`

This distinction is very important.

### `done()`

Checks:

> Has the task finished?

Returns:

    True
    False

### `result()`

Asks:

> Give me the task's result.

It may wait if the task is still running.

Therefore:

    future.done()
        ↓
    Status


    future.result()
        ↓
    Result

---

# 🔹 `future.running()`

**`Future.running()` checks whether the task is currently being executed by a worker.**

Example:

    future = executor.submit(calculate, 5)

    print(future.running())

Depending on timing, it may return:

    True

while the task is actively executing.

A Future generally moves through states such as:

    Pending
       ↓
    Running
       ↓
    Finished

---

# 🔹 `future.cancel()`

**`Future.cancel()` attempts to cancel a task that has not started executing.**

Example:

    future = executor.submit(calculate, 5)

    cancelled = future.cancel()

    print(cancelled)

It returns:

    True

if the task was successfully cancelled.

If the task is already running, cancellation normally cannot stop that running function through `Future.cancel()`.

Therefore:

    Not started
         ↓
      cancel()
         ↓
      Can cancel


    Already running
         ↓
      cancel()
         ↓
    Usually cannot cancel

---

# 🧠 Future Lifecycle

A simplified Future lifecycle is:

    submit()
       ↓
    Future Created
       ↓
    Pending
       ↓
    Running
       ↓
    Completed
       ↓
    result()

Possible alternative:

    submit()
       ↓
    Pending
       ↓
    cancel()
       ↓
    Cancelled

---

# 🔹 `future.exception()`

**`Future.exception()` returns the exception raised by the task, if one occurred.**

Example:

    future = executor.submit(function)

    result = future.exception()

If the task completed successfully:

    None

If the task raised an exception:

    ValueError(...)
    
This can be useful for inspecting task failures.

---

# ⚠️ Exception Handling with `Future.result()`

Suppose:

    from concurrent.futures import ProcessPoolExecutor


    def divide(a, b):
        return a / b


    if __name__ == "__main__":
        with ProcessPoolExecutor() as executor:
            future = executor.submit(divide, 10, 0)

            try:
                result = future.result()
                print(result)

            except ZeroDivisionError as error:
                print("Error:", error)

The exception raised by the worker can be observed when retrieving the result.

Possible output:

    Error: division by zero

This is one reason `Future` is useful: task execution and result retrieval are separated.

---

# 🧩 Multiple Futures

We can submit multiple tasks:

    future1 = executor.submit(calculate, 2)
    future2 = executor.submit(calculate, 3)
    future3 = executor.submit(calculate, 4)

Then retrieve their results:

    result1 = future1.result()
    result2 = future2.result()
    result3 = future3.result()

Conceptually:

    submit(Task 1) → Future 1
    submit(Task 2) → Future 2
    submit(Task 3) → Future 3

          ↓

    Workers execute tasks

          ↓

    Future 1 → Result 1
    Future 2 → Result 2
    Future 3 → Result 3

---

# 💻 Multiple Futures Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=3) as executor:

            future1 = executor.submit(calculate, 2)
            future2 = executor.submit(calculate, 3)
            future3 = executor.submit(calculate, 4)

            print("All tasks submitted")

            result1 = future1.result()
            result2 = future2.result()
            result3 = future3.result()

            print("Results:")
            print(result1)
            print(result2)
            print(result3)

Output:

    All tasks submitted
    Results:
    4
    9
    16

The tasks can execute concurrently while the main program holds the Future objects.

---

# 🧠 `map()` vs `submit()`

This is an important distinction.

### `map()`

Best when:

- You have a collection of inputs.
- The same function should be applied to every input.
- You want a simple interface.

Example:

    results = executor.map(calculate, numbers)

### `submit()`

Best when:

- You want individual control over tasks.
- Tasks may have different arguments.
- You need individual Future objects.
- You want to inspect task status.
- You need individual exception handling.

Example:

    future = executor.submit(calculate, 5)

---

# 📊 `map()` vs `submit()`

| Feature | `map()` | `submit()` |
|---|---|---|
| Multiple inputs | Excellent | Possible |
| Individual Future | Not directly exposed in the same way | Yes |
| Task status | Less direct | `Future` methods |
| Individual cancellation | Not the main interface | Possible before execution |
| Simple repeated tasks | Excellent | More verbose |
| Fine-grained control | Lower | Higher |
| Result retrieval | Iterator | `future.result()` |

---

# 🧠 Executor Workflow

A common `concurrent.futures` workflow is:

    Create Executor
          ↓
    Submit Tasks
          ↓
    Executor schedules work
          ↓
    Workers execute
          ↓
    Future represents task
          ↓
    Retrieve result
          ↓
    Executor shuts down

With `map()`:

    Executor
       ↓
    map(function, data)
       ↓
    Workers
       ↓
    Results

With `submit()`:

    Executor
       ↓
    submit()
       ↓
    Future
       ↓
    result()

---

# 🔐 Executor Cleanup

When using:

    with ProcessPoolExecutor(...) as executor:

the executor is automatically shut down when the `with` block ends.

This is similar to the resource-management patterns we have already seen.

Conceptually:

    with Executor:
        work
    ↓
    Shutdown / Cleanup

This helps prevent worker resources from being left active unnecessarily.

---

# 🧩 Manual Shutdown

An executor also provides:

    executor.shutdown()

This tells the executor to shut down after handling its work according to the shutdown configuration.

In normal code, using:

    with ...

is often simpler and safer.

---

# 🤖 `concurrent.futures` in AI Engineering

`concurrent.futures` is particularly useful in AI Engineering because AI applications often have multiple independent operations.

For example:

    AI Application
         │
         ├── API Request
         ├── File Processing
         ├── Database Query
         └── CPU Processing

Different tasks may require different concurrency approaches.

---

# 🌐 Example: Parallel API-like Tasks

For I/O-bound operations, `ThreadPoolExecutor` can be useful.

Conceptually:

    User Request
         │
         ├── API 1 ──→ Thread 1
         ├── API 2 ──→ Thread 2
         └── API 3 ──→ Thread 3

The threads can spend their waiting time independently.

---

# 🧮 Example: CPU-heavy AI Preprocessing

For CPU-bound work, `ProcessPoolExecutor` can be useful.

Conceptually:

    Dataset
       │
       ├── Chunk 1 → Process 1
       ├── Chunk 2 → Process 2
       ├── Chunk 3 → Process 3
       └── Chunk 4 → Process 4

Each worker can perform CPU-heavy preprocessing.

---

# 🤖 AI Assistant Example

Imagine an AI assistant needs to process several independent sources:

    User Query
         │
         ├── Web Search
         ├── Database Search
         ├── File Search
         └── API Request

If these are I/O-bound operations, a ThreadPoolExecutor could allow multiple operations to be in progress concurrently.

Conceptually:

    User Query
         │
         ↓
    ThreadPoolExecutor
         │
    ┌────┼────┬────┐
    ↓    ↓    ↓    ↓
   Web  DB   File API
    │    │    │    │
    └────┴────┴────┘
         ↓
    Collect Results
         ↓
      AI Response

Later in this chapter, we will see `asyncio`, which provides another approach particularly suited to large numbers of asynchronous I/O operations.

---

# 📊 Complete `concurrent.futures` Comparison

| Tool | Worker | Common Use |
|---|---|---|
| `ThreadPoolExecutor` | Threads | I/O-bound tasks |
| `ProcessPoolExecutor` | Processes | CPU-bound tasks |
| `executor.map()` | Workers | Apply function to many inputs |
| `executor.submit()` | Workers | Submit individual task |
| `Future` | Task handle | Track future result |
| `future.result()` | — | Retrieve result |
| `future.done()` | — | Check completion |
| `future.running()` | — | Check running state |
| `future.cancel()` | — | Attempt cancellation |
| `future.exception()` | — | Inspect task exception |

---

# 🧠 Why `concurrent.futures` is Important

Before learning `concurrent.futures`, we had to think directly about:

    Process
    start()
    join()
    Pool
    Queue

With `concurrent.futures`, we get a higher-level interface:

    Executor
       ↓
    Submit Tasks
       ↓
    Future
       ↓
    Get Results

This abstraction makes many concurrent programs easier to read and maintain.

---

# ⚠️ Important Limitation

`concurrent.futures` does not automatically make every program faster.

Performance still depends on:

- Task type
- CPU resources
- Number of workers
- Task size
- I/O latency
- Data transfer overhead
- Serialization overhead
- Operating system
- External service speed

Concurrency is a tool, not a guarantee of better performance.

---

# 🧠 Practical Decision Guide

Ask:

    What kind of task am I running?
              │
       ┌──────┴──────┐
       ↓             ↓
    I/O-bound     CPU-bound
       │             │
       ↓             ↓
    Threads       Processes
       │             │
       ↓             ↓
 ThreadPool      ProcessPool
 Executor        Executor

For large numbers of asynchronous I/O operations, `asyncio` may also be a strong option.

---

# 🤖 AI Engineer Perspective

For an AI Engineer, the important thing is not memorizing every API.

The important skill is understanding:

> **What is the workload, and which concurrency model fits it?**

Examples:

    API Requests
        ↓
    I/O-bound
        ↓
    ThreadPoolExecutor / asyncio


    Heavy Preprocessing
        ↓
    CPU-bound
        ↓
    ProcessPoolExecutor


    Many Independent Tasks
        ↓
    Executor
        ↓
    Workers
        ↓
    Futures / Results

This decision-making becomes useful when building real AI applications.

---

# 🧠 Key Takeaways

- `concurrent.futures` provides a high-level interface for concurrent execution.
- An `Executor` manages worker threads or processes.
- `ThreadPoolExecutor` manages worker threads.
- `ProcessPoolExecutor` manages worker processes.
- `max_workers` controls the maximum number of workers.
- `executor.map()` applies a function to multiple inputs.
- `executor.submit()` schedules an individual task.
- `submit()` returns a `Future`.
- A `Future` represents the eventual result of a submitted task.
- `future.result()` retrieves the result and may wait for completion.
- `future.done()` checks whether the task has finished.
- `future.running()` checks whether the task is currently running.
- `future.cancel()` attempts to cancel a task that has not started.
- `future.exception()` can be used to inspect task exceptions.
- `map()` is convenient for applying one function to many inputs.
- `submit()` provides more fine-grained control over individual tasks.
- `ThreadPoolExecutor` is commonly useful for I/O-bound workloads.
- `ProcessPoolExecutor` is commonly useful for CPU-bound workloads.
- Using `with` automatically handles executor cleanup.
- Concurrency does not automatically guarantee better performance.

---

# 🔚 Summary

The central abstraction is:

    concurrent.futures
           │
           ↓
       Executor
           │
      ┌────┴────┐
      ↓         ↓
   Threads   Processes
      ↓         ↓
 ThreadPool  ProcessPool
 Executor    Executor

Tasks can be submitted using:

    executor.submit()

which returns:

    Future

The Future can then be inspected using:

    future.done()
    future.running()
    future.cancel()
    future.exception()

and its result can be retrieved using:

    future.result()

For collections of similar tasks:

    executor.map()

provides a simpler approach.

The next topic will focus specifically on **`Future`**, including its lifecycle, state checking, result retrieval, exceptions, and practical examples.


# 1️⃣2️⃣ `Future`

## 🧩 What is a `Future`?

**A `Future` represents the result of a task that has been submitted for execution and may still be running or may complete later.**

A `Future` does not directly contain the final result when it is created.

Instead, it acts as a handle through which we can:

- Check whether a task is completed
- Check whether a task is running
- Retrieve its result
- Check for exceptions
- Attempt cancellation

Conceptually:

    Submit Task
         ↓
       Future
         │
         ├── Pending
         ├── Running
         ├── Completed
         └── Failed / Cancelled
                  ↓
              Get Result

---

# 🎯 Why Do We Need `Future`?

Consider this:

    future = executor.submit(task)

The task may take some time to complete.

Instead of forcing the main program to immediately wait, Python gives us a `Future` object.

The program can continue doing other work.

Conceptually:

    Main Program
         │
         ├── Submit Task
         │       ↓
         │     Future
         │
         ├── Continue Other Work
         │
         ├── Continue Other Work
         │
         └── Get Result
                 ↓
              Future

This is one of the important ideas behind asynchronous task management.

---

# 🧠 Future as a Task Handle

Think of a `Future` as a **reference to a task's eventual result**.

For example:

    future = executor.submit(calculate, 5)

Here:

    calculate(5)

is the actual task.

The variable:

    future

represents that task's future outcome.

It does not mean:

    future = 25

Instead:

    future → Task → Eventually produces 25

---

# 💻 Basic Future Example

File:

    13_concurrent_futures.py

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=2) as executor:

            future = executor.submit(calculate, 5)

            print("Task submitted")

            result = future.result()

            print("Result:", result)

Possible output:

    Task submitted
    Result: 25

The important point is:

    submit()
       ↓
    Future
       ↓
    result()
       ↓
    25

---

# 🔹 `submit()`

**`submit()` schedules a callable for execution and returns a `Future` object representing that task.**

Syntax:

    future = executor.submit(function, arguments)

Example:

    future = executor.submit(calculate, 5)

This means:

    calculate(5)

is submitted to the executor.

The executor decides when and where the task executes.

---

# 🧠 `submit()` Does Not Mean "Result Immediately"

Consider:

    future = executor.submit(calculate, 5)

At this moment:

    calculate(5)

may be:

- Waiting to start
- Already running
- Already completed

The `Future` allows us to interact with the task regardless of its current state.

---

# 🔄 Future Lifecycle

A simplified lifecycle is:

    submit()
       ↓
    Future Created
       ↓
    Pending
       ↓
    Running
       ↓
    Completed
       ↓
    Result Available

There can also be another path:

    submit()
       ↓
    Future Created
       ↓
    Pending
       ↓
    Cancelled

Or:

    submit()
       ↓
    Future Created
       ↓
    Running
       ↓
    Exception
       ↓
    Failed

---

# 📊 Future States

A Future can conceptually be in different states:

| State | Meaning |
|---|---|
| Pending | Task has been submitted but has not started |
| Running | Task is currently executing |
| Completed | Task finished successfully |
| Failed | Task finished with an exception |
| Cancelled | Task was cancelled before execution |

These states help us understand what is happening with a submitted task.

---

# 🔹 `future.done()`

**`Future.done()` returns `True` if the submitted task has finished executing; otherwise, it returns `False`.**

Example:

    future = executor.submit(calculate, 5)

    print("Task completed:", future.done())

Possible output:

    Task completed: False

The task may still be running.

After waiting for the result:

    result = future.result()

    print("Task completed:", future.done())

Output:

    Task completed: True

---

# 🧠 Understanding `done()`

Suppose the task takes 2 seconds.

Immediately after submission:

    submit()
       ↓
    done()
       ↓
    False

While the task is still running:

    Running
       ↓
    done()
       ↓
    False

After completion:

    Completed
       ↓
    done()
       ↓
    True

Therefore:

    done() → Status Check

It does not return the actual result.

---

# 🔹 `future.result()`

**`Future.result()` returns the result produced by the submitted task, waiting for completion if necessary.**

Example:

    result = future.result()

If the task returns:

    return 25

then:

    result

will contain:

    25

---

# 🧠 `done()` vs `result()`

This distinction is extremely important.

### `done()`

Answers:

> Has the task finished?

Example:

    future.done()

Result:

    True
    False

### `result()`

Answers:

> What did the task return?

Example:

    future.result()

Result:

    25

Therefore:

    future.done()
        ↓
    Status


    future.result()
        ↓
    Actual Result

---

# ⚠️ `result()` Can Wait

Suppose:

    future = executor.submit(calculate, 5)

and `calculate()` takes 5 seconds.

If we immediately write:

    result = future.result()

the main program may wait until the task finishes.

Conceptually:

    future.result()
          ↓
    Task still running?
          │
         YES
          ↓
        Wait
          ↓
    Task completed
          ↓
      Return result

Therefore, `result()` is not simply a status check.

---

# 💻 Future Status Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=1) as executor:

            future = executor.submit(calculate, 5)

            print("Task completed:", future.done())

            result = future.result()

            print("Result:", result)
            print("Task completed:", future.done())

Possible output:

    Task completed: False
    Result: 25
    Task completed: True

This is one of the most useful examples for understanding Future.

---

# 🔹 `future.running()`

**`Future.running()` returns `True` if the task is currently being executed and `False` otherwise.**

Example:

    future = executor.submit(calculate, 5)

    print("Running:", future.running())

Depending on timing, the result may be:

    True

or:

    False

because the task may not have started yet or may have already finished.

---

# 🧠 `done()` vs `running()`

These methods answer different questions.

### `running()`

> Is the task currently executing?

### `done()`

> Has the task finished?

Possible state:

    Pending

    running() → False
    done()    → False


    Running

    running() → True
    done()    → False


    Completed

    running() → False
    done()    → True

Conceptually:

    Pending
       ↓
    Running
       ↓
    Completed

---

# 📊 Future State Table

| State | `running()` | `done()` |
|---|---:|---:|
| Pending | False | False |
| Running | True | False |
| Completed | False | True |
| Failed | False | True |
| Cancelled | False | True |

This table is useful for understanding the Future lifecycle.

---

# 🔹 `future.cancel()`

**`Future.cancel()` attempts to cancel a task if it has not started executing.**

Example:

    future = executor.submit(calculate, 5)

    cancelled = future.cancel()

    print("Cancelled:", cancelled)

Possible output:

    Cancelled: True

if the task had not started yet.

---

# ⚠️ Important Cancellation Rule

A running task normally cannot be cancelled using:

    future.cancel()

For example:

    Task
      ↓
    Running
      ↓
    cancel()
      ↓
    Usually False

If the task is still waiting to start:

    Pending
      ↓
    cancel()
      ↓
    True

Therefore, cancellation works primarily before execution begins.

---

# 🔹 `future.cancelled()`

**`Future.cancelled()` returns `True` if the task was successfully cancelled.**

Example:

    if future.cancelled():
        print("Task was cancelled")

Otherwise:

    False

This is different from:

    future.done()

A cancelled Future is also considered done, but `done()` only tells us that it has reached a terminal state; `cancelled()` tells us specifically that cancellation occurred.

---

# 🧠 `done()` vs `cancelled()`

Example:

    future.done()

means:

> Has the Future finished its lifecycle?

While:

    future.cancelled()

means:

> Was the Future cancelled?

Possible state:

    Cancelled

    done()       → True
    cancelled()  → True

Successful completion:

    Completed

    done()       → True
    cancelled()  → False

---

# 🔹 `future.exception()`

**`Future.exception()` returns the exception raised by the task, if the task failed.**

Suppose:

    def divide(a, b):
        return a / b

and:

    future = executor.submit(divide, 10, 0)

The task raises:

    ZeroDivisionError

We can inspect the exception:

    error = future.exception()

Then:

    print(error)

Possible output:

    division by zero

If the task completed successfully:

    future.exception()

returns:

    None

---

# 💻 Exception Example

    from concurrent.futures import ProcessPoolExecutor


    def divide(a, b):
        return a / b


    if __name__ == "__main__":
        with ProcessPoolExecutor() as executor:

            future = executor.submit(divide, 10, 0)

            error = future.exception()

            print("Exception:", error)

Possible output:

    Exception: division by zero

The exact displayed message can vary slightly by Python version and context.

---

# 🔹 Exception Through `result()`

We can also handle the exception using `result()`.

Example:

    from concurrent.futures import ProcessPoolExecutor


    def divide(a, b):
        return a / b


    if __name__ == "__main__":
        with ProcessPoolExecutor() as executor:

            future = executor.submit(divide, 10, 0)

            try:
                result = future.result()
                print("Result:", result)

            except ZeroDivisionError as error:
                print("Error:", error)

Output:

    Error: division by zero

This approach is often useful because it directly handles the failure when retrieving the task's result.

---

# 🧠 `exception()` vs `result()`

| Method | Purpose |
|---|---|
| `result()` | Retrieves the returned value; raises the task's exception if it failed |
| `exception()` | Retrieves the exception object, or `None` if no exception occurred |

Example:

    future.result()

means:

> Give me the successful result, or raise the task's exception.

While:

    future.exception()

means:

> Tell me whether the task produced an exception.

---

# 🔹 Multiple Futures

One of the major benefits of `Future` is that we can manage multiple submitted tasks individually.

Example:

    future1 = executor.submit(calculate, 2)
    future2 = executor.submit(calculate, 3)
    future3 = executor.submit(calculate, 4)

Now we have:

    Future 1 → calculate(2)
    Future 2 → calculate(3)
    Future 3 → calculate(4)

Each Future can be inspected separately.

---

# 💻 Multiple Futures Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=3) as executor:

            future1 = executor.submit(calculate, 2)
            future2 = executor.submit(calculate, 3)
            future3 = executor.submit(calculate, 4)

            print("All tasks submitted")

            print("Task 1 completed:", future1.done())
            print("Task 2 completed:", future2.done())
            print("Task 3 completed:", future3.done())

            result1 = future1.result()
            result2 = future2.result()
            result3 = future3.result()

            print("Results:")
            print(result1)
            print(result2)
            print(result3)

Possible output:

    All tasks submitted
    Task 1 completed: False
    Task 2 completed: False
    Task 3 completed: False
    Results:
    4
    9
    16

The exact status values can vary depending on timing.

---

# 🧠 Why Multiple Futures Are Useful

Suppose an application has several independent tasks:

    Task 1 → Web processing
    Task 2 → Data processing
    Task 3 → File processing

Instead of waiting for each task before submitting the next one:

    Submit Task 1
         ↓
      Wait
         ↓
    Submit Task 2
         ↓
      Wait
         ↓
    Submit Task 3

we can submit all of them:

    Submit Task 1 → Future 1
    Submit Task 2 → Future 2
    Submit Task 3 → Future 3

Then monitor or retrieve them later.

This allows the executor to manage concurrent execution.

---

# 🔄 Future-Based Workflow

    Task 1 ──→ Future 1 ──→ Result 1
    Task 2 ──→ Future 2 ──→ Result 2
    Task 3 ──→ Future 3 ──→ Result 3

Each Future represents one submitted task.

---

# 🧩 Different Completion Times

Suppose:

    Task 1 → 3 seconds
    Task 2 → 1 second
    Task 3 → 2 seconds

Possible completion order:

    Task 2
       ↓
    Task 3
       ↓
    Task 1

But if we store:

    future1
    future2
    future3

we can retrieve each task's result using the corresponding Future.

This provides more control than simply treating everything as one result sequence.

---

# 🧠 `Future` and Concurrency

A Future separates two concepts:

### Task Submission

    executor.submit(task)

### Result Retrieval

    future.result()

Between these two operations, the task may be executing concurrently.

This separation is one of the main ideas behind the `concurrent.futures` API.

---

# 🤖 Future in AI Engineering

Futures are useful in AI applications where several independent operations are submitted and their results are needed later.

For example:

    AI Assistant
         │
         ├── Search → Future 1
         ├── Database → Future 2
         ├── File Processing → Future 3
         └── API Request → Future 4

The application can later collect:

    Future 1 → Search Result
    Future 2 → Database Result
    Future 3 → File Result
    Future 4 → API Result

Conceptually:

    User Query
         │
         ↓
    Submit Independent Tasks
         │
    ┌────┼────┬────┐
    ↓    ↓    ↓    ↓
   F1   F2   F3   F4
    │    │    │    │
    └────┴────┴────┘
         ↓
    Collect Results
         ↓
      AI Response

For I/O-heavy AI applications, `ThreadPoolExecutor` may be used.

For CPU-heavy processing, `ProcessPoolExecutor` may be used.

---

# 🧠 Future in an AI Data Pipeline

Imagine an AI application preprocessing multiple documents.

    Document 1 → Future 1
    Document 2 → Future 2
    Document 3 → Future 3
    Document 4 → Future 4

Each task can represent:

    Load
      ↓
    Clean
      ↓
    Transform
      ↓
    Return Result

The main program can later collect the completed results.

This pattern becomes useful when building scalable data-processing pipelines.

---

# ⚠️ Future Does Not Mean "Background Thread"

A common misunderstanding is:

> "Future means a background thread."

That is not correct.

A Future is an abstraction representing the eventual outcome of a submitted task.

The task may be executed by:

- A thread
- A process
- Another executor-managed worker

depending on the executor being used.

For example:

    ThreadPoolExecutor
          ↓
       Future
          ↓
       Thread


    ProcessPoolExecutor
          ↓
       Future
          ↓
       Process

The Future interface remains similar.

---

# 📊 Future Methods Quick Reference

| Method | Purpose |
|---|---|
| `result()` | Get task result |
| `done()` | Check whether task finished |
| `running()` | Check whether task is currently running |
| `cancel()` | Attempt to cancel task |
| `cancelled()` | Check whether task was cancelled |
| `exception()` | Get task exception |
| `add_done_callback()` | Run a callback when task finishes |

---

# 🔹 `add_done_callback()`

**`add_done_callback()` registers a function that will be called when the Future completes.**

Example:

    def completed(future):
        print("Task finished")


    future.add_done_callback(completed)

When the task finishes, Python calls:

    completed(future)

This can be useful when we want to perform some action automatically after a task finishes.

---

# 💻 Callback Example

    from concurrent.futures import ThreadPoolExecutor
    import time


    def task():
        time.sleep(2)
        return "Task completed"


    def completed(future):
        print("Callback:", future.result())


    with ThreadPoolExecutor(max_workers=1) as executor:

        future = executor.submit(task)

        future.add_done_callback(completed)

Possible output:

    Callback: Task completed

The callback runs after the Future completes.

---

# 🧠 Callback Flow

    submit(task)
         ↓
       Future
         ↓
      Running
         ↓
     Completed
         ↓
    Callback executes
         ↓
    future.result()

This is useful when an application needs to automatically react to task completion.

---

# 📊 Complete Future Lifecycle

    ┌───────────────┐
    │    submit()   │
    └───────┬───────┘
            ↓
    ┌───────────────┐
    │ Future Created│
    └───────┬───────┘
            ↓
         Pending
            │
       ┌────┴─────┐
       ↓          ↓
    Running    Cancelled
       │
       ↓
    ┌───────┬─────────┐
    ↓       ↓         ↓
 Success  Exception  Cancelled
    │       │
    ↓       ↓
 Result   Failed
    │       │
    └───┬───┘
        ↓
      Done

Important methods:

    running()
    done()
    cancelled()
    result()
    exception()

---

# 🧠 Important Distinctions

### `submit()`

    Submit task

### `Future`

    Represents submitted task

### `running()`

    Is task currently executing?

### `done()`

    Has task reached completion?

### `result()`

    What did task return?

### `exception()`

    Did task raise an exception?

### `cancel()`

    Can the pending task be cancelled?

### `cancelled()`

    Was the task cancelled?

Remembering these distinctions makes the `Future` API much easier to understand.

---

# 📌 Future Example to Remember

The most important pattern is:

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=2) as executor:

            future = executor.submit(calculate, 5)

            print("Task completed:", future.done())

            result = future.result()

            print("Result:", result)

            print("Task completed:", future.done())

Expected output:

    Task completed: False
    Result: 25
    Task completed: True

This single example demonstrates the basic Future lifecycle.

---

# 🤖 AI Engineer Practical Pattern

A simplified AI application could use:

    executor.submit(search_web, query)
        ↓
      Future 1

    executor.submit(search_database, query)
        ↓
      Future 2

    executor.submit(process_file, file)
        ↓
      Future 3

Then:

    Future 1 → result()
    Future 2 → result()
    Future 3 → result()

Finally:

    Collected Results
          ↓
       AI Model
          ↓
      Final Answer

This pattern is useful when independent tasks can be executed concurrently.

---

# 🧠 Key Takeaways

- A `Future` represents the eventual result of a submitted task.
- `submit()` creates and returns a Future.
- A Future does not necessarily contain the result immediately.
- `result()` retrieves the result and may wait for completion.
- `done()` checks whether the task has finished.
- `running()` checks whether the task is currently executing.
- `cancel()` attempts to cancel a task that has not started.
- `cancelled()` checks whether cancellation occurred.
- `exception()` retrieves the exception raised by a failed task.
- `add_done_callback()` allows code to run automatically when a task finishes.
- A Future can represent work performed by either a thread or a process.
- Multiple Futures allow individual tracking of multiple concurrent tasks.
- Futures separate task submission from result retrieval.
- In AI Engineering, Futures can represent independent searches, API calls, preprocessing jobs, or other concurrent operations.

---

# 🔚 Summary

The central idea is:

    executor.submit(task)
             ↓
          Future
             ↓
      ┌──────┼────────┐
      ↓      ↓        ↓
   running  done   cancelled
      │
      ↓
   result()
      ↓
   Final Result

The most important methods are:

    future.done()
    future.running()
    future.result()
    future.cancel()
    future.cancelled()
    future.exception()

And the most important relationship is:

    Executor
       ↓
    submit()
       ↓
    Future
       ↓
    Task executes
       ↓
    result()

With `Future` understood, the next topics will move into the practical executors themselves: **`ThreadPoolExecutor`** and **`ProcessPoolExecutor`**.



# 1️⃣3️⃣ `ThreadPoolExecutor`

## 🧩 What is `ThreadPoolExecutor`?

**`ThreadPoolExecutor` is a high-level Python tool that manages a pool of worker threads to execute multiple tasks concurrently, especially useful for I/O-bound tasks.**

It is part of the `concurrent.futures` module.

Conceptually:

    ThreadPoolExecutor
          │
          ├── Thread 1
          ├── Thread 2
          └── Thread 3
                  ↓
                Tasks

Instead of manually creating and managing multiple threads using:

    threading.Thread

we can let `ThreadPoolExecutor` manage a group of worker threads for us.

---

# 🎯 Why Do We Need `ThreadPoolExecutor`?

Earlier, we learned how to manually create threads:

    thread1 = threading.Thread(...)
    thread2 = threading.Thread(...)
    thread3 = threading.Thread(...)

Then:

    thread1.start()
    thread2.start()
    thread3.start()

And:

    thread1.join()
    thread2.join()
    thread3.join()

For a large number of tasks, manually managing threads becomes repetitive.

`ThreadPoolExecutor` simplifies this process.

Instead of manually managing every thread:

    ThreadPoolExecutor
          ↓
    Worker Threads
          ↓
    Tasks

The executor manages the worker threads for us.

---

# 📦 Importing `ThreadPoolExecutor`

`ThreadPoolExecutor` is available from:

    concurrent.futures

Import it using:

    from concurrent.futures import ThreadPoolExecutor

We may also import `Future` if needed, but the executor itself is enough for basic usage.

---

# 💻 Basic `ThreadPoolExecutor` Example

File:

    14_thread_pool_executor.py

    from concurrent.futures import ThreadPoolExecutor
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(
                task,
                ["Task 1", "Task 2", "Task 3"]
            )

        print("All tasks completed")

---

# 📤 Possible Output

    Task 1 started
    Task 2 started
    Task 3 started
    Task 1 completed
    Task 3 completed
    Task 2 completed
    All tasks completed

The completion order may be different in another execution.

For example:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 2 completed
    Task 1 completed
    Task 3 completed
    All tasks completed

This is normal in concurrent programming.

---

# 🧠 Understanding `max_workers`

This line:

    ThreadPoolExecutor(max_workers=3)

creates an executor that can use up to three worker threads.

Conceptually:

    ThreadPoolExecutor
          │
          ├── Thread 1
          ├── Thread 2
          └── Thread 3

If we have:

    Task 1
    Task 2
    Task 3
    Task 4
    Task 5

the first three tasks can be assigned to available workers.

When one worker becomes available, another task can be processed.

Conceptually:

    Thread 1 → Task 1
    Thread 2 → Task 2
    Thread 3 → Task 3

              ↓

    Thread 1 → Task 4
    Thread 2 → Task 5

The executor handles the scheduling.

---

# 🔄 Thread Pool Workflow

The general workflow is:

    Create ThreadPoolExecutor
              ↓
        Create Workers
              ↓
        Submit Tasks
              ↓
      Threads Execute Tasks
              ↓
       Tasks Complete
              ↓
       Executor Cleanup

Using:

    with ThreadPoolExecutor(...) as executor:
        ...

makes this lifecycle easier to manage.

---

# 🔹 `executor.map()`

**`executor.map()` applies a function to each item in an iterable and schedules those tasks using the executor's worker threads.**

Example:

    names = ["Task 1", "Task 2", "Task 3"]

    executor.map(task, names)

This is conceptually similar to:

    task("Task 1")
    task("Task 2")
    task("Task 3")

but the executor manages the worker threads.

---

# 🧠 `map()` and Result Order

Suppose the function returns a value:

    def task(number):
        time.sleep(number)
        return number * 10

And:

    numbers = [3, 1, 2]

We can write:

    results = executor.map(task, numbers)

The tasks may complete in this order:

    1
    ↓
    2
    ↓
    3

But the results are yielded according to input order:

    [30, 10, 20]

Therefore:

    Execution order
        ≠
    Result order

This is an important concept to remember.

---

# 💻 `map()` Returning Results

    from concurrent.futures import ThreadPoolExecutor
    import time


    def square(number):
        time.sleep(1)
        return number * number


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:

            results = executor.map(
                square,
                [1, 2, 3, 4, 5]
            )

        print("Results:", list(results))

Output:

    Results: [1, 4, 9, 16, 25]

The executor manages the worker threads while the result iterator provides results in input order.

---

# 🔹 `submit()`

**`submit()` schedules one task for execution and returns a `Future` object representing that task.**

Example:

    future = executor.submit(task, "Task 1")

The executor schedules:

    task("Task 1")

and returns:

    Future

We can then use:

    future.result()

to retrieve the result.

---

# 💻 `submit()` Example

    from concurrent.futures import ThreadPoolExecutor
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")

        return f"{name} result"


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:

            future = executor.submit(task, "Task 1")

            print("Task submitted")

            result = future.result()

            print("Result:", result)

Possible output:

    Task 1 started
    Task submitted
    Task 1 completed
    Result: Task 1 result

The exact ordering of output can vary because thread scheduling is concurrent.

---

# 🧠 `submit()` vs `map()`

Both can execute tasks concurrently, but they provide different levels of control.

### `map()`

Useful when:

- We have many inputs.
- The same function is applied to each input.
- We want a simple interface.

Example:

    results = executor.map(task, items)

### `submit()`

Useful when:

- We want individual task control.
- We want a `Future`.
- Different tasks may have different arguments.
- We need individual status checks.
- We want individual exception handling.

Example:

    future = executor.submit(task, item)

---

# 📊 `map()` vs `submit()`

| Feature | `map()` | `submit()` |
|---|---|---|
| Many similar tasks | Excellent | Possible |
| Individual Future | Not directly exposed | Yes |
| Task status | Less direct | Yes |
| Individual cancellation | Not the main interface | Possible |
| Simple syntax | Yes | Slightly more verbose |
| Fine-grained control | Lower | Higher |

A simple rule:

    Same function + many inputs
              ↓
            map()


    Individual task control
              ↓
           submit()

---

# 🔹 `Future` with `ThreadPoolExecutor`

Since `submit()` returns a Future, we can use the methods learned earlier.

Example:

    future = executor.submit(task, "Task 1")

    print(future.done())

    result = future.result()

    print(future.done())

Possible output:

    False
    Task 1 result
    True

The Future allows us to track the thread's task.

---

# 🧠 ThreadPoolExecutor + Future Flow

    executor.submit(task)
             ↓
          Future
             │
             ├── Pending
             │
             ├── Running
             │
             └── Completed
                    ↓
              future.result()

This is one of the most important patterns in `concurrent.futures`.

---

# 🔹 `future.done()`

**`done()` checks whether the submitted task has completed.**

Example:

    future = executor.submit(task, "Task 1")

    print("Completed:", future.done())

If the task is still executing:

    Completed: False

After:

    future.result()

we can check again:

    print("Completed:", future.done())

Output:

    Completed: True

---

# 🔹 `future.running()`

**`running()` checks whether the submitted task is currently being executed by a worker thread.**

Example:

    future = executor.submit(task, "Task 1")

    print("Running:", future.running())

Depending on timing, it may return:

    True

or:

    False

because the task may still be pending or may have already finished.

---

# 🔹 `future.cancel()`

**`cancel()` attempts to cancel a task that has not started running.**

Example:

    future = executor.submit(task, "Task 1")

    cancelled = future.cancel()

    print("Cancelled:", cancelled)

If the task has already started, cancellation normally fails.

Therefore:

    Pending
       ↓
    cancel()
       ↓
    Possible


    Running
       ↓
    cancel()
       ↓
    Usually not possible

---

# 🔹 `future.exception()`

**`exception()` returns the exception raised by the task, if the task failed.**

Example:

    def divide(a, b):
        return a / b


    future = executor.submit(divide, 10, 0)

    try:
        future.result()

    except ZeroDivisionError:
        print("Division by zero occurred")

The Future can also be inspected using:

    future.exception()

if we want to retrieve the exception object.

---

# 🧩 Multiple Tasks with `submit()`

We can submit multiple tasks:

    future1 = executor.submit(task, "Task 1")
    future2 = executor.submit(task, "Task 2")
    future3 = executor.submit(task, "Task 3")

Conceptually:

    Task 1 → Future 1
    Task 2 → Future 2
    Task 3 → Future 3

The executor manages the worker threads.

---

# 💻 Multiple Futures Example

    from concurrent.futures import ThreadPoolExecutor
    import time


    def task(name):
        print(f"{name} started")

        time.sleep(2)

        print(f"{name} completed")

        return f"{name} result"


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:

            future1 = executor.submit(task, "Task 1")
            future2 = executor.submit(task, "Task 2")
            future3 = executor.submit(task, "Task 3")

            print("All tasks submitted")

            result1 = future1.result()
            result2 = future2.result()
            result3 = future3.result()

            print("Results:")
            print(result1)
            print(result2)
            print(result3)

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    All tasks submitted
    Task 2 completed
    Task 1 completed
    Task 3 completed
    Results:
    Task 1 result
    Task 2 result
    Task 3 result

Notice that:

    Completion order

can differ from:

    Result retrieval order

---

# 🧠 Why Are Threads Useful for I/O-bound Tasks?

Threads are particularly useful when tasks spend significant time waiting.

For example:

    API Request
         ↓
       Wait
         ↓
      Response

During the waiting period, another thread can perform useful work.

Conceptually:

    Thread 1 → API Request → Waiting
                         │
                         ↓
    Thread 2 → API Request → Waiting
                         │
                         ↓
    Thread 3 → File Read  → Waiting

This allows multiple I/O operations to be in progress.

---

# 🌐 API Request Simulation

A common example is simulating multiple API calls.

    from concurrent.futures import ThreadPoolExecutor
    import time


    def call_api(api_name):
        print(f"{api_name} request started")

        time.sleep(2)

        print(f"{api_name} response received")

        return f"{api_name} data"


    if __name__ == "__main__":
        with ThreadPoolExecutor(max_workers=3) as executor:

            results = executor.map(
                call_api,
                ["User API", "Weather API", "News API"]
            )

        print("Results:", list(results))

Possible output:

    User API request started
    Weather API request started
    News API request started
    User API response received
    News API response received
    Weather API response received
    Results: ['User API data', 'Weather API data', 'News API data']

The completion order may vary.

---

# 🤖 Why This Matters for AI Engineering

AI applications frequently communicate with external services.

For example:

    AI Assistant
         │
         ├── Weather API
         ├── News API
         ├── Database
         ├── Search Service
         └── Other APIs

These operations can involve network waiting.

A ThreadPoolExecutor can allow multiple independent I/O operations to be in progress concurrently.

Conceptually:

    User Query
         │
         ↓
    ThreadPoolExecutor
         │
    ┌────┼────┬────┐
    ↓    ↓    ↓    ↓
   Web  API  DB  File
    │    │    │    │
    └────┴────┴────┘
         ↓
    Collect Results
         ↓
       AI Model
         ↓
     Final Response

This is a simplified representation of a real AI application.

---

# 📁 File Processing Example

Suppose an application needs to read multiple files.

Conceptually:

    File 1 → Thread 1
    File 2 → Thread 2
    File 3 → Thread 3
    File 4 → Thread 4

The threads can spend time waiting for file I/O while other threads continue working.

Example:

    from concurrent.futures import ThreadPoolExecutor


    def read_file(filename):
        with open(filename, "r") as file:
            return file.read()


    if __name__ == "__main__":
        filenames = [
            "file1.txt",
            "file2.txt",
            "file3.txt"
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = executor.map(read_file, filenames)

        for content in results:
            print(content)

This is a simple example of concurrent file operations.

---

# 🌐 Web Request Example

In a real application, network libraries can be used to perform HTTP requests.

The basic architecture could be:

    User Query
         │
         ↓
    ThreadPoolExecutor
         │
    ┌────┼────┐
    ↓    ↓    ↓
   API  API  API
    │    │    │
    └────┴────┘
         ↓
      Results

The actual HTTP library and whether it supports threads safely must be considered when implementing this in production.

---

# ⚠️ ThreadPoolExecutor Is Not Only for APIs

Although API requests are a common example, ThreadPoolExecutor can be useful for many I/O-bound tasks.

Examples:

- Network requests
- File operations
- Database operations
- Web scraping
- Cloud service calls
- Reading external resources
- Waiting for external processes

The important characteristic is that the task spends significant time waiting for I/O.

---

# 🧠 I/O-bound Example

Consider:

    time.sleep(2)

This is not actual I/O.

It is only being used to simulate waiting.

For example:

    def task():
        time.sleep(2)

represents:

    Task starts
       ↓
    Waiting
       ↓
    Task continues

In real applications, the waiting could come from:

    API response
    Database response
    File operation
    Network response

---

# ⏱️ Sequential vs Thread Pool

Suppose we have three independent tasks:

    Task 1 → 2 seconds
    Task 2 → 2 seconds
    Task 3 → 2 seconds

Sequentially:

    Task 1
       ↓
    2 sec

    Task 2
       ↓
    2 sec

    Task 3
       ↓
    2 sec

Approximate total:

    6 seconds

With three worker threads, the waiting periods can overlap:

    Task 1 ──────────→ 2 sec
    Task 2 ──────────→ 2 sec
    Task 3 ──────────→ 2 sec

Approximate elapsed time:

    around 2 seconds

Real-world performance depends on the actual workload and system conditions.

---

# ⚠️ ThreadPoolExecutor Does Not Guarantee Speedup

Thread pools are useful for suitable workloads, but they do not automatically make every program faster.

Potential limitations include:

- Thread creation/management overhead
- Lock contention
- CPU-bound Python code
- Shared-state problems
- External service limitations
- Rate limits
- Too many threads
- Context switching

Therefore:

> **Choose ThreadPoolExecutor based on workload characteristics, not simply because concurrency is available.**

---

# 🔐 Shared Data and Thread Safety

Because threads share memory within the same process, multiple threads can access shared variables.

For example:

    counter = 0

Multiple threads modifying the same variable can create race conditions.

Therefore, synchronization mechanisms such as:

    threading.Lock()

may be required.

Conceptually:

    Thread 1 ──┐
               ├──→ Shared Data
    Thread 2 ──┘

Without proper synchronization:

    Race Condition

With appropriate synchronization:

    Lock
      ↓
    Critical Section
      ↓
    Safe Access

This connects directly to the race-condition and thread-safety concepts learned earlier.

---

# 🧠 ThreadPoolExecutor and the GIL

In standard CPython, the Global Interpreter Lock affects execution of pure-Python CPU-bound code.

Therefore, `ThreadPoolExecutor` is generally not the preferred solution for CPU-heavy pure-Python computation when the goal is CPU parallelism.

For CPU-bound workloads, consider:

    ProcessPoolExecutor

or other specialized parallelism provided by the libraries being used.

For I/O-bound workloads, threads can still be very useful because threads can make progress while other threads are waiting on I/O.

---

# 📊 ThreadPoolExecutor vs ProcessPoolExecutor

| Feature | ThreadPoolExecutor | ProcessPoolExecutor |
|---|---|---|
| Worker | Thread | Process |
| Memory | Shared | Separate |
| Typical use | I/O-bound | CPU-bound |
| GIL | Relevant for pure-Python CPU work | Separate processes |
| Communication | Easier | More overhead |
| Startup cost | Generally lower | Generally higher |
| Isolation | Lower | Higher |
| API calls | Often useful | Usually unnecessary overhead |
| CPU-heavy preprocessing | Usually not ideal | Often suitable |

---

# 🧠 Choosing the Right Executor

Ask:

    What is my task doing most of the time?

          │
     ┌────┴────┐
     ↓         ↓
   Waiting   Computing
     │         │
     ↓         ↓
   I/O-bound CPU-bound
     │         │
     ↓         ↓
 ThreadPool  ProcessPool
 Executor    Executor

Examples:

    API Request
        ↓
    ThreadPoolExecutor


    Database Query
        ↓
    ThreadPoolExecutor


    File I/O
        ↓
    ThreadPoolExecutor


    Heavy CPU Calculation
        ↓
    ProcessPoolExecutor


    CPU-heavy preprocessing
        ↓
    ProcessPoolExecutor

This is a practical guideline, not an absolute rule.

---

# 🤖 AI Engineer Example: Multi-Source Assistant

Suppose an AI assistant receives:

    "What is the weather today and what are today's important news headlines?"

The application may need to call:

    Weather API
    News API

These requests are independent.

A simplified architecture:

    User Query
         │
         ↓
    ThreadPoolExecutor
         │
       ┌─┴─┐
       ↓   ↓
    Weather News
      API    API
       │      │
       └──┬───┘
          ↓
     Collect Results
          ↓
       AI Model
          ↓
      Final Answer

Instead of waiting for one API before starting the other, both can be in progress concurrently.

---

# 🧠 ThreadPoolExecutor and AI APIs

A real AI application may involve:

- LLM API calls
- Embedding API calls
- Web search
- Database queries
- File retrieval
- Cloud storage

Some of these are I/O-bound.

A thread pool can sometimes be used to overlap independent blocking operations.

However, if the library already provides native asynchronous APIs, `asyncio` may be a better fit, especially when handling many concurrent operations.

This will become important in the later `asyncio` section.

---

# 📌 Important Methods

| Method | Purpose |
|---|---|
| `ThreadPoolExecutor()` | Creates a thread pool |
| `max_workers` | Controls maximum worker threads |
| `executor.map()` | Applies a function to multiple inputs |
| `executor.submit()` | Submits an individual task |
| `future.result()` | Gets the task result |
| `future.done()` | Checks whether task completed |
| `future.running()` | Checks whether task is currently running |
| `future.cancel()` | Attempts cancellation |
| `future.exception()` | Retrieves task exception |
| `executor.shutdown()` | Shuts down executor |

---

# 🔄 Complete ThreadPoolExecutor Workflow

    Import ThreadPoolExecutor
              ↓
    Create Executor
              ↓
    Define Worker Function
              ↓
    Submit Tasks
              ↓
    Worker Threads Execute
              ↓
    Tasks Complete
              ↓
    Retrieve Results
              ↓
    Executor Cleanup

Using `map()`:

    executor.map(function, data)

Using `submit()`:

    future = executor.submit(function, argument)

Then:

    result = future.result()

---

# 🧠 Key Takeaways

- `ThreadPoolExecutor` manages a pool of worker threads.
- It is part of `concurrent.futures`.
- It provides a higher-level interface than manually creating threads.
- `max_workers` controls the maximum number of worker threads.
- `executor.map()` applies a function to multiple inputs.
- `executor.submit()` schedules an individual task.
- `submit()` returns a `Future`.
- `Future` allows us to monitor and retrieve task results.
- `future.result()` retrieves the result.
- `future.done()` checks completion.
- `future.running()` checks whether the task is currently executing.
- `future.cancel()` attempts to cancel a task that has not started.
- `future.exception()` can inspect task failures.
- ThreadPoolExecutor is commonly useful for I/O-bound work.
- Threads share memory, so shared-state synchronization may be necessary.
- `time.sleep()` can simulate waiting but is not itself an I/O operation.
- ThreadPoolExecutor is not automatically faster for every workload.
- For CPU-bound pure-Python work, ProcessPoolExecutor is often a more appropriate choice.
- For large numbers of asynchronous I/O operations, `asyncio` can also be an effective approach.
- AI applications can use ThreadPoolExecutor for independent API, database, file, and network operations.

---

# 🔚 Summary

The central idea is:

    ThreadPoolExecutor
           │
      ┌────┼────┐
      ↓    ↓    ↓
    Thread Thread Thread
      │    │    │
      ↓    ↓    ↓
    Task  Task  Task

For simple repeated tasks:

    executor.map()

For individual task control:

    executor.submit()
           ↓
         Future
           ↓
    future.result()

The practical rule to remember is:

    I/O-bound task
          ↓
    ThreadPoolExecutor
          ↓
    Multiple worker threads
          ↓
    Concurrent waiting / processing

While for CPU-bound work:

    CPU-bound task
          ↓
    ProcessPoolExecutor
          ↓
    Multiple processes

The next topic will cover **`ProcessPoolExecutor`**, which uses the same high-level `concurrent.futures` style but manages processes instead of threads.


# 1️⃣4️⃣ `ProcessPoolExecutor`

## 🧩 What is `ProcessPoolExecutor`?

**`ProcessPoolExecutor` is a high-level Python tool that manages a pool of worker processes to execute multiple tasks concurrently, especially useful for CPU-bound tasks.**

It is part of Python's `concurrent.futures` module.

Conceptually:

    ProcessPoolExecutor
           │
       ┌───┼───┐
       ↓   ↓   ↓
    Process Process Process
       │   │   │
       ↓   ↓   ↓
      Task Task Task

Instead of manually creating multiple `multiprocessing.Process` objects, `ProcessPoolExecutor` manages a group of worker processes for us.

---

# 🎯 Why Do We Need `ProcessPoolExecutor`?

Earlier, we learned how to create individual processes:

    Process(...)
        ↓
    start()
        ↓
    join()

We also learned about:

    multiprocessing.Pool

`ProcessPoolExecutor` provides another, higher-level way to manage multiple processes.

It is particularly useful when we want:

- CPU-bound parallel work
- A simple executor interface
- `Future` objects
- Individual task tracking
- Easy result retrieval
- A consistent API with `ThreadPoolExecutor`

---

# 📦 Importing `ProcessPoolExecutor`

Use:

    from concurrent.futures import ProcessPoolExecutor

Example:

    from concurrent.futures import ProcessPoolExecutor


The executor can then be created using:

    ProcessPoolExecutor(max_workers=3)

---

# 💻 Basic `ProcessPoolExecutor` Example

File:

    15_process_pool_executor.py

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        print(f"Calculating {number}")

        time.sleep(2)

        return number * number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]

        with ProcessPoolExecutor(max_workers=2) as executor:
            results = executor.map(calculate, numbers)

        print("Results:", list(results))

---

# 📤 Possible Output

    Calculating 1
    Calculating 2
    Calculating 3
    Calculating 4
    Calculating 5
    Results: [1, 4, 9, 16, 25]

The exact order of the `Calculating...` messages can vary.

However, the results produced by `executor.map()` correspond to the input order.

---

# 🧠 Understanding `max_workers`

This line:

    ProcessPoolExecutor(max_workers=2)

creates an executor that can use up to two worker processes.

Suppose we have:

    numbers = [1, 2, 3, 4, 5]

Conceptually:

    Worker 1 → Task 1
    Worker 2 → Task 2

After one worker becomes available:

    Worker 1 → Task 3

Then:

    Worker 2 → Task 4

And so on.

The executor manages this scheduling automatically.

---

# 🔄 ProcessPoolExecutor Workflow

The general workflow is:

    Create ProcessPoolExecutor
              ↓
        Create Workers
              ↓
        Submit Tasks
              ↓
      Processes Execute
              ↓
       Tasks Complete
              ↓
       Retrieve Results
              ↓
       Executor Cleanup

Using:

    with ProcessPoolExecutor(...) as executor:
        ...

makes the lifecycle easier to manage.

---

# 🔹 `executor.map()`

**`executor.map()` applies a function to each item in an iterable and schedules those tasks using the executor's worker processes.**

Example:

    numbers = [1, 2, 3, 4, 5]

    results = executor.map(calculate, numbers)

Conceptually:

    calculate(1)
    calculate(2)
    calculate(3)
    calculate(4)
    calculate(5)

The executor determines which worker process handles each task.

---

# 🧠 Result Order with `map()`

Suppose:

    numbers = [1, 2, 3]

The tasks may finish in this order:

    Task 2
       ↓
    Task 3
       ↓
    Task 1

But:

    list(executor.map(...))

will provide results corresponding to:

    Task 1
    Task 2
    Task 3

Therefore:

    Execution order
         ≠
    Result order

This is the same important behavior we saw with `ThreadPoolExecutor`.

---

# 💻 Simple `map()` Example

    from concurrent.futures import ProcessPoolExecutor


    def square(number):
        return number * number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]

        with ProcessPoolExecutor(max_workers=3) as executor:
            results = executor.map(square, numbers)

        print("Results:", list(results))

Output:

    Results: [1, 4, 9, 16, 25]

---

# 🧩 Why Use `ProcessPoolExecutor` for CPU-bound Tasks?

CPU-bound tasks spend most of their time performing computations.

Examples:

- Large mathematical calculations
- Image preprocessing
- Video processing
- Numerical operations
- CPU-heavy data transformations
- Simulations
- Some computationally expensive preprocessing pipelines

Conceptually:

    CPU-bound Work
          ↓
    ProcessPoolExecutor
          ↓
    Multiple Processes
          ↓
    Multiple CPU Cores
          ↓
    Parallel Computation

This is one of the main reasons to use process-based concurrency.

---

# 🧠 `ProcessPoolExecutor` and the GIL

In standard CPython, the Global Interpreter Lock limits simultaneous execution of Python bytecode by multiple threads within a single interpreter process.

`ProcessPoolExecutor` uses separate processes.

Conceptually:

    Process 1
      ↓
    Python Interpreter


    Process 2
      ↓
    Python Interpreter


    Process 3
      ↓
    Python Interpreter

Each process has its own interpreter and memory space.

Therefore, CPU-bound pure-Python work can be distributed across processes and potentially executed on multiple CPU cores.

---

# ⚠️ Important GIL Clarification

The GIL does not mean that:

> "Threads are completely useless."

Threads remain very useful for I/O-bound work.

The practical guideline is:

    I/O-bound
       ↓
    ThreadPoolExecutor


    CPU-bound pure Python
       ↓
    ProcessPoolExecutor

This is a guideline rather than an absolute law.

Libraries such as NumPy, PyTorch, and other native extensions may use optimized native code and have their own parallel execution behavior.

---

# 🔹 `submit()`

**`submit()` schedules an individual task and returns a `Future` representing that task.**

Example:

    future = executor.submit(calculate, 5)

The executor schedules:

    calculate(5)

and returns:

    Future

We can later retrieve its result:

    result = future.result()

---

# 💻 `submit()` Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=2) as executor:

            future = executor.submit(calculate, 5)

            print("Task submitted")

            result = future.result()

            print("Result:", result)

Possible output:

    Task submitted
    Result: 25

The task executes in a worker process while the Future represents its eventual result.

---

# 🧠 ProcessPoolExecutor + Future

The workflow is:

    executor.submit()
           ↓
         Future
           ↓
    Worker Process
           ↓
      Task Executes
           ↓
       Result Ready
           ↓
    future.result()

This gives us more control over individual tasks than `map()`.

---

# 🔹 `future.done()`

**`done()` checks whether the submitted process task has completed.**

Example:

    future = executor.submit(calculate, 5)

    print("Task completed:", future.done())

Possible output:

    Task completed: False

After:

    result = future.result()

we can check again:

    print("Task completed:", future.done())

Output:

    Task completed: True

---

# 💻 Future Status Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=1) as executor:

            future = executor.submit(calculate, 5)

            print("Task completed:", future.done())

            result = future.result()

            print("Result:", result)

            print("Task completed:", future.done())

Possible output:

    Task completed: False
    Result: 25
    Task completed: True

This demonstrates the Future lifecycle.

---

# 🔹 `future.running()`

**`running()` checks whether the task is currently being executed by a worker process.**

Example:

    print("Running:", future.running())

Depending on timing, it may return:

    True

or:

    False

because the task may be:

- Waiting to start
- Currently running
- Already completed

---

# 🔹 `future.cancel()`

**`cancel()` attempts to cancel a task that has not started running.**

Example:

    future = executor.submit(calculate, 5)

    cancelled = future.cancel()

    print("Cancelled:", cancelled)

If the task has already started:

    future.cancel()

will generally return:

    False

because a running task cannot normally be stopped through Future cancellation.

---

# 🔹 `future.cancelled()`

**`cancelled()` checks whether the Future was successfully cancelled.**

Example:

    if future.cancelled():
        print("Task was cancelled")

Possible result:

    True

for a successfully cancelled task.

---

# 🔹 `future.exception()`

**`exception()` returns the exception raised by the task, if the task failed.**

Example:

    future = executor.submit(divide, 10, 0)

Then:

    error = future.exception()

can provide the exception raised by the worker task.

---

# 💻 Exception Handling Example

    from concurrent.futures import ProcessPoolExecutor


    def divide(a, b):
        return a / b


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=2) as executor:

            future = executor.submit(divide, 10, 0)

            try:
                result = future.result()
                print("Result:", result)

            except ZeroDivisionError as error:
                print("Error:", error)

Possible output:

    Error: division by zero

The exception raised in the worker process can be observed when retrieving the Future's result.

---

# 🧠 `map()` vs `submit()`

The same distinction applies here as with `ThreadPoolExecutor`.

### `map()`

Use when:

- Same function
- Many inputs
- Simple result collection
- Individual task control is not required

Example:

    results = executor.map(calculate, numbers)

### `submit()`

Use when:

- Individual task control is needed
- Different arguments may be used
- Future status needs to be inspected
- Individual exceptions need to be handled
- Individual tasks may need cancellation

Example:

    future = executor.submit(calculate, 5)

---

# 📊 `map()` vs `submit()`

| Feature | `map()` | `submit()` |
|---|---|---|
| Multiple similar tasks | Excellent | Possible |
| Returns Future objects individually | No | Yes |
| Task status | Less direct | Yes |
| Individual cancellation | Not the main interface | Possible |
| Simple syntax | Yes | More verbose |
| Fine-grained control | Lower | Higher |

---

# 🧩 Multiple Futures

We can submit multiple CPU-bound tasks:

    future1 = executor.submit(calculate, 2)
    future2 = executor.submit(calculate, 3)
    future3 = executor.submit(calculate, 4)

Conceptually:

    Future 1 → calculate(2)
    Future 2 → calculate(3)
    Future 3 → calculate(4)

The executor distributes these tasks among its worker processes.

---

# 💻 Multiple Futures Example

    from concurrent.futures import ProcessPoolExecutor
    import time


    def calculate(number):
        time.sleep(2)
        return number * number


    if __name__ == "__main__":
        with ProcessPoolExecutor(max_workers=3) as executor:

            future1 = executor.submit(calculate, 2)
            future2 = executor.submit(calculate, 3)
            future3 = executor.submit(calculate, 4)

            print("All tasks submitted")

            result1 = future1.result()
            result2 = future2.result()
            result3 = future3.result()

            print("Results:")
            print(result1)
            print(result2)
            print(result3)

Possible output:

    All tasks submitted
    Results:
    4
    9
    16

The tasks may execute concurrently in separate worker processes.

---

# 🧠 Process Pool Execution Model

Suppose:

    max_workers = 3

and:

    Task 1
    Task 2
    Task 3
    Task 4
    Task 5

Conceptually:

    Worker 1 → Task 1
    Worker 2 → Task 2
    Worker 3 → Task 3

When workers become available:

    Worker 1 → Task 4
    Worker 2 → Task 5

The executor manages this scheduling.

The exact scheduling strategy and timing should not be assumed from the simplified diagram.

---

# ⚙️ Process Creation Overhead

Processes generally have more overhead than threads.

Creating a process involves additional resources such as:

- Process management
- Memory
- Interpreter startup
- Communication
- Serialization

Therefore:

    ProcessPoolExecutor

is not automatically the best choice for every task.

For very small tasks, process-management overhead may outweigh the benefit of parallel execution.

---

# 🧠 Task Granularity

**Task granularity refers to how much useful work is performed by each individual task.**

Very small tasks:

    Task 1 → tiny
    Task 2 → tiny
    Task 3 → tiny

may not benefit much from multiprocessing.

Larger CPU-intensive tasks:

    Task 1 → heavy
    Task 2 → heavy
    Task 3 → heavy

are more likely to justify process-based parallelism.

Therefore:

> The amount of useful work should be large enough to justify the overhead of using multiple processes.

---

# 📊 ProcessPoolExecutor vs ThreadPoolExecutor

| Feature | `ThreadPoolExecutor` | `ProcessPoolExecutor` |
|---|---|---|
| Worker | Thread | Process |
| Memory | Shared | Separate |
| Typical workload | I/O-bound | CPU-bound |
| GIL | Relevant for pure-Python CPU work | Separate processes |
| Startup overhead | Generally lower | Generally higher |
| Communication | Easier | More overhead |
| Isolation | Lower | Higher |
| API calls | Often suitable | Usually unnecessary overhead |
| Heavy computation | Usually not ideal for pure Python | Often suitable |

---

# 🔄 Choosing Between the Two

Ask:

    What is the task mostly doing?

            │
       ┌────┴────┐
       ↓         ↓
    Waiting   Computing
       │         │
       ↓         ↓
    I/O-bound CPU-bound
       │         │
       ↓         ↓
    ThreadPool ProcessPool
    Executor   Executor

Examples:

    Network Request
         ↓
    ThreadPoolExecutor


    Database Query
         ↓
    ThreadPoolExecutor


    File I/O
         ↓
    ThreadPoolExecutor


    Heavy Mathematical Calculation
         ↓
    ProcessPoolExecutor


    CPU-heavy Data Processing
         ↓
    ProcessPoolExecutor

---

# 🤖 AI Engineering Use Cases

`ProcessPoolExecutor` can be useful in AI Engineering when the workload contains independent CPU-heavy operations.

Examples include:

### 🖼️ Image Preprocessing

    Images
       │
       ├── Image 1 → Process 1
       ├── Image 2 → Process 2
       ├── Image 3 → Process 3
       └── Image 4 → Process 4
                         ↓
                    Processed Images

---

### 📊 Dataset Preprocessing

    Large Dataset
          │
          ├── Chunk 1 → Process 1
          ├── Chunk 2 → Process 2
          ├── Chunk 3 → Process 3
          └── Chunk 4 → Process 4
                           ↓
                    Combined Dataset

---

### 🔢 Numerical Processing

    Calculations
          │
          ├── Calculation 1 → Process 1
          ├── Calculation 2 → Process 2
          ├── Calculation 3 → Process 3
          └── Calculation 4 → Process 4

---

### 📝 CPU-heavy Text Processing

Some computationally expensive preprocessing operations can potentially be divided among worker processes.

For example:

    Documents
        ↓
    Split into independent groups
        ↓
    ProcessPoolExecutor
        ↓
    CPU-heavy processing
        ↓
    Combined results

Whether this is beneficial depends on the actual workload and libraries being used.

---

# 🤖 AI Data Pipeline Example

Consider a document-processing pipeline:

    Raw Documents
          ↓
    Split into chunks
          ↓
    ProcessPoolExecutor
          │
     ┌────┼────┐
     ↓    ↓    ↓
   CPU   CPU   CPU
   Work  Work  Work
     │    │    │
     └────┼────┘
          ↓
    Processed Documents
          ↓
    Embedding / ML Pipeline

The process pool can be used for CPU-heavy preprocessing before the data reaches later AI stages.

---

# ⚠️ AI Libraries May Already Be Parallel

Modern AI and scientific libraries can already use optimized native implementations.

Examples include:

- NumPy
- PyTorch
- TensorFlow
- OpenCV
- BLAS-based numerical libraries

These libraries may use:

- Native threads
- Vectorization
- GPU acceleration
- Internal parallelism

Therefore, wrapping every AI operation inside `ProcessPoolExecutor` is not automatically beneficial.

Always consider how the underlying library performs its work.

---

# 🧠 Serialization Overhead

Because processes have separate memory spaces, data passed to worker processes generally needs to be serialized.

Conceptually:

    Main Process
         │
         │ Python Object
         ↓
    Serialization
         ↓
    Worker Process
         ↓
    Deserialization
         ↓
       Task

When the returned result comes back, communication happens in the opposite direction.

Therefore, sending huge objects between processes can be expensive.

---

# ⚠️ Large Data Warning

Suppose we pass a very large dataset to every worker:

    Huge Dataset
         ↓
    Serialize
         ↓
    Transfer
         ↓
    Worker

If this happens repeatedly, communication overhead can become significant.

Therefore, process-based systems should carefully consider:

- Data size
- Serialization cost
- Number of tasks
- Memory usage
- Worker count
- Computation time

---

# 🧠 Good ProcessPool Workload

A good candidate generally looks like:

    Large CPU Work
          +
    Independent Tasks
          +
    Reasonable Data Transfer
          ↓
    ProcessPoolExecutor

A poor candidate may look like:

    Tiny CPU Work
          +
    Huge Data Transfer
          ↓
    High Overhead

The goal is to make the useful computation significant enough to justify the process overhead.

---

# 🔹 Executor Cleanup

Using:

    with ProcessPoolExecutor(max_workers=3) as executor:
        ...

allows the executor to manage its lifecycle.

Conceptually:

    Create Worker Processes
             ↓
        Execute Tasks
             ↓
       Finish Work
             ↓
       Shutdown/Cleanup

This is generally preferred over leaving worker resources unmanaged.

---

# 🔹 `shutdown()`

An executor provides:

    executor.shutdown()

for explicitly shutting down the executor.

However, the common pattern:

    with ProcessPoolExecutor(...) as executor:
        ...

handles shutdown automatically when leaving the block.

---

# 🧠 ProcessPoolExecutor vs `multiprocessing.Pool`

Both can manage pools of worker processes, but they provide different interfaces.

| Feature | `multiprocessing.Pool` | `ProcessPoolExecutor` |
|---|---|---|
| Module | `multiprocessing` | `concurrent.futures` |
| Worker type | Processes | Processes |
| `map()` | Yes | Yes |
| Async mapping | `map_async()` | Executor/Future based |
| Future abstraction | `AsyncResult` | `Future` |
| `submit()` | No | Yes |
| Task status | Different API | Future methods |
| Interface consistency | Pool-specific | Similar to ThreadPoolExecutor |

One major advantage of `concurrent.futures` is that the thread and process executors use a similar high-level interface.

---

# 🧠 One Interface, Different Workers

Thread version:

    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, data)

Process version:

    with ProcessPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, data)

The overall pattern remains similar:

    Executor
       ↓
    submit()
       ↓
    Future
       ↓
    result()

Only the worker execution model changes.

---

# 🤖 AI Engineer Decision Guide

A useful mental model is:

    ┌─────────────────────────────┐
    │        What is the task?    │
    └──────────────┬──────────────┘
                   ↓
           Mostly waiting?
             /          \
           YES           NO
            ↓             ↓
        I/O-bound     CPU-bound
            ↓             ↓
    ThreadPool /       ProcessPool /
       asyncio        multiprocessing

For example:

    API Call
       ↓
    I/O-bound
       ↓
    ThreadPoolExecutor


    Heavy preprocessing
       ↓
    CPU-bound
       ↓
    ProcessPoolExecutor

This is one of the most useful practical decisions from this chapter.

---

# 📌 Important Methods

| Method | Purpose |
|---|---|
| `ProcessPoolExecutor()` | Creates process executor |
| `max_workers` | Controls maximum worker processes |
| `executor.map()` | Applies function to multiple inputs |
| `executor.submit()` | Submits individual task |
| `future.result()` | Retrieves result |
| `future.done()` | Checks completion |
| `future.running()` | Checks running state |
| `future.cancel()` | Attempts cancellation |
| `future.cancelled()` | Checks cancellation |
| `future.exception()` | Retrieves task exception |
| `executor.shutdown()` | Shuts down executor |

---

# 🧠 Complete Workflow

The standard `ProcessPoolExecutor` workflow is:

    Import ProcessPoolExecutor
              ↓
    Create Executor
              ↓
    Define CPU-bound function
              ↓
    Submit tasks
              ↓
    Worker processes execute
              ↓
    Retrieve results
              ↓
    Executor cleanup

Using `map()`:

    executor.map(function, data)

Using `submit()`:

    future = executor.submit(function, argument)

Then:

    result = future.result()

---

# 🧠 Important Concepts to Remember

### ProcessPoolExecutor

Manages a pool of worker processes.

### `max_workers`

Controls the maximum number of workers.

### `map()`

Runs the same function over multiple inputs.

### `submit()`

Submits one task and returns a Future.

### Future

Represents the eventual result of the task.

### `result()`

Retrieves the task's result.

### `done()`

Checks whether the task has finished.

### `running()`

Checks whether the task is currently executing.

### `cancel()`

Attempts to cancel a task that has not started.

---

# 🧠 Key Takeaways

- `ProcessPoolExecutor` is part of `concurrent.futures`.
- It manages a pool of worker processes.
- It provides a high-level alternative to manually managing `Process` objects.
- It is commonly useful for CPU-bound workloads.
- `max_workers` controls the maximum number of worker processes.
- `executor.map()` applies a function to multiple inputs.
- `executor.submit()` schedules an individual task.
- `submit()` returns a `Future`.
- `future.result()` retrieves the task's result.
- `future.done()` checks completion.
- `future.running()` checks whether the task is executing.
- `future.cancel()` attempts cancellation before execution starts.
- `future.exception()` can inspect task failures.
- Processes have separate memory spaces.
- Data transferred between processes can involve serialization overhead.
- Too many workers can create unnecessary overhead.
- Very small tasks may not benefit from multiprocessing.
- Large independent CPU-heavy tasks are better candidates.
- AI applications can use ProcessPoolExecutor for CPU-heavy preprocessing and data-processing pipelines.
- Modern AI libraries may already provide optimized parallelism, so process pools should not be added blindly.
- `ThreadPoolExecutor` and `ProcessPoolExecutor` provide a similar high-level programming style.

---

# 🔚 Summary

The central concept is:

    ProcessPoolExecutor
            │
       ┌────┼────┐
       ↓    ↓    ↓
    Process Process Process
       │    │    │
       ↓    ↓    ↓
      Task Task Task

For multiple similar tasks:

    executor.map()

For individual task control:

    executor.submit()
           ↓
         Future
           ↓
    future.result()

The most important practical distinction is:

    I/O-bound
       ↓
    ThreadPoolExecutor


    CPU-bound
       ↓
    ProcessPoolExecutor

`ProcessPoolExecutor` gives us a clean, high-level way to perform process-based concurrency without manually managing every process.

At this point, the process-based side of `concurrent.futures` is covered. The next major section moves into **`asyncio`**, which introduces asynchronous programming and the event loop.


# 1️⃣5️⃣ `asyncio`

## 🧩 What is `asyncio`?

**`asyncio` is a Python library for writing concurrent programs using asynchronous programming, especially useful for I/O-bound tasks such as network requests, APIs, database operations, and other operations that involve waiting.**

Unlike multiprocessing, which creates separate processes, and threading, which creates multiple threads, `asyncio` primarily uses a single thread with an **event loop** to manage multiple asynchronous tasks.

Conceptually:

    asyncio
       │
       ↓
    Event Loop
       │
       ├── Task 1 → Waiting
       ├── Task 2 → Running
       ├── Task 3 → Waiting
       └── Task 4 → Ready

When one task is waiting, the event loop can work on another task.

---

# 🎯 Why Do We Need `asyncio`?

Consider an application that needs to perform several network requests.

For example:

    API 1 → Wait 2 seconds
    API 2 → Wait 3 seconds
    API 3 → Wait 1 second

If we execute them sequentially:

    API 1
      ↓
    Wait 2 sec
      ↓
    API 2
      ↓
    Wait 3 sec
      ↓
    API 3
      ↓
    Wait 1 sec

Approximate waiting time:

    2 + 3 + 1 = 6 seconds

But these operations are independent.

We can allow them to be in progress concurrently:

    API 1 ──────────→ 2 sec
    API 2 ────────────────→ 3 sec
    API 3 ─────→ 1 sec

Approximate elapsed time:

    around 3 seconds

The exact performance depends on the actual operations and environment.

This is where asynchronous programming becomes useful.

---

# 🧠 What is Asynchronous Programming?

**Asynchronous programming is a programming model in which a task can pause while waiting for an operation to complete, allowing other tasks to make progress during that waiting period.**

The important idea is:

    Task 1
      ↓
    Waiting
      ↓
    Event Loop switches to Task 2
      ↓
    Task 2
      ↓
    Waiting
      ↓
    Event Loop switches to Task 3

Instead of blocking the entire program during every waiting period, other available tasks can make progress.

---

# 🔄 Synchronous vs Asynchronous

## Synchronous

In synchronous execution, operations generally proceed one after another.

    Task 1
      ↓
    Wait
      ↓
    Complete
      ↓
    Task 2
      ↓
    Wait
      ↓
    Complete

The next operation waits for the previous one to finish.

---

## Asynchronous

In asynchronous execution:

    Task 1
      ↓
    Waiting
      ↓
    Task 2
      ↓
    Waiting
      ↓
    Task 3
      ↓
    Task 1 continues
      ↓
    Task 2 continues

The event loop can switch between tasks when they are waiting.

---

# 🧩 The `asyncio` Module

Python provides the built-in:

    asyncio

module for asynchronous programming.

Import it using:

    import asyncio

It provides tools for:

- Coroutines
- Tasks
- Event loops
- Asynchronous sleeping
- Concurrent execution
- Timers
- Synchronization primitives
- Asynchronous queues
- Networking support through async libraries

---

# 💻 First `asyncio` Program

File:

    16_asyncio.py

    import asyncio


    async def task():
        print("Task Started")

        await asyncio.sleep(2)

        print("Task completed")


    asyncio.run(task())

Output:

    Task Started
    Task completed

The program waits for approximately two seconds between the two messages.

---

# 🔍 Understanding the Example

The program contains:

    async def task():

This defines an asynchronous function.

Inside it:

    await asyncio.sleep(2)

temporarily pauses the coroutine.

Finally:

    asyncio.run(task())

starts the asynchronous execution.

The three important pieces are:

    async def
       ↓
    await
       ↓
    asyncio.run()

These concepts will be explored in detail.

---

# 🔹 `async def`

**`async def` defines a coroutine function that can perform asynchronous operations using `await`.**

Example:

    async def task():
        print("Task started")

Calling:

    task()

does not execute the coroutine in the same way as a normal function call.

Instead, it produces a coroutine object.

Conceptually:

    async def task()
          ↓
    Coroutine Function

    task()
          ↓
    Coroutine Object

The coroutine needs to be executed by an event loop.

---

# 🧠 Normal Function vs Coroutine Function

Normal function:

    def task():
        return "Done"


    result = task()

Here:

    task()

executes the function immediately.

With:

    async def task():
        return "Done"


    result = task()

`result` is a coroutine object.

The coroutine has not completed simply because we called the function.

It needs to be awaited or scheduled.

---

# 🔹 Coroutine

**A coroutine is a special Python function defined with `async def` that can pause its execution with `await` and later resume from where it paused.**

Example:

    async def task():
        await asyncio.sleep(2)
        return "Done"

The coroutine can:

    Start
      ↓
    Pause
      ↓
    Allow other async work
      ↓
    Resume
      ↓
    Complete

This ability to pause and resume is fundamental to asynchronous programming.

---

# 🧠 Coroutine Lifecycle

A simplified coroutine lifecycle is:

    Define coroutine
          ↓
    Create coroutine object
          ↓
    Schedule / await coroutine
          ↓
    Coroutine starts
          ↓
    Reaches await
          ↓
    Pauses
          ↓
    Event loop runs other work
          ↓
    Awaited operation becomes ready
          ↓
    Coroutine resumes
          ↓
    Coroutine completes

---

# 🔹 `await`

**`await` pauses the current coroutine until an asynchronous operation is ready to continue, allowing the event loop to run other available asynchronous work.**

Example:

    await asyncio.sleep(2)

This does not mean:

> Stop the entire Python program for two seconds.

Instead, it means approximately:

> Pause this coroutine while the asynchronous operation is waiting, and allow the event loop to handle other work.

This distinction is extremely important.

---

# 🧩 `asyncio.sleep()`

**`asyncio.sleep()` asynchronously suspends the current coroutine for a specified amount of time.**

Example:

    await asyncio.sleep(2)

It is commonly used for:

- Demonstrations
- Simulating network waiting
- Timers
- Rate-control logic
- Testing asynchronous programs

Unlike:

    time.sleep(2)

`asyncio.sleep(2)` is designed to work cooperatively with the asyncio event loop.

---

# ⚠️ `time.sleep()` vs `asyncio.sleep()`

### `time.sleep()`

    time.sleep(2)

This blocks the current thread.

During the sleep, the thread cannot execute other work.

---

### `asyncio.sleep()`

    await asyncio.sleep(2)

This suspends the current coroutine and allows the event loop to run other asynchronous tasks.

Conceptually:

    time.sleep()

        Thread
          │
          └── BLOCKED


    await asyncio.sleep()

        Coroutine
          │
          └── PAUSED
                 ↓
             Event Loop
                 ↓
          Other Tasks

This is one of the most important differences in asynchronous Python.

---

# 🔹 `asyncio.run()`

**`asyncio.run()` runs a coroutine using an asyncio event loop and manages the event loop lifecycle for the program.**

Example:

    asyncio.run(task())

The simplified flow is:

    Coroutine
       ↓
    asyncio.run()
       ↓
    Event Loop
       ↓
    Execute Coroutine
       ↓
    Coroutine Completes
       ↓
    Event Loop Closes

For a normal top-level Python program, `asyncio.run()` is the standard simple way to execute the main coroutine.

---

# 🧠 What is an Event Loop?

**An event loop is the mechanism that manages and schedules asynchronous tasks, allowing the program to switch between tasks when they are waiting.**

Conceptually:

    ┌───────────────────────────┐
    │        Event Loop         │
    │                           │
    │  Check ready tasks        │
    │          ↓                │
    │  Run a task               │
    │          ↓                │
    │  Task reaches await       │
    │          ↓                │
    │  Run another task         │
    │          ↓                │
    │  Check waiting tasks      │
    │          ↓                │
    │  Resume ready task        │
    └───────────────────────────┘

The event loop is the central mechanism behind `asyncio`.

---

# 🔄 Event Loop Example

Suppose we have:

    Task 1
    Task 2
    Task 3

The event loop may operate conceptually like:

    Task 1 starts
        ↓
    Task 1 waits
        ↓
    Task 2 starts
        ↓
    Task 2 waits
        ↓
    Task 3 starts
        ↓
    Task 3 waits
        ↓
    Task 1 becomes ready
        ↓
    Task 1 resumes
        ↓
    Task 3 becomes ready
        ↓
    Task 3 resumes
        ↓
    Task 2 resumes
        ↓
    All complete

The exact scheduling order depends on the tasks and event-loop behavior.

---

# 🧠 Important Point: `asyncio` Is Not Automatically Parallel

A very important distinction:

> **Asynchronous concurrency is not the same thing as CPU parallelism.**

With typical asyncio programs, multiple coroutines can make progress within an event loop, usually on one thread.

Conceptually:

    One Thread
        │
        ↓
    Event Loop
        │
        ├── Coroutine 1
        ├── Coroutine 2
        └── Coroutine 3

This is different from:

    Process 1 → CPU Core 1
    Process 2 → CPU Core 2
    Process 3 → CPU Core 3

which represents process-based parallelism.

---

# 📊 `asyncio` vs Threading vs Multiprocessing

| Feature | `asyncio` | Threading | Multiprocessing |
|---|---|---|---|
| Main model | Coroutines | Threads | Processes |
| Typical execution | Event loop | Multiple threads | Multiple processes |
| Memory | Usually shared within one process | Shared within process | Separate |
| Best suited for | I/O-bound async work | I/O-bound work | CPU-bound work |
| Context switching | Cooperative | OS/thread scheduling | Process scheduling |
| CPU parallelism | Not by itself | Limited for pure Python in standard CPython | Yes, across processes |
| Overhead | Often low | Moderate | Higher |
| Common examples | Async APIs, networking | Blocking APIs, file operations | CPU-heavy computation |

---

# 🌐 Why `asyncio` Is Useful for APIs

Suppose an AI assistant needs to call:

    User API
    Weather API
    News API

Each request spends time waiting for a response.

Using asynchronous programming:

    User API
       ↓
     Waiting

    Weather API
       ↓
     Waiting

    News API
       ↓
     Waiting

The event loop can manage these waiting operations concurrently.

Conceptually:

    AI Assistant
         │
         ↓
      Event Loop
         │
    ┌────┼────┐
    ↓    ↓    ↓
   API  API  API
    │    │    │
    └────┴────┘
         ↓
      Results
         ↓
     AI Response

This is highly relevant to modern AI applications.

---

# 🤖 `asyncio` in AI Engineering

Modern AI applications frequently communicate with external services.

Examples:

- LLM APIs
- Embedding APIs
- Web search
- Vector databases
- SQL databases
- Cloud storage
- External tools
- Microservices

Many of these operations are I/O-bound.

Therefore, asynchronous programming can allow an AI application to keep multiple operations in progress without creating a separate thread for every waiting operation.

---

# 💻 Simple AI-style Example

    import asyncio


    async def web_search():
        print("Web search started")

        await asyncio.sleep(2)

        return "Web search result"


    async def database_search():
        print("Database search started")

        await asyncio.sleep(2)

        return "Database result"


    async def llm_request():
        print("LLM request started")

        await asyncio.sleep(2)

        return "LLM response"


    async def main():
        result1 = await web_search()
        result2 = await database_search()
        result3 = await llm_request()

        print(result1)
        print(result2)
        print(result3)


    asyncio.run(main())

This example uses asynchronous functions, but notice something important:

    await web_search()
    await database_search()
    await llm_request()

These calls are still executed sequentially.

This is an important lesson:

> **Using `async` and `await` alone does not automatically make independent operations concurrent.**

We need to schedule multiple tasks appropriately.

That will be covered in the next topics.

---

# 🧠 Sequential `await`

Consider:

    async def main():
        await task("Task 1")
        await task("Task 2")

The flow is:

    Task 1
       ↓
    Wait
       ↓
    Task 1 Complete
       ↓
    Task 2
       ↓
    Wait
       ↓
    Task 2 Complete

This is asynchronous code, but the two operations are being awaited sequentially.

Therefore:

    async ≠ automatically concurrent

To execute independent coroutines concurrently, we can use mechanisms such as:

    asyncio.create_task()

and:

    asyncio.gather()

These will be covered in the upcoming topics.

---

# 🔹 Blocking vs Non-Blocking

### Blocking operation

A blocking operation prevents the current thread from doing other work while it waits.

Example:

    time.sleep(2)

Conceptually:

    Thread
      │
      ↓
    sleep()
      │
      └── BLOCKED
            ↓
         2 seconds
            ↓
         Continue

---

### Non-blocking asynchronous waiting

Example:

    await asyncio.sleep(2)

Conceptually:

    Coroutine
       │
       ↓
    await
       │
       ↓
    Coroutine pauses
       │
       ↓
    Event loop handles other work
       │
       ↓
    Coroutine resumes

This cooperative behavior is central to asyncio.

---

# 🧠 Cooperative Concurrency

**Cooperative concurrency is a model where tasks voluntarily give control back to the event loop at points such as `await`, allowing other tasks to execute.**

Conceptually:

    Task 1
      ↓
    await
      ↓
    Give control
      ↓
    Task 2
      ↓
    await
      ↓
    Give control
      ↓
    Task 3

The tasks cooperate with the event loop.

This differs from operating-system scheduling of independent processes and threads.

---

# ⚠️ Blocking Code Inside `asyncio`

Consider:

    async def task():
        time.sleep(5)

This is problematic.

Although the function is declared with:

    async def

the:

    time.sleep(5)

call blocks the event-loop thread.

That means other asynchronous tasks may be prevented from making progress during those five seconds.

A cooperative async version would use:

    await asyncio.sleep(5)

when the goal is simply to simulate asynchronous waiting.

---

# 🚨 Important Rule

Inside an asynchronous application:

    Avoid unnecessary blocking operations
              ↓
    Especially on the event-loop thread

Prefer asynchronous alternatives when available.

For example:

    Blocking:
    time.sleep()

    Async:
    await asyncio.sleep()

Similarly, if a network library provides a proper asynchronous API, it can often be preferable to using a blocking network call directly inside an async function.

---

# 🧩 Async Function Returning a Value

A coroutine can return a normal Python value.

Example:

    async def calculate():
        await asyncio.sleep(1)
        return 25

When awaited:

    result = await calculate()

we receive:

    25

Conceptually:

    Coroutine
       ↓
    await
       ↓
    Execute
       ↓
    return 25
       ↓
    result = 25

---

# 💻 Return Value Example

    import asyncio


    async def calculate():
        await asyncio.sleep(1)
        return 25


    async def main():
        result = await calculate()

        print("Result:", result)


    asyncio.run(main())

Output:

    Result: 25

This demonstrates that coroutines can produce results just like normal functions.

---

# 🔄 Coroutine vs Task

These two concepts are related but different.

### Coroutine

A coroutine is created by calling an `async def` function.

Example:

    coroutine = task()

### Task

A Task schedules a coroutine to run through the event loop.

Example:

    task_object = asyncio.create_task(task())

Conceptually:

    async def task()
          ↓
    Coroutine Function

    task()
          ↓
    Coroutine Object

    create_task(coroutine)
          ↓
    asyncio Task

Tasks will be covered in detail later.

---

# 🧠 Important Terminology

| Term | Meaning |
|---|---|
| `asyncio` | Python library for asynchronous programming |
| `async def` | Defines a coroutine function |
| Coroutine | Async function execution that can pause and resume |
| `await` | Pauses current coroutine until awaited operation is ready |
| Event Loop | Schedules and manages async tasks |
| `asyncio.run()` | Runs a top-level coroutine |
| `asyncio.sleep()` | Non-blocking asynchronous delay |
| Task | Scheduled coroutine managed by the event loop |

---

# 🤖 Practical AI Architecture

A modern AI application may contain:

    User Request
          │
          ↓
    Async Application
          │
          ↓
    Event Loop
          │
    ┌─────┼──────────┐
    ↓     ↓          ↓
   Web   Database   LLM API
    │     │          │
    └─────┴──────────┘
          ↓
    Gather Information
          ↓
      AI Response

This architecture becomes particularly useful when several independent I/O operations need to be handled concurrently.

Later, we will combine:

    async
    await
    create_task()
    asyncio.gather()

to build more realistic concurrent AI-style workflows.

---

# 🧠 Common Beginner Mistakes

## Mistake 1: Forgetting `await`

Incorrect:

    async def main():
        task()

Correct:

    async def main():
        await task()

if the intention is to wait for that coroutine's completion.

---

## Mistake 2: Using `asyncio.run()` repeatedly unnecessarily

A typical top-level program uses:

    asyncio.run(main())

rather than repeatedly creating separate event loops for individual operations.

---

## Mistake 3: Assuming `async` means parallel CPU execution

This is incorrect.

    async
       ≠
    CPU parallelism

Asyncio is primarily useful for cooperative concurrency and I/O-bound workloads.

---

## Mistake 4: Using `time.sleep()` inside async code

Avoid unnecessary:

    time.sleep()

inside an event-loop coroutine.

Prefer:

    await asyncio.sleep()

when an asynchronous delay is intended.

---

## Mistake 5: Sequentially awaiting independent tasks

Example:

    await task1()
    await task2()
    await task3()

This does not schedule all three tasks concurrently.

Later we will learn:

    asyncio.create_task()

and:

    asyncio.gather()

for concurrent execution of independent coroutines.

---

# 📊 `asyncio` Decision Guide

Use `asyncio` when:

- Operations are mostly I/O-bound
- Many operations may be waiting at the same time
- Async-compatible libraries are available
- You want to manage many concurrent operations efficiently

Examples:

    API requests
    Network communication
    WebSockets
    Async database operations
    External service calls
    Async file/network operations

For heavy CPU computation, consider:

    ProcessPoolExecutor
    multiprocessing
    Specialized native/GPU libraries

---

# 🧠 `asyncio` vs `ThreadPoolExecutor`

Both can be useful for I/O-bound workloads, but their programming models differ.

### ThreadPoolExecutor

    Multiple Threads
         ↓
    Blocking operations
         ↓
    Threads wait independently

### asyncio

    Event Loop
         ↓
    Coroutines
         ↓
    await
         ↓
    Cooperative switching

A simple guideline:

    Blocking I/O library
          ↓
    ThreadPoolExecutor may be useful


    Async-compatible I/O library
          ↓
    asyncio may be a strong choice

The best choice depends on the libraries and application architecture.

---

# 🧠 Key Takeaways

- `asyncio` is Python's built-in framework for asynchronous programming.
- It is especially useful for I/O-bound workloads.
- `async def` defines a coroutine function.
- Calling an async function produces a coroutine object.
- A coroutine can pause and resume.
- `await` pauses the current coroutine while allowing the event loop to handle other work.
- `asyncio.sleep()` provides an asynchronous delay.
- `time.sleep()` blocks the current thread.
- `asyncio.run()` runs a top-level coroutine using an event loop.
- The event loop schedules and manages asynchronous work.
- Async concurrency is not the same as CPU parallelism.
- `asyncio` typically uses a single event-loop thread for coroutine scheduling.
- `async` and `await` alone do not automatically make independent operations concurrent.
- Sequential `await` statements execute one awaited operation before moving to the next.
- `asyncio.create_task()` can schedule coroutines for concurrent execution.
- `asyncio.gather()` can run multiple awaitables concurrently and collect their results.
- Blocking operations inside the event-loop thread can prevent other async tasks from making progress.
- `asyncio` is highly relevant to AI applications that interact with APIs, databases, search services, and other external systems.

---

# 🔚 Summary

The fundamental `asyncio` model is:

    async def
        ↓
    Coroutine
        ↓
    await
        ↓
    Event Loop
        ↓
    Pause / Resume
        ↓
    Result

The basic program structure is:

    import asyncio


    async def main():
        await some_async_operation()


    asyncio.run(main())

The most important idea is:

    ┌────────────────────────────┐
    │        Event Loop          │
    │                            │
    │  Task 1 → await → pause   │
    │       ↓                    │
    │  Task 2 → await → pause   │
    │       ↓                    │
    │  Task 3 → await → pause   │
    │       ↓                    │
    │  Resume ready tasks        │
    └────────────────────────────┘

`asyncio` becomes especially powerful when we combine multiple independent coroutines instead of awaiting them one by one.

The next topic will focus specifically on **`async` and `await`**, including coroutines, suspension points, sequential vs concurrent awaiting, and how the event loop handles them.


# 🔹 `async` / `await` in Python

## 📌 Topic Overview

`async` and `await` are the fundamental keywords used in Python's asynchronous programming model.

They allow a coroutine to **pause while waiting for an asynchronous operation and later resume execution**, giving the event loop an opportunity to handle other tasks.

File:

    17_async_await.py

---

# 🧩 What is `async`?

**`async` is a Python keyword used with `def` to define a coroutine function that can perform asynchronous operations.**

Syntax:

    async def function_name():
        # asynchronous code

Example:

    async def task():
        print("Task started")

The function `task()` is now a coroutine function.

---

# 🧩 What is `await`?

**`await` is a Python keyword used inside a coroutine to pause that coroutine until an asynchronous operation is ready to continue.**

Example:

    async def task():
        print("Task started")

        await asyncio.sleep(2)

        print("Task completed")

Here:

    await asyncio.sleep(2)

means that the current coroutine temporarily gives control back to the event loop while the asynchronous sleep is in progress.

---

# 🔄 Basic Relationship

The relationship can be remembered as:

    async
      ↓
    Defines coroutine
      ↓
    await
      ↓
    Pauses coroutine when waiting
      ↓
    Event loop can handle other work
      ↓
    Coroutine resumes

So:

    async → "This function can work asynchronously."

    await → "Pause this coroutine until this async operation is ready."

---

# 🧠 Coroutine Function vs Coroutine Object

This distinction is important.

Consider:

    async def task():
        return "Done"

Here:

    task

is a **coroutine function**.

When we call:

    task()

Python creates a:

    coroutine object

Conceptually:

    async def task()
          ↓
    Coroutine Function

    task()
          ↓
    Coroutine Object

The coroutine object must then be:

- awaited
- or scheduled as a Task

before it actually completes.

---

# 💻 Example

File:

    17_async_await.py

    import asyncio


    async def task():
        return "Task completed"


    async def main():
        result = await task()

        print(result)


    asyncio.run(main())

Output:

    Task completed

Here:

    task()

creates a coroutine.

Then:

    await task()

waits for that coroutine to finish and retrieves its returned value.

---

# 🔍 Step-by-Step Execution

The program:

    asyncio.run(main())

starts the main coroutine.

Then:

    result = await task()

causes the following flow:

    main()
      ↓
    task()
      ↓
    Coroutine created
      ↓
    await
      ↓
    task executes
      ↓
    return "Task completed"
      ↓
    result receives value
      ↓
    print(result)

Output:

    Task completed

---

# ⏸️ `await` as a Suspension Point

An `await` expression creates a point where the current coroutine can suspend.

Example:

    async def task():
        print("Before await")

        await asyncio.sleep(2)

        print("After await")

Execution:

    Before await
          ↓
       await
          ↓
      Coroutine
       pauses
          ↓
    2 seconds waiting
          ↓
    Coroutine resumes
          ↓
    After await

This point is often called a **suspension point**.

---

# 📌 Suspension Point

**A suspension point is a point in an asynchronous coroutine where execution can temporarily pause and allow the event loop to handle other work.**

Common example:

    await some_async_operation()

The coroutine does not permanently stop.

It can resume after the awaited operation becomes ready.

---

# 🧠 `await` Does NOT Mean "Block Everything"

This is one of the most important concepts.

Consider:

    await asyncio.sleep(3)

It does **not** mean:

    Entire Python program
            ↓
         BLOCKED
            ↓
        3 seconds

Instead, conceptually:

    Current Coroutine
          ↓
        await
          ↓
       PAUSED
          ↓
    Event Loop continues
          ↓
    Other async work can run

Therefore:

    await ≠ block the entire event loop

However, this is true only when the awaited operation itself is asynchronous/non-blocking.

---

# ⚠️ Blocking Inside an Async Function

Consider:

    import time
    import asyncio


    async def task():
        print("Task started")

        time.sleep(3)

        print("Task completed")

Although the function uses:

    async def

the following line:

    time.sleep(3)

blocks the current thread.

Therefore, other coroutines running on the same event loop may not get a chance to execute during that time.

---

# ✅ Asynchronous Version

Instead of:

    time.sleep(3)

use:

    await asyncio.sleep(3)

Example:

    import asyncio


    async def task():
        print("Task started")

        await asyncio.sleep(3)

        print("Task completed")


    asyncio.run(task())

Now the delay cooperates with the asyncio event loop.

---

# 🔄 Sequential `await`

Consider:

    async def task(name, delay):
        print(f"{name} started")

        await asyncio.sleep(delay)

        print(f"{name} completed")


    async def main():
        await task("Task 1", 2)
        await task("Task 2", 2)


    asyncio.run(main())

Output:

    Task 1 started
    Task 1 completed
    Task 2 started
    Task 2 completed

Approximate execution:

    Task 1
      ↓
    Wait 2 sec
      ↓
    Complete
      ↓
    Task 2
      ↓
    Wait 2 sec
      ↓
    Complete

Total waiting time is approximately:

    2 + 2 = 4 seconds

The functions are asynchronous, but they are still being awaited sequentially.

---

# 🧠 Important Lesson

This is a very common beginner misunderstanding:

    async def
        ≠
    automatically concurrent

And:

    await
        ≠
    automatically concurrent

For example:

    await task1()
    await task2()
    await task3()

means:

    Task 1 → finish
       ↓
    Task 2 → finish
       ↓
    Task 3 → finish

If the tasks are independent and we want them to make progress concurrently, we need to schedule them appropriately.

---

# 🔄 Concurrent Async Execution

The concept is:

    Task 1 ────────────┐
                      │
    Task 2 ────────────┼──→ Event Loop
                      │
    Task 3 ────────────┘

Instead of:

    Task 1 → Task 2 → Task 3

we want:

    Task 1
       ↘
        Event Loop
       ↗
    Task 2

    Task 3

Python provides tools such as:

    asyncio.create_task()

and:

    asyncio.gather()

to manage concurrent asynchronous operations.

These will be covered in the upcoming topics.

---

# 🧩 `await` and Return Values

`await` can retrieve the value returned by an asynchronous operation.

Example:

    import asyncio


    async def calculate():
        await asyncio.sleep(1)

        return 25


    async def main():
        result = await calculate()

        print("Result:", result)


    asyncio.run(main())

Output:

    Result: 25

The flow is:

    calculate()
       ↓
    Coroutine
       ↓
    await
       ↓
    Operation completes
       ↓
    return 25
       ↓
    result = 25

---

# 🔹 `await` Can Be Used Only in Async Context

Normally, `await` must be used inside an asynchronous function.

Correct:

    async def main():
        result = await task()

Incorrect:

    def main():
        result = await task()

A normal `def` function cannot directly use `await`.

Instead, an asynchronous function should be defined using:

    async def

---

# 🧠 Why Does `await` Need `async`?

The reason is that `await` interacts with the asynchronous execution model.

Conceptually:

    async def
        ↓
    Coroutine context
        ↓
    await
        ↓
    Suspension / resumption
        ↓
    Event loop

A normal synchronous function does not provide this coroutine context.

---

# 🔄 Multiple `await` Statements

A coroutine can contain multiple `await` expressions.

Example:

    import asyncio


    async def task():
        print("Step 1")

        await asyncio.sleep(1)

        print("Step 2")

        await asyncio.sleep(1)

        print("Step 3")


    asyncio.run(task())

Output:

    Step 1
    Step 2
    Step 3

Execution flow:

    Step 1
       ↓
    await
       ↓
    Wait
       ↓
    Step 2
       ↓
    await
       ↓
    Wait
       ↓
    Step 3

Each `await` provides an opportunity for the coroutine to suspend.

---

# 🧠 Multiple Coroutines

Suppose we have:

    async def task1():
        await asyncio.sleep(2)
        return "Task 1 completed"


    async def task2():
        await asyncio.sleep(2)
        return "Task 2 completed"

We could write:

    async def main():
        result1 = await task1()
        result2 = await task2()

But this is sequential.

Conceptually:

    task1
      ↓
    wait
      ↓
    result1
      ↓
    task2
      ↓
    wait
      ↓
    result2

If these tasks are independent, we may want them to run concurrently.

That is where **Tasks** become important.

---

# 🤖 Why This Matters in AI Engineering

Suppose an AI assistant needs:

    Web Search
    Database Search
    LLM Request

Each operation may spend time waiting for an external service.

A sequential approach:

    Web Search
        ↓
      wait
        ↓
    Database
        ↓
      wait
        ↓
    LLM
        ↓
      wait

can unnecessarily increase total response time.

An asynchronous architecture can instead schedule independent operations so their waiting periods overlap.

Conceptually:

    ┌───────────────┐
    │ AI Assistant  │
    └───────┬───────┘
            ↓
       Event Loop
       /    |     \
      ↓     ↓      ↓
    Web   Database  LLM
    API      API    API
      \      |      /
       \     |     /
            ↓
        Collect Data
            ↓
       Generate Answer

This pattern is common in API-heavy AI applications.

---

# 🌐 Real-World AI Example

Imagine an AI assistant receiving:

    "What is today's weather and latest news?"

It may need:

    Weather API
    News API
    LLM API

The operations may involve network waiting.

With async programming, the application can potentially keep multiple requests in progress rather than waiting for each response before starting the next independent request.

A simplified model:

    User Query
        ↓
    AI Controller
        ↓
    ┌───────┼────────┐
    ↓       ↓        ↓
 Weather   News     LLM
   API      API      API
    ↓       ↓        ↓
    └───────┼────────┘
            ↓
       Combine Results
            ↓
        Final Answer

---

# 🧩 Coroutine Chaining

One coroutine can await another coroutine.

Example:

    import asyncio


    async def get_data():
        await asyncio.sleep(1)

        return "Data received"


    async def process_data():
        data = await get_data()

        return f"Processed: {data}"


    async def main():
        result = await process_data()

        print(result)


    asyncio.run(main())

Output:

    Processed: Data received

Execution:

    main()
      ↓
    process_data()
      ↓
    get_data()
      ↓
    await
      ↓
    Data received
      ↓
    process_data()
      ↓
    main()
      ↓
    Result

This is called coroutine chaining.

---

# 🧠 Coroutine Chaining

**Coroutine chaining occurs when one coroutine awaits another coroutine to obtain its result before continuing.**

Example:

    main()
      ↓
    await process_data()
      ↓
    await get_data()
      ↓
    result
      ↓
    process_data()
      ↓
    main()

This is useful when one operation depends on another.

For example:

    Authenticate
        ↓
    Fetch User
        ↓
    Fetch User Data
        ↓
    Generate Response

These operations may have dependencies, so they cannot always be executed independently.

---

# ⚡ Independent vs Dependent Tasks

This distinction is important.

## Independent operations

Example:

    Weather API
    News API
    Stock API

One does not necessarily depend on the result of another.

These may be candidates for concurrent execution.

---

## Dependent operations

Example:

    Login
      ↓
    Get User ID
      ↓
    Get User Data

The second operation depends on the first.

Therefore:

    Login → User ID → User Data

must follow the dependency chain.

---

# 📊 Comparison

| Situation | Suitable approach |
|---|---|
| Task B depends on Task A | Sequential `await` |
| Tasks are independent | Async Tasks / `gather()` |
| CPU-heavy computation | Multiprocessing / ProcessPoolExecutor |
| Blocking I/O | ThreadPoolExecutor may help |
| Async-compatible I/O | `asyncio` |

This is a practical decision-making framework for Python concurrency.

---

# ⚠️ Common Mistake: Forgetting to Await

Consider:

    async def get_data():
        return "Data"


    async def main():
        result = get_data()

        print(result)

Here `result` is not:

    "Data"

Instead, it is a coroutine object.

Conceptually:

    get_data()
       ↓
    Coroutine Object

To execute and retrieve its result:

    result = await get_data()

Then:

    result
       ↓
    "Data"

---

# 🧠 Coroutine Warning

If a coroutine is created but never awaited or scheduled, Python may produce a warning such as:

    RuntimeWarning:
    coroutine 'get_data' was never awaited

This usually indicates that an asynchronous function was called incorrectly.

Correct:

    result = await get_data()

or, when appropriate:

    task = asyncio.create_task(get_data())

---

# 🔹 `asyncio.run()` and the Main Coroutine

A common structure is:

    import asyncio


    async def main():
        # asynchronous application logic
        ...


    asyncio.run(main())

This pattern is commonly used for standalone Python scripts.

The architecture is:

    Python Program
          ↓
    asyncio.run(main())
          ↓
    Event Loop
          ↓
    main() coroutine
          ↓
    Other coroutines
          ↓
    Results
          ↓
    Program finishes

---

# 🧠 Event Loop and `await`

A simplified model:

    ┌────────────────────────────┐
    │        Event Loop          │
    ├────────────────────────────┤
    │                            │
    │ Task 1 → running           │
    │           ↓                │
    │         await              │
    │           ↓                │
    │ Task 2 → running           │
    │           ↓                │
    │         await              │
    │           ↓                │
    │ Task 3 → running           │
    │           ↓                │
    │       operation ready      │
    │           ↓                │
    │ Task 1 → resumes           │
    │                            │
    └────────────────────────────┘

The event loop coordinates when coroutines are able to continue.

---

# 🧠 Important Mental Model

Think of an event loop like a manager.

Suppose three workers have tasks:

    Worker 1 → Waiting for API
    Worker 2 → Waiting for Database
    Worker 3 → Ready to process data

Instead of the manager waiting with Worker 1:

    "I'll wait here until API responds."

the manager can say:

    "Worker 1 is waiting.
     I'll work with Worker 3."

This is the basic intuition behind cooperative asynchronous programming.

---

# 🤖 AI Engineer Example

Consider an AI research assistant.

It receives:

    "Research Python concurrency
     and summarize the latest information."

It may need:

    Web Search
    ↓
    Retrieve pages
    ↓
    Extract information
    ↓
    LLM summarization

Some operations can be independent:

    Search A
    Search B
    Search C

These can potentially be handled concurrently.

Then:

    Search Results
         ↓
    Combine Results
         ↓
    LLM
         ↓
    Final Summary

This is one reason asynchronous programming is useful in AI systems.

---

# 📝 Final Example for Topic 17

File:

    17_async_await.py

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        # Asynchronous waiting allows the event loop
        # to handle other available async work.
        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        # These are awaited one after another,
        # so the operations are still sequential.
        result1 = await task("Task 1", 2)
        result2 = await task("Task 2", 2)

        print("Results:")
        print(result1)
        print(result2)


    # Starts the event loop and executes the main coroutine.
    asyncio.run(main())

Output:

    Task 1 started
    Task 1 completed
    Task 2 started
    Task 2 completed
    Results:
    Task 1 result
    Task 2 result

The important lesson from this example is:

    async + await
          ↓
    Asynchronous programming

but:

    async + await
          ≠
    automatically concurrent execution

For independent tasks, we need to schedule them concurrently.

---

# 🔑 Key Takeaways

- `async def` defines a coroutine function.
- Calling an async function creates a coroutine object.
- A coroutine can pause and resume.
- `await` creates a suspension point.
- `await` allows the event loop to handle other asynchronous work when the awaited operation is waiting.
- `await` does not automatically make multiple operations concurrent.
- Sequential `await` statements execute one awaited operation before the next.
- `asyncio.sleep()` is asynchronous and cooperates with the event loop.
- `time.sleep()` blocks the current thread.
- `await` normally belongs inside an `async def` function.
- A coroutine can return values.
- Coroutine chaining is useful when one operation depends on another.
- Independent operations can potentially be scheduled concurrently.
- `asyncio.create_task()` and `asyncio.gather()` are important tools for concurrent coroutine execution.
- Async programming is especially useful for I/O-bound AI applications.

---

# 📌 Topic Summary

The core concepts are:

    async
      ↓
    Define coroutine function

    function()
      ↓
    Coroutine object

    await coroutine
      ↓
    Execute / wait for coroutine

    await async_operation
      ↓
    Suspend current coroutine
      ↓
    Event loop handles other work
      ↓
    Coroutine resumes

The most important distinction:

    async
      ↓
    Asynchronous programming

    create_task() / gather()
      ↓
    Concurrent scheduling of independent async work

The next topic will cover **Asyncio Tasks and `asyncio.create_task()`**, including Task objects, `done()`, `result()`, task scheduling, and how multiple coroutines actually run concurrently.


# 🔹 Asyncio Tasks

## 📌 Topic Overview

**An `asyncio` Task is an object that schedules and manages the execution of a coroutine concurrently within the asyncio event loop.**

File:

    18_asyncio_tasks.py

So far we learned:

    async def
        ↓
    Coroutine
        ↓
    await

Now we will learn:

    Coroutine
        ↓
    asyncio.create_task()
        ↓
    Task
        ↓
    Event Loop
        ↓
    Concurrent execution

---

# 🧩 What is an Asyncio Task?

**An asyncio Task is a scheduled coroutine that is managed by the asyncio event loop and can execute concurrently with other asyncio Tasks.**

A coroutine by itself is not automatically scheduled for concurrent execution.

Example:

    coroutine = task()

This creates a coroutine object.

To schedule it as a Task:

    task_object = asyncio.create_task(task())

Conceptually:

    async def task()
          ↓
    Coroutine Function

    task()
          ↓
    Coroutine Object

    asyncio.create_task(...)
          ↓
    Asyncio Task

    Task
      ↓
    Event Loop
      ↓
    Execution

---

# 🔄 Coroutine vs Task

This distinction is extremely important.

| Coroutine | Task |
|---|---|
| Created by calling an `async def` function | Created by scheduling a coroutine |
| Represents asynchronous work | Represents scheduled asynchronous work |
| Not necessarily scheduled yet | Scheduled to run through event loop |
| Can be awaited | Can be awaited |
| Can be converted into a Task | Manages the coroutine execution |
| Basic async building block | Useful for concurrent async execution |

Example:

    coroutine = task()

versus:

    task_object = asyncio.create_task(task())

---

# 🔹 `asyncio.create_task()`

**`asyncio.create_task()` schedules a coroutine to run concurrently as an asyncio Task and returns a Task object representing that execution.**

Syntax:

    task = asyncio.create_task(coroutine())

Example:

    task1 = asyncio.create_task(task("Task 1"))

The Task is now scheduled to run through the event loop.

---

# 💻 Basic Task Example

File:

    18_asyncio_tasks.py

    import asyncio


    async def task(name):
        print(f"{name} started")

        await asyncio.sleep(2)

        print(f"{name} completed")


    async def main():
        task1 = asyncio.create_task(task("Task 1"))
        task2 = asyncio.create_task(task("Task 2"))

        await task1
        await task2


    asyncio.run(main())

Output:

    Task 1 started
    Task 2 started
    Task 1 completed
    Task 2 completed

Both tasks can make progress during the same period of waiting.

---

# 🧠 Why Are Both Tasks Started Before Completion?

Look at:

    task1 = asyncio.create_task(task("Task 1"))
    task2 = asyncio.create_task(task("Task 2"))

The first line schedules Task 1.

The second line schedules Task 2.

The event loop can then execute both.

Conceptually:

    create_task(Task 1)
          ↓
    Task 1 scheduled

    create_task(Task 2)
          ↓
    Task 2 scheduled

    Event Loop
       ↓
    ┌─────────────┐
    │ Task 1      │
    │ Task 2      │
    └─────────────┘
       ↓
    Both begin
       ↓
    Both reach await
       ↓
    Event loop handles waiting
       ↓
    Tasks resume
       ↓
    Complete

---

# 🔄 Execution Flow

Consider:

    async def task(name):
        print(f"{name} started")

        await asyncio.sleep(2)

        print(f"{name} completed")

The flow is approximately:

    Task 1 starts
        ↓
    Task 1 reaches await
        ↓
    Task 2 starts
        ↓
    Task 2 reaches await
        ↓
    Waiting period
        ↓
    Task 1 resumes
        ↓
    Task 1 completes
        ↓
    Task 2 resumes
        ↓
    Task 2 completes

The exact ordering can vary depending on the program and event-loop scheduling.

---

# ⚠️ Important: Task Scheduling ≠ CPU Parallelism

Asyncio Tasks do not automatically mean:

    Task 1 → CPU Core 1
    Task 2 → CPU Core 2

Instead, they normally run through the same event loop.

Conceptually:

    One Thread
        ↓
    Event Loop
        ↓
    Task 1
        ↓
    await
        ↓
    Task 2
        ↓
    await
        ↓
    Task 3

This is asynchronous concurrency rather than CPU parallelism.

---

# 🧩 Why `create_task()` Is Important

Without scheduling:

    await task1()
    await task2()

the operations are sequential.

With:

    task1 = asyncio.create_task(task1())
    task2 = asyncio.create_task(task2())

both operations are scheduled before we wait for their completion.

Then:

    await task1
    await task2

waits for the scheduled Tasks to finish.

This allows independent asynchronous operations to overlap their waiting periods.

---

# 📊 Sequential vs Task-Based Execution

## Sequential

    await task1()
         ↓
    Task 1 completes
         ↓
    await task2()
         ↓
    Task 2 completes

---

## Task-Based

    create_task(task1())
         ↓
    Task 1 scheduled

    create_task(task2())
         ↓
    Task 2 scheduled

         ↓
      Event Loop

    Task 1 ↔ Task 2

         ↓
    await both

This difference is fundamental to asyncio concurrency.

---

# 🔹 Awaiting a Task

Once a Task has been created:

    task1 = asyncio.create_task(task("Task 1"))

we can wait for it:

    await task1

This means:

> Wait until this scheduled Task completes and obtain its result if it returns one.

Example:

    async def task():
        await asyncio.sleep(1)

        return "Completed"


    async def main():
        task1 = asyncio.create_task(task())

        result = await task1

        print(result)

Output:

    Completed

---

# 🧠 Task as a Handle

A Task can be thought of as a **handle to an asynchronous operation**.

For example:

    task1 = asyncio.create_task(download_data())

`task1` gives us an object through which we can:

- Wait for completion
- Check whether it is finished
- Retrieve its result
- Check whether it is running
- Cancel it
- Inspect exceptions

Conceptually:

    Task Object
        │
        ├── done()
        ├── result()
        ├── cancel()
        ├── cancelled()
        ├── exception()
        └── await task

---

# 🔹 `Task.done()`

**`Task.done()` returns `True` if the asyncio Task has finished executing; otherwise, it returns `False`.**

Example:

    import asyncio


    async def task():
        await asyncio.sleep(2)

        return "Task completed"


    async def main():
        task1 = asyncio.create_task(task())

        print("Task completed:", task1.done())

        await task1

        print("Task completed:", task1.done())


    asyncio.run(main())

Output:

    Task completed: False
    Task completed: True

---

# 🔍 Understanding `done()`

Immediately after:

    task1 = asyncio.create_task(task())

the Task has only been scheduled.

It may still be running.

Therefore:

    task1.done()

may return:

    False

After:

    await task1

the Task has completed.

Therefore:

    task1.done()

returns:

    True

---

# 🔄 Task Lifecycle

A simplified Task lifecycle is:

    Created
       ↓
    Scheduled
       ↓
    Running
       ↓
    Waiting at await
       ↓
    Resumed
       ↓
    Completed

A Task can also end through:

    Exception
       ↓
    Failed

or:

    Cancellation
       ↓
    Cancelled

Conceptually:

    ┌──────────┐
    │ Created  │
    └────┬─────┘
         ↓
    ┌──────────┐
    │Scheduled │
    └────┬─────┘
         ↓
    ┌──────────┐
    │ Running  │
    └────┬─────┘
         ↓
    ┌────────────────────┐
    │                    │
    ↓                    ↓
 Completed             Failed
    │
    ↓
   Done

Cancellation can occur before normal completion.

---

# 🔹 `Task.result()`

**`Task.result()` returns the value returned by a completed asyncio Task.**

Example:

    import asyncio


    async def task():
        await asyncio.sleep(1)

        return "Task completed"


    async def main():
        task1 = asyncio.create_task(task())

        await task1

        print("Result:", task1.result())


    asyncio.run(main())

Output:

    Result: Task completed

The important sequence is:

    create_task()
         ↓
    await task
         ↓
    Task completed
         ↓
    task.result()
         ↓
    Returned value

---

# ⚠️ Calling `result()` Too Early

Consider:

    task1 = asyncio.create_task(task())

    print(task1.result())

If the Task has not completed yet, calling `result()` is not the correct way to wait for it.

Instead:

    await task1

should be used when we need to wait.

Then:

    task1.result()

can retrieve the completed value.

---

# 🧠 `await task` vs `task.result()`

These are related but serve different purposes.

### `await task`

Used to:

    Wait for the Task to complete

and obtain its result.

Example:

    result = await task1

---

### `task.result()`

Used to:

    Retrieve the result of an already completed Task.

Example:

    await task1

    result = task1.result()

A simple rule:

    Need to wait?
        ↓
    await task

    Already completed?
        ↓
    task.result()

---

# 🔹 Task Returning a Value

Example:

    import asyncio


    async def calculate(number):
        await asyncio.sleep(1)

        return number * number


    async def main():
        task1 = asyncio.create_task(calculate(5))

        await task1

        print("Result:", task1.result())


    asyncio.run(main())

Output:

    Result: 25

The Task stores the returned value after completion.

---

# 🔹 Multiple Tasks

Multiple independent operations can be scheduled.

Example:

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        task1 = asyncio.create_task(task("Task 1", 2))
        task2 = asyncio.create_task(task("Task 2", 3))
        task3 = asyncio.create_task(task("Task 3", 1))

        result1 = await task1
        result2 = await task2
        result3 = await task3

        print(result1)
        print(result2)
        print(result3)


    asyncio.run(main())

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 3 completed
    Task 1 completed
    Task 2 completed
    Task 1 result
    Task 2 result
    Task 3 result

Notice something important.

Completion order:

    Task 3
    Task 1
    Task 2

But the result retrieval above is:

    Task 1
    Task 2
    Task 3

because we explicitly awaited them in that order.

---

# 🧠 Completion Order vs Result Retrieval Order

These are two different concepts.

### Completion order

Determined by:

- Task duration
- External API response
- I/O readiness
- Scheduling

Example:

    Task 3 → completed first
    Task 1 → completed second
    Task 2 → completed third

---

### Retrieval order

Determined by our code.

Example:

    await task1
    await task2
    await task3

This waits/retrieves them in that sequence.

Therefore:

> **Tasks can complete in one order while the program retrieves their results in another order.**

This distinction becomes especially important when working with multiple API calls.

---

# 🤖 AI Engineering Example

Suppose an AI assistant needs three independent services:

    User API
    Weather API
    News API

Each request can take a different amount of time.

Example:

    User API → 2 seconds
    Weather API → 3 seconds
    News API → 1 second

Create Tasks:

    user_task = asyncio.create_task(call_api("User API", 2))

    weather_task = asyncio.create_task(call_api("Weather API", 3))

    news_task = asyncio.create_task(call_api("News API", 1))

All three can be scheduled before waiting for their completion.

Conceptually:

    User API ──────────→ 2 sec
    Weather API ───────────────→ 3 sec
    News API ─────→ 1 sec

This allows the waiting periods to overlap.

---

# 💻 AI API Simulation

File:

    18_asyncio_tasks.py

    import asyncio


    async def call_api(api_name, delay):
        print(f"{api_name} request started")

        # Simulates waiting for an external API response.
        await asyncio.sleep(delay)

        print(f"{api_name} response received")

        return f"{api_name} data"


    async def main():
        user_task = asyncio.create_task(
            call_api("User API", 2)
        )

        weather_task = asyncio.create_task(
            call_api("Weather API", 3)
        )

        news_task = asyncio.create_task(
            call_api("News API", 1)
        )

        user_data = await user_task
        weather_data = await weather_task
        news_data = await news_task

        print("\nResults:")
        print(user_data)
        print(weather_data)
        print(news_data)


    asyncio.run(main())

Possible output:

    User API request started
    Weather API request started
    News API request started
    News API response received
    User API response received
    Weather API response received

    Results:
    User API data
    Weather API data
    News API data

The exact ordering of log messages can vary.

---

# 🧠 Why This Is Useful for AI Engineers

AI applications frequently need to communicate with several external services.

For example:

    AI Assistant
         │
         ↓
    ┌────┼─────────┐
    ↓    ↓         ↓
   Web  Database  User API
   API    API       API
    │     │         │
    └─────┼─────────┘
          ↓
     Gather Results
          ↓
       LLM
          ↓
     Final Answer

Instead of waiting for:

    Web → Database → User API

one after another, independent requests can potentially be scheduled together.

This can reduce unnecessary waiting time.

---

# 🔹 `Task.cancel()`

**`Task.cancel()` requests cancellation of an asyncio Task that has not yet completed.**

Example:

    task1.cancel()

Cancellation is cooperative.

It does not mean that the Task is forcibly terminated in the same way as killing an operating-system process.

The cancellation request is delivered through the coroutine's asynchronous execution.

---

# 💻 Cancellation Example

    import asyncio


    async def task():
        try:
            print("Task started")

            await asyncio.sleep(5)

            print("Task completed")

        except asyncio.CancelledError:
            print("Task was cancelled")


    async def main():
        task1 = asyncio.create_task(task())

        await asyncio.sleep(1)

        task1.cancel()

        await task1


    asyncio.run(main())

Possible output:

    Task started
    Task was cancelled

The Task does not reach:

    Task completed

because cancellation was requested while it was waiting.

---

# 🔹 `Task.cancelled()`

**`Task.cancelled()` returns `True` if the Task was successfully cancelled.**

Example:

    task1.cancel()

    await task1

    print(task1.cancelled())

Possible output:

    True

This allows us to check whether a Task ended because of cancellation.

---

# 🧠 Cancellation Flow

    Task running
         ↓
    cancel()
         ↓
    Cancellation requested
         ↓
    Coroutine receives cancellation
         ↓
    Cleanup / handling
         ↓
    Task cancelled

Cancellation is useful for:

- User cancelling a request
- Timeout handling
- Unnecessary background work
- Application shutdown
- Stopping expensive operations

---

# 🔹 `Task.exception()`

**`Task.exception()` returns the exception raised by a completed Task, if one occurred.**

Example:

    import asyncio


    async def task():
        await asyncio.sleep(1)

        raise ValueError("Something went wrong")


    async def main():
        task1 = asyncio.create_task(task())

        try:
            await task1
        except ValueError:
            print("Task failed")

        print("Exception:", task1.exception())


    asyncio.run(main())

The Task stores information about the exception after it fails.

---

# ⚠️ Task Exceptions

A Task can finish in different ways:

    Task
      │
      ├── Successful
      │
      ├── Failed with exception
      │
      └── Cancelled

This is why Task objects are useful.

They provide information about the state and outcome of asynchronous work.

---

# 🧠 Task Status Methods

Important methods:

| Method | Purpose |
|---|---|
| `done()` | Checks whether Task has finished |
| `result()` | Retrieves returned value |
| `cancel()` | Requests cancellation |
| `cancelled()` | Checks whether Task was cancelled |
| `exception()` | Retrieves Task exception |

These methods are useful when managing complex asynchronous workflows.

---

# 🔄 Task State Example

Conceptually:

    create_task()
          ↓
       Pending
          ↓
       Running
          ↓
       Awaiting
          ↓
    ┌─────┼─────────┐
    ↓     ↓         ↓
 Success Failed   Cancelled
    ↓     ↓         ↓
   Done  Done      Done

The exact internal scheduling is more nuanced, but this model is useful for understanding Task lifecycle.

---

# ⚠️ Don't Create Tasks Unnecessarily

Not every coroutine needs to become a Task.

If you simply need to execute one asynchronous operation and wait for it:

    result = await task()

is usually sufficient.

Use:

    asyncio.create_task()

when you specifically want to schedule work independently so that it can make progress alongside other asynchronous work.

---

# 📊 `await` vs `create_task()`

| `await` | `create_task()` |
|---|---|
| Waits for an awaitable | Schedules coroutine as a Task |
| Useful for dependencies | Useful for independent work |
| Can be sequential | Allows concurrent scheduling |
| Directly obtains result | Returns Task object |
| `result = await task()` | `task = create_task(task())` |

Example:

    result = await fetch_data()

means:

    Wait for fetch_data()

while:

    task = asyncio.create_task(fetch_data())

means:

    Schedule fetch_data() as a Task.

---

# 🧠 Important Pattern

A common pattern is:

    task1 = asyncio.create_task(operation1())
    task2 = asyncio.create_task(operation2())
    task3 = asyncio.create_task(operation3())

Then:

    result1 = await task1
    result2 = await task2
    result3 = await task3

Conceptually:

    Schedule everything
          ↓
    ┌─────┼─────┐
    ↓     ↓     ↓
   T1    T2    T3
    │     │     │
    └─────┼─────┘
          ↓
       Await
          ↓
       Results

This pattern is particularly useful for independent I/O operations.

---

# 🤖 AI Assistant Example

Imagine an AI assistant receives:

    "Give me a summary using my profile,
     today's weather, and current news."

It could potentially perform:

    Profile API
    Weather API
    News API

concurrently.

Architecture:

    User Request
          ↓
    AI Controller
          ↓
    ┌─────┼────────┐
    ↓     ↓        ↓
 Profile Weather  News
   API     API     API
    ↓       ↓       ↓
    └───────┼───────┘
            ↓
      Collect Results
            ↓
        LLM Prompt
            ↓
       Final Answer

The API requests are independent, so they are good candidates for concurrent async execution.

---

# 🧠 Important Limitation

Asyncio is not a universal solution for every performance problem.

If the program spends most of its time performing CPU-heavy calculations:

    Large numerical computation
    Image processing
    Heavy data transformation
    CPU-intensive algorithms

then simply creating more asyncio Tasks will not automatically provide CPU parallelism.

For CPU-bound workloads, consider:

    multiprocessing
    ProcessPoolExecutor
    NumPy
    specialized native libraries
    GPU-based processing

depending on the workload.

---

# 📌 Final Practical Example

File:

    18_asyncio_tasks.py

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        # Simulates an I/O-bound waiting period.
        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        # Schedule independent coroutines as Tasks so that
        # their waiting periods can overlap.
        task1 = asyncio.create_task(task("Task 1", 2))
        task2 = asyncio.create_task(task("Task 2", 3))
        task3 = asyncio.create_task(task("Task 3", 1))

        # Wait for the scheduled Tasks and collect their results.
        result1 = await task1
        result2 = await task2
        result3 = await task3

        print("\nResults:")
        print(result1)
        print(result2)
        print(result3)


    # Starts the asyncio event loop and executes main().
    asyncio.run(main())

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 3 completed
    Task 1 completed
    Task 2 completed

    Results:
    Task 1 result
    Task 2 result
    Task 3 result

Notice:

    Completion order:
    Task 3 → Task 1 → Task 2

while:

    Result retrieval order:
    Task 1 → Task 2 → Task 3

This demonstrates an important principle:

> **Concurrent tasks may finish in different orders, while our code can still retrieve their results in a specific order.**

---

# 🔑 Key Takeaways

- An asyncio Task represents scheduled asynchronous work.
- `asyncio.create_task()` schedules a coroutine as a Task.
- Tasks are managed by the asyncio event loop.
- Multiple independent Tasks can make progress concurrently.
- `await task` waits for a Task to complete.
- `task.done()` checks whether a Task has finished.
- `task.result()` retrieves the returned value of a completed Task.
- `task.cancel()` requests cancellation.
- `task.cancelled()` checks whether cancellation occurred.
- `task.exception()` retrieves an exception from a failed Task.
- A Task can complete successfully, fail with an exception, or be cancelled.
- Task completion order does not necessarily match the order in which Tasks were created.
- Scheduling Tasks before awaiting them allows independent I/O operations to overlap.
- Asyncio Tasks provide concurrency, not automatic CPU parallelism.
- Tasks are especially useful for API calls, web requests, database operations, and other I/O-bound AI workloads.

---

# 📌 Topic Summary

The basic asyncio Task pattern is:

    Coroutine
        ↓
    asyncio.create_task()
        ↓
    Task
        ↓
    Event Loop
        ↓
    Concurrent execution
        ↓
    await task
        ↓
    Result

The most important distinction is:

    await coroutine
          ↓
    Wait for this operation

    create_task(coroutine)
          ↓
    Schedule this operation
    so it can run alongside other async work

Therefore:

    async + await
        ↓
    Asynchronous programming

    create_task()
        ↓
    Concurrent task scheduling

The next topic will cover **`asyncio.gather()`**, which provides a cleaner way to run multiple awaitables concurrently and collect their results, including exception handling with `return_exceptions=True`.


# 🔹 `asyncio.gather()`

## 📌 Topic Overview

**`asyncio.gather()` runs multiple awaitable objects concurrently and collects their results into a single result sequence.**

File:

    19_asyncio_gather.py

So far we have learned:

    async def
        ↓
    Coroutine
        ↓
    await
        ↓
    asyncio.create_task()
        ↓
    Task

Now we will learn a convenient way to handle multiple asynchronous operations together:

    asyncio.gather()

---

# 🧩 Why Do We Need `asyncio.gather()`?

Suppose an AI application needs to call three independent services:

    User API
    Weather API
    News API

We could manually create Tasks:

    task1 = asyncio.create_task(...)
    task2 = asyncio.create_task(...)
    task3 = asyncio.create_task(...)

and then:

    result1 = await task1
    result2 = await task2
    result3 = await task3

This works, but for multiple independent operations it can become repetitive.

`asyncio.gather()` provides a simpler pattern:

    results = await asyncio.gather(
        operation1(),
        operation2(),
        operation3()
    )

Conceptually:

    ┌─────────────┐
    │ gather()    │
    └──────┬──────┘
           │
      ┌────┼────┐
      ↓    ↓    ↓
     T1   T2   T3
      │    │    │
      └────┼────┘
           ↓
        Results

---

# 🔹 Definition

**`asyncio.gather()` runs multiple awaitable objects concurrently and returns their results together in the order in which the awaitables were provided.**

Syntax:

    results = await asyncio.gather(
        coroutine1(),
        coroutine2(),
        coroutine3()
    )

The important points are:

- Multiple awaitables can be provided.
- They are scheduled to run concurrently.
- `gather()` waits for them.
- Their results are collected together.
- Result order follows the input order.

---

# 💻 Basic Example

File:

    19_asyncio_gather.py

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        results = await asyncio.gather(
            task("Task 1", 2),
            task("Task 2", 2),
            task("Task 3", 2)
        )

        print("Results:", results)


    asyncio.run(main())

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 1 completed
    Task 2 completed
    Task 3 completed
    Results: ['Task 1 result', 'Task 2 result', 'Task 3 result']

All three tasks are allowed to make progress concurrently.

---

# 🔄 Execution Flow

The code:

    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 2),
        task("Task 3", 2)
    )

can be understood as:

    Task 1 ───────────→ Complete
    Task 2 ───────────→ Complete
    Task 3 ───────────→ Complete
            ↓
        gather()
            ↓
         results

The waiting periods overlap.

If each task takes approximately 2 seconds, the total elapsed time can be around 2 seconds rather than:

    2 + 2 + 2 = 6 seconds

The exact runtime depends on the environment and actual operations.

---

# 🧠 `gather()` vs Sequential `await`

## Sequential

    result1 = await task1()
    result2 = await task2()
    result3 = await task3()

Execution:

    Task 1
       ↓
     wait
       ↓
    Task 1 complete
       ↓
    Task 2
       ↓
     wait
       ↓
    Task 2 complete
       ↓
    Task 3
       ↓
     wait
       ↓
    Task 3 complete

If each takes 2 seconds:

    ≈ 6 seconds

---

## `asyncio.gather()`

    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

Execution:

    Task 1 ──────────→
    Task 2 ──────────→
    Task 3 ──────────→
             ↓
          Results

If each takes approximately 2 seconds:

    ≈ 2 seconds

Again, this applies when the tasks are independent and primarily waiting on asynchronous operations.

---

# 🧩 Result Ordering

One of the most important properties of `gather()` is:

> **Results are returned in the same order as the awaitables passed to `gather()`, not necessarily in the order in which they finish.**

Example:

    results = await asyncio.gather(
        task("Task 1", 3),
        task("Task 2", 1),
        task("Task 3", 2)
    )

Completion order may be:

    Task 2
    Task 3
    Task 1

But the result list will be:

    [
        "Task 1 result",
        "Task 2 result",
        "Task 3 result"
    ]

because that is the order in which the operations were supplied.

---

# 🔍 Example: Different Completion Times

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        results = await asyncio.gather(
            task("Task 1", 3),
            task("Task 2", 1),
            task("Task 3", 2)
        )

        print("Results:", results)


    asyncio.run(main())

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 2 completed
    Task 3 completed
    Task 1 completed
    Results: ['Task 1 result', 'Task 2 result', 'Task 3 result']

Notice:

    Completion:
    Task 2 → Task 3 → Task 1

but:

    Results:
    Task 1 → Task 2 → Task 3

This distinction is extremely important when processing concurrent API responses.

---

# 🧠 Why Does `gather()` Preserve Input Order?

Suppose we provide:

    gather(
        API_A(),
        API_B(),
        API_C()
    )

Internally, we can think of the result positions as:

    Position 0 → API_A
    Position 1 → API_B
    Position 2 → API_C

Even if:

    API_C finishes first

its result is still placed at:

    Position 2

Therefore:

    Results[0] → API_A result
    Results[1] → API_B result
    Results[2] → API_C result

---

# 🤖 AI Engineering Example

Imagine an AI assistant that needs:

    User information
    Weather information
    News information

These operations are independent.

We can write:

    import asyncio


    async def call_api(api_name, delay):
        print(f"{api_name} request started")

        await asyncio.sleep(delay)

        print(f"{api_name} response received")

        return f"{api_name} data"


    async def main():
        results = await asyncio.gather(
            call_api("User API", 2),
            call_api("Weather API", 3),
            call_api("News API", 1)
        )

        print("\nResults:")
        print(results)


    asyncio.run(main())

Possible output:

    User API request started
    Weather API request started
    News API request started
    News API response received
    User API response received
    Weather API response received

    Results:
    ['User API data', 'Weather API data', 'News API data']

Notice:

    Completion order:
    News → User → Weather

but:

    Result order:
    User → Weather → News

---

# 🧠 Why `gather()` Is Useful for AI Engineers

Modern AI applications often need information from multiple sources.

For example:

    User Query
         ↓
    AI Controller
         ↓
    ┌────┼──────────┐
    ↓    ↓          ↓
   Web  Database   API
   API    API       API
    │     │          │
    └─────┼──────────┘
          ↓
      gather()
          ↓
    Combined Results
          ↓
        LLM
          ↓
     Final Response

Instead of:

    Web → wait
         ↓
    Database → wait
         ↓
    API → wait

independent operations can be started concurrently.

This can reduce unnecessary waiting time.

---

# 🔹 `gather()` with Returned Values

Each coroutine can return a value.

Example:

    async def square(number):
        await asyncio.sleep(1)

        return number * number


    async def main():
        results = await asyncio.gather(
            square(2),
            square(3),
            square(4)
        )

        print(results)


    asyncio.run(main())

Output:

    [4, 9, 16]

The values are collected into one sequence.

---

# 🔄 Flow of Returned Values

    square(2) → 4
    square(3) → 9
    square(4) → 16

            ↓

       asyncio.gather()

            ↓

       [4, 9, 16]

This makes it convenient to process multiple independent asynchronous operations together.

---

# 🧩 `gather()` vs `create_task()`

Both are important, but their roles are slightly different.

## `create_task()`

Used when you want to explicitly create and manage Task objects.

Example:

    task1 = asyncio.create_task(task("Task 1"))
    task2 = asyncio.create_task(task("Task 2"))

Then:

    result1 = await task1
    result2 = await task2

You can inspect:

    task1.done()
    task1.result()
    task1.cancel()

---

## `gather()`

Useful when you want to execute several awaitables together and collect their results.

Example:

    results = await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

You don't need to manually manage each Task object.

---

# 📊 Comparison

| Feature | `create_task()` | `asyncio.gather()` |
|---|---|---|
| Schedules coroutine | Yes | Yes |
| Returns Task object | Yes | No |
| Collects results | Manually | Automatically |
| Multiple operations | Yes | Yes |
| Individual Task control | Strong | Less direct |
| Cancellation management | Task-based | Group-oriented |
| Simple batch of async work | More code | Very convenient |

A useful rule:

    Need individual Task control?
        ↓
    create_task()

    Need to run multiple awaitables and collect results?
        ↓
    asyncio.gather()

---

# 🧠 Can `gather()` Accept Tasks?

Yes.

For example:

    task1 = asyncio.create_task(task("Task 1", 2))
    task2 = asyncio.create_task(task("Task 2", 3))

Then:

    results = await asyncio.gather(
        task1,
        task2
    )

So `gather()` can work with awaitables such as:

- Coroutines
- Tasks
- Other awaitable objects

---

# 💻 Example with Tasks

    import asyncio


    async def task(name, delay):
        await asyncio.sleep(delay)

        return f"{name} completed"


    async def main():
        task1 = asyncio.create_task(task("Task 1", 2))
        task2 = asyncio.create_task(task("Task 2", 1))

        results = await asyncio.gather(
            task1,
            task2
        )

        print(results)


    asyncio.run(main())

Output:

    ['Task 1 completed', 'Task 2 completed']

The Tasks were created explicitly, and `gather()` collected their results.

---

# ⚠️ Exception Handling

An important part of `asyncio.gather()` is handling exceptions.

Suppose one coroutine fails.

Example:

    import asyncio


    async def task1():
        await asyncio.sleep(1)

        return "Task 1 completed"


    async def task2():
        await asyncio.sleep(1)

        raise ValueError("Something went wrong in Task 2")


    async def task3():
        await asyncio.sleep(1)

        return "Task 3 completed"


    async def main():
        results = await asyncio.gather(
            task1(),
            task2(),
            task3()
        )

        print(results)


    asyncio.run(main())

Here `task2()` raises:

    ValueError

With the default behavior, the exception propagates to the caller of `gather()`.

---

# 🔴 Default Exception Behavior

Conceptually:

    Task 1 → Success
    Task 2 → Exception
    Task 3 → Success

Then:

    gather()
       ↓
    Exception propagated

The calling coroutine can handle it using:

    try:
        ...
    except ValueError:
        ...

Example:

    async def main():
        try:
            results = await asyncio.gather(
                task1(),
                task2(),
                task3()
            )

            print(results)

        except ValueError as error:
            print("Error:", error)

Possible output:

    Error: Something went wrong in Task 2

---

# 🧠 Why Handle Exceptions?

In a real AI application, multiple external operations can fail.

For example:

    Web API → Success
    Database → Success
    Weather API → Failure

If the entire application crashes because one optional service failed, the user experience may be poor.

Therefore, AI applications often need deliberate error handling.

For example:

    Web Search → available
    Weather → unavailable
    LLM → available

The application might still be able to produce a useful response.

---

# 🔹 `return_exceptions=True`

**`return_exceptions=True` causes `asyncio.gather()` to return exceptions as values in the result sequence instead of immediately propagating them as exceptions.**

Syntax:

    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

Now an exception can appear directly in the returned results.

---

# 💻 Example

    import asyncio


    async def task1():
        await asyncio.sleep(1)

        return "Task 1 completed"


    async def task2():
        await asyncio.sleep(1)

        raise ValueError("Something went wrong in Task 2")


    async def task3():
        await asyncio.sleep(1)

        return "Task 3 completed"


    async def main():
        results = await asyncio.gather(
            task1(),
            task2(),
            task3(),
            return_exceptions=True
        )

        print("Results:", results)


    asyncio.run(main())

Output:

    Results: [
        'Task 1 completed',
        ValueError('Something went wrong in Task 2'),
        'Task 3 completed'
    ]

The exception is now an element of the returned result sequence.

---

# 🔍 Understanding `return_exceptions=True`

Without:

    return_exceptions=True

we can think of the behavior as:

    Task 1 → Result
    Task 2 → Exception
                    ↓
                Propagate
                    ↓
                 Caller

With:

    return_exceptions=True

the behavior becomes:

    Task 1 → Result
    Task 2 → Exception Object
    Task 3 → Result
            ↓
         gather()
            ↓
    [Result, Exception, Result]

This allows the caller to inspect each result individually.

---

# 🧠 Checking for Exceptions

If we use:

    return_exceptions=True

we should inspect the results when necessary.

Example:

    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print("Task failed:", result)
        else:
            print("Task succeeded:", result)

Possible output:

    Task succeeded: Task 1 completed
    Task failed: Something went wrong in Task 2
    Task succeeded: Task 3 completed

This pattern can be useful when partial failure is acceptable.

---

# 🤖 AI Engineering Example with Partial Failure

Imagine an AI assistant calls:

    Weather API
    News API
    Search API

Suppose:

    Weather → Success
    News → Failure
    Search → Success

With:

    return_exceptions=True

we can receive:

    [
        Weather Data,
        Exception(...),
        Search Data
    ]

The AI controller can then decide:

    Weather → Use
    News → Ignore or mention unavailable
    Search → Use

and continue processing the successful information.

---

# ⚠️ `return_exceptions=True` Does Not Fix the Error

This is important.

It does not magically repair the failed operation.

It simply changes how the exception is returned.

Without it:

    Exception
       ↓
    Propagates

With it:

    Exception
       ↓
    Returned as a result object

The application still needs to decide what to do with the exception.

---

# 🔄 Exception Handling Strategy

A useful pattern is:

    results = await asyncio.gather(
        operation1(),
        operation2(),
        operation3(),
        return_exceptions=True
    )

    for result in results:

        if isinstance(result, Exception):
            # Handle failure
            ...

        else:
            # Process successful result
            ...

This is especially useful when each operation is independent.

---

# 🧩 Important Difference: `gather()` vs `wait()`

Python's asyncio module also provides:

    asyncio.wait()

However, `gather()` and `wait()` serve different purposes.

### `gather()`

Primarily useful for:

    Run multiple awaitables
          ↓
    Wait for them
          ↓
    Collect their results

### `wait()`

Provides more control over:

    Done tasks
    Pending tasks
    Timeout behavior
    Completion conditions

For many straightforward concurrent operations:

    asyncio.gather()

is simpler.

`asyncio.wait()` is useful when more detailed task-state control is required.

---

# 🧠 `gather()` and Dependencies

`gather()` is best suited to operations that can proceed independently.

Good example:

    Weather API
    News API
    Search API

These can often run concurrently.

But if:

    Task B needs Task A's result

then they cannot simply be treated as fully independent.

Example:

    Login
      ↓
    Get User ID
      ↓
    Get User Profile

Here:

    Get User ID

depends on:

    Login

and:

    Get User Profile

depends on:

    User ID

So the dependency chain must be respected.

---

# 🤖 AI Pipeline Example

Independent:

    Query Expansion
         │
    ┌────┼────┐
    ↓    ↓    ↓
   Web  Vector DB  Metadata
    │    │    │
    └────┼────┘
         ↓
       Gather
         ↓
     Combined Data

Dependent:

    Retrieve Documents
          ↓
    Build Context
          ↓
    Send to LLM
          ↓
    Generate Answer

A good AI Engineer needs to recognize which operations are independent and which are dependent.

---

# ⏱️ Performance Example

Suppose:

    API 1 → 2 seconds
    API 2 → 3 seconds
    API 3 → 1 second

Sequential execution:

    2 + 3 + 1
       =
      6 seconds

Concurrent execution using `gather()`:

    max(2, 3, 1)
       =
      3 seconds

This is an idealized model.

Real-world performance can be affected by:

- Network latency
- Server response time
- Connection setup
- CPU processing
- Serialization
- Rate limits
- Event-loop overhead
- Retries
- Local system load

So `gather()` does not guarantee a specific speedup.

---

# 💻 Complete Practical Example

File:

    19_asyncio_gather.py

    import asyncio


    async def task(name, delay):
        print(f"{name} started")

        # Simulates an I/O-bound waiting period.
        await asyncio.sleep(delay)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        # Run independent async operations concurrently
        # and collect their results in input order.
        results = await asyncio.gather(
            task("Task 1", 2),
            task("Task 2", 3),
            task("Task 3", 1)
        )

        print("\nResults:")
        print(results)


    # Starts the asyncio event loop and executes main().
    asyncio.run(main())

Possible output:

    Task 1 started
    Task 2 started
    Task 3 started
    Task 3 completed
    Task 1 completed
    Task 2 completed

    Results:
    ['Task 1 result', 'Task 2 result', 'Task 3 result']

The important observation is:

    Start order:
    Task 1 → Task 2 → Task 3

    Completion order:
    Task 3 → Task 1 → Task 2

    Result order:
    Task 1 → Task 2 → Task 3

This demonstrates the difference between scheduling, completion, and result ordering.

---

# 🤖 Complete AI API Simulation

A more realistic AI-style example:

    import asyncio


    async def call_api(api_name, delay):
        print(f"{api_name} request started")

        # Simulates waiting for an external API response.
        await asyncio.sleep(delay)

        print(f"{api_name} response received")

        return f"{api_name} data"


    async def main():
        results = await asyncio.gather(
            call_api("User API", 2),
            call_api("Weather API", 3),
            call_api("News API", 1)
        )

        print("\nAll API responses:")
        print(results)


    asyncio.run(main())

Possible output:

    User API request started
    Weather API request started
    News API request started
    News API response received
    User API response received
    Weather API response received

    All API responses:
    ['User API data', 'Weather API data', 'News API data']

This simulates an AI assistant obtaining information from multiple independent services concurrently.

---

# 🧠 `create_task()` vs `gather()` in AI Applications

Consider three API calls.

### Explicit Task Management

    user_task = asyncio.create_task(
        call_api("User API", 2)
    )

    weather_task = asyncio.create_task(
        call_api("Weather API", 3)
    )

    news_task = asyncio.create_task(
        call_api("News API", 1)
    )

    user_data = await user_task
    weather_data = await weather_task
    news_data = await news_task

This provides individual Task objects.

---

### `gather()`

    results = await asyncio.gather(
        call_api("User API", 2),
        call_api("Weather API", 3),
        call_api("News API", 1)
    )

This is shorter and convenient when we mainly want all the results together.

---

# 📊 Practical Choice

| Requirement | Suitable approach |
|---|---|
| One async operation | `await` |
| Multiple independent operations + collect results | `asyncio.gather()` |
| Need individual Task objects | `asyncio.create_task()` |
| Need task state monitoring | `create_task()` |
| Need cancellation of individual Tasks | `create_task()` |
| Need partial failure results | `gather(..., return_exceptions=True)` |
| Need detailed done/pending control | `asyncio.wait()` |

---

# ⚠️ Common Beginner Mistakes

## Mistake 1: Assuming `gather()` Means Parallel CPU Execution

Incorrect idea:

    gather()
       ↓
    Multiple CPU cores

Actually:

    gather()
       ↓
    Async concurrency
       ↓
    Event Loop

It is especially useful for I/O-bound asynchronous operations.

---

## Mistake 2: Forgetting `await`

Incorrect:

    results = asyncio.gather(
        task1(),
        task2()
    )

Correct:

    results = await asyncio.gather(
        task1(),
        task2()
    )

when inside an async function.

---

## Mistake 3: Using `gather()` for Dependent Tasks

If:

    Task B depends on Task A

then simply placing both into `gather()` does not automatically create the required dependency.

The dependency should be handled explicitly.

---

## Mistake 4: Ignoring Exceptions

If one operation can fail, decide whether you want:

    Exception propagation

or:

    return_exceptions=True

depending on the application's requirements.

---

# 🤖 AI Engineer Relevance

`asyncio.gather()` is highly useful in AI systems that perform multiple independent I/O operations.

Examples:

### AI Research Assistant

    Web Search 1
    Web Search 2
    Web Search 3
          ↓
       gather()
          ↓
    Search Results
          ↓
         LLM

### RAG System

    Query Embedding
         ↓
    Vector Search
         ↓
    Retrieve Documents

Independent metadata or external service calls can sometimes be performed concurrently around the retrieval workflow.

### AI Agent

    Tool 1
    Tool 2
    Tool 3
          ↓
       gather()
          ↓
    Tool Results
          ↓
    Agent Reasoning

The exact concurrency strategy depends on whether the tools are independent and whether their underlying libraries support asynchronous execution.

---

# 🔑 Key Takeaways

- `asyncio.gather()` runs multiple awaitables concurrently.
- It waits for the supplied awaitables and collects their results.
- Results are returned in input order.
- Completion order may be different from result order.
- `gather()` is especially useful for independent I/O-bound operations.
- `create_task()` provides more direct control over individual Task objects.
- `gather()` is convenient when we primarily want a combined collection of results.
- `return_exceptions=True` returns exceptions as result objects instead of immediately propagating them.
- `return_exceptions=True` does not fix errors; it changes how they are delivered.
- Independent operations are good candidates for `gather()`.
- Dependent operations should respect their dependency chain.
- `gather()` provides asynchronous concurrency, not automatic CPU parallelism.
- AI applications can use `gather()` for concurrent API calls, searches, database operations, and external tool calls.
- Proper exception handling is essential in production AI applications.

---

# 📌 Topic Summary

The core pattern is:

    async operation 1
    async operation 2
    async operation 3
           ↓
    asyncio.gather()
           ↓
    Concurrent execution
           ↓
    Wait for all
           ↓
    Collect results
           ↓
    [result1, result2, result3]

With exception handling:

    asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

can produce:

    [
        successful_result,
        Exception(...),
        successful_result
    ]

The most important concept from this topic is:

> **`asyncio.gather()` is a convenient way to execute independent asynchronous operations concurrently and collect their results while preserving the order of the supplied awaitables.**

This completes the core `asyncio.gather()` concept. The next section will move to **I/O-bound vs CPU-bound tasks**, where we will connect everything learned so far and understand when to use `asyncio`, `ThreadPoolExecutor`, `multiprocessing`, and `ProcessPoolExecutor`.


# 🔹 I/O-Bound vs CPU-Bound Tasks

## 📌 Topic Overview

**An I/O-bound task spends most of its time waiting for input/output operations, while a CPU-bound task spends most of its time performing computations using the CPU.**

File:

    20_io_bound_vs_cpu_bound.py

Understanding this difference is extremely important because the type of workload helps us decide which concurrency technique is appropriate.

The basic idea is:

    I/O-bound
        ↓
    Mostly waiting
        ↓
    asyncio / Threading

    CPU-bound
        ↓
    Mostly computing
        ↓
    Multiprocessing / ProcessPoolExecutor

This is not an absolute rule, but it is a very useful practical guideline.

---

# 🧩 What is I/O?

**I/O stands for Input/Output and refers to operations where a program communicates with something outside its immediate computation.**

Examples include:

- Network requests
- API calls
- Database queries
- Reading files
- Writing files
- Downloading data
- Uploading data
- Waiting for external services
- User input

Conceptually:

    Python Program
          │
          ↓
    External Resource
          │
          ↓
    Wait for response
          │
          ↓
    Continue processing

The waiting time is an important part of I/O operations.

---

# 🔹 What is an I/O-Bound Task?

**An I/O-bound task spends most of its execution time waiting for input/output operations rather than performing computation.**

Examples:

    API request
    Database query
    File download
    Network request
    Cloud service request

For example:

    Send API request
          ↓
       WAIT...
          ↓
       WAIT...
          ↓
    Response received
          ↓
    Process response

During the waiting period, the CPU may not be doing significant computation for that particular task.

---

# 🌐 Real-World I/O Examples

### API Request

    Application
         ↓
      API call
         ↓
       Network
         ↓
      Server
         ↓
      Response
         ↓
    Application

### Database Query

    Application
         ↓
      Database
         ↓
       WAIT...
         ↓
      Results
         ↓
    Application

### File Reading

    Application
         ↓
      File System
         ↓
       WAIT...
         ↓
       Data
         ↓
    Application

All of these can involve significant waiting.

---

# 💻 Simulating an I/O-Bound Task

File:

    20_io_bound_vs_cpu_bound.py

    import time


    def io_task():
        print("I/O task started")

        # Simulates waiting for an external I/O operation.
        time.sleep(2)

        print("I/O task completed")


    start = time.time()

    io_task()

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

Possible output:

    I/O task started
    I/O task completed
    Time taken: 2.00 seconds

Here:

    time.sleep(2)

is being used only to simulate a waiting period.

It is not performing an actual network or file operation.

---

# ⚠️ Important Clarification About `time.sleep()`

`time.sleep()` itself is not an I/O operation.

It simply pauses the current thread.

We use it in demonstrations because it provides a simple way to simulate:

    "The program is waiting for something."

For example, an actual API request might behave conceptually like:

    Send request
         ↓
    Wait for server
         ↓
    Receive response

We can simulate that waiting using:

    time.sleep(2)

But real applications would use an HTTP client or another appropriate I/O library.

---

# 🔹 What is CPU-Bound?

**A CPU-bound task spends most of its execution time performing computations that require significant CPU processing.**

Examples:

- Large mathematical calculations
- Complex algorithms
- Image processing
- Video processing
- Data transformation
- Numerical computation
- CPU-heavy preprocessing
- Some machine learning preprocessing operations

Conceptually:

    Input Data
        ↓
    CPU Computation
        ↓
    CPU Computation
        ↓
    CPU Computation
        ↓
    Result

The task spends most of its time actively using the CPU rather than waiting for an external resource.

---

# 💻 CPU-Bound Example

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

Possible output:

    CPU task started
    CPU task completed
    Time taken: 0.33 seconds

The exact timing will vary depending on the computer and system load.

This is only a demonstration, not a proper CPU benchmark.

---

# 🧠 Why Is the CPU Example Different?

In:

    for i in range(10_000_000):
        total += i

the processor is repeatedly performing calculations.

The program is not primarily waiting for:

    Network
    Database
    Disk
    External API

Instead, it is spending time doing computation.

Therefore, this is a CPU-bound workload.

---

# 📊 I/O-Bound vs CPU-Bound

| Feature | I/O-Bound | CPU-Bound |
|---|---|---|
| Main bottleneck | Waiting for I/O | CPU computation |
| CPU usage | Often lower while waiting | Often high |
| Examples | APIs, DB, network | Computation, image processing |
| Asyncio | Often useful | Usually not enough by itself |
| Threading | Often useful | Limited for pure Python CPU work |
| Multiprocessing | Usually unnecessary | Often useful |
| ProcessPoolExecutor | Usually unnecessary | Often useful |
| Main challenge | Waiting | Computation |

---

# 🔄 Visual Comparison

## I/O-Bound

    CPU
     │
     ├── Request
     │
     ├── WAIT ──────────────┐
     │                      │
     │                      ↓
     │                 Response
     │                      │
     └──────────────────────┘

The program spends significant time waiting.

---

## CPU-Bound

    CPU
     │
     ├── Calculate
     ├── Calculate
     ├── Calculate
     ├── Calculate
     ├── Calculate
     └── Result

The CPU remains busy performing computation.

---

# 🧠 Why Does This Difference Matter?

Because different concurrency techniques are optimized for different types of work.

For example:

    API Calls
       ↓
    I/O-bound
       ↓
    asyncio
       or
    ThreadPoolExecutor

While:

    Heavy Computation
       ↓
    CPU-bound
       ↓
    ProcessPoolExecutor
       or
    multiprocessing

Choosing the wrong model can provide little benefit or even make the program more complicated.

---

# 🔹 I/O-Bound + `asyncio`

`asyncio` is particularly useful when many operations spend time waiting.

Example:

    async def call_api(name):
        print(f"{name} started")

        await asyncio.sleep(2)

        print(f"{name} completed")

Suppose we have:

    API 1
    API 2
    API 3

Using:

    asyncio.gather()

we can allow their waiting periods to overlap.

Conceptually:

    API 1 ──────────→
    API 2 ──────────→
    API 3 ──────────→
             ↓
         Results

---

# 💻 I/O-Bound with `asyncio`

    import asyncio


    async def api_call(name):
        print(f"{name} started")

        await asyncio.sleep(2)

        print(f"{name} completed")

        return f"{name} result"


    async def main():
        results = await asyncio.gather(
            api_call("API 1"),
            api_call("API 2"),
            api_call("API 3")
        )

        print(results)


    asyncio.run(main())

If each operation waits approximately two seconds, the total elapsed time can be around two seconds rather than six seconds, assuming the operations are independent and the simulated waits dominate the runtime.

---

# 🔹 I/O-Bound + ThreadPoolExecutor

Sometimes we have a blocking library that does not provide an async interface.

For example, suppose a function performs blocking I/O:

    def download_data():
        # Blocking operation
        ...

A thread pool can allow several such blocking operations to proceed concurrently.

Conceptually:

    Thread 1 → API 1 → Waiting
    Thread 2 → API 2 → Waiting
    Thread 3 → API 3 → Waiting

This can be useful when the library or operation is synchronous.

---

# 🧠 `asyncio` vs ThreadPoolExecutor for I/O

Both can be useful for I/O-bound workloads.

### `asyncio`

Best suited when:

- The library supports async operations.
- The application is already asynchronous.
- Many concurrent operations are expected.
- You want event-loop-based concurrency.

### ThreadPoolExecutor

Useful when:

- The operation is blocking.
- The library is synchronous.
- An async equivalent is unavailable or inconvenient.
- You want to run blocking functions concurrently.

Example:

    Async API
        ↓
    asyncio

    Blocking API
        ↓
    ThreadPoolExecutor

This is a practical guideline rather than a strict rule.

---

# 🔹 CPU-Bound + Multiprocessing

CPU-heavy tasks can benefit from multiple processes.

Example:

    Process 1 → CPU Core
    Process 2 → CPU Core
    Process 3 → CPU Core
    Process 4 → CPU Core

Each process has its own Python interpreter and memory space.

This allows CPU-bound work to use multiple CPU cores when the workload and system support it.

---

# 💻 CPU-Bound with ProcessPoolExecutor

Example:

    from concurrent.futures import ProcessPoolExecutor


    def square(number):
        total = 0

        for i in range(5_000_000):
            total += i

        return total + number


    if __name__ == "__main__":
        numbers = [1, 2, 3, 4]

        with ProcessPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(square, numbers))

        print(results)

The exact performance depends on:

- CPU cores
- Operating system
- Task size
- Process creation overhead
- Serialization
- Other system activity

---

# 🧠 Why Processes Help CPU-Bound Python Code

In standard CPython, the **Global Interpreter Lock (GIL)** limits multiple threads from executing Python bytecode simultaneously within a single interpreter in the way that many people expect for CPU-bound work.

Processes use separate Python interpreter processes.

Conceptually:

    Process 1
    Python Interpreter
         ↓
       CPU


    Process 2
    Python Interpreter
         ↓
       CPU


    Process 3
    Python Interpreter
         ↓
       CPU

Therefore, multiprocessing can provide true process-level CPU parallelism.

---

# ⚠️ Important GIL Clarification

The GIL is relevant primarily to standard CPython's execution of Python bytecode.

It does not mean:

> "Python can never use multiple CPU cores."

Python programs can use multiple CPU cores through:

- Multiprocessing
- ProcessPoolExecutor
- Native libraries that release the GIL
- NumPy and other optimized libraries
- GPU-based frameworks

The correct idea is:

    CPU-bound pure Python
          ↓
    Threads may not provide
    expected CPU parallelism
          ↓
    Processes can provide
    process-level parallelism

---

# 🧠 Why Asyncio Is Usually Not the Solution for CPU-Bound Work

Suppose:

    async def heavy_computation():
        for i in range(100_000_000):
            ...
    
There is no meaningful asynchronous waiting in the loop.

The event loop needs opportunities to switch between tasks.

If one coroutine performs a long CPU-heavy operation without yielding:

    Coroutine
       ↓
    Heavy CPU work
       ↓
    Event Loop blocked
       ↓
    Other async tasks cannot
    make normal progress

Therefore, simply writing:

    async def

does not make CPU-heavy computation asynchronous in a useful way.

---

# 🔄 CPU-Bound vs I/O-Bound Mental Model

Ask:

> "Is my program mostly waiting or mostly calculating?"

If:

    Mostly WAITING
          ↓
       I/O-bound

If:

    Mostly CALCULATING
          ↓
       CPU-bound

Then choose an appropriate approach.

---

# 🧩 Practical Decision Tree

    What is the task doing?
             │
       ┌─────┴─────┐
       ↓           ↓
    Waiting      Computing
       │           │
       ↓           ↓
    I/O-bound    CPU-bound
       │           │
    ┌──┴──┐      ┌─┴─────────┐
    ↓     ↓      ↓           ↓
 asyncio Threads Processes ProcessPool
                         Executor

This is a simplified decision guide.

---

# 📊 Concurrency Decision Table

| Workload | First options to consider |
|---|---|
| Async HTTP requests | `asyncio` |
| Many async API calls | `asyncio.gather()` |
| Blocking HTTP library | `ThreadPoolExecutor` |
| Blocking file operations | Threads may help |
| Database with async driver | `asyncio` |
| CPU-heavy pure Python | `ProcessPoolExecutor` |
| CPU-heavy independent tasks | `multiprocessing` |
| Mixed async + CPU-heavy work | `asyncio` + process-based workers |
| GPU-heavy ML | GPU framework / optimized libraries |

The actual choice depends on the specific application and libraries.

---

# 🤖 AI Engineering Applications

Understanding I/O-bound and CPU-bound workloads is particularly important in AI Engineering.

Modern AI systems often combine both.

For example:

    AI Assistant
         │
         ├── Web Search
         │      ↓
         │   I/O-bound
         │
         ├── Database Query
         │      ↓
         │   I/O-bound
         │
         ├── LLM API
         │      ↓
         │   I/O-bound
         │
         └── Data Processing
                ↓
             CPU-bound

Different parts of the same application can therefore use different concurrency strategies.

---

# 🤖 Example: AI Assistant

Suppose an AI assistant receives:

    "Research this topic and summarize it."

It may perform:

    1. Web Search
    2. Database Search
    3. Document Retrieval
    4. Text Processing
    5. LLM Request

A possible classification:

    Web Search
       ↓
    I/O-bound


    Database Search
       ↓
    I/O-bound


    Document Retrieval
       ↓
    I/O-bound


    Text Processing
       ↓
    Depends on workload


    LLM API
       ↓
    I/O-bound

The architecture could therefore combine:

    asyncio
       +
    ThreadPoolExecutor
       +
    ProcessPoolExecutor
       +
    Specialized ML libraries

when appropriate.

---

# 🧠 Mixed Workload Architecture

A more realistic AI system might look like:

    ┌───────────────────────────────┐
    │        AI Application         │
    └───────────────┬───────────────┘
                    ↓
              Async Controller
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       Web API    Database   LLM API
          │         │         │
          └─────────┼─────────┘
                    ↓
              Gather Results
                    ↓
             Data Processing
                    ↓
             Process Pool
                    ↓
              Final Context
                    ↓
                  LLM
                    ↓
              Final Response

The actual architecture depends on the application.

---

# ⚠️ Concurrency Has Overhead

Concurrency is not automatically faster.

Every technique has some overhead.

### Threads

Possible overhead:

- Thread creation
- Scheduling
- Synchronization
- Context switching

### Processes

Possible overhead:

- Process creation
- Memory
- Serialization
- Inter-process communication

### Asyncio

Possible overhead:

- Coroutine scheduling
- Event-loop management
- Async-compatible architecture

Therefore:

> **Concurrency should be used where it solves an actual waiting or computation bottleneck.**

---

# 🧠 Small Tasks May Become Slower

Suppose a CPU task takes only:

    0.001 seconds

Creating processes to run thousands of such tiny tasks may cost more than simply executing them sequentially.

Conceptually:

    Task execution
       ↓
    0.001 sec

but:

    Process overhead
       ↓
    0.010 sec

Then concurrency may actually make the overall program slower.

This is why task granularity matters.

---

# 🔹 Task Granularity

**Task granularity refers to the amount of work contained in each individual task submitted to a concurrency system.**

Large enough tasks:

    Task 1 ───────────────
    Task 2 ───────────────
    Task 3 ───────────────

may justify concurrency.

Very small tasks:

    T1 T2 T3 T4 T5 T6 T7...

may suffer from scheduling and communication overhead.

Therefore:

    More tasks
       ≠
    Automatically faster

---

# 🧠 I/O-Bound Example in AI

Imagine:

    20 API requests

Sequential:

    Request 1 → wait
    Request 2 → wait
    Request 3 → wait
    ...
    Request 20 → wait

With asynchronous concurrency:

    Request 1 ────────→
    Request 2 ────────→
    Request 3 ────────→
       ...
    Request 20 ───────→

The network waiting periods can overlap.

This is one of the most common practical reasons AI engineers use asynchronous programming.

---

# 🧠 CPU-Bound Example in AI

Suppose an application needs to preprocess thousands of independent images.

Conceptually:

    Image 1 → Resize → Normalize
    Image 2 → Resize → Normalize
    Image 3 → Resize → Normalize
    Image 4 → Resize → Normalize

If preprocessing is CPU-heavy, independent images can potentially be distributed among worker processes.

    Process 1 → Image 1
    Process 2 → Image 2
    Process 3 → Image 3
    Process 4 → Image 4

However, many production ML libraries already provide optimized parallelism, vectorization, or native implementations, so the best solution depends on the actual workload.

---

# ⚠️ Not Every ML Task Is CPU-Bound

Machine learning workloads can involve:

- CPU
- GPU
- Memory
- Disk
- Network
- Database
- External APIs

For example:

    Training neural network
        ↓
    GPU-heavy

while:

    Download training data
        ↓
    I/O-bound

and:

    Python preprocessing loop
        ↓
    Potentially CPU-bound

Therefore, identify the actual bottleneck rather than automatically choosing multiprocessing.

---

# 🔍 How to Identify the Bottleneck

Ask these questions:

### Question 1

> Is the program waiting for an external resource?

If yes:

    I/O-bound

---

### Question 2

> Is the CPU continuously performing calculations?

If yes:

    CPU-bound

---

### Question 3

> Is the workload GPU-heavy?

Then:

    GPU-based optimization
    may be more relevant.

---

### Question 4

> Is the task too small to justify concurrency?

If yes:

    Sequential execution
    may be simpler and faster.

---

# 🧠 Measurement Matters

Do not assume a concurrency technique is faster.

Measure the actual application.

Basic timing:

    import time

    start = time.perf_counter()

    # Code being measured

    end = time.perf_counter()

    print(f"Time taken: {end - start:.4f} seconds")

`time.perf_counter()` is generally preferable to `time.time()` for measuring elapsed durations in performance experiments.

---

# 📊 Comparing Approaches

A simplified model:

| Workload | Sequential | Threads | Asyncio | Processes |
|---|---|---|---|---|
| Single API request | Simple | Unnecessary | Unnecessary | Unnecessary |
| Many blocking API requests | Slow | Useful | Possible with adapters/async APIs | Usually unnecessary |
| Many async API requests | Simple but sequential | Possible | Very suitable | Usually unnecessary |
| CPU-heavy Python tasks | Often slow | Limited CPU parallelism | Usually unsuitable | Often suitable |
| Tiny tasks | Often simplest | May add overhead | May add overhead | May add high overhead |
| GPU-heavy ML | Depends | Usually not main solution | Usually not main solution | Depends |

This table is a guideline, not a universal rule.

---

# 🧠 Complete Concurrency Decision Guide

A practical decision process:

    Step 1
       ↓
    Identify bottleneck
       ↓
    ┌───────────────┐
    │               │
    ↓               ↓
   I/O             CPU
    │               │
    ↓               ↓
 Is async API    Heavy Python
 available?      computation?
    │               │
   Yes             Yes
    ↓               ↓
 asyncio       Process-based
                   workers

If the I/O library is blocking:

    Blocking I/O
         ↓
    ThreadPoolExecutor
    may be useful

If the workload is GPU-based:

    GPU computation
         ↓
    Use appropriate
    GPU/ML framework

---

# 🤖 AI Engineer Decision Guide

For an AI Engineer, remember:

    🌐 API / Network
          ↓
       I/O-bound
          ↓
       asyncio


    🗄️ Database
          ↓
       I/O-bound
          ↓
    async DB driver
    or threads


    📁 Blocking file operations
          ↓
       I/O-bound
          ↓
       Threads may help


    🧮 Heavy Python computation
          ↓
       CPU-bound
          ↓
    ProcessPoolExecutor


    🖼️ CPU-heavy preprocessing
          ↓
       CPU-bound
          ↓
    Process pool / optimized library


    🧠 Deep Learning
          ↓
       Often GPU-heavy
          ↓
    PyTorch / CUDA / optimized framework

---

# 🧩 Complete Practical Example

File:

    20_io_bound_vs_cpu_bound.py

    import time


    def io_task():
        print("I/O task started")

        # Simulates waiting for an external operation.
        time.sleep(2)

        print("I/O task completed")


    def cpu_task():
        print("CPU task started")

        total = 0

        # Performs repeated calculations to simulate
        # CPU-bound work.
        for i in range(10_000_000):
            total += i

        print("CPU task completed")


    # Measure the simulated I/O-bound operation.
    start = time.perf_counter()

    io_task()

    end = time.perf_counter()

    print(f"I/O time: {end - start:.2f} seconds")


    # Measure the CPU-bound operation.
    start = time.perf_counter()

    cpu_task()

    end = time.perf_counter()

    print(f"CPU time: {end - start:.2f} seconds")

Possible output:

    I/O task started
    I/O task completed
    I/O time: 2.00 seconds

    CPU task started
    CPU task completed
    CPU time: 0.33 seconds

The exact CPU timing will vary significantly between systems.

The purpose of the example is to understand the difference in workload type, not to compare the numerical timings.

---

# 🧠 Important Observation

The output might make it look like:

    CPU task = faster
    I/O task = slower

But that conclusion would be incorrect.

Why?

Because the examples perform completely different amounts and types of work.

The important question is not:

> Which took fewer seconds?

The important question is:

> What is the program spending its time doing?

In the I/O example:

    Waiting

In the CPU example:

    Computing

---

# 🔑 Key Takeaways

- I/O-bound tasks spend significant time waiting for input/output operations.
- CPU-bound tasks spend significant time performing computations.
- API calls are commonly I/O-bound.
- Database queries are commonly I/O-bound.
- Network communication is commonly I/O-bound.
- File operations can be I/O-bound.
- Heavy calculations can be CPU-bound.
- Image and video processing can be CPU-bound, although optimized libraries may use native code or GPUs.
- `asyncio` is particularly useful for async I/O-bound workloads.
- `ThreadPoolExecutor` can be useful for blocking I/O.
- `ProcessPoolExecutor` is often useful for CPU-bound Python workloads.
- Multiprocessing can provide process-level CPU parallelism.
- `asyncio` does not automatically provide CPU parallelism.
- `async def` alone does not make CPU-heavy code asynchronous in a useful way.
- Blocking code inside an event loop can prevent other async tasks from making progress.
- Concurrency introduces overhead.
- Very small tasks may not benefit from concurrency.
- Task granularity matters.
- Always consider the actual bottleneck before choosing a concurrency technique.
- Many AI applications contain both I/O-bound and CPU-bound components.
- GPU-heavy workloads require different optimization strategies.
- Measuring real performance is better than assuming concurrency will be faster.

---

# 📌 Final Concurrency Decision Table

| Situation | Recommended starting point |
|---|---|
| One simple operation | Sequential code |
| Many async API calls | `asyncio` + `gather()` |
| Many independent async operations | `asyncio` |
| Blocking network/API library | `ThreadPoolExecutor` |
| Blocking I/O functions | `ThreadPoolExecutor` may help |
| Heavy CPU-bound Python work | `ProcessPoolExecutor` |
| Multiple CPU-heavy independent tasks | `multiprocessing` |
| GPU-heavy ML workload | GPU/ML framework |
| Very small tasks | Sequential execution may be better |
| Mixed AI workload | Combine techniques based on each component |

---

# 📌 Topic Summary

The fundamental question is:

    What is my program mostly doing?

              │
       ┌──────┴──────┐
       ↓             ↓
    Waiting       Computing
       ↓             ↓
    I/O-bound     CPU-bound
       ↓             ↓
    asyncio       Processes
       │             │
    Threads        ProcessPool
    for blocking   Executor
    I/O

For AI Engineering:

    APIs
    Web Search
    Databases
    External Services
          ↓
       I/O-bound
          ↓
       asyncio


    CPU-heavy preprocessing
    Heavy Python calculations
    Independent computation
          ↓
       CPU-bound
          ↓
    ProcessPoolExecutor


    Deep Learning
          ↓
    Often GPU-heavy
          ↓
    PyTorch / CUDA / optimized libraries

The most important lesson is:

> **Do not choose a concurrency technique first. Identify the workload and bottleneck first, then choose the technique that matches it.**

This completes the **I/O-bound vs CPU-bound** section and gives us the foundation for the final section of Chapter 14: **Concurrency in AI Engineering**, where all these concepts will be connected to practical AI applications such as API calls, web search, databases, LLM requests, and AI assistants.


# 🤖 Concurrency in AI Engineering

## 📌 Topic Overview

**Concurrency in AI Engineering allows an application to handle multiple independent tasks efficiently, especially when those tasks involve waiting for APIs, databases, files, web services, or other external resources.**

File:

    21_ai_engineer_concurrency.py

Throughout Chapter 14, we learned:

    Threading
        ↓
    Locks
        ↓
    Multiprocessing
        ↓
    Process
        ↓
    Process Pool
        ↓
    Queue / IPC
        ↓
    concurrent.futures
        ↓
    Future
        ↓
    ThreadPoolExecutor
        ↓
    ProcessPoolExecutor
        ↓
    asyncio
        ↓
    async / await
        ↓
    asyncio Tasks
        ↓
    asyncio.gather()
        ↓
    I/O-bound vs CPU-bound

Now we will connect these concepts to **real AI Engineering workflows**.

---

# 🎯 Why Concurrency Matters in AI Engineering

Modern AI applications rarely perform only one operation.

An AI system may need to:

- Call an LLM API
- Search the web
- Query a database
- Search a vector database
- Read documents
- Call external tools
- Retrieve user information
- Fetch weather or other external data
- Process files
- Generate embeddings
- Run model inference
- Communicate with multiple services

Many of these operations are independent.

For example:

    User Request
         ↓
    AI Controller
         ↓
    ┌────┼──────────┐
    ↓    ↓          ↓
   Web  Database   APIs
   API    API       API
    │     │          │
    └─────┼──────────┘
          ↓
      Combine Data
          ↓
          LLM
          ↓
      Final Answer

Concurrency allows independent operations to make progress without unnecessarily waiting for each other.

---

# 🧠 AI Application Without Concurrency

Imagine an AI assistant needs:

    1. User data
    2. Weather data
    3. News data

Sequential execution:

    User API
       ↓
     Wait
       ↓
    Weather API
       ↓
     Wait
       ↓
    News API
       ↓
     Wait
       ↓
    Combine results

If the API calls take approximately:

    User API     → 2 sec
    Weather API  → 3 sec
    News API     → 1 sec

The idealized sequential waiting time is:

    2 + 3 + 1
        =
       6 sec

---

# ⚡ AI Application With Concurrency

The independent requests can potentially be started together:

    User API ─────────────→ 2 sec
    Weather API ─────────────────→ 3 sec
    News API ───────→ 1 sec

The idealized waiting time becomes approximately:

    max(2, 3, 1)
        =
       3 sec

The actual application may take longer because of:

- Network overhead
- Server latency
- Connection setup
- Serialization
- Rate limits
- Retries
- CPU processing
- Scheduling overhead

So concurrency does not guarantee a specific speedup.

---

# 🌐 Use Case 1: Concurrent API Calls

One of the most common AI Engineering use cases is calling multiple APIs.

Example:

    User API
    Weather API
    News API
    Search API

These are generally I/O-bound operations.

Therefore:

    asyncio
        +
    asyncio.gather()

can be useful when asynchronous API clients are available.

---

# 💻 API Call Simulation

File:

    21_ai_engineer_concurrency.py

    import asyncio


    async def call_api(api_name, delay):
        print(f"{api_name} request started")

        # Simulates waiting for an external API response.
        await asyncio.sleep(delay)

        print(f"{api_name} response received")

        return f"{api_name} data"


    async def main():
        results = await asyncio.gather(
            call_api("User API", 2),
            call_api("Weather API", 3),
            call_api("News API", 1)
        )

        print("\nAll API responses:")
        print(results)


    asyncio.run(main())

Possible output:

    User API request started
    Weather API request started
    News API request started
    News API response received
    User API response received
    Weather API response received

    All API responses:
    ['User API data', 'Weather API data', 'News API data']

This simulates three independent API requests being handled concurrently.

---

# 🧠 Understanding the API Example

The code:

    asyncio.gather(
        call_api("User API", 2),
        call_api("Weather API", 3),
        call_api("News API", 1)
    )

creates one concurrent workflow.

Conceptually:

    ┌───────────────┐
    │ AI Controller │
    └───────┬───────┘
            ↓
        gather()
       /    |     \
      ↓     ↓      ↓
    User  Weather  News
     API    API     API
      │      │       │
      └──────┼───────┘
             ↓
          Results

The API calls do not need to wait for one another.

---

# 🤖 Use Case 2: AI Assistant

A modern AI assistant can combine information from several sources.

For example:

    User:
    "What's the weather today and what are
     the latest news updates?"

The assistant may need:

    Weather API
    News API
    User preferences
    LLM

Possible architecture:

    User Query
         ↓
    AI Controller
         ↓
    ┌────┼──────────┐
    ↓    ↓          ↓
 Weather News    User Data
   API    API       API
    │     │          │
    └─────┼──────────┘
          ↓
      Gather Data
          ↓
       LLM Prompt
          ↓
       LLM API
          ↓
     Final Response

Independent data retrieval can happen concurrently.

---

# 🧠 Use Case 3: Web Search

AI systems frequently perform multiple searches.

For example:

    Search 1 → Python concurrency
    Search 2 → asyncio
    Search 3 → ProcessPoolExecutor

Instead of:

    Search 1 → wait
        ↓
    Search 2 → wait
        ↓
    Search 3 → wait

we can potentially use:

    Search 1 ─────────→
    Search 2 ─────────→
    Search 3 ─────────→

Then:

    Search Results
          ↓
    Combine Information
          ↓
       LLM / AI
          ↓
      Final Answer

This pattern is particularly useful for research-oriented AI applications.

---

# 💻 Simulating Concurrent Web Searches

    import asyncio


    async def web_search(query, delay):
        print(f"Searching: {query}")

        # Simulates network waiting.
        await asyncio.sleep(delay)

        return f"Results for {query}"


    async def main():
        results = await asyncio.gather(
            web_search("Python concurrency", 2),
            web_search("asyncio", 1),
            web_search("AI agents", 3)
        )

        print("\nSearch results:")
        for result in results:
            print(result)


    asyncio.run(main())

Possible output:

    Searching: Python concurrency
    Searching: asyncio
    Searching: AI agents

    Search results:
    Results for Python concurrency
    Results for asyncio
    Results for AI agents

The actual completion order can differ from the order in the result list.

---

# 🗄️ Use Case 4: Database Operations

AI applications frequently communicate with databases.

Examples:

- User profiles
- Chat history
- Conversation memory
- Product information
- Document metadata
- Application state
- Retrieval data

For example:

    AI Assistant
         ↓
    ┌────┼─────────┐
    ↓    ↓         ↓
  User  History  Metadata
   DB     DB       DB
    │      │        │
    └──────┼────────┘
           ↓
       AI Context

If the database operations are independent and the database driver supports asynchronous execution, they can potentially be performed concurrently.

---

# 🤖 Use Case 5: LLM API Requests

AI applications often communicate with an external LLM service.

For example:

    User Query
         ↓
    Prompt Builder
         ↓
    LLM API
         ↓
    Response

But sometimes an application needs multiple model calls.

For example:

    Query Classification
          │
          ├── Model A
          ├── Model B
          └── Model C
                 ↓
          Compare Results
                 ↓
             Final Model

If those calls are independent and the service/API limits permit it, they can potentially be executed concurrently.

---

# ⚠️ API Rate Limits

Concurrency does not mean:

> "Send unlimited requests at the same time."

External services often impose:

- Rate limits
- Request limits
- Token limits
- Connection limits
- Quotas
- Cost limits

For example:

    1000 concurrent requests
          ↓
       API Limit
          ↓
       Rejected requests

Therefore, production AI systems often need:

    Concurrency
        +
    Rate limiting
        +
    Retries
        +
    Timeouts
        +
    Error handling

These concepts become especially important in production systems.

---

# ⏱️ Use Case 6: Timeouts

External services may become slow or unavailable.

Example:

    AI Application
         ↓
      Weather API
         ↓
       WAIT...
         ↓
       WAIT...
         ↓
       WAIT...

The application should not necessarily wait forever.

A production system can use timeouts.

Conceptually:

    API Request
         ↓
    Start timer
         ↓
    ┌───────────────┐
    │ Response?     │
    └───────┬───────┘
            │
       ┌────┴────┐
       ↓         ↓
    Received   Timeout
       ↓         ↓
    Continue   Handle Error

Timeouts will be covered more deeply in the Robust Python Code chapter.

---

# 🔁 Use Case 7: Retry Logic

External requests can fail temporarily.

For example:

    API Request
         ↓
       Failed
         ↓
       Retry
         ↓
       Failed
         ↓
       Retry
         ↓
      Success

A production AI application may use:

- Retry limits
- Exponential backoff
- Timeouts
- Error classification

Again, this connects directly to the next chapter on robust Python code.

---

# 🧠 Use Case 8: RAG Systems

**RAG stands for Retrieval-Augmented Generation.**

A simplified RAG pipeline is:

    User Query
         ↓
    Query Processing
         ↓
    Retrieve Information
         ↓
    Build Context
         ↓
    LLM
         ↓
    Final Answer

Retrieval may involve:

- Vector database
- SQL database
- Document store
- Metadata service
- Search engine

Some retrieval operations may be independent.

For example:

    Vector Search
         │
    Metadata Search
         │
    Keyword Search
         │
         ↓
      Combine
         ↓
      Context
         ↓
        LLM

Concurrency can potentially reduce the waiting time for independent retrieval operations.

---

# 🤖 RAG Concurrency Example

Conceptually:

    User Query
         ↓
    ┌────┼──────────────┐
    ↓    ↓              ↓
 Vector  Keyword      Metadata
 Search  Search        Search
    │      │             │
    └──────┼─────────────┘
           ↓
       Merge Results
           ↓
      Build Context
           ↓
          LLM
           ↓
       Final Answer

This is a common architecture pattern, although the exact implementation depends on the retrieval stack.

---

# 🧩 Use Case 9: AI Agents

AI agents may use multiple tools.

For example:

    AI Agent
       │
       ├── Web Search
       ├── Database
       ├── Calculator
       ├── File System
       └── External API

Some tool calls can be independent.

For example:

    Web Search
        +
    Database Search
        +
    Weather API

can potentially run concurrently.

But other tool calls may depend on previous results.

Example:

    Search
      ↓
    Extract ID
      ↓
    Query API using ID

This must follow the dependency chain.

---

# 🧠 Independent vs Dependent Agent Tools

### Independent

    Search Web
    Check Weather
    Query Database

These can potentially run concurrently.

### Dependent

    Search Product
          ↓
    Extract Product ID
          ↓
    Get Product Details

These operations are dependent.

Therefore:

> **Concurrency should be based on task dependencies, not simply on the number of tasks.**

---

# 📁 Use Case 10: File Processing

AI applications frequently work with files:

- PDFs
- Images
- CSV files
- Text documents
- Audio
- Videos

Suppose we have:

    document1.pdf
    document2.pdf
    document3.pdf

If the operations are primarily waiting on storage I/O, concurrency may help.

However, if PDF processing involves heavy CPU computation, process-based parallelism may be more appropriate.

This demonstrates why we first classify the workload.

---

# 🖼️ Image Processing

Suppose an AI pipeline processes:

    Image 1
    Image 2
    Image 3
    Image 4

If the workload is CPU-heavy:

    Process 1 → Image 1
    Process 2 → Image 2
    Process 3 → Image 3
    Process 4 → Image 4

may be useful.

But if the actual processing is handled by:

- GPU
- NumPy
- OpenCV native code
- PyTorch
- Other optimized libraries

then the optimal strategy can be different.

---

# 🧮 Use Case 11: CPU-Heavy AI Preprocessing

Suppose we need to perform expensive preprocessing on a large dataset.

Example:

    Dataset
       ↓
    ┌────┼────┐
    ↓    ↓    ↓
   CPU  CPU  CPU
   Job  Job  Job
    ↓    ↓    ↓
    └────┼────┘
         ↓
      Dataset

A process pool may be useful for independent CPU-heavy Python tasks.

Example:

    from concurrent.futures import ProcessPoolExecutor


    def preprocess(data):
        # CPU-heavy preprocessing
        return processed_data


    if __name__ == "__main__":
        with ProcessPoolExecutor() as executor:
            results = list(
                executor.map(preprocess, dataset)
            )

The exact implementation depends on the data and preprocessing library.

---

# 🧠 Use Case 12: ThreadPoolExecutor in AI

Not every AI application uses `asyncio`.

Suppose an existing SDK provides only blocking functions:

    result = sdk.generate(prompt)

If we need multiple independent calls:

    ThreadPoolExecutor

may be useful.

Conceptually:

    Thread 1 → LLM request
    Thread 2 → Search request
    Thread 3 → Database request

Each thread can wait independently.

This can be particularly useful when working with synchronous third-party libraries.

---

# 🔄 AI Concurrency Architecture

A larger AI application can combine multiple approaches:

    ┌──────────────────────────────┐
    │       AI Application         │
    └──────────────┬───────────────┘
                   ↓
             AI Controller
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
    Async APIs   Database   Web Search
        │          │          │
        └──────────┼──────────┘
                   ↓
               Gather
                   ↓
             Combined Data
                   ↓
          CPU Processing
                   ↓
          Process Pool
                   ↓
              AI Context
                   ↓
                 LLM
                   ↓
             Final Answer

Different components can use different concurrency models.

---

# 🧠 Concurrency Is an Architecture Tool

Concurrency should not be treated simply as:

> "Make everything parallel."

Instead:

> **Use concurrency where independent operations can safely make progress without unnecessary waiting.**

A good AI Engineer asks:

    1. What is the bottleneck?
    2. Is it I/O-bound or CPU-bound?
    3. Are the operations independent?
    4. Is the library async-compatible?
    5. Are there rate limits?
    6. Can failures occur?
    7. Do we need retries?
    8. Do we need timeouts?
    9. Is concurrency worth its overhead?
    10. How will results be combined?

---

# 🔐 Security Considerations

Concurrency also introduces engineering concerns.

For example:

    Multiple Tasks
         ↓
    Shared Resource
         ↓
    Race Condition

This can happen with:

- Shared files
- Shared counters
- Shared memory
- Database records
- Caches
- Application state

Therefore, concurrency must be combined with appropriate synchronization and transactional mechanisms.

Examples:

    Locks
    Transactions
    Atomic operations
    Queues
    Proper database isolation

---

# 🧠 AI Memory and Concurrency

Imagine an AI assistant maintaining conversation memory.

Two concurrent operations might attempt:

    Task 1 → Update Memory
    Task 2 → Update Memory

If both modify shared state incorrectly, data may become inconsistent.

Possible solutions include:

    Lock
    Queue
    Database transaction
    Atomic update
    Serialized access

The correct solution depends on the storage system and application design.

---

# 📊 Choosing the Right Tool

| Situation | Tool to consider |
|---|---|
| Async API calls | `asyncio` |
| Multiple async operations | `asyncio.gather()` |
| Individual async task control | `asyncio.create_task()` |
| Blocking I/O | `ThreadPoolExecutor` |
| Shared thread data | Lock / synchronization |
| CPU-heavy Python work | `ProcessPoolExecutor` |
| Multiple CPU-heavy jobs | `multiprocessing` |
| Process-to-process communication | `Queue` |
| Complex async workflow | `asyncio` Tasks |
| Partial async failures | `gather(..., return_exceptions=True)` |
| External API protection | Rate limiting + concurrency limits |
| Slow external service | Timeout |
| Temporary failures | Retry logic |

---

# 💻 Complete AI Engineer Example

File:

    21_ai_engineer_concurrency.py

    import asyncio


    async def call_api(api_name, delay):
        print(f"{api_name} request started")

        # Simulates waiting for an external API response.
        await asyncio.sleep(delay)

        print(f"{api_name} response received")

        return f"{api_name} data"


    async def main():
        # These API calls are independent, so they can be
        # executed concurrently instead of waiting for each
        # response before starting the next request.
        results = await asyncio.gather(
            call_api("User API", 2),
            call_api("Weather API", 3),
            call_api("News API", 1)
        )

        print("\nAll API responses:")
        print(results)


    # Starts the asyncio event loop and runs the main coroutine.
    asyncio.run(main())

Possible output:

    User API request started
    Weather API request started
    News API request started
    News API response received
    User API response received
    Weather API response received

    All API responses:
    ['User API data', 'Weather API data', 'News API data']

---

# 🧠 What This Example Demonstrates

This small program combines several Chapter 14 concepts:

    async def
       ↓
    Coroutine
       ↓
    await
       ↓
    asyncio.gather()
       ↓
    Concurrent I/O operations
       ↓
    Collect results

It simulates a realistic AI Engineering pattern:

    AI Application
          ↓
    Multiple external APIs
          ↓
    Concurrent requests
          ↓
    Combined information
          ↓
    AI processing

The actual production implementation would replace:

    asyncio.sleep()

with real asynchronous API/network operations.

---

# 🤖 Building an AI Assistant

A simplified architecture could be:

    ┌──────────────────────────┐
    │       User Query         │
    └────────────┬─────────────┘
                 ↓
    ┌──────────────────────────┐
    │      AI Controller        │
    └────────────┬─────────────┘
                 ↓
         Identify Required Tools
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
      Web      Database   APIs
     Search               │
       │         │         │
       └─────────┼─────────┘
                 ↓
             Concurrent
              Execution
                 ↓
           Gather Results
                 ↓
          Context Building
                 ↓
              LLM Call
                 ↓
           Final Response

This is a simplified architecture, but it demonstrates where concurrency can fit inside an AI system.

---

# 🧠 Concurrency in a RAG + Agent System

A more advanced conceptual architecture:

    User Query
         ↓
    Agent Controller
         ↓
    ┌────┴───────────────────┐
    │                        │
    ↓                        ↓
  RAG Search              Tool Calls
    │                        │
 ┌──┼──┐               ┌────┼────┐
 ↓  ↓  ↓               ↓    ↓    ↓
Vec DB BM25 Metadata   Web  API  DB
 └──┼──┘               └────┼────┘
    │                        │
    └──────────┬─────────────┘
               ↓
         Combine Results
               ↓
          Context Builder
               ↓
              LLM
               ↓
         Final Response

Independent operations may be concurrent, while dependent operations remain sequential.

---

# ⚠️ Production Considerations

A real AI application requires more than simply adding `asyncio.gather()`.

Production systems may need:

### 1. Timeouts

Prevent indefinite waiting.

### 2. Retries

Recover from temporary failures.

### 3. Rate Limits

Avoid overwhelming external APIs.

### 4. Concurrency Limits

Control the number of simultaneous operations.

### 5. Exception Handling

Handle partial failures.

### 6. Logging

Track what happened during execution.

### 7. Monitoring

Measure latency and failures.

### 8. Cancellation

Stop unnecessary work.

### 9. Resource Management

Close network connections and other resources properly.

### 10. Security

Protect credentials, files, APIs, and shared state.

These concepts become increasingly important when moving from learning projects to production AI systems.

---

# 📈 Measuring AI Application Performance

When improving an AI application, don't simply ask:

> "Is it concurrent?"

Instead measure:

- Total latency
- Individual API latency
- CPU usage
- Memory usage
- Number of concurrent tasks
- Error rate
- Retry count
- Throughput
- Token usage
- API cost

For example:

    User Request
         ↓
    Start Timer
         ↓
    Concurrent Operations
         ↓
    LLM
         ↓
    Final Response
         ↓
    Stop Timer

Then compare:

    Sequential latency
          vs
    Concurrent latency

This gives an actual performance measurement.

---

# 🧠 Latency vs Throughput

These concepts are important in AI systems.

### Latency

**Latency is the time required to complete a single operation or request.**

Example:

    User sends request
          ↓
       2.5 sec
          ↓
    AI response

Latency:

    2.5 seconds

---

### Throughput

**Throughput is the amount of work a system can complete within a given period of time.**

Example:

    100 requests
        /
    1 minute

Throughput:

    100 requests/minute

Concurrency can potentially improve both latency and throughput, but the actual effect depends on the workload and system architecture.

---

# 🤖 Why This Matters for AI Engineers

Imagine an AI API serving many users.

Without appropriate concurrency:

    User 1 → processing
    User 2 → waiting
    User 3 → waiting
    User 4 → waiting

With appropriate asynchronous architecture:

    User 1 ─────→
    User 2 ─────→
    User 3 ─────→
    User 4 ─────→

The server can make progress on multiple I/O-bound requests.

This is one reason asynchronous frameworks and concurrency patterns are common in modern AI/backend systems.

---

# 🧠 Chapter 14 Complete Mental Model

The entire chapter can now be viewed as:

    ┌─────────────────────────────┐
    │       Concurrency           │
    └──────────────┬──────────────┘
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
     Threads               Processes
        │                     │
        ↓                     ↓
     Lock /             Process / Pool
    Thread Safety            │
                              ↓
                         Queue / IPC
                              │
              ┌───────────────┴──────────────┐
              ↓                              ↓
      concurrent.futures                 asyncio
              │                              │
       ┌──────┴──────┐                 ┌─────┴─────┐
       ↓             ↓                 ↓           ↓
    ThreadPool   ProcessPool         async       await
    Executor     Executor              │
       │             │                 ↓
       │             │              Tasks
       │             │                 │
       │             │                 ↓
       │             │             gather()
       └─────────────┴─────────────────┘
                         ↓
                 Workload Analysis
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
           I/O-bound             CPU-bound
              ↓                     ↓
         asyncio / Threads      Processes
              ↓                     ↓
                 AI Engineering
                         ↓
           APIs / Search / DB / RAG
                         ↓
                    AI Systems

---

# 🔑 Chapter 14 Final Key Takeaways

- Concurrency allows multiple tasks to make progress without unnecessarily waiting for one another.
- Concurrency and parallelism are related but different concepts.
- Threads are useful for many I/O-bound workloads.
- Locks protect shared data from race conditions.
- Processes provide separate execution environments.
- Process pools distribute independent CPU-heavy tasks.
- Queues enable safe communication between processes.
- `concurrent.futures` provides a high-level concurrency interface.
- `Future` represents the eventual result of submitted work.
- `ThreadPoolExecutor` is useful for blocking I/O.
- `ProcessPoolExecutor` is useful for CPU-bound workloads.
- `asyncio` provides asynchronous programming through an event loop.
- `async def` defines coroutine functions.
- `await` allows a coroutine to suspend while waiting.
- `asyncio.create_task()` schedules coroutines as Tasks.
- `asyncio.gather()` runs multiple awaitables concurrently and collects their results.
- `I/O-bound` and `CPU-bound` workloads require different approaches.
- Concurrency does not automatically make every program faster.
- Concurrency introduces overhead and complexity.
- Task dependencies must be considered before running operations concurrently.
- Real AI systems frequently combine several concurrency techniques.
- API calls, web searches, databases, and external services are commonly I/O-bound.
- CPU-heavy preprocessing may benefit from process-based execution.
- Production AI systems also need timeouts, retries, rate limiting, logging, monitoring, and proper error handling.

---

# 🧠 AI Engineer Takeaway

The most important skill is not memorizing:

    asyncio
    Threading
    Multiprocessing
    ProcessPoolExecutor
    ThreadPoolExecutor

The important skill is knowing **when and why to use each one**.

A practical mental model is:

    What is the bottleneck?
            ↓
    ┌───────┴────────┐
    ↓                ↓
   I/O              CPU
    ↓                ↓
 Is it async?    Heavy Python work?
    ↓                ↓
   Yes              Yes
    ↓                ↓
 asyncio         Processes
    │
    ├── Multiple independent operations?
    │
    └──→ asyncio.gather()

For blocking I/O:

    Blocking I/O
         ↓
    ThreadPoolExecutor

For CPU-heavy work:

    CPU-bound
         ↓
    ProcessPoolExecutor

For GPU-heavy ML:

    GPU workload
         ↓
    PyTorch / CUDA /
    optimized ML libraries

---

# 🚀 How Chapter 14 Connects to AI Engineering

Chapter 14 provides the concurrency foundation needed for building modern AI applications.

Later AI systems may contain:

    User Interface
          ↓
    AI Controller
          ↓
    ┌─────┼─────────────┐
    ↓     ↓             ↓
   Web   Database      APIs
    │     │             │
    └─────┼─────────────┘
          ↓
        RAG
          ↓
    Vector Database
          ↓
       Context
          ↓
         LLM
          ↓
       Response

Concurrency can help coordinate the I/O-heavy parts of this architecture.

Later, when building AI Agents, RAG systems, API services, and AI assistants, these concepts will become practical rather than theoretical.

---

# 📚 Chapter 14 Final Summary

Chapter 14 introduced Python concurrency from the fundamentals to AI Engineering applications.

We started with:

    Concurrency
        ↓
    Threads
        ↓
    Race Conditions
        ↓
    Locks
        ↓
    Multiprocessing
        ↓
    Process Pools
        ↓
    Queue / IPC
        ↓
    concurrent.futures
        ↓
    Futures
        ↓
    ThreadPoolExecutor
        ↓
    ProcessPoolExecutor
        ↓
    asyncio
        ↓
    async / await
        ↓
    Asyncio Tasks
        ↓
    asyncio.gather()
        ↓
    I/O-bound vs CPU-bound
        ↓
    AI Engineering Applications

The final goal is not simply to know Python concurrency APIs.

The goal is to understand:

> **How to design an efficient AI application where independent work can happen concurrently, dependent work happens in the correct order, and resources are handled safely.**

---

# 🎯 Chapter 14 Completion Checklist

- [x] Concurrency Basics
- [x] Sequential vs Concurrent Execution
- [x] Concurrency vs Parallelism
- [x] Process vs Thread
- [x] Threading
- [x] `start()`
- [x] `join()`
- [x] Multiple Threads
- [x] Race Condition
- [x] Lock & Thread Safety
- [x] Multiprocessing
- [x] `Process`
- [x] Process Pool
- [x] Queue
- [x] Inter-Process Communication
- [x] `concurrent.futures`
- [x] `Future`
- [x] `ThreadPoolExecutor`
- [x] `ProcessPoolExecutor`
- [x] `asyncio`
- [x] Coroutine
- [x] `async`
- [x] `await`
- [x] Event Loop
- [x] Asyncio Tasks
- [x] `asyncio.create_task()`
- [x] `Task.done()`
- [x] `Task.result()`
- [x] Task cancellation
- [x] Task exceptions
- [x] `asyncio.gather()`
- [x] `return_exceptions=True`
- [x] I/O-bound Tasks
- [x] CPU-bound Tasks
- [x] Choosing the right concurrency technique
- [x] API concurrency
- [x] Web search concurrency
- [x] Database concurrency
- [x] LLM API concurrency
- [x] RAG concurrency
- [x] AI Agent concurrency
- [x] AI Assistant architecture
- [x] Production considerations

---

# 🏁 Chapter 14 Complete

You now have a practical foundation in **Python Concurrency** and understand how the concepts connect to AI Engineering.

The progression is:

    Python Concurrency
          ↓
    Efficient I/O
          ↓
    Concurrent APIs
          ↓
    AI Assistants
          ↓
    RAG Systems
          ↓
    AI Agents
          ↓
    Production AI Applications



---
## 📚 Course Information

- **Course:** Python for AI Engineering
- **Chapter:** Chapter 14 — Python Concurrency
- **Chapter Type:** AI Engineer Supplementary Chapter
- **Difficulty Level:** Intermediate
- **Programming Language:** Python
- **Main Focus:** Concurrency, Multithreading, Multiprocessing and Asynchronous Programming
- **Purpose:** To understand how Python can handle multiple tasks efficiently and how concurrency concepts are applied in AI Engineering.
- **Topics Covered:** Threading, Locks, Multiprocessing, Process Pool, Queue, `concurrent.futures`, Futures, ThreadPoolExecutor, ProcessPoolExecutor, `asyncio`, Tasks, `async`/`await`, `asyncio.gather()`, I/O-bound vs CPU-bound tasks, and AI Engineer applications.
- **Practical Focus:** API calls, concurrent I/O operations, CPU-intensive tasks, AI pipelines, and real-world AI Engineering use cases.
- **Status:** ✅ Completed
---

# 👨‍💻 Author

**Sonal Rai**