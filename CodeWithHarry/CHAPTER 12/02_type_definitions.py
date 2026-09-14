#Type definitions/ type hints: Type Hints are optional annotations in Python that specify the expected data type of variables, function parameters, and return values.
#It makes code easier to understand and helps IDEs (like VS Code) catch mistakes.
#Type hints are added using the colon(:) syntax for variables and the -> syntax for function return types.

#1- Variable Type Hints
#Basic syntax: variable: data_type = value
name: str = "Sonal"
age: int = 20
height: float = 5.9
is_student: bool = True

print("Variable Type Hints")
print("Age:", age)
print("Name:", name)
print("Height:", height)
print("Is Student:", is_student)

#2- Function with int return type
#Basic syntax: def function_name() -> data_type:
def add(a:int, b:int) -> int:
    return a + b

print("\nFunction Returning int")
print("Sum:", add(10, 20))

#3- Funtion with string return trype
#Basic syntax: def function_name() -> str:
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

message = greet("Rahul", 20)

print("\nFunction Returning string")
print(message)

#Common Python Type Hints
# Python Type	Type Hint
# Integer	     int
# Decimal	     float
# Text	         str
# True/False	 bool
# List	         list
# Tuple	         tuple
# Set	         set
# Dictionary	 dict

#4- List Type Hint
numbers: list[int] = [10, 20, 25, 35, 40]
names: list[str] = ["Aman", "Anil", "Priya", "Rahul"]

print("\nList Type Hint")
print("Numbers:", numbers)
print("Names:", names)

#5- Dictionary Type Hints
marks: dict[str, int] ={
    "Maths": 90,
    "Physics": 89,
    "Chemistry": 87,
    "Python": 97
}
print("\nDictionary Type Hints")
print(marks)

#6- Tuple Type Hints
student: tuple[str, int] = ("Sonal", "Hello", 34, 56)

print("\nTuple Type Hints")
print(student)

#7- Set Type Hints
color: set[str] = {"Red", "Green", "Black", "White"}

print("\nTuple type hint")
print(color)

#8- Type Hints with Functions
def calculate_average(marks: list[int]) -> float:
    return sum(marks)/ len(marks)

marks = [80, 90, 70, 86]

average = calculate_average(marks)
print(f"Average of marks are: {average}")

#9- Function returning None
def display(message: str) -> None:
    print(message)

print("\nFunction returning None")
display("Hello! How are you?")

#Example 1:
name: str = "Anil"
age: int = 34
height: float = 5.6

print("Name:", name)
print("Age:", age)
print("Height:", height)

#Example 2:
def mul(a:int, b:int) -> int:
    return a * b

print(mul(5, 6))

#Example 3:
def calculate_result(
    name: str,
    marks: list[int]
) -> tuple[float, str]:

    average = sum(marks) / len(marks)

    if average >= 75:
        grade = "A"

    elif average >= 60 and average < 75:
        grade = "B"

    elif average >= 50 and average < 60:
        grade = "C"

    else:
        grade = "Fail"

    return average, grade


name = "Harry"
marks = [80, 75, 90, 85]

average, grade = calculate_result(name, marks)

print("Student Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)

#Example 4
class Student:
    def __init__(self, name: str, age: int, marks: list[int]):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def get_grade(self) -> str:
        average = self.calculate_average()

        if average >= 75:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"

student = Student("Harry", 20, [80, 75, 90, 85])

print("Name:", student.name)
print("Age:", student.age)
print("Average:", student.calculate_average())
print("Grade:", student.get_grade())