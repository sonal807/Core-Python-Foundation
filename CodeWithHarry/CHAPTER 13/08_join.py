#join(): The join() method combines multiple strings from an iterable 
#into a single string using a specified separator.
#join() ka use multiple strings ko ek single string mein combine karne ke liye hota hai.

#Syantax: separator.join(iterable)

#Basic Example
words = ["Python", "is", "easy"]  #We have to combine this with space

result = " ".join(words)  #" " is seperator

print(result)

#Example
names = ["Sonal", "Aman", "Rahul"] #we have to combine this names with ','

result = ", ".join(names)  #", " is seperator

print(result)

#Example
words = ["2026", "09", "18"]

date = "-".join(words)  #"-" is seperator

print(date)

#Generally join() is used with string's iterable, if we have to use it with integers we have to convert it to string

#Example:
numbers = [1, 2, 3]

result = "-".join(map(str, numbers))

print(result)

#intresting connection:
#map() → numbers ko strings mein convert karta hai
#join() → strings ko combine karta hai

#Example
words = ["Python", "is", "powerful"]

result = " ".join(words)

print(result)

#Example:
names = ["Sonal", "Aman", "Rahul", "Rohit"]

final = ", ".join(names)

print(final)

#Example
letters = ["P", "Y", "T", "H", "O", "N"]

word = "".join(letters)

print(word)

#Example:
numbers = [10, 20, 30, 40, 50]

result = " - ".join(map(str, numbers))

print(result)