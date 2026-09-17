#Write a program to open three files 1.txt, 2.txt and 3.txt.
#If any of these files are not present, a message without exiting the program
#must be printes prompting tha same.

#using for loop
files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"Contents of file {file}: ")
            print(f.read())

    except FileNotFoundError:
        print(f"File {file} doesn't exist")

#without for loop
try:
    with open("1.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("1.txt is not present")

try:
    with open("2.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("2.txt is not present")

try:
    with open("3.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("3.txt is not present")

print("Thank you!")