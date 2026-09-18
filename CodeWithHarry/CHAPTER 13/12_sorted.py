#sorted(): sorted() is a built-in Python function that returns a new sorted list from an iterable without modifying the original iterable.

numbers = [50, 10, 40, 20, 30]

result = sorted(numbers)  #it will created a new sorted list without modifying original one

print(numbers)
print(result)

#Descending order: for sorting in descending order we can use reverse= True

numbers = [50, 10, 40, 20, 30]

result = sorted(numbers, reverse= True)

print(result)

#key= : key= tells the basis on which sorting has to be done

#Example: 
names = ["Sonal", "Aman", "Rahul", "Om", "Narendra"]

result = sorted(names, key= len) #it will sort on the basis of lenght of the string

print(result)


#with key=lambda
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

result = sorted(students, key=lambda student: student[1])  #it means makes the second element of each tuple as sorting basis

print(result)

#In key= we can use normal functions too, lambda is not compulsory

students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]
def get_marks(student):
    return student[1]

result = sorted(students, key=get_marks)
print(result)

#Example:
products = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]
# def lowest_highest(product):
#     return product[1]

# final = sorted(products, key=lowest_highest)
final = sorted(products, key=lambda product : product[1])

print(final)