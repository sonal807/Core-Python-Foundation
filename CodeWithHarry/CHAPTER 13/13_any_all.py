#any() / all(): any() returns True if at least one element in an iterable is truthy, 
#while all() returns True only if every element in an iterable is truthy.

#any()
#Example: suppose we have a list of numbers and we have to check that is any number in the list is greater than 25

numbers = [10, 20, 30, 40]

result = any(number > 25 for number in numbers)  #any() wants only one true

print(result)

#Example;
values = [False, False, True, False] #if one true the output will be True

print(any(values))

#Example:
values = [False, False, False] #if all false the output will be false

print(any(values))


#all(): it is opposite of any
#Example:

numbers = [10, 20, 30, 40] #if any value get false by checking the condition the output will be false

result = all(number > 5 for number in numbers)

print(result)

#Example:
scores = [85, 90, 78, 92]

print(all(score >= 50 for score in scores))
print(any(score >= 90 for score in scores))


#In python somes values are considered as False:
# False
# 0
# 0.0
# ""
# None
# []
# {}
# ()

#and rest values are True

#Example: with any
values = [0, "", False, 10] #Here 10 is truthy value and rest are false so it got one true then output will be True

print(any(values))

#Example: with all
values = [10, "Python", True, 5]  #all values are truthy values, output will be true

print(all(values))

#Example:
values = [10, "Python", 0, 5]  #since 0 is falsy so the output will be False

print(all(values))

#Example: suppose we have required fields for form validation
name = "Sonal"
email = "sonal@example.com"
phone = ""

fields = [name, email, phone]   #phoone is an emppty string "" here which is falsy

print(all(fields)) #so, the output will be False

#Example:
marks = [75, 82, 91, 68, 45]

result1 = any(mark >= 90 for mark in marks)
result2 = all(mark >= 50 for mark in marks)

print(f"Output of any: {result1}")
print(f"Output of all: {result2}")