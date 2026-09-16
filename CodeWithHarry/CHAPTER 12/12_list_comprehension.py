#List comprehension: List Comprehension is a concise way to create a new list by applying an expression to each item of an iterable.
#Basic syntax: [expression for item in iterable]

#Normally
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

#now same work with list comprehension
squares = [number ** 2 for number in numbers] #same work is done here in one line

print(squares)

#Example:

#normal
names = ["Harry", "Rohan", "Aman"]

upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)

#list comprehension
upper_names =[(name.upper()) for name in names]

print(upper_names)

#Example:
numbers = [2, 4, 6, 8, 10]

cubes = [number ** 3 for number in numbers]

print(cubes)


#List Comprehension with if: List Comprehension with an if condition is used to create a new list containing only the items that satisfy a specified condition.
#Basic syntax: [expression for item in iterable if condition]

#Normally
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

#List comprehension 
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

#Example:
numbers = [2, 4, 6, 8, 3, 9, 1]

greater_than_five = [number for number in numbers if number > 5]

print(greater_than_five)

#Example:
numbers = [10, 15, 20, 25, 30, 35, 40]

larger = [number for number in numbers if number > 20]
smaller = [number for number in numbers if number <= 20]

print(larger)
print(smaller)


#List Comprehension with if-else: List Comprehension with if-else is used to create a new list by applying different expressions 
#depending on whether a condition is true or false
#Basic Syntax: [expression_if_true if condition else expression_if_false for item in iterable]

#normal
numbers = [1, 2, 3, 4, 5, 6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

print(result)

#list comprehension (if-else)
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)

#Example:
marks = [80, 90, 45, 70, 30, 55, 12]

status = ["Pass" if mark >= 50 else "Fail" for mark in marks]

print(status)

#Example:
numbers = [5, 12, 7, 20, 3, 18]

result = ["BIG" if number >= 10 else "SMALL" for number in numbers]

print(result)

#Example:
numbers = [10, 15, 20, 25, 30]

result = [number + 10 if number >= 20 else number - 5 for number in numbers]

print(result)