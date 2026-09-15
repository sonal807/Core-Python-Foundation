#Multiple Context Managers in a Single with:
#A context manager is an object that manages the setup and cleanup of a resource automatically, usually through the with statement.
# Multiple context managers can be used in a single with statement to manage multiple resources together.

#with statement - Basic idea:
#Normal way of opening file
file = open("file1.txt", "r")

data = file.read()

file.close()

#using with:
with open("file1.txt", "r") as file:  #with is safer and cleaner for resource management
    data = file.read()

#Multiple with statement:
#Now suppose we have to open two files
with open("file1.txt", "r") as file1:
    with open("file2.txt", "r") as file2:
        data1 = file1.read()
        data2 = file2.read()
#It's totaly valid, but we can also write this in only one single with statement

#Multiple Context Manager in One with:
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    data1 = file1.read()
    data2 = file2.read()

print(data1)
print(data2)

#Different Modes: Multiple context manager can be used with different modes in one with statement.
with open('file1.txt',"r") as file1, open('file2.txt',"w") as file2:
    data= file1.read()
    file2.write(data)

#Function with Multiple context managers
def read_files(file1_name: str, file2_name: str) -> None:

    with open(file1_name, "r") as file1, open(file2_name, "r") as file2:
        data1 = file1.read()
        data2 = file2.read()

        print("File 1:", data1)
        print("File 2:", data2)


read_files("file1.txt", "file2.txt")