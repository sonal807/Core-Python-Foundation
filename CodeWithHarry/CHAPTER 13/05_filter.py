#filter(): The filter() function selects elements from an iterable based on a condition and returns only the elements for which the condition is true.

# Simple words:
# map() → values ko transform karta hai
# filter() → values ko select karta hai

#Syntax: filter(function, iterable)
#Syntax with lambda: filter(lambda x: condition, data)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))

#Example:
numbers = [10, 15, 20, 25, 30, 35, 40]

greater = filter(lambda x: x > 20, numbers)

print(list(greater))

#Example:
names = ["Sonal", "Aman", "Raj", "Rahul", "Om"]

words = filter(lambda name: len(name) > 4, names)

print(list(words))

#without lambda
names = ["Sonal", "Aman", "Raj", "Rahul", "Om"]

def name_length(name):
    return len(name) > 4

words = filter(name_length, names)

print(list(words))

#if function id easy and we have to use it once -> lambda is convenient
#if logic is big or we have to use function multiple times -> def is better

#it is not mandatory to use lambda with map() and filter()

#Example:
numbers = [-10, 5, -3, 8, -2, 12, -7]

positive_numbers = filter(lambda x: x > 0, numbers)

print(list(positive_numbers))

#list comprehension
positive = [x for x in numbers if x > 0]

print(positive)
