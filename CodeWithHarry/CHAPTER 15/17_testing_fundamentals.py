#Testing is the process of checking whether a program
#behaves correctly under expected and unexpected conditions.

def add(a, b):
    return a + b

#Expected result: 5
result = add(2, 3)

if result == 5:
    print("Test pass.")
else:
    print("Test failed.")

#Example:
def multiply(a, b):
    return a + b

result = multiply(5, 4)

if result == 20:
    print("Test passed.")
else:
    print("Test failed.")