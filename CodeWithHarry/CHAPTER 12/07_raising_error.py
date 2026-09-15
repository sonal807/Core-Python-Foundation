#Raising Exceptions (raise): The raise statement is used to manually raise an exception in Python when a specific condition is not satisfied.

#Basic syntax: raise ExceptionType("Error message")

#Example:
def square_root(number):
    if number < 0:
        raise ValueError("Number cannot be negative")

    return number ** 0.5

print(square_root(4))

#raise + try-except
age = 15 

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")

    else:
        print("You are eligible")

except ValueError as error:
    print("Error: ", error)

#Example:
def calculate_square(number: int) -> int:
    if number < 0:
        raise ValueError("Number must be positive")
    return number ** 2

try:
    result = calculate_square(-5)
    print("Result: ", result)

except ValueError as error:
    print("Error:", error)

#Example:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    elif age >= 18:
        print("You are eligible.")

    else:
        print("Not eligible.")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as v:
    print("Error: ", v)