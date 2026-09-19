#A list contains multiplication table of 7. Write a program to convert it to vertical string.

table = [f"7 X {i} = {7 * i}"for i in range(1, 11)]

s = "\n".join(table)
print(s)