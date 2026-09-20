#Concurrency: Concurrency is the ability of a program to manage multiple tasks during the same period of time,
#allowing progress on more than one task without necessarily executing them at the exact same moment.

#Concurrency ≠ necessarily parallel execution.

# Real-life example

# Tum restaurant mein ho.
# Ek waiter:

# Customer A ka order leta hai
# Kitchen ko order deta hai
# Jab food ban raha hai, Customer B ka order leta hai
# Customer C ko bill deta hai
# Phir A ka food serve karta hai

# Waiter ek hi person hai, lekin woh multiple tasks ko manage kar raha hai.

# Ye concurrency ko samajhne ka simple example hai.

#Example:
print("Task 1 started")
print("Task 1 completed")

print("Task 2 started")
print("Task 2 completed")

print("Task 3 started")
print("Task 3 completed")

#The purpose of the example is not to implement concurrency.
#It's just for observing that normal Python executes code instructions sequentially
