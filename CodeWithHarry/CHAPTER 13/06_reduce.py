#reduce(): The reduce() function repeatedly applies a function to the elements of an iterable and reduces them to a single final value.

#reduce() → multiple elements ko combine karke ek result banata hai

#Syntax: from functools import reduce
#        reduce(function, iterable)

from functools import reduce  #reduce is not built-in function so, we need to import it from functools

numbers = [1, 2, 3, 4, 5, 6]

total = reduce(lambda a, b: a + b, numbers)

print(total)

#Example:
from functools import reduce

numbers = [2, 3, 4, 5, 6]

multiplication = reduce(lambda a, b: a * b, numbers)

print(multiplication)

#Example:
from functools import reduce

numbers = [15, 42, 8, 31, 27]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)