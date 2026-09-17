#map(): The map() function applies a given function to every item of an iterable and returns a map object containing the results.
#syntax: map(function, iterable)

#without map()
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)

#with map()
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x * x, numbers)

print(list(squares))

#Example:
numbers = [10, 20, 30, 40, 50, 60]

result = map(lambda n: n * 5, numbers)

print(list(result))

#Example:
names = ["sonal", "rahul", "aman", "rohit"]

upper = map(lambda name: name.upper(), names)

print(list(upper))

#Example:
words = ["Python", "AI", "Machine", "Learning"]

length = map(lambda word: len(word), words)

print(list(length))