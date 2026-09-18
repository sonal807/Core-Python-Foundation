#zip (): zip() is a built-in Python function that combines elements from two or more iterables pair by pair and returns them as tuples.

names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

result = zip(names, marks) #zip() will pair the elements at same index in both iterables

print(list(result))

#with loop
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name,":", mark)

#Example:
features = ["age", "salary", "expericence"]
values = [25, 60000, 2]

for feature, value in zip(features, values):
    print(feature,":", value)

#Lists with different length
names = ["Sonal", "Aman", "Rahul", "Rohit"]
marks = [85, 90, 78]

result = zip(names, marks) #zip() will make pairs upto shortest iterable, it will ignore Rohit as second iterable doesn't have value on same index

print(list(result))  

#we can also zip 3 lists
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]
cities = ["Lucknow", "Delhi", "Kanpur"]

result = zip(names, marks, cities)

print(list(result))

#Making dictionary with zip()
keys = ["name", "age", "course"]
values = ["Sonal", 25, "Python"]

student = dict(zip(keys, values))  #here zip() will first make pairs then dict will convert this pairs into dictionary

print(student)

#Example:
subjects = ["Python", "AI", "ML"]
marks = [85, 90, 88]

details = dict(zip(subjects, marks))

print(details)

#zip() + List Unpacking: sometimes we need to convert zip in to paricular lists
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

zipped = zip(names, marks) 

student_names, student_marks = zip(*zipped)  #here *zipped is unpacking the pairs in to two different iterables

print(student_names)
print(student_marks)