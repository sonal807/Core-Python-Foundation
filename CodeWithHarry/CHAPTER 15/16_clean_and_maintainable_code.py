#Clean and maintainable code is code that is easy to 
#read, understand, modify, test, and reuse.

# Simple words mein:
# Aisa code jo aaj tum khud samajh sako aur kuch months baad
# bhi easily samajh aur modify kar sako.

#❌ Unclean Code
n1 = 80
n2 = 90
n3 = 70

x = (n1 + n2 + n3) / 3

print(x)

#✅ Cleaner Code
marks = [80, 90, 70]

average_marks = sum(marks) / len(marks)

print("Average marks:", average_marks)

#Example:
#unclean code
x = [80, 90, 70, 85]
y = sum(x) / len(x)
print(y)

#Clean code:
marks = [80, 90, 70]

def calculate_average(marks):
    return sum(marks) / len(marks)

average = calculate_average(marks)

print("Average: ", average)