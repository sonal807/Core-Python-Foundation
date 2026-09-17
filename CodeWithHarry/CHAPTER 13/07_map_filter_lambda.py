#map() + filter() + lambda Together: map() and filter() can be combined with lambda functions to first select specific elements
#  and then transform those elements.


#Example: Suppose we want only even numbers from the list and theri square.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = filter(lambda x: x % 2 ==0, numbers)
squares = map(lambda x: x * x, even_number)

print(list(squares))

#Example
numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = filter(lambda x: x % 2 ==0, numbers)
result = map(lambda x: x * 2, even_numbers)

print(list(result))

#Example:
numbers = [5, 12, 18, 7, 25, 30, 9, 40]

result = filter(lambda x: x > 10, numbers)
multiply = map(lambda x: x * 3, result)

print(list(multiply))