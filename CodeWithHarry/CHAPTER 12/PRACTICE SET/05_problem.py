#Store the multiplication tables generated in problem 3 in a file named Tables.txt.

number = int(input("Enter the number: "))

tableList = [f"{number} X {i} = {number * i}" for i in range(1, 11)]

with open("Tables.txt", "a") as f:
    f.write(f"Table of {number} :\n")
    for line in tableList:
        print(line)
        f.write(line+ "\n")
    f.write("\n")