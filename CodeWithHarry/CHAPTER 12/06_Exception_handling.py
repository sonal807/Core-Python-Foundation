#Exception Handling: Exception Handling is a mechanism in Python used to handle runtime errors gracefully so that the program can continue running instead of crashing.

#try and except:The try block contains code that may cause an exception, while the except block handles that exception if it occurs.
#we can tell python - "Try this code . If an error occurs, dont crash. Handle it."

#Basic Syntax:
# try:
    # code that may cause an exception
# except:
    # code to handle the exception

#Example: Normal code
# a = 10 
# b = 0

# print(a/b)  #It will show ZeroDivisionError and the next statement will not execute
# print("Program Ended")

#With try-except:
a = 10 
b = 0

try:
    print(a/b)

except:
    print("Cannot divide by zero")

print("Program Ended")

#If there doesn't come any exception in try then except will not execute
a = 10 
b = 2

try:
    print(a/b)

except:
    print("Something went wrong")


#Example:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    print("Solution: ", a/b)
except:
    print("Cannot divide by 0")

print("Program Ended")

#Important point: Technically we can write only (except:) but generally writing the specific exception is better practice.
#like -> except ZeroDivisionError:

#Specific Exception — ZeroDivisionError: ZeroDivisionError is a built-in Python exception that occurs when a number is divided by zero.
#In the above example we can see that except: is empty and it can catch any type of exception, so the bettre approach is to tell that which exception we have to handle.

#Example
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    print("Solution: ", a/b)

except ZeroDivisionError:  ## If a ZeroDivisionError occurs in the try block, this code will execute.
    print("Cannot divide by 0")

print("Program Ended") 

#ValueError:ValueError is a built-in Python exception that occurs when a function receives a value of the correct type but an invalid value.
try:
    age = int(input("Enter your age: ")) #Here exception is coming during int() conversion, so it is necessary to write int(input()) inside try
    print("Your age is: ", age)

except ValueError:
    print("Please enter a valid number.")

#Example:
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"The sum of {a} and {b}: {a + b}")

except ValueError:
    print("Please enter valid number.")

#similarly for different situations there are different built-in exceptions
# TypeError
# IndexError
# KeyError
# FileNotFoundError

#Multiple except blocks: Multiple except blocks are used to handle different types of exceptions separately in the same try block
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

#except Exception:Exception is the base class for most built-in exceptions in Python, and except Exception can be used to catch unexpected runtime errors.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception:  #Works as a fallback
    print("An unexpected error occurred.")

#Capturing Exception in variable - as e: The as keyword is used in exception handling to store the exception object in a variable, 
#allowing us to access the actual error message.
try: 
    a = 10
    b = 0

    print(a/b)

except ZeroDivisionError as e:  #e name is not fixed we can take any variable
    print("Error:", e) #e will show the actual error message

#Example:
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number"))

    print("Result: ", a/ b)

except ValueError as v:
    print("Error: ", v)

except ZeroDivisionError as e:
    print("Error: ", e)


#Exception handling with functions: Exception handling with functions means using try-except 
#inside or around a function to handle errors that may occur during the function's execution.

#Simple Example:
def divide(a: int, b: int) -> None:
    try:
        print("Result: ", a / b)

    except ZeroDivisionError as e:
        print("Error: ", e)

divide(50, 2)
divide(30, 0)

#We can also use try-except outside function
def divide(a, b):
    return a / b


try:
    print(divide(10, 0))

except ZeroDivisionError:
    print("Cannot divide by zero.")

#Example:
def divide_numbers() -> None:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Result: ", a / b)

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

divide_numbers()

#Exception handling with classes(OOP): Exception handling with classes means using try-except with class methods or objects to 
#safely handle errors that may occur during their execution.
class Calculator:

    def divide(self, a: int, b: int) -> float:
        try:
            return a / b

        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return 0.0


calculator = Calculator()

print(calculator.divide(10, 2))
print(calculator.divide(10, 0))