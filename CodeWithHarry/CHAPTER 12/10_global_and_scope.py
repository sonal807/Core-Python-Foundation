#Scope: Scope refers to the region of a Python program where a variable can be accessed or used.
#Scope = where the variable is available

#1- local scope: Variable that are being assigned inside a function is said to be local variable.
def greet():
    name = "Harry"  #Here name is local variable
    print(name)
greet()

#2- Global scope: The variable which are defined outside function, comes under global scope.
name = "Rohan" #here name is outside function, so this is a global variable

def greet():
    print(name)
greet()

#Example:
name = "Andrew"

def show_name():
    print("Inside function: ", name)
show_name()

print("Outside function: ", name)

#but it is difficult to modify global variables inside function, so then we need 'global' keyword.

#global keyword: The global keyword is used inside a function to indicate that a variable refers to the global variable defined outside the function.

#Witout global
count = 10

def change_count():
    count = 20  #Since it is treated as local variable here so the value of global count doesn't change
    print("Inside: ", count)

change_count()

print("Outside: ", count)

#With global
count = 10

def change_count():
    global count  #global identifies that this count is not local; so modify the value of global count
    count = 20
    print("Inside: ", count)

change_count()

print("Outside: ", count)

#Example:
#without global
a = 89
def show():
    a = 3
    print(a)

show()

print(a)

#with global
a = 87
def fun():
    global a
    a = 3
    print(a)

fun()

print(a)

# Without global, assignment inside a function creates/uses a local variable.
# With global, the assignment modifies the existing global variable