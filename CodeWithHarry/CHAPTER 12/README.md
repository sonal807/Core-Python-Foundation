# 📘 Chapter 12 — Python Advanced Features & Utilities

## 🎯 Objective

The objective of this chapter is to learn several useful and advanced
Python features that improve code readability, flexibility, error handling,
data processing, and file management.

This chapter covers modern Python syntax and important Python utilities
such as the Walrus Operator, Type Hints, Match-Case, Dictionary Merge
Operators, Exception Handling, Context Managers, List Comprehensions,
File Handling, and JSON Handling.

These concepts help in writing cleaner, more readable, maintainable,
and practical Python programs. They also provide a strong foundation
for working with APIs, automation, data processing, and AI/ML applications.

---

# 📌 Topics Covered

1. Walrus Operator `:=`
2. Type Hints / Type Definitions
3. Match-Case
4. Dictionary Merge Operators
5. Multiple Context Managers
6. Exception Handling
7. Raising Errors — `raise`
8. `try-except-else`
9. `finally`
10. `__name__ == "__main__"`
11. Global Keyword & Scope
12. `enumerate()`
13. List Comprehension
14. File Handling
15. JSON Handling
16. Practical Concepts
17. Chapter 12 Summary
18. AI Engineer Relevance

---

# 1️⃣ Walrus Operator `:=`

## 🧠 What is the Walrus Operator?

The **Walrus Operator (`:=`)** is an assignment expression operator
introduced in Python 3.8 that allows us to assign a value to a variable
and use that value within the same expression.

It is called the **Walrus Operator** because the `:=` symbol visually
resembles a walrus.

---

## 🔹 Basic Syntax

```python
(variable := value)
```

The Walrus Operator performs two operations:

1. Assigns a value to a variable.
2. Returns that value as part of the expression.

### Example

```python
print(x := 20)
```

Output:

```text
20
```

Here, `20` is assigned to `x`, and the same value is returned by the
assignment expression and passed to `print()`.

---

## 🔹 Difference Between `=` and `:=`

### Assignment Operator `=`

The normal assignment operator is used to assign a value to a variable.

```python
x = 20
print(x)
```

### Walrus Operator `:=`

The Walrus Operator allows assignment inside an expression.

```python
print(x := 20)
```

Both examples assign `20` to `x`, but `:=` can also return the assigned
value as part of the expression.

---

## 🔹 Walrus Operator with `if`

The Walrus Operator can be useful when a value needs to be assigned
and checked within the same condition.

```python
if (marks := 75) > 50:
    print("Marks is greater than 50")
```

Output:

```text
Marks is greater than 50
```

Here:

```python
marks := 75
```

assigns `75` to `marks`.

Then:

```python
marks > 50
```

checks whether the value is greater than `50`.

---

## 🔹 Walrus Operator with `while`

The Walrus Operator can also be useful when taking input repeatedly.

```python
while (number := int(input("Enter the number: "))) != 0:
    print(f"You entered: {number}")
```

The input is assigned to `number` and checked in the same expression.

The loop continues until the user enters `0`.

---

## 🔹 Walrus Operator with `len()`

```python
numbers = [10, 20, 30, 40, 50]

if (length := len(numbers)) > 3:
    print(f"The list contains {length} elements.")
```

Output:

```text
The list contains 5 elements.
```

Here, `len(numbers)` is calculated once, assigned to `length`, and then
used in the condition.

---

## ⭐ Use Cases

The Walrus Operator can be useful when:

- A value needs to be assigned and checked in the same expression.
- A calculation would otherwise need to be repeated.
- Input needs to be processed inside a loop condition.
- Code can be made shorter without reducing readability.

---

## ⚠️ Important Note

The Walrus Operator should be used carefully.

Although it can make code shorter, excessive use can make code harder
to read and understand.

Use it when it improves clarity rather than simply reducing the number
of lines.

---

## 🤖 AI Engineer Relevance

The Walrus Operator can occasionally be useful in data processing,
input handling, filtering operations, and situations where a calculated
value needs to be checked immediately.

However, readability should always be prioritized in larger AI/ML projects.

---

# 2️⃣ Type Hints / Type Definitions

## 🧠 What are Type Hints?

**Type Hints** are optional annotations in Python that specify the
expected data type of variables, function parameters, and return values.

They improve code readability, documentation, IDE support, and
maintainability.

---

## 🔹 Variable Type Hints

Basic syntax:

```python
variable: data_type = value
```

### Example

```python
name: str = "Anil"
age: int = 34
height: float = 5.6

print("Name:", name)
print("Age:", age)
print("Height:", height)
```

Output:

```text
Name: Anil
Age: 34
Height: 5.6
```

Here:

- `name: str` indicates that `name` is expected to contain a string.
- `age: int` indicates that `age` is expected to contain an integer.
- `height: float` indicates that `height` is expected to contain a float.

---

## 🔹 Function Parameter Type Hints

Type hints can be used with function parameters.

```python
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(5, 6))
```

Output:

```text
30
```

Here:

```python
a: int
b: int
```

indicate that the parameters are expected to be integers.

The return type:

```python
-> int
```

indicates that the function is expected to return an integer.

---

## 🔹 Return Type `None`

If a function does not return a value, `None` can be used as the return
type hint.

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")

greet("Sonal")
```

Output:

```text
Hello, Sonal
```

---

## 🔹 Common Type Hints

| Type | Meaning |
|------|---------|
| `int` | Integer |
| `float` | Floating-point number |
| `str` | String |
| `bool` | Boolean |
| `list` | List |
| `tuple` | Tuple |
| `set` | Set |
| `dict` | Dictionary |
| `None` | No return value |

---

## 🔹 Collection Type Hints

Modern Python allows us to specify the expected types of elements
inside collections.

### List

```python
marks: list[int] = [80, 75, 90, 85]
```

This indicates that the list is expected to contain integers.

### Tuple

```python
student: tuple[str, int] = ("Harry", 20)
```

This indicates that the tuple contains a string followed by an integer.

### Set

```python
numbers: set[int] = {10, 20, 30}
```

This indicates that the set is expected to contain integers.

### Dictionary

```python
scores: dict[str, int] = {
    "Python": 90,
    "DBMS": 85
}
```

This indicates that the dictionary is expected to have string keys
and integer values.

---

## 🔹 Union Types

Sometimes a variable or function parameter may accept more than one
possible data type.

Modern Python provides the `|` operator for specifying Union Types.

```python
value: int | float = 10
```

The variable can contain either an integer or a floating-point number.

### Example

```python
def calculate(value: int | float) -> float:
    return float(value)
```

The parameter `value` can be either an `int` or a `float`.

---

## 🔹 Type Hints with Functions

Type hints become especially useful when functions work with multiple
parameters and return multiple values.

### Example

```python
def calculate_result(
    name: str,
    marks: list[int]
) -> tuple[float, str]:

    average = sum(marks) / len(marks)

    if average >= 75:
        grade = "A"

    elif average >= 60:
        grade = "B"

    elif average >= 50:
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
```

Output:

```text
Student Name: Harry
Marks: [80, 75, 90, 85]
Average: 82.5
Grade: A
```

The return type:

```python
-> tuple[float, str]
```

indicates that the function returns a tuple containing:

- a `float`
- a `str`

---

## 🏫 Type Hints with Classes

Type hints can also be used with class constructors, attributes,
parameters, and methods.

```python
class Student:

    def __init__(
        self,
        name: str,
        age: int,
        marks: list[int]
    ):
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
```

Here:

```python
name: str
age: int
marks: list[int]
```

specify the expected types of the constructor parameters.

The method:

```python
calculate_average() -> float
```

is expected to return a floating-point number.

The method:

```python
get_grade() -> str
```

is expected to return a string.

---

## ⚠️ Important Note — Type Hints Do Not Enforce Types

Type hints are **not runtime type enforcement**.

For example:

```python
age: int = "Twenty"
```

Python does not normally raise an error simply because the value does
not match the type hint.

Type hints mainly provide:

- Better code readability
- IDE and editor support
- Static type checking
- Better documentation
- Easier maintenance of large projects

---

## 🛠️ Type Hints vs Runtime Type Checking

Type hints:

```python
age: int = 20
```

tell the developer and development tools what type is expected.

They do not automatically prevent:

```python
age = "Twenty"
```

from being assigned later.

For actual runtime validation, additional logic or validation libraries
may be required.

---

## 🤖 AI Engineer Relevance

Type Hints are highly useful in AI/ML projects because such projects
often contain functions for:

- Data preprocessing
- Feature engineering
- Model training
- Prediction
- API requests and responses
- Configuration handling
- Data transformation

For example:

```python
def predict(features: list[float]) -> float:
    ...
```

makes the expected input and output of the function immediately clear.

Type hints also become increasingly valuable as AI projects grow larger
and contain multiple modules, classes, APIs, and data-processing pipelines.

# 3️⃣ Match-Case

## 🧠 What is Match-Case?

The `match-case` statement is a Python control-flow feature used to
compare a value against multiple patterns and execute the code
associated with the first matching pattern.

It was introduced in **Python 3.10**.

It can be used as an alternative to long `if-elif-else` statements
when multiple possible patterns need to be matched.

---

## 🔹 Basic `match-case` Syntax

```python
match value:

    case pattern1:
        # code

    case pattern2:
        # code

    case _:
        # default code
```

The `match` statement checks the value against each `case`.

---

## 🔹 Basic Example

```python
day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid day")
```

Output:

```text
Tuesday
```

Python checks the cases from top to bottom and executes the first
matching case.

---

## 🔹 Default Case `_`

The `_` pattern acts as a default case.

It executes when none of the previous cases match.

```python
operator = "%"

match operator:

    case "+":
        print("Addition")

    case "-":
        print("Subtraction")

    case "*":
        print("Multiplication")

    case "/":
        print("Division")

    case _:
        print("Invalid operator")
```

Output:

```text
Invalid operator
```

---

## 🔹 Multiple Values Using `|`

The `|` operator can be used when multiple values should execute
the same case.

```python
day = "Saturday"

match day:

    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case _:
        print("Invalid day")
```

Output:

```text
Weekend
```

Here, multiple patterns are combined into a single case.

---

## 🔹 Guard Conditions

A guard allows us to add an additional condition to a `case`.

Syntax:

```python
case variable if condition:
```

### Example

```python
marks = 85

match marks:

    case marks if 90 <= marks <= 100:
        print("Grade: A+")

    case marks if 75 <= marks < 90:
        print("Grade: A")

    case marks if 50 <= marks < 75:
        print("Grade: B")

    case _:
        print("Fail")
```

Output:

```text
Grade: A
```

The `if` condition after the pattern is called a **guard**.

---

## 🔹 Practical Grading Example

```python
marks = int(input("Enter Marks: "))

match marks:

    case marks if 90 <= marks <= 100:
        print("Grade: A")

    case marks if 75 <= marks <= 89:
        print("Grade: B")

    case marks if 50 <= marks <= 74:
        print("Grade: C")

    case marks if 0 <= marks <= 49:
        print("Grade: Fail")

    case _:
        print("Invalid Marks")
```

The chained comparison:

```python
90 <= marks <= 100
```

checks that `marks` is between `90` and `100`.

---

## 🔹 Match-Case with Functions

`match-case` can be used inside functions to organize decision-making
logic.

```python
def get_grade(marks: int) -> str:

    match marks:

        case marks if 90 <= marks <= 100:
            return "A"

        case marks if 75 <= marks <= 89:
            return "B"

        case marks if 50 <= marks <= 74:
            return "C"

        case marks if 0 <= marks <= 49:
            return "Fail"

        case _:
            return "Invalid Marks"


marks = int(input("Enter Marks: "))

grade = get_grade(marks)

print("Grade:", grade)
```

---

## 🔹 Match-Case with Classes

`match-case` can also be used inside class methods.

```python
class Student:

    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def get_grade(self) -> str:

        match self.marks:

            case marks if 90 <= marks <= 100:
                return "A"

            case marks if 75 <= marks <= 89:
                return "B"

            case marks if 50 <= marks <= 74:
                return "C"

            case marks if 0 <= marks <= 49:
                return "Fail"

            case _:
                return "Invalid Marks"


student = Student("Harry", 85)

print("Student:", student.name)
print("Marks:", student.marks)
print("Grade:", student.get_grade())
```

Output:

```text
Student: Harry
Marks: 85
Grade: B
```

---

## ⚖️ Match-Case vs `if-elif-else`

Both can be used for decision-making, but they have different strengths.

### `if-elif-else`

```python
if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

else:
    print("C")
```

### `match-case`

```python
match marks:

    case marks if marks >= 90:
        print("A")

    case marks if marks >= 75:
        print("B")

    case _:
        print("C")
```

`if-elif-else` is often more natural for general conditions and
complex boolean logic.

`match-case` is useful when matching specific values or patterns.

---

## ⚠️ Important Note

When using `match-case` with ranges, guards are required.

For example:

```python
case marks if marks >= 90:
```

Here the `if` is a guard condition.

---

## 🤖 AI Engineer Relevance

`match-case` can be useful in AI applications when different actions
need to be performed based on a command, status, category, or type.

For example, an application may receive commands such as:

```text
"train"
"predict"
"evaluate"
"exit"
```

and use `match-case` to decide which operation should be performed.

---

# 4️⃣ Dictionary Merge Operators

## 🧠 What are Dictionary Merge Operators?

Dictionary Merge Operators are operators used to combine dictionaries
into a single dictionary.

Python provides:

- `|` — creates a new merged dictionary.
- `|=` — merges another dictionary into the existing dictionary.

These operators were introduced in **Python 3.9**.

---

## 🔹 `|` Operator

The `|` operator combines two dictionaries and creates a **new
dictionary**.

```python
personal = {
    "name": "Sonal",
    "age": 25
}

academic = {
    "course": "B.Tech CSE",
    "semester": 6
}

student = personal | academic

print(student)
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'course': 'B.Tech CSE', 'semester': 6}
```

The original dictionaries remain unchanged.

---

## 🔹 Duplicate Keys

If both dictionaries contain the same key, the value from the
**right-hand dictionary** is used.

```python
student1 = {
    "name": "Sonal",
    "age": 20
}

student2 = {
    "age": 25,
    "course": "Python"
}

result = student1 | student2

print(result)
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'course': 'Python'}
```

The value `25` replaces `20` because `student2` is on the right side.

### Rule

```text
Left Dictionary | Right Dictionary
                       ↓
                Duplicate key wins
```

---

## 🔹 `|=` Operator

The `|=` operator updates an existing dictionary in-place.

```python
student = {
    "name": "Sonal",
    "age": 20
}

student |= {
    "age": 21,
    "course": "Python"
}

print(student)
```

Output:

```text
{'name': 'Sonal', 'age': 21, 'course': 'Python'}
```

Here, the original `student` dictionary itself is modified.

---

## ⚖️ `|` vs `|=`

### `|`

Creates a new dictionary.

```python
result = dict1 | dict2
```

The original dictionaries are not modified.

### `|=`

Updates the existing dictionary.

```python
dict1 |= dict2
```

The left-hand dictionary is modified.

---

## ⚖️ `|` vs `.update()`

The following:

```python
student |= academic
```

is conceptually similar to:

```python
student.update(academic)
```

Both modify the existing dictionary.

However:

```python
result = personal | academic
```

creates a new dictionary without modifying the original dictionaries.

---

## 🔹 Practical Example

Dictionary merging is useful when information is stored in separate
categories.

```python
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
```

Output:

```text
{
    'name': 'Harry',
    'age': 20,
    'python': 'Advanced',
    'sql': 'Intermediate'
}
```

---

## 🔹 Dictionary Merge with Type Hints

```python
def merge_data(
    personal: dict[str, str | int],
    academic: dict[str, str | int]
) -> dict[str, str | int]:

    return personal | academic


personal = {
    "name": "Sonal",
    "age": 25
}

academic = {
    "course": "Python",
    "level": "Beginner"
}

result = merge_data(personal, academic)

print(result)
```

---

## 🏫 Dictionary Merge with Classes

```python
class Student:

    def __init__(
        self,
        personal: dict,
        academic: dict
    ):
        self.personal = personal
        self.academic = academic

    def get_details(self) -> dict:
        return self.personal | self.academic


student = Student(
    {"name": "Harry", "age": 20},
    {"course": "Python", "level": "Beginner"}
)

print(student.get_details())
```

---

## 🤖 AI Engineer Relevance

Dictionary merging is useful when combining structured information
from different sources.

For example, an AI application may have:

```python
model_config = {
    "model": "example-model",
    "temperature": 0.7
}

user_config = {
    "temperature": 0.2
}

final_config = model_config | user_config
```

This approach can be useful when combining configuration data,
parameters, API responses, or other structured information.

---

# 5️⃣ Multiple Context Managers

## 🧠 What is a Context Manager?

A **Context Manager** is an object that manages the setup and cleanup
of a resource automatically, usually through the `with` statement.

Context managers are commonly used with resources such as:

- Files
- Database connections
- Network connections
- Locks
- Other resources that require proper cleanup

---

## 🔹 Basic `with` Statement

A single context manager can be used to open a file.

```python
with open("file1.txt", "r") as file:
    data = file.read()
    print(data)
```

When the `with` block finishes, Python automatically handles closing
the file.

---

## 🔹 Multiple `with` Statements

Multiple resources can be handled using nested `with` statements.

```python
with open("file1.txt", "r") as file1:

    with open("file2.txt", "r") as file2:

        data1 = file1.read()
        data2 = file2.read()

        print("File 1:", data1)
        print("File 2:", data2)
```

Although this works, multiple context managers can often be written
more cleanly in a single `with` statement.

---

## 🔹 Multiple Context Managers in a Single `with`

Python allows multiple context managers in one `with` statement.

```python
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:

    data1 = file1.read()
    data2 = file2.read()

    print("File 1:", data1)
    print("File 2:", data2)
```

This is cleaner than deeply nested `with` statements.

---

## 🔹 Function-Based Example

Multiple context managers can be used inside functions.

```python
def read_files(
    file1_name: str,
    file2_name: str
) -> None:

    with open(file1_name, "r") as file1, open(file2_name, "r") as file2:

        data1 = file1.read()
        data2 = file2.read()

        print("File 1:", data1)
        print("File 2:", data2)


read_files("file1.txt", "file2.txt")
```

The function opens both files and automatically handles their cleanup
when the `with` block finishes.

---

## 🏫 Multiple Context Managers with Classes

```python
class FileReader:

    def __init__(
        self,
        file1_name: str,
        file2_name: str
    ):
        self.file1_name = file1_name
        self.file2_name = file2_name

    def read_files(self) -> None:

        with open(self.file1_name, "r") as file1, \
             open(self.file2_name, "r") as file2:

            data1 = file1.read()
            data2 = file2.read()

            print("File 1:", data1)
            print("File 2:", data2)


reader = FileReader("file1.txt", "file2.txt")

reader.read_files()
```

---

## 🔹 Custom Context Manager — Basic Overview

A class can act as a custom context manager by implementing:

- `__enter__()`
- `__exit__()`

### Example

```python
class Demo:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with Demo() as obj:
    print("Inside context")
```

Output:

```text
Entering context
Inside context
Exiting context
```

`__enter__()` runs when entering the `with` block.

`__exit__()` runs when leaving the `with` block.

---

## ⚠️ Important Note

The `with` statement is preferred for resources that need reliable
cleanup because it helps ensure that resources are properly released
even when an exception occurs inside the block.

---

## 🤖 AI Engineer Relevance

Context managers are useful in AI/ML applications for handling:

- Dataset files
- Configuration files
- Database connections
- API/network resources
- Temporary resources
- Resource management during data processing

For example, large datasets may be read from files using a context
manager so that the file resource is properly closed after processing.

# 6️⃣ Exception Handling

## 🧠 What is Exception Handling?

**Exception Handling** is a mechanism in Python used to handle runtime
errors gracefully so that the program can continue running instead of
crashing unexpectedly.

An exception can occur when a program encounters an unexpected situation,
such as:

- Dividing a number by zero
- Converting invalid input into an integer
- Accessing a missing file
- Performing an invalid operation

Python provides several keywords for handling exceptions:

```text
try
except
else
finally
raise
```

---

## ❓ What is an Exception?

An **Exception** is an error that occurs during the execution of a
Python program and interrupts its normal flow.

For example:

```python
a = 10
b = 0

print(a / b)
```

This produces:

```text
ZeroDivisionError: division by zero
```

Instead of allowing the program to crash, we can handle the exception
using `try-except`.

---

## 🔹 `try`

The `try` block contains the code that may potentially raise an
exception.

### Syntax

```python
try:
    # Code that may cause an exception
```

Example:

```python
try:
    result = 10 / 0
```

The division operation can raise a `ZeroDivisionError`.

---

## 🔹 `except`

The `except` block is used to handle an exception raised inside the
`try` block.

### Example

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

The program handles the error instead of terminating with an
unhandled exception.

---

## 🔹 Handling User Input

User input can also produce exceptions.

```python
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number.")
```

If the user enters:

```text
abc
```

the program handles the `ValueError`.

---

## 🔹 Multiple `except` Blocks

Different types of exceptions can be handled separately.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Here:

- `ValueError` handles invalid numeric input.
- `ZeroDivisionError` handles division by zero.

---

## 🔹 Using `as error`

The `as` keyword can be used to store the exception object in a variable.

```python
try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError as error:
    print("Error:", error)
```

Output:

```text
Error: division by zero
```

The variable `error` contains information about the exception.

---

## 🔹 General `Exception`

Python provides the `Exception` class as a general base class for
many built-in exceptions.

```python
try:
    number = int(input("Enter a number: "))

    print(10 / number)

except Exception:
    print("An unexpected error occurred.")
```

`except Exception` can catch many unexpected exceptions.

However, specific exceptions should generally be handled when possible.

For example:

```python
except ValueError:
```

is more informative than immediately using:

```python
except Exception:
```

---

## 🔹 Complete Exception Handling Example

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception:
    print("An unexpected error occurred.")
```

This example handles multiple possible runtime errors.

---

## 🔧 Function-Based Exception Handling

Exception handling can also be used with functions.

```python
def divide(a: int, b: int) -> float:
    return a / b


try:
    result = divide(10, 0)
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

The function performs the operation, while the calling code handles
the exception.

---

## 🏫 Class-Based Exception Handling

Exception handling can also be implemented inside class methods.

```python
class Calculator:

    def divide(self, a: int, b: int) -> float:

        try:
            return a / b

        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return 0.0


calculator = Calculator()

print(calculator.divide(10, 2))
print(calculator.divide(10, 0))
```

Output:

```text
5.0
Cannot divide by zero.
0.0
```

Here, the `divide()` method handles the `ZeroDivisionError` internally.

---

## ⚠️ Important Notes

### 1. Avoid unnecessary broad exception handling

Instead of:

```python
try:
    ...
except Exception:
    ...
```

prefer specific exceptions when you know what can go wrong.

### 2. Do not silently ignore errors

Avoid:

```python
try:
    ...
except:
    pass
```

because it can hide important errors and make debugging difficult.

---

# 7️⃣ Raising Errors — `raise`

## 🧠 What is `raise`?

The **`raise` statement** is used to manually raise an exception in
Python when a specific condition is not satisfied.

It allows the programmer to define when an error should occur.

---

## 🔹 Basic `raise`

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")
```

Output:

```text
ValueError: Age must be 18 or above
```

Here, the programmer manually raises a `ValueError`.

---

## 🔹 Why Use `raise`?

`raise` is useful when the program needs to enforce a specific rule.

For example:

- Age cannot be negative.
- Marks must be within a valid range.
- A required value must not be empty.
- A function argument must satisfy a condition.

---

## 🔹 `raise` with a Function

```python
def check_age(age: int) -> None:

    if age < 0:
        raise ValueError("Age cannot be negative.")

    elif age >= 18:
        print("You are eligible.")

    else:
        print("Not eligible.")


check_age(20)
```

Output:

```text
You are eligible.
```

---

## 🔹 `raise` with `try-except`

A manually raised exception can be caught using `try-except`.

```python
def check_age(age: int) -> None:

    if age < 0:
        raise ValueError("Age cannot be negative.")

    elif age >= 18:
        print("You are eligible.")

    else:
        print("Not eligible.")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as error:
    print("Error:", error)
```

If the user enters:

```text
-5
```

the function raises:

```python
ValueError("Age cannot be negative.")
```

and the `except` block handles it.

---

## 🔹 Custom Error Messages

The programmer can provide a meaningful message with the exception.

```python
marks = 120

if marks > 100 or marks < 0:
    raise ValueError("Marks must be between 0 and 100.")
```

This makes the reason for the error easier to understand.

---

## 💡 Practical Example

```python
def withdraw(balance: float, amount: float) -> float:

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


try:
    balance = 5000
    amount = 6000

    remaining_balance = withdraw(balance, amount)

    print("Remaining Balance:", remaining_balance)

except ValueError as error:
    print("Error:", error)
```

Output:

```text
Error: Insufficient balance.
```

---

## ⚠️ Important Note

`raise` does not mean the error must always be handled immediately.

If there is no suitable `try-except` block to handle the exception,
the exception will propagate upward and may eventually terminate
the program.

---

# 8️⃣ `try-except-else`

## 🧠 What is `else` in Exception Handling?

The `else` block is executed **only when the `try` block completes
successfully without raising an exception**.

### Basic Structure

```python
try:
    # Code that may raise an exception

except SomeException:
    # Runs if exception occurs

else:
    # Runs if no exception occurs
```

---

## 🔹 Example

```python
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by 0.")

except ValueError:
    print("Invalid number.")

else:
    print("Division result:", result)
```

If the user enters:

```text
10
2
```

Output:

```text
Division result: 5.0
```

The `else` block runs because no exception occurred.

If the user enters:

```text
10
0
```

Output:

```text
Cannot divide by 0.
```

The `else` block does not execute.

---

## 🔍 When Does `else` Execute?

```text
try
 ↓
Exception?
 ├── Yes → except
 │
 └── No  → else
```

Therefore:

- `try` → code that may cause an exception.
- `except` → handles the exception.
- `else` → runs only when `try` succeeds.

---

## 🔧 Function Example

```python
def divide(a: int, b: int) -> float:

    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by 0.")
        return 0.0

    else:
        print("Division successful.")
        return result


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = divide(a, b)

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")
```

The `else` block inside `divide()` executes only when the division
is successful.

---

# 9️⃣ `finally`

## 🧠 What is `finally`?

The **`finally` block** is used to execute code regardless of whether
an exception occurs or not.

It is commonly used for cleanup operations.

---

## 🔹 Basic Syntax

```python
try:
    # Code

except SomeException:
    # Error handling

finally:
    # Always executes
```

---

## 🔹 Basic Example

```python
try:
    number = int(input("Enter a number: "))

    print(10 / number)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program execution completed.")
```

The final message is printed whether the operation succeeds or fails.

---

## 🔹 `finally` with `try-except-else`

All three blocks can be used together.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division result:", result)

finally:
    print("Program execution completed.")
```

Execution flow:

```text
try
 ↓
Exception?
 ├── Yes → except
 │
 └── No  → else
             ↓
          finally
```

The `finally` block executes in both cases.

---

## 🔄 `finally` with `return`

The `finally` block executes even if a `return` statement is present
inside the `try` or `except` block.

```python
def divide(a: int, b: int) -> float:

    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0.0

    else:
        print("Division successful.")
        return result

    finally:
        print("Division operation completed.")


print("Result:", divide(10, 2))
print("Result:", divide(10, 0))
```

Output:

```text
Division successful.
Division operation completed.
Result: 5.0

Cannot divide by zero.
Division operation completed.
Result: 0.0
```

Even though `return` is executed, the `finally` block still runs before
the function actually returns.

---

## ⚠️ Important Note About `return` in `finally`

Although Python allows `return` inside `finally`, it should generally
be avoided because it can override a previous return value or exception.

Example:

```python
def example():
    try:
        return 10

    finally:
        return 20
```

The function returns:

```text
20
```

The `return` inside `finally` overrides the earlier `return`.

Therefore, `finally` should normally be used for cleanup rather than
returning values.

---

## 🧹 Common Use Cases of `finally`

`finally` is useful when some cleanup operation must happen regardless
of whether an error occurs.

Examples include:

- Closing resources
- Releasing locks
- Cleaning temporary resources
- Logging completion of an operation
- Closing connections

---

## 🤖 AI Engineer Relevance

Exception handling is extremely important in AI/ML and production
applications.

AI systems may encounter errors while:

- Loading datasets
- Reading model files
- Calling APIs
- Processing user input
- Loading configuration files
- Running model predictions
- Connecting to external services

Using `try-except`, `raise`, `else`, and `finally` allows AI applications
to handle failures more safely and provide meaningful error messages
instead of unexpectedly crashing.

For example, an AI API application can catch network or input errors
and return a controlled response to the user.

# 🔟 `__name__ == "__main__"`

## 🧠 What is `__name__`?

`__name__` is a special built-in variable in Python that represents
the name of the current module.

Its value depends on how the Python file is being used.

When a Python file is executed directly, Python sets:

```python
__name__ = "__main__"
```

When the same file is imported as a module, `__name__` contains the
name of that module.

---

## 🔹 Understanding `__main__`

Consider the following code:

```python
print(__name__)
```

If the file is executed directly:

```text
__main__
```

This happens because Python considers the directly executed file to be
the main program.

---

## 🔹 `if __name__ == "__main__":`

The common pattern is:

```python
if __name__ == "__main__":
    # Code to execute only when this file is run directly
```

This ensures that the code inside the block runs only when the file is
executed directly.

---

## 🔹 Basic Example

```python
print(__name__)

if __name__ == "__main__":
    print("This file is running directly")
```

When the file is executed directly:

```text
__main__
This file is running directly
```

---

## 🔄 Direct Execution vs Importing

Suppose we have a file called `main.py`:

```python
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print("Testing calculator module...")
    print("Addition:", add(10, 20))
    print("Multiplication:", multiply(5, 4))
```

If we run:

```text
python main.py
```

the code inside:

```python
if __name__ == "__main__":
```

will execute.

---

## 🔹 Importing the Module

Now suppose another file imports `main.py`:

```python
import main

print("Using calculator module...")

print("Addition:", main.add(5, 10))
print("Multiplication:", main.multiply(4, 6))
```

When `main.py` is imported, its:

```python
if __name__ == "__main__":
```

block does **not** execute.

Only the functions and other module-level definitions that are meant
to be available are imported.

---

## 📁 `main.py` + `test.py` Example

### `main.py`

```python
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)


def get_grade(average: float) -> str:

    if average >= 75:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 50:
        return "C"

    else:
        return "Fail"


def main() -> None:

    name = "Harry"
    marks = [80, 75, 90, 85]

    average = calculate_average(marks)
    grade = get_grade(average)

    print("Student Name:", name)
    print("Marks:", marks)
    print("Average:", average)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
```

### `test.py`

```python
import main


marks = [80, 75, 90, 85]

average = main.calculate_average(marks)
grade = main.get_grade(average)

print("Average:", average)
print("Grade:", grade)
```

When `main.py` is executed directly, `main()` runs.

When `main.py` is imported by `test.py`, `main()` does not run
automatically.

---

## ⭐ Why is `__name__ == "__main__"` Useful?

This pattern is useful because it allows a Python file to work as both:

- A standalone program
- An importable module

It prevents testing or execution code from running automatically when
the file is imported.

This is especially useful when working with larger projects containing
multiple Python modules.

---

## 🤖 AI Engineer Relevance

AI projects are commonly divided into multiple modules such as:

```text
data_processing.py
model.py
training.py
prediction.py
main.py
```

Using:

```python
if __name__ == "__main__":
```

allows individual modules to be imported without automatically running
their test or execution code.

This helps keep AI projects modular and maintainable.

---

# 1️⃣1️⃣ Global Keyword & Scope

## 🧠 What is Scope?

**Scope** refers to the region of a Python program where a variable can
be accessed or used.

Python mainly works with different levels of scope such as:

- Local Scope
- Global Scope

Understanding scope helps determine where variables are available and
how their values behave inside and outside functions.

---

## 🔹 Local Scope

A variable created inside a function normally belongs to the local
scope of that function.

```python
def show_number():
    number = 10
    print("Inside:", number)


show_number()
```

Output:

```text
Inside: 10
```

The variable `number` exists inside the function's local scope.

Trying to access it outside the function:

```python
def show_number():
    number = 10


show_number()

print(number)
```

will result in a `NameError` because `number` is not defined in the
global scope.

---

## 🌍 Global Scope

A variable created outside a function belongs to the global scope.

```python
count = 10


def show_count():
    print("Inside:", count)


show_count()

print("Outside:", count)
```

Output:

```text
Inside: 10
Outside: 10
```

The function can read the global variable.

---

## 🔹 Local Variable with the Same Name

If a variable with the same name is assigned inside a function, Python
treats it as a local variable.

```python
count = 10


def change_count():
    count = 20
    print("Inside:", count)


change_count()

print("Outside:", count)
```

Output:

```text
Inside: 20
Outside: 10
```

The local `count` is different from the global `count`.

---

## 🔑 `global` Keyword

The **`global` keyword** is used inside a function to indicate that a
variable refers to the global variable defined outside the function.

It allows a function to modify the value of a global variable.

---

## 🔹 Without `global`

```python
count = 10


def change_count():
    count = 20
    print("Inside:", count)


change_count()

print("Outside:", count)
```

Output:

```text
Inside: 20
Outside: 10
```

The global variable remains unchanged.

---

## 🔹 With `global`

```python
count = 10


def change_count():

    global count

    count = 20

    print("Inside:", count)


change_count()

print("Outside:", count)
```

Output:

```text
Inside: 20
Outside: 20
```

The `global` keyword tells Python that the `count` inside the function
refers to the global variable.

---

## 🔄 Modifying a Global Variable

Another example:

```python
score = 0


def increase_score():

    global score

    score += 10


increase_score()
increase_score()

print("Score:", score)
```

Output:

```text
Score: 20
```

The function modifies the global `score`.

---

## ⚠️ Important Note

Global variables should be used carefully.

Using too many global variables can make programs harder to understand,
debug, and maintain because many parts of the program may modify the
same data.

In larger applications, including AI/ML projects, it is often better to
pass data through function parameters, return values, classes, or other
controlled structures.

---

## 💡 Practical Example

```python
temperature = 25


def increase_temperature(value: int) -> None:

    global temperature

    temperature += value


increase_temperature(5)

print("Temperature:", temperature)
```

Output:

```text
Temperature: 30
```

---

## 🤖 AI Engineer Relevance

Understanding scope is important when working with:

- Configuration values
- Model settings
- Data-processing functions
- Classes and modules
- Larger Python applications

However, global state should generally be minimized in production
projects because uncontrolled shared state can make debugging and
testing more difficult.

---

# 1️⃣2️⃣ `enumerate()`

## 🧠 What is `enumerate()`?

The **`enumerate()` function** is used to iterate over an iterable while
keeping track of both the index and the value of each item.

It is especially useful when both the position and the actual value
are required during iteration.

---

## 🔹 Basic Usage

Consider a normal loop:

```python
fruits = ["Apple", "Banana", "Mango"]

for index in range(len(fruits)):
    print(index, fruits[index])
```

This works, but Python provides a cleaner approach using `enumerate()`.

```python
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 Apple
1 Banana
2 Mango
```

`enumerate()` provides both:

```text
index
value
```

during each iteration.

---

## 🔹 Basic Syntax

```python
enumerate(iterable, start=0)
```

By default, the index starts from `0`.

---

## 🔢 `start` Parameter

The `start` parameter allows us to specify the starting index.

```python
fruits = ["Apple", "Banana", "Mango"]

for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)
```

Output:

```text
1 Apple
2 Banana
3 Mango
```

This is useful when displaying human-readable numbering.

---

## 📋 Using `enumerate()` with Lists

```python
subjects = [
    "Python",
    "DBMS",
    "Computer Networks",
    "AI"
]

for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")
```

Output:

```text
1. Python
2. DBMS
3. Computer Networks
4. AI
```

---

## 🔤 Using `enumerate()` with Strings

`enumerate()` can also be used with strings because strings are iterable.

```python
name = "Sonal"

for number, character in enumerate(name, start=1):
    print(f"{number}. {character}")
```

Output:

```text
1. S
2. o
3. n
4. a
5. l
```

---

## 🔧 Using `enumerate()` with Functions

A function can return an iterable, which can then be used with
`enumerate()`.

```python
def get_subjects():
    return [
        "Python",
        "DBMS",
        "AI",
        "Computer Networks"
    ]


subjects = get_subjects()

for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")
```

Output:

```text
1. Python
2. DBMS
3. AI
4. Computer Networks
```

---

## 🔹 `enumerate()` Inside a Function

```python
def display_marks(marks: list[int]) -> None:

    for number, mark in enumerate(marks, start=1):
        print(f"Subject {number}: {mark}")


marks = [80, 75, 90, 85]

display_marks(marks)
```

Output:

```text
Subject 1: 80
Subject 2: 75
Subject 3: 90
Subject 4: 85
```

---

## ⚖️ `enumerate()` vs `range(len())`

### Using `range(len())`

```python
subjects = ["Python", "AI", "DBMS"]

for index in range(len(subjects)):
    print(index, subjects[index])
```

### Using `enumerate()`

```python
subjects = ["Python", "AI", "DBMS"]

for index, subject in enumerate(subjects):
    print(index, subject)
```

`enumerate()` is usually cleaner and easier to read when both the index
and value are required.

---

## 🤖 AI Engineer Relevance

`enumerate()` is useful in data-processing and AI/ML code when both
the position and value of an item are required.

For example, it can be used when:

- Processing datasets
- Displaying prediction results
- Tracking processed items
- Generating numbered outputs
- Debugging data-processing pipelines

It is a simple but useful Python tool that appears frequently in
practical programming.

# 1️⃣3️⃣ List Comprehension

## 🧠 What is List Comprehension?

**List Comprehension** is a concise way to create a new list by applying
an expression to each item of an iterable.

It provides a shorter and often more readable alternative to writing
a traditional `for` loop for list creation.

---

## 🔹 Basic List Comprehension

### Traditional `for` Loop

```python
numbers = [2, 4, 6, 8, 10]

cubes = []

for number in numbers:
    cubes.append(number ** 3)

print(cubes)
```

Output:

```text
[8, 64, 216, 512, 1000]
```

### Using List Comprehension

The same operation can be written as:

```python
numbers = [2, 4, 6, 8, 10]

cubes = [number ** 3 for number in numbers]

print(cubes)
```

Output:

```text
[8, 64, 216, 512, 1000]
```

The list comprehension is shorter while performing the same operation.

---

## 🔹 Basic Syntax

```python
[expression for item in iterable]
```

The three main parts are:

- `expression` → What should be added to the new list.
- `item` → Each element from the iterable.
- `iterable` → The collection being iterated over.

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## 🔹 List Comprehension with `if`

List Comprehension can include an `if` condition to filter elements.

### Definition

> **List Comprehension with an `if` condition is used to create a new
> list containing only the items that satisfy a specified condition.**

### Syntax

```python
[expression for item in iterable if condition]
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

Only the numbers satisfying:

```python
number % 2 == 0
```

are included in the new list.

---

## 🔹 Another Example with `if`

```python
numbers = [2, 4, 6, 8, 3, 9, 1]

greater_than_five = [
    number
    for number in numbers
    if number > 5
]

print(greater_than_five)
```

Output:

```text
[6, 8, 9]
```

---

## 🔹 List Comprehension with `if-else`

### Definition

> **List Comprehension with `if-else` is used to create a new list by
> applying different expressions depending on whether a condition is
> true or false.**

### Syntax

```python
[expression_if_true if condition else expression_if_false
 for item in iterable]
```

The important difference is that with `if-else`, the condition comes
**before the `for` loop**.

---

## 🔹 Example — Even or Odd

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
```

Here:

```python
"Even" if number % 2 == 0 else "Odd"
```

means:

- If the number is even → `"Even"`
- Otherwise → `"Odd"`

---

## 🔄 Modifying Values using `if-else`

List Comprehension can also modify numbers based on a condition.

### Example

If a number is greater than or equal to `20`, add `10`.
Otherwise, subtract `5`.

```python
numbers = [10, 15, 20, 25, 30]

result = [
    number + 10 if number >= 20 else number - 5
    for number in numbers
]

print(result)
```

Output:

```text
[5, 10, 30, 35, 40]
```

For `20`:

```python
20 + 10
```

produces:

```text
30
```

For `15`:

```python
15 - 5
```

produces:

```text
10
```

---

## 🔁 Nested List Comprehension

### Definition

> **Nested List Comprehension is a list comprehension that contains
> another `for` loop inside it and is commonly used to process nested
> iterables such as lists of lists.**

### Traditional Nested Loop

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []

for row in matrix:
    for number in row:
        result.append(number)

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Using Nested List Comprehension

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    number
    for row in matrix
    for number in row
]

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The order of the `for` loops remains the same:

```python
for row in matrix
for number in row
```

---

## 🔀 Nested `if` in List Comprehension

Multiple conditions can be used to filter elements.

### Example

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [
    number
    for number in numbers
    if number > 3
    if number % 2 == 0
]

print(result)
```

Output:

```text
[4, 6, 8, 10]
```

Both conditions must be satisfied:

```text
number > 3
AND
number is even
```

---

## 🔀 Nested `if-else` in List Comprehension

Multiple conditions can also be combined using nested `if-else`
expressions.

### Example

```python
numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0
    else "Positive" if number > 0
    else "Zero"
    for number in numbers
]

print(result)
```

Output:

```text
['Positive', 'Even', 'Positive', 'Even', 'Positive']
```

Nested `if-else` expressions can become difficult to read when too many
conditions are used. In such cases, a normal `if-elif-else` structure
may be clearer.

---

## ⚠️ Important Notes

List Comprehensions are useful for concise list creation, but they
should not be used when the resulting expression becomes difficult to
understand.

Prefer a normal loop when:

- There are many conditions.
- Multiple statements are required.
- Complex logic is involved.
- Readability would be reduced.

---

## 🤖 AI Engineer Relevance

List Comprehensions are frequently useful in data-processing tasks.

They can be used for:

- Filtering data
- Transforming values
- Cleaning simple datasets
- Preparing lists for ML operations
- Processing model outputs
- Performing simple preprocessing operations

For example:

```python
values = [10, 20, 30, 40, 50]

scaled_values = [
    value / 10
    for value in values
]

print(scaled_values)
```

Output:

```text
[1.0, 2.0, 3.0, 4.0, 5.0]
```

However, for large numerical datasets, libraries such as NumPy are
generally preferred because they provide optimized numerical operations.

---

# 1️⃣4️⃣ File Handling

> **Note:** File Handling was studied previously and is included in
> this chapter as a revision/reference topic.

## 🧠 What is File Handling?

**File Handling** is the process of creating, reading, writing, and
modifying files using Python.

Files allow programs to store data permanently so that the data can
be used even after the program stops running.

---

## 🔹 `open()`

The `open()` function is used to open a file.

### Basic Syntax

```python
open(file_name, mode)
```

Example:

```python
file = open("file.txt", "r")
```

After working with the file, it should be closed:

```python
file.close()
```

However, using `with open()` is generally preferred because Python
automatically handles closing the file.

---

## 🔹 File Modes

Common file modes include:

| Mode | Purpose |
|------|---------|
| `"r"` | Read |
| `"w"` | Write |
| `"a"` | Append |
| `"x"` | Create a new file |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

---

## 📖 Reading Files

A file can be read using the `read()` method.

```python
with open("file.txt", "r") as file:
    data = file.read()

print(data)
```

---

## 🔹 Reading Specific Lines

### `readline()`

Reads one line at a time.

```python
with open("file.txt", "r") as file:
    line = file.readline()

print(line)
```

### `readlines()`

Reads all lines and returns them as a list.

```python
with open("file.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

---

## ✍️ Writing Files

The `"w"` mode is used to write data to a file.

```python
with open("file.txt", "w") as file:
    file.write("Hello Python")
```

⚠️ `"w"` mode can overwrite existing file content.

---

## ➕ Appending Files

The `"a"` mode adds new content to the end of an existing file.

```python
with open("file.txt", "a") as file:
    file.write("\nLearning Python")
```

Existing content remains and the new content is added at the end.

---

## 🔐 Using `with open()`

The `with` statement automatically handles resource cleanup.

```python
with open("file.txt", "r") as file:
    data = file.read()

print(data)
```

There is no need to manually write:

```python
file.close()
```

when using the context manager.

---

## 📂 Multiple File Handling

Multiple files can be opened using multiple context managers in a
single `with` statement.

```python
with open("file1.txt", "r") as file1, \
     open("file2.txt", "r") as file2:

    data1 = file1.read()
    data2 = file2.read()

    print("File 1:", data1)
    print("File 2:", data2)
```

This provides a clean way to manage multiple file resources.

---

## 💡 Practical Example

```python
with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("AI\n")
    file.write("Machine Learning\n")


with open("notes.txt", "r") as file:
    notes = file.read()

print(notes)
```

Output:

```text
Python
AI
Machine Learning
```

---

## ⚠️ Common File Handling Errors

### `FileNotFoundError`

This occurs when Python cannot find the specified file.

```python
with open("missing.txt", "r") as file:
    data = file.read()
```

If the file does not exist in the expected location, Python raises:

```text
FileNotFoundError
```

The current working directory is important when using relative paths.

---

## 🤖 AI Engineer Relevance

File Handling is important in AI/ML because applications frequently
work with stored data and resources such as:

- Text files
- CSV files
- Configuration files
- Model files
- Dataset files
- Logs
- JSON files

File Handling also provides the foundation for working with structured
data formats and data-processing pipelines.

In modern AI projects, specialized libraries such as Pandas are often
used for structured datasets, while Python's built-in file handling
remains useful for general file operations.

# 1️⃣5️⃣ JSON Handling

## 🧠 What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight, text-based data
format used to store and exchange structured data between applications.

JSON is widely used in:

- APIs
- Web applications
- Configuration files
- Data exchange
- Automation
- AI/ML applications

JSON data is written using key-value pairs and commonly uses structures
similar to Python dictionaries and lists.

---

## 🔹 Basic JSON Structure

A simple JSON object looks like:

```json
{
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}
```

JSON objects use:

- `{ }` for objects
- `[ ]` for arrays
- `" "` for strings
- Key-value pairs separated using `:`
- Multiple items separated using `,`

---

## 🔹 JSON Object and Python Dictionary

JSON:

```json
{
    "name": "Sonal",
    "age": 25
}
```

Python:

```python
{
    "name": "Sonal",
    "age": 25
}
```

They look similar, but JSON is a **data format**, while a Python
dictionary is a **Python data structure**.

Python provides the built-in `json` module to work with JSON data.

---

## 🔹 Python `json` Module

The `json` module provides functions for converting Python objects
to JSON and JSON data back to Python objects.

```python
import json
```

The four main functions are:

| Function | Purpose |
|----------|---------|
| `json.dumps()` | Python object → JSON string |
| `json.loads()` | JSON string → Python object |
| `json.dump()` | Python object → JSON file |
| `json.load()` | JSON file → Python object |

---

## 🔄 `json.dumps()`

### Definition

> **`json.dumps()` converts a Python object into a JSON-formatted string.**

Example:

```python
import json

student = {
    "name": "Harry",
    "age": 20,
    "course": "Python"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
```

Output:

```text
{"name": "Harry", "age": 20, "course": "Python"}
<class 'str'>
```

The Python dictionary has been converted into a JSON-formatted string.

---

## 🎨 `indent` Parameter

The `indent` parameter formats JSON data in a more readable,
human-friendly structure.

Without `indent`:

```python
print(json.dumps(student))
```

Output:

```text
{"name": "Harry", "age": 20, "course": "Python"}
```

With `indent=4`:

```python
print(json.dumps(student, indent=4))
```

Output:

```text
{
    "name": "Harry",
    "age": 20,
    "course": "Python"
}
```

### Definition

> **The `indent` parameter is used to format JSON data with indentation,
> making it easier to read.**

---

## 🔄 `json.loads()`

### Definition

> **`json.loads()` converts a JSON-formatted string into a Python object.**

It is the reverse of `json.dumps()`.

### Example

```python
import json

json_data = '{"name": "Sonal", "age": 25, "skill": "Python"}'

details = json.loads(json_data)

print(details)
print(type(details))
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'skill': 'Python'}
<class 'dict'>
```

The JSON string is converted into a Python dictionary.

---

## 💾 `json.dump()`

### Definition

> **`json.dump()` is used to write a Python object directly into a JSON file.**

Example:

```python
import json

student = {
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

This creates a file named:

```text
student.json
```

The file contains:

```json
{
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}
```

Here:

```python
json.dump(student, file, indent=4)
```

means:

- `student` → Python object to be stored.
- `file` → target JSON file.
- `indent=4` → readable formatting.

---

## 📂 `json.load()`

### Definition

> **`json.load()` is used to read JSON data from a JSON file and convert
> it into a Python object.**

Example:

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(type(student))
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'skill': 'Python'}
<class 'dict'>
```

The JSON file is converted back into a Python dictionary.

---

## 🔁 Python ↔ JSON Conversion

The complete conversion process can be remembered as:

```text
Python Object
      │
      ▼
 json.dumps()
      │
      ▼
 JSON String
      │
      ▼
 json.loads()
      │
      ▼
Python Object
```

For files:

```text
Python Object
      │
      ▼
 json.dump()
      │
      ▼
 JSON File
      │
      ▼
 json.load()
      │
      ▼
Python Object
```

---

## 📊 `dump` vs `dumps`

The extra `s` is an important clue.

### `json.dump()`

Used with a file:

```python
json.dump(data, file)
```

### `json.dumps()`

Used to create a JSON string:

```python
json_string = json.dumps(data)
```

```text
dump  → File
dumps → String
```

---

## 📊 `load` vs `loads`

Similarly:

### `json.load()`

Reads from a JSON file:

```python
data = json.load(file)
```

### `json.loads()`

Reads from a JSON string:

```python
data = json.loads(json_string)
```

```text
load  → File
loads → String
```

---

## 📄 Complete JSON File Example

### Writing Data

```python
import json

student = {
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

### Reading Data

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'skill': 'Python'}
```

---

## ✏️ Adding / Updating Data in JSON

JSON data can be loaded into Python, modified, and then written back
to the JSON file.

Suppose `student.json` contains:

```json
{
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}
```

We can add new information:

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

student["course"] = "B.Tech CSE"
student["city"] = "Lucknow"

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

After execution, the JSON file becomes:

```json
{
    "name": "Sonal",
    "age": 25,
    "skill": "Python",
    "course": "B.Tech CSE",
    "city": "Lucknow"
}
```

The general process is:

```text
Read JSON File
      ↓
json.load()
      ↓
Python Object
      ↓
Modify Data
      ↓
json.dump()
      ↓
Write JSON File
```

---

## ⚠️ Important JSON Notes

### 1. JSON strings use double quotes

Valid JSON:

```json
{
    "name": "Sonal"
}
```

Python strings can use either single or double quotes, but JSON
specification uses double quotes for strings.

### 2. JSON and Python are not exactly the same

Although JSON objects resemble Python dictionaries, they are different
concepts.

JSON is a format for representing and exchanging data.

Python dictionaries are Python data structures.

### 3. JSON is commonly used with APIs

Many APIs send and receive structured data in JSON format.

---

## 🤖 AI Engineer Relevance

JSON is extremely important in modern AI and software development.

AI applications frequently use JSON for:

- API requests
- API responses
- Model configuration
- Application settings
- Structured data exchange
- Storing metadata
- Communication between frontend and backend
- Working with AI services and LLM APIs

For example, an AI application may receive a structured response like:

```json
{
    "question": "What is Python?",
    "answer": "Python is a programming language.",
    "confidence": 0.95
}
```

Python can easily convert this JSON data into dictionaries and lists
using the `json` module.

---

# 1️⃣6️⃣ Practical Concepts

The following examples combine multiple concepts learned in Chapter 12.

---

## 🔹 Type Hints + Functions

Type Hints can make function inputs and outputs easier to understand.

```python
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)


marks = [80, 75, 90, 85]

average = calculate_average(marks)

print("Average:", average)
```

Output:

```text
Average: 82.5
```

Concepts used:

- Functions
- Type Hints
- Lists
- Return Type
- Built-in `sum()`
- `len()`

---

## 🔹 Match-Case + Type Hints

```python
def get_grade(marks: int) -> str:

    match marks:

        case marks if 90 <= marks <= 100:
            return "A"

        case marks if 75 <= marks <= 89:
            return "B"

        case marks if 50 <= marks <= 74:
            return "C"

        case marks if 0 <= marks <= 49:
            return "Fail"

        case _:
            return "Invalid Marks"


marks = 85

print("Grade:", get_grade(marks))
```

Output:

```text
Grade: B
```

Concepts used:

- Functions
- Type Hints
- Match-Case
- Guard Conditions

---

## 🔹 Dictionary Merge

```python
personal = {
    "name": "Sonal",
    "age": 25
}

skills = {
    "python": "Advanced",
    "sql": "Intermediate"
}

profile = personal | skills

print(profile)
```

Output:

```text
{
    'name': 'Sonal',
    'age': 25,
    'python': 'Advanced',
    'sql': 'Intermediate'
}
```

Concepts used:

- Dictionaries
- Dictionary Merge Operator `|`
- Structured data

---

## 🔹 Exception Handling + Functions

```python
def divide(a: int, b: int) -> float:
    return a / b


try:
    result = divide(10, 0)
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

Concepts used:

- Functions
- Type Hints
- `try`
- `except`
- `ZeroDivisionError`

---

## 🔹 `__name__ == "__main__"` + Modules

A Python module can contain reusable functions and a main execution
section.

```python
def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print("Result:", add(10, 20))


if __name__ == "__main__":
    main()
```

When this file is executed directly, `main()` runs.

When the module is imported, the `main()` function is not automatically
executed.

---

## 🔹 JSON File Handling

```python
import json

student = {
    "name": "Sonal",
    "age": 25,
    "skill": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'skill': 'Python'}
```

Concepts used:

- Dictionary
- JSON
- `json.dump()`
- `json.load()`
- Context Manager
- File Handling

---

## 🔗 Chapter 12 Concepts Working Together

Many real-world Python programs combine several concepts rather than
using each feature independently.

For example:

```text
Type Hints
    ↓
Functions
    ↓
Exception Handling
    ↓
File Handling
    ↓
JSON
    ↓
Structured Application Data
```

These concepts form useful building blocks for larger Python
applications and AI/ML projects.

# 1️⃣7️⃣ Chapter 12 Summary

## 📚 What I Learned

In Chapter 12, I learned several advanced and practical Python
features that are useful for writing cleaner, safer, and more
maintainable programs.

### 🔹 Topics Covered

1. **Walrus Operator `:=`**
   - Assign and use a value within the same expression.
   - Useful in conditions and loops.

2. **Type Hints / Type Definitions**
   - Specify expected data types for variables, function parameters,
     and return values.
   - Helps improve code readability and development experience.

3. **Match-Case**
   - Used for pattern matching and handling multiple possible cases.
   - Supports conditions using guards.

4. **Dictionary Merge Operators**
   - `|` creates a new merged dictionary.
   - `|=` updates an existing dictionary.

5. **Multiple Context Managers**
   - Allows multiple resources to be managed using a single `with`
     statement.
   - Useful when working with multiple files or resources.

6. **Exception Handling**
   - Used to handle runtime errors gracefully.
   - Covered `try`, `except`, and exception types.

7. **Raising Errors**
   - The `raise` statement allows us to manually raise exceptions when
     specific conditions are not satisfied.

8. **`try-except-else`**
   - The `else` block executes when the `try` block completes
     successfully without an exception.

9. **`finally`**
   - Used for code that must execute regardless of whether an
     exception occurs.

10. **`__name__ == "__main__"`**
    - Controls whether a block of code executes when a file is run
      directly or imported as a module.

11. **Global Keyword & Scope**
    - Learned local and global scope.
    - Learned how the `global` keyword can modify a global variable
      from inside a function.

12. **`enumerate()`**
    - Used to iterate through an iterable while keeping track of
      index and value.

13. **List Comprehension**
    - Learned concise ways to create lists.
    - Covered conditions, `if-else`, and basic nested comprehensions.

14. **File Handling**
    - Reviewed opening, reading, writing, appending, and working with
      multiple files using context managers.

15. **JSON Handling**
    - Learned how to convert Python objects to JSON and JSON data back
      to Python objects.
    - Covered `json.dumps()`, `json.loads()`, `json.dump()`, and
      `json.load()`.

---

## 🧠 Important Concepts to Remember

```text
:=              → Assignment Expression

Type Hints      → Expected Data Types

match-case      → Pattern Matching

|               → Merge Dictionaries

|=              → Update Dictionary

with            → Resource Management

try-except      → Exception Handling

raise           → Manually Raise Exception

else            → Runs When try Succeeds

finally         → Always Executes

__main__        → Direct Execution Check

global          → Access/Modify Global Variable

enumerate()     → Index + Value

List Comprehension
                → Concise List Creation

JSON            → Structured Data Exchange
```

---

## 💡 Chapter 12 Takeaway

Chapter 12 focused on practical Python features that help move from
basic Python programming toward writing more structured and
production-oriented code.

The most important concepts from this chapter are:

- Type Hints
- Exception Handling
- Context Managers
- `__name__ == "__main__"`
- List Comprehensions
- `enumerate()`
- JSON Handling

These concepts will be useful when building larger Python projects
and working with APIs, data, automation, and AI/ML applications.

---

# 1️⃣8️⃣ AI Engineer Relevance

The concepts learned in this chapter are useful for an AI Engineer
because AI applications are not limited to writing machine learning
models. Real AI systems also require clean code, data handling,
error handling, APIs, configuration, and modular project structure.

---

## 🐍 Type Hints

Type Hints are especially useful in larger AI/ML projects.

Example:

```python
def predict(features: list[float]) -> float:
    return 0.95
```

They make function inputs and outputs easier to understand and can
improve code readability and development experience.

---

## 🛡️ Exception Handling

AI applications can encounter many runtime problems, such as:

- Invalid input data
- Missing files
- API failures
- Incorrect user input
- Model loading errors
- Network problems
- Unexpected data formats

Exception handling allows these situations to be handled gracefully.

Example:

```python
try:
    result = model.predict(data)

except Exception as error:
    print("Prediction failed:", error)
```

---

## 📄 JSON

JSON is one of the most important data formats used in modern
software and AI applications.

It is commonly used for:

- API requests
- API responses
- Model configurations
- Application settings
- Metadata
- Structured AI responses
- Communication between frontend and backend

Example:

```json
{
    "question": "What is Python?",
    "answer": "Python is a programming language.",
    "confidence": 0.95
}
```

---

## 🔗 Context Managers

Context managers are useful when working with resources such as:

- Files
- Database connections
- Network resources
- Temporary resources

Example:

```python
with open("data.json", "r") as file:
    data = json.load(file)
```

The resource is automatically managed and properly closed.

---

## 🧩 Modules and `__main__`

Large AI projects are usually divided into multiple modules.

For example:

```text
AI-Project/
│
├── main.py
├── model.py
├── data.py
├── utils.py
└── config.py
```

The `__name__ == "__main__"` pattern helps separate reusable module
code from code that should run when a file is executed directly.

---

## ⚡ List Comprehension

List comprehensions are useful for concise data processing.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

Similar filtering and transformation operations are frequently used
while preparing data.

---

## 🔢 `enumerate()`

`enumerate()` is useful when processing datasets while keeping track
of indexes.

Example:

```python
documents = ["Document 1", "Document 2", "Document 3"]

for index, document in enumerate(documents):
    print(index, document)
```

This becomes useful when processing collections of documents,
records, or other data.

---

## 🗂️ Dictionary Merge

AI applications often combine different configuration or metadata
dictionaries.

Example:

```python
default_config = {
    "model": "AI_Model",
    "temperature": 0.7
}

user_config = {
    "temperature": 0.2
}

final_config = default_config | user_config

print(final_config)
```

Output:

```text
{
    'model': 'AI_Model',
    'temperature': 0.2
}
```

---

## 🚀 Overall AI Engineer Connection

The concepts from this chapter can be connected to an AI project like:

```text
Python
   ↓
Type Hints
   ↓
Functions & Modules
   ↓
Exception Handling
   ↓
File Handling
   ↓
JSON
   ↓
Data Processing
   ↓
API / AI Model
   ↓
AI Application
```

Chapter 12 therefore provides several practical programming skills
that will be useful before moving deeper into NumPy, Pandas,
Machine Learning, Deep Learning, APIs, and LLM-based applications.

---

# 📌 Final Chapter 12 Takeaway

> **Chapter 12 helped me understand practical Python features that
> improve code readability, error handling, data processing, resource
> management, and modular programming.**

The concepts learned here will serve as a foundation for building
larger Python applications and future AI/ML projects.

---

# 📚 Course Information

**Course:** CodeWithHarry — Python Programming  
**Chapter:** 12  
**Topic:** Python Advanced Features & Utilities  
**Language:** Python

---

# 👨‍💻 Author

**Sonal Rai**