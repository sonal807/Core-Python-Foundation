#A proper error message is a clear and meaningful message that explains what went wrong and,
#when useful, how the problem can be fixed.

#Poor error message
#raise ValueError("Invalid input")

#Proper Error Message
#raise ValueError("Age must be between 18 and 100.")

#Example:
temperature = 5

if temperature < 0 or temperature > 2:
    raise ValueError("Invalid temperature. Allowed range is 0 to 2")