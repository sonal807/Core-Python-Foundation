#Robust Code: Robust code is code that can handle unexpected inputs, errors,
#and unusual situations without crashing or producing incorrect results.

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")

print("Your age is: ", age)

# Robust Code:
# Code that can handle unexpected inputs, errors, and unusual situations
# without crashing or producing incorrect results.

# Key characteristics:
# - Handles unexpected inputs
# - Handles errors properly
# - Validates data
# - Handles edge cases
# - Provides meaningful feedback
# - Maintains predictable behavior

# AI relevance:
# Robust code is important for building reliable AI applications,
# APIs, RAG systems, and AI agents.

#Example

while True:
    try:
        num = int(input("Enter a number: "))
        print("Square: ", num ** 2)
        break
    except ValueError:
        print("Enter a valid number.")