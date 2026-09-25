#assert: assert is a debugging statement used to check whether a condition is true.
#If the condition is false, Python raises an AssertionError.

#Example:
# age = 15 

# assert age >= 18

# print("Age is valid.")

#We also give custome error message with assert
# age = 15

# assert age >= 18, "Age must be 18 or above"

# print("Age is valid.")

#Eaxample:
temperature = 1.5

assert 0 <= temperature <= 2, "Temperature must be between 0 and 2."

print("Temperature is valid.")