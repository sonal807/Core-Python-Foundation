#Enumerate() -The enumerate() function is used to iterate over an iterable while keeping track of both the index and the value of each item.

#What we do normally 
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#if we want index + value both
for i in range(len(fruits)):
    print(i, fruits[i])

#this work is easily done by enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")

#enumerate() provides index and value pair in each iteration

#Normally starting index is 0, but we can change starting index but with start parameter
for index, fruit in enumerate(fruits, start= 1):
    print(f"{index} : {fruit}")

#If we want to print without for loop
print(list(enumerate(fruits)))  #it will give key value pair of index and items in form of list

#Example- 1: 
marks = [80, 75, 90, 85]

for index, mark in enumerate(marks):
    print(index, mark)

#Example-2:
students = ["Tony", "Hulk", "Strange", "Captain"]

for number, student in enumerate(students, start= 1):
    print(f"{number}. {student}")

#Example-3:
subjects = ["Python", "DBMS", "Computer Networks", "AI"]

for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")

#enumerate() with string
name = "Rohan"

for index, character in enumerate(name):
    print(f"The letter at index {index} is {character}")

#Example:
name = "Narendra"

for index, character in enumerate(name, start=1):
    print(f"{index}. {character}")
