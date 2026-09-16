#finnally- The finally block is used to execute code regardless of whether an exception occurs or not
#Basic suntax:
#try:
    # Code that may cause an exception

#except:
    # Runs if an exception occurs

#finally:
    # Always runs

#Simple example:
try:
    a = 10
    b = 2  #If we put 0 here except will run, but finally will also run

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:   #When no exception finally will execute and even if there is exception finally will execute
    print("Program execution completed.")

#try-except-else-finally: We can also use all together.
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Operation completed.")

#Example:
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division result:", result)

finally:
    print("Program execution completed.")

#else: runs when their is no exception
#finally: runs in both case when no exception and when exception is there

#finally runs whether an exception occurs or not, even when the try or except block contains a return statement.

#finally with function:
def divide(a: int, b: int) -> float:
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0.0

    else:
        print("Division successful.")
        return result

    finally:
        print("Division operation completed.")

print("Result: ", divide(10, 2))
print("Result: ", divide(10, 0))

#Example:
def main():
    try:
       a=int(input("Enter a number: "))
       print(a)

    except ValueError as e:
       print(e)

    finally:
        print("finally executed") 

main()