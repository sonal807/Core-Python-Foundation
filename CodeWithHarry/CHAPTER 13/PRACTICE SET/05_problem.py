#Write a program to find the maximum of the numbers in a list using reduce().

from functools import reduce

numbers = [10, 25, 7, 42, 18, 35]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum number:", maximum)