#Lambda function: A lambda function is a small anonymous function that can take arguments and return a value in a single expression.

#Normal function
def square(number):
    return number * number

print(square(5))

#lambda function
square = lambda number: number * number

print(square(5))

#basic structure: lamda parameter: expression
#lambda is said to be a keyword which helps us to create a function using expression.

#Example:
add = lambda a, b: a + b

print(add(10, 20))

# def - used for large functios that include multiple statements
# lambda - used for one line expresson functions

#Example:
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(3))

#Example:
maximum = lambda a, b, c: a if a > b and a > c else (b if b > a and b > c else c)

print(maximum(10, 25, 77))