#queue: A multiprocessing queue is a process-safe data structure used to exchange data between multiple processes.

#Basic queue example:
import multiprocessing

def worker(queue):
    queue.put("Hello from worker process")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=worker,
        args=(queue,)
    )

    process.start()
    process.join()

    message = queue.get()

    print("Message: ", message)

#Complete flow
# Main Process
#      │
#      ├── Queue create
#      │
#      ├── Child Process create
#      │
#      ├── start()
#      │       ↓
#      │   Worker Process
#      │       │
#      │       └── queue.put("Hello...")
#      │                 ↓
#      │               Queue
#      │
#      ├── join()
#      │
#      └── queue.get()
#              ↓
#         "Hello..."


#Multiple values
import multiprocessing

def worker(queue):
    queue.put("Message 1")
    queue.put("Message 2")
    queue.put("Message 3")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=worker,
        args=(queue,)
    )

    process.start()
    process.join()

    print(queue.get())
    print(queue.get())
    print(queue.get())

#Producer and consumer: A producer generates data and puts it into a queue,
#while a consumer retrieves and processes that data from the queue.

import multiprocessing  # Multiple processes aur Queue ko use karne ke liye


def producer(queue):
    # Producer data generate karta hai aur Queue mein add karta hai
    for i in range(5):
        queue.put(i)  # Generated value ko Queue mein daalta hai
        print(f"Produced: {i}")  # Batata hai ki kaunsi value produce hui


def consumer(queue):
    # Consumer Queue se data retrieve karke process karta hai
    for i in range(5):
        item = queue.get()  # Queue se next available item retrieve karta hai
        print(f"Consumed: {item}")  # Batata hai ki kaunsi value consume hui


if __name__ == "__main__":

    # Process-safe Queue create karta hai,
    # jiske through Producer aur Consumer data exchange karenge
    queue = multiprocessing.Queue()

    # Producer process create kiya aur Queue ko producer function mein pass kiya
    producer_process = multiprocessing.Process(
        target=producer,  # Producer process mein producer() function execute hoga
        args=(queue,)  # Queue object ko producer() ke argument ke roop mein pass kiya
    )

    # Consumer process create kiya aur same Queue ko consumer function mein pass kiya
    consumer_process = multiprocessing.Process(
        target=consumer,  # Consumer process mein consumer() function execute hoga
        args=(queue,)  # Same Queue ko consumer() ke argument ke roop mein pass kiya
    )

    # Producer process ko start karta hai
    producer_process.start()

    # Consumer process ko start karta hai
    consumer_process.start()

    # Main process ko Producer ke complete hone tak wait karwata hai
    producer_process.join()

    # Main process ko Consumer ke complete hone tak wait karwata hai
    consumer_process.join()

    # Dono processes complete hone ke baad final message
    print("Producer and consumer finished")


#Queue.empty(): empty() checks whether a multiprocessing queue currently contains no items.

import multiprocessing


def producer(queue):
    # Producer process data generate karke Queue mein add karta hai
    queue.put("Data 1")
    queue.put("Data 2")
    queue.put("Data 3")


if __name__ == "__main__":

    # A process-safe Queue create karta hai,
    # jiske through processes ke beech data exchange kiya ja sakta hai
    queue = multiprocessing.Queue()

    # Producer process create kiya aur Queue ko uske function mein pass kiya
    process = multiprocessing.Process(
        target=producer,
        args=(queue,)
    )

    # Producer process start karta hai
    process.start()

    # Main process ko producer ke complete hone tak wait karwata hai
    process.join()

    # Jab tak Queue mein data available hai,
    # tab tak items ko one by one retrieve karte hain
    while not queue.empty():

        # Queue se next item retrieve karta hai
        data = queue.get()

        # Retrieved data display karta hai
        print("Received:", data)

    # Loop ke end mein Queue empty ho chuki hai
    print("Queue is empty")