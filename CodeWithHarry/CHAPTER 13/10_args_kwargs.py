#*args and **kwargs: *args allows a function to accept a variable number of positional arguments, 
# while **kwargs allows a function to accept a variable number of keyword arguments.

# Simple words mein:
# *args → kitne bhi positional arguments
# **kwargs → kitne bhi keyword arguments

#Normally
def add(a, b):  #It will accept only two arguments
    return a + b

print(add(10, 20))  #and if we write here (10, 20, 30) it will give error

#With *args
def add(*args):  #It will accept any numbers of arguments passed
    print(args)

add(10, 20, 30, 40)

#Example:
def show(*args):
    for item in args:
        print(item)

show("Python", "AI", "ML", "Deep Learning")

#Example: a fuction that will sum any numbers of arguments passed
def add(*args):  #args is tuple so we can use loop
    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30, 40, 50))

#Example:
def multiply(*args):
    result = 1

    for number in args:
        result = result * number

    return result

print(multiply(2, 3, 4))
print(multiply(2, 3, 4, 5))

#Normal arguments + *args
def student(name, *subjects):
    print("Name: ", name)
    print("Subjects: ", subjects)

student("Sonal", "Python", "AI", "ML")

#Example:
def student(name, *marks):
    print("Name: ", name)
    print("Marks: ", marks)
    
    total_marks =0

    for number in marks:
        total_marks += number

    print("Tolat: ", total_marks)
        
student("Sonal", 80, 75, 90)

#**kwargs: **kwargs allows a function to accept a 
# variable number of keyword arguments and stores them as a dictionary.

# *args → multiple positional arguments → tuple
# **kwargs → multiple keyword arguments → dictionary

def student(**kwargs):
    print(kwargs)

student(name="Sonal", age=25, course="Python")

#If we want to access the values inside kwargs, we can access it normally like dictionary

def student(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])

student(name="Sonal", age=25)

#With loop
def student(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)

student(
    name="Sonal",
    age=25,
    course="Python"
)

#Example:
def profile(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)

profile(
    name="Sonal", 
    age=25, 
    city="Lucknow", 
    skill="Python"
)

#Example:
def student(name, *marks, **details):
    print("Name:", name)
    print("Marks:", marks)

    for key, value in details.items():
        print(key, ":", value)

student(
    "Sonal",
    80, 75, 90,
    age=25,
    course="Python"
)