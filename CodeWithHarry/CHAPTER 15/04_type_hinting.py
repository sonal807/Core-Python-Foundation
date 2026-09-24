#Type hinting: It is a Python feature that allows us to specify the expected data types of
#variables, function parameters, and return values.

#Example:
# age: int = 25
# name: str = "Sonal"
# price: float = 99.9
# is_active: bool = True

#In fumction
def add(a: int, b: int) -> int:
    return a + b

#it means
# a → int expected
# b → int expected
# -> int → function se int return hone ki expectation
result = add(10, 20)
print(result)

#Example:
def calculate_area(length: float, width: float) -> float:
    return length * width

area = calculate_area(10.5, 5.2)
print(area)


#typing module: The typing module provides tools for adding type hints to Python code, especially when working with
#collections, optional values, multiple possible types, and complex data structures.

#When data gets more complex like:
# List of integers
# Dictionary of strings and integers
# A value that can be string OR None
# A value that can be int OR float
#typing module is useful.

#For using typing mpdule we write from typing import ..... 

#For List:
#With type hinting
# Student ke marks ki list.
# list[int] ka matlab hai ki list mein integer values expected hain.
marks: list[int] = [80, 75, 90, 85]


def calculate_average(marks: list[int]) -> float:
    # sum() sabhi marks ka total calculate karega.
    total = sum(marks)

    # len() total marks ki count dega.
    count = len(marks)

    # Average calculate karke return kar rahe hain.
    return total / count


# Function ko student ke marks pass kar rahe hain.
average = calculate_average(marks)

# Final average print kar rahe hain.
print("Average marks:", average)

##With typing module
from typing import List

#Ye list integers contain karne ke liye expected hai
numbers: List[int] = [10, 20, 30, 40]

print(numbers)

#Example:
from typing import List

def calculate_sum(numbers: List[int]) -> int:
        # List ke saare numbers ka sum return karega.
    return sum(numbers)

numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print("Sum:", result)


#For dictionary:
from typing import Dict

# Keys strings hain aur values integers hain.
marks: Dict[str, int] = {
    "Python": 90,
    "DBMS": 85,
    "Java": 80
}

print(marks)

#For tuples:
from typing import Tuple

# Tuple mein pehla element string aur doosra integer expected hai.
student: Tuple[str, int] = ("Sonal", 25)

print(student)

#For set:
from typing import Set

# Set ke andar integer values expected hain.
numbers: Set[int] = {10, 20, 30, 40}

print(numbers)

#For optional
from typing import Optional

# Username string ho sakta hai ya None ho sakta hai.
username: Optional[str] = None

print(username)

#Union:
from typing import Union

def calculate_square(number: Union[int, float]) -> Union[int, float]:
    # Integer ya float dono ka square calculate kar sakta hai.
    return number * number


print(calculate_square(5))
print(calculate_square(5.5))


#Full example where we will use multiple tools of typing module
from typing import List, Dict, Optional, Tuple


# Students ke naam ki list.
# List ke andar strings expected hain.
students: List[str] = [
    "Sonal",
    "Rahul",
    "Aman"
]


# Har student ke marks store karne ke liye dictionary.
# Key → string
# Value → integer
marks: Dict[str, int] = {
    "Sonal": 85,
    "Rahul": 78,
    "Aman": 92
}


# Student ki basic information.
# First value → string
# Second value → integer
student_info: Tuple[str, int] = (
    "Sonal",
    25
)


# Email available ho sakti hai ya nahi bhi.
# Isliye value string ya None ho sakti hai.
email: Optional[str] = None


def calculate_average(marks: List[int]) -> float:
    # Student ke marks ka average calculate karta hai.
    return sum(marks) / len(marks)


student_marks: List[int] = [85, 90, 80]

average = calculate_average(student_marks)

print("Students:", students)
print("Marks:", marks)
print("Student Info:", student_info)
print("Email:", email)
print("Average:", average)


#Example
from typing import List

marks: List[int] = [80, 75, 90, 85]

def calculate_average(marks: List[int]) -> float:
    return sum(marks) / len(marks)

average = calculate_average(marks)

print("Average: ", average)

#Example:
from typing import Dict

subject_marks: Dict[str, int] = {
    "Python": 90,
    "DBMS": 85,
    "Java": 80
}

def get_total_marks(subject_marks: Dict[str, int]) -> int:
    return sum(subject_marks.values())

total_marks = get_total_marks(subject_marks)

print("Total marks: ", total_marks)