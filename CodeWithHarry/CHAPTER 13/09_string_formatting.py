#String Formatting: String formatting is the process of inserting variables and expressions into a string in a readable and controlled way.

#f-string
name = "Sahil"
age = 25

#normal concatenation:
print("My name is " + name + " and I am " + str(age) + " years old.")

#with f-string
print(f"My name is {name} and I am {age} years old.")

#Multiple variables:
name = "Sonal"
course = "Python"
chapter = 13

print(f"My name is {name}. I am learning {course}. I am currently on Chapter {chapter}.")

#Not only variables expressions can also be written
a = 10
b = 20

print(f"Sum = {a + b}")

#Example
name = "sonal"

print(f"Name in uppercase: {name.upper()}")

#Number Formatting
price = 99.45678

print(f"Price: ₹{price:.2f}")

#f → floating-point number
#.2 → decimal ke baad 2 digits

#Example:
percentage = 87.5678

print(f"Percentage: {percentage:.1f}%")

#Example:
price = 1499.786

print(f"Price: ₹{price:.2f}")

# .format() method: It was used commonly before f-string

name = "Sonal"
age = 25

print("My name is {} and I am {} years old.".format(name, age)) #Here {} are placeholders and .format(name, age) inserts values in it

#f-strings are generally preferred in modern Python because they are more readable, concise, and often faster. format() is still useful, 
# \especially in older codebases or when formatting strings dynamically.

#Example;
name = "Sonal"
course = "Python"
chapter = 13

print("My name is {}, I am learning {}, and I am on Chapter {}.".format(name, course, chapter))

#Alignment & Width Formatting: It is useful when we need output to be in proper columns/table format
name = "Sonal"
age = 24

print(f"{name:<10} | {age}")

#Common options
# f"{name:<10}"   # Left align
# f"{name:>10}"   # Right align
# f"{name:^10}"   # Center align

#Example
name = "AI"

print(f"{name:<10}|")
print(f"{name:>10}|")
print(f"{name:^10}|")

#Example
name = "Python"
version = "3.14"

print(f"{name:<10} | {version}")