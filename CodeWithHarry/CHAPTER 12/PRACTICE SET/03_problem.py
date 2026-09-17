#Write a list comprehension to print a list which contains tha multiplication table of a user entered number.

number = int(input("Enter a number: "))

table = [number * i for i in range(1, 11)]

print(table)

#If we want in form of table
number = int(input("Enter the number: "))

tableList = [f"{number} X {i} = {number * i}" for i in range(1, 11)]

for line in tableList:
    print(line)