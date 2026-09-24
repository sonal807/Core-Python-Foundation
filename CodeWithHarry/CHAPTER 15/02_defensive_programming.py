#Defensive programming: It is a coding approach in which we anticipate possible errors, invalid inputs,
# and unexpected situations and handle them before they cause problems.

while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age > 120:
            print("Please enter a valid age.")
            continue

        break

    except ValueError:
        print("Please enter a number.")

print("Your age is: ", age)

#Example:
while True:
    try:
        num = int(input("Enter your marks: "))

        if num < 0 or num > 100:
            print("Invalid marks. Enter marks between 0 to 100")
            continue

        break

    except ValueError:
        print("Please enter number.")

print("Marks: ", num)