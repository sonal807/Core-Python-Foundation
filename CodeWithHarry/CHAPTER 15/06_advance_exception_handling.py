#Advanced exception handling is the practice of handling different types of errors precisely,
#preserving useful error information, and controlling how failures propagate through an application.

try:
    result = 10 / 0

except:                            #except is very broad, it can catch almost every type of exception, which can hide actual problem
    print("Something went wrong")


#Better way
try:
    result = 10 / 0
except ZeroDivisionError:           #Here we know which error to handle
    print("Cannot divide by zero.")


#Multiple specific exception
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


#as e - is used to give error message and it represent exception object
try:
    number = int("hello")

except ValueError as e:
    print("Error:", e)

#Raising exception
def process_data(data):
    try:
        return int(data)

    except ValueError:
        print("Invalid data received")
        raise                         #Here raise again propogates the same exception

#Exception chaining- raise.......from
# try:
#     number = int("Hello")

# except ValueError as e:
#     raise RuntimeError("Failed to process user input") from e


#AI engineer example:
def load_temperature(value):
    try:
        return float(value)

    except ValueError as e:
        raise ValueError(
            "Invalid AI model temperature. Expected a numeric value."
        ) from e

#Example
try:
    number = int(input("Enter the number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid ineger")

except ZeroDivisionError as e:
    print("Erroe: ", e)

else:
    print("Result: ", result)


#raise and re-raising exception
#The raise statement is used to manually trigger an exception when a specific condition occurs.
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")

#Re-raising simple means sending existing exception again
#Example:
def process_number(value):
    try:
        return int(value)

    except ValueError as e:
        print("Invalid value received:", e)

        # Same exception ko caller tak dobara bhej rahe hain.
        raise


try:
    process_number("hello")

except ValueError:
    print("Error handled by main program.")


#Example:
def validate_temperature(temperature):
    try:
        # AI model ke temperature ki valid range check kar rahe hain.
        if temperature < 0 or temperature > 2:
            raise ValueError("Temperature must be between 0 and 2.")

        return temperature

    except ValueError as e:
        # Error ko yahin observe/report kar rahe hain.
        print("Validation error:", e)

        # Same exception ko caller tak dobara bhej rahe hain.
        raise


try:
    temperature = validate_temperature(5)

    print("Valid temperature:", temperature)

except ValueError as e:
    # Final exception handling yahan ho rahi hai.
    print("Main program handled the error:", e)