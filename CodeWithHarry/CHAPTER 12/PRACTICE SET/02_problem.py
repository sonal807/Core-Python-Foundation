#Write a program to print third, fifth and seventh element from a list using
#enumerate function.

items = ["A", "B", "C", "D", "E", "F", "G"]

for index, item in enumerate(items, start= 1):
    if index == 3 or index == 5 or index == 7:
        print(f"{index}. {item}")