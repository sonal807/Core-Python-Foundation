#Write a program to filter a list of numbers which are divisible by 5.

#1st approach
numbers = [10, 12, 15, 21, 25, 30, 33, 40]

division = filter(lambda x: x % 5 == 0, numbers)

print(list(division))

#2nd approach
numbers = [10, 12, 15, 21, 25, 30, 33, 40]

def divisible_by_5(x):
    return x % 5 == 0

result = filter(divisible_by_5, numbers)

print(list(result))