#Dictionary Merge Operators: Dictionary Merge Operators are operators used to combine two dictionaries into a single dictionary.
#Python provides | for creating a new merged dictionary and |= for merging one dictionary into another.

# | operator: | operator merges dictionaries and returns new dictionary
#new_dict = dict1 | dict2

#Example
id1 = {
    "name": "Sonal",
    "age": 24
}

id2 = {
    "course": "Python",
    "level": "Begineer"
}

student = id1 | id2  #id1 and id2 are merged and stored in new dictionary

print(student)

#Original dictionaries doesn't change using | operator, and it's the important point.
dict1 = {
    "name": "Sonal"
}

dict2 = {
    "age": 20
}

result = dict1 | dict2

print(dict1)  #Original dictionaries remains unchanged
print(dict2)
print(result)

#When the same key exists in both dictionaries, the value from the right-hand dictionary takes precedence.
#Example:
student1 = {
    "name": "Rahul",
    "age": 20
}

student2 = {
    "age": 25,
    "course": "Python"
}

result = student1 | student2  #student2 will overwrite the value of the value of student2 when key is same

print(result)

# |= operator: |= operator updates the in-place and existing dictionary.
#It is the modern way of update().
#It deosn't give new dictionary, it just updates the existing one.

#Example:
student = {
    "name": "Shyam",
    "age": 20
}

student |= {
    "course": "Python",
    "level": "Begineer"
}

print(student)


# | vs |=:
# | ➡️ Merges and create new dictionary
# |= ➡️ Updates the existing dictionary

#Duplicate keys with |=: Here also, the value from the right-hand dictionary takes precedence.
#Example:
student = {
    "name": "Rahul",
    "age": 20
}

student |= {
    "age": 21,
    "course": "Python"
}

print(student)

# | vs update():
#dict1.update(dict2) is the old and common method of merging dictionaries and modifying.
# dict1 | dict2 is the modern operator which provides cleaner/readable syntax.

#Merging dictionary in function:
def merge_data(
        personal: dict,    #Type hints are also used here.
        academic: dict
) -> dict:
    return personal | academic

personal = {
    "name": "Shyam",
    "age": 20
}

academic = {
    "course": "Python",
    "marks": 90
}
result = merge_data(personal, academic)

print(result)

#Better Type Hints:
# def merge_data(
#     personal: dict[str, str | int],
#     academic: dict[str, str | int]
# ) -> dict[str, str | int]:

#     return personal | academic

#Dictionary merge with class:
class Student:
    def __init__(
            self,
            personal: dict,
            academic:dict
    ):
        self.personal = personal
        self.academic = academic

    def get_details(self) -> dict:
        return self.personal | self.academic

personal = {
    "name": "Aman",
    "age": 20
}

academic = {
    "course": "Python",
    "marks": 90
}

student = Student(personal, academic)

print(student.get_details())

#Practical AI/ML example:
default_config = {
    "model": "BERT",
    "batch_size": 32,
    "epochs": 10
}

user_config = {
    "batch_size": 64,
    "epochs": 20
}

config = default_config | user_config

print(config)
#This pattern is useful in configuration systems.


#Example:
personal = {
    "name": "Harry",
    "age": 20
}

skills = {
    "python": "Advanced",
    "sql": "Intermediate"
}

profile = personal | skills

print(profile)

#Example:
default_settings = {
    "theme": "light",
    "language": "English",
    "notifications": True
}

user_settings = {
    "theme": "dark",
    "notifications": False
}

final_settings = default_settings | user_settings

print(final_settings)


#Example:
user = {
    "name": "Harry",
    "age": 20
}

user |= {
    "age": 21,
    "course": "Python"
}

print(user)