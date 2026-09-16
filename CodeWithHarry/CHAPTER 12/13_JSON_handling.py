#JSON Handling: JSON (JavaScript Object Notation) is a lightweight data format commonly used to store and exchange structured data between applications.

#It looks like python dictionary but it's not python dictionary, JSON is a data format.
#{
#     "name": "Harry",
#     "age": 20,
#     "skills": ["Python", "AI", "ML"]
#}

#In python we use built-in json module to handle JSON (import json)

#Python → JSON:
# Python Object
#      ↓
# json.dumps() : Converts python data into JSON string
#      ↓
# JSON String

# JSON → Python:
# JSON String
#      ↓
# json.loads() : Converts JSON string to python data
#      ↓
# Python Object

#json.dumps():converts a Python object into a JSON-formatted string.
#Example:

import json

student = {               #Initially student was python dictionary
    "name": "Harry",
    "age": 20,
    "course": "Python"
}

json_data = json.dumps(student)   #after json.dumps() it became JSON-formatted string

print(json_data)
print(type(json_data))

#indent Parameter: The indent parameter in json.dumps() is used to format JSON data with indentation, making it easier to read.
import json

student = {
    "name": "Harry",
    "age": 20,
    "course": "Python"
}

print(json.dumps(student)) #Output: {"name": "Harry", "age": 20, "course": "Python"}

#With indent=4:
import json

student = {
    "name": "Harry",
    "age": 20,
    "course": "Python"
}

print(json.dumps(student, indent=4))  #Output: {
                                      #     "name": "Harry",
                                      #     "age": 20,
                                      #     "course": "Python"
                                      # }


#json.loads(): json.loads() converts a JSON-formatted string into a Python object.

#Example:
import json

json_data = '{"name": "Harry", "age": 20, "course": "Python"}'  #it was JSON string

student = json.loads(json_data)  #after json.loads() it became python dictionary

print(student)
print(type(student)) #Output: <class 'dict'>

#Example:
import json

json_data = '{"name": "Sonal", "age": 25, "skill": "Python"}'

details = json.loads(json_data)

print(details)
print(type(details))


#json.dump(): json.dump() is used to write a Python object directly into a JSON file
# json.dumps() → Python object → JSON string
# json.dump() → Python object → JSON file

#Example:
import json
student = {
    "name": "Rohan",
    "age": 25,
    "skills": "Python"
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
#after running this code student.json file will be created in same folder.

#json.load(): json.load() is used to read JSON data from a JSON file and convert it into a Python object.
#json.loads() - JSON String → Python
#json.load() - JSON File → Python

#Example:
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(type(student))
#After running this code python will read data in student.json and give output in dictionary type.