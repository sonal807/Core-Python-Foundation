#Input validation is the process of checking whether input data is valid, safe, 
#and in the expected format before using it in a program.

#Data ko use karne se pehle check karo ki data sahi hai ya nahi

#What do we check in input validation:

#1- Type
age = 25        #integer
name = "Somal"  #string

#2- Range
if age < 0 or age > 120:
    print("Valid age")

#3- Length
# if len(username) < 3:
#     print("Usename is too short")

#4- Fromat -> let's take example of email
#sonal@example.com  -> valid format
#sonal@             -> invalid format

#5- Required value
name = input("Enter name: ")

if not name.strip():
    print("Name is required")

#Example:
while True:
    username = input("Enter username: ")

    if not username.strip():
        print("Username is required.")
    elif len(username.strip()) < 3:
        print("Username must contain at least 3 characters.")
    else:
        print("Valid username:", username)
        break