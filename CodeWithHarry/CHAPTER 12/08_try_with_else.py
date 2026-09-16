#try-except-else: The else block in exception handling is executed only when the try block completes successfully without raising any exception.
#Basic syntax:
# try:
     # Risky operation

# except:
     # Error handling

# else:
     # Successful operation

#Simple Example:
try:
    a = 10
    b = 2    #If we give 0 here the try will not execute successfully, then else will execute not else.

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:   #Here try executed successfully, so else executed
    print("Result:", result)

#Why else? :Technically we can put successful code in try, but else purpose is to contain the code that will run after successfull execution of try.

#Example:
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered: ", number)

#Example:
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Enter a valid number.")

else:
    print("Number entered successfully: ", number)
    print("Square: ", number ** 2)

#Example:
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by 0.")

except ValueError:
    print("Invalid number.")

else:
    print("Division result: ", result)

#try-except-else with function:
def divide(a: int, b: int) -> float:
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by 0.")
        return 0.0

    else:
        print("Division successful.")
        return result

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = divide(a, b)
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")