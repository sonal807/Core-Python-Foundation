#Match-Case: The match-case statement is a Python control-flow feature used to compare 
#a value against multiple patterns and execute the code associated with the first matching pattern.

#In python match-case can be undertanded as advance version of if-elif-else statement, although it can do more powerful pattern matching
#and similar to switch-case statement in C, Java or Javascript.

##Basic syntax:
# match expression:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case pattern3:
#         # code
#     case _:
#         # default code

#Simple example
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 1:
        print("Wednesday")
    case _:
        print("Invalid day")

#if-elif-else vs match-case
#In if-elif-else
day = 2

if day == 1:
    print("Monday")
if day == 2:
    print("Tuesday")
if day == 1:
    print("Wednesday")
else:
    print("Invalid day")

#In match-case
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 1:
        print("Wednesday")
    case _:
        print("Invalid day")


#Default Case (_):If none of the previous cases match, execute this case (can be taken as similar to else)
choice = 5

match choice:
    case 1:
        print("Start")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:      #Default case(if above cases doesn't match the it will execute)
        print("Invalid Choice")

#Multiple values in one case: If we want same output for multiple case, the we use (|)
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:  #Multiple cases for same output
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")

#Match-Case with Strings
command = "start"

match command:
    case "start":
        print("Starting...")
    case "srop":
        print("Stopping...")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")

#User Input Example:
choice = input("Enter your choice: ")

match choice:
    case "1":
        print("You selected Python")
    case "2":
        print("You selected Java")
    case "3":
        print("You selected C++")
    case _:
        print("Invalid choice")

#Match-case with Conditions-- Guard: if can be used in match-case, this is called guard.
marks = 85

match marks:
    case marks if marks >= 90:  #(if marks >= 90) is a guard case.
        print("Excellent")
    case marks if marks >= 75:
        print("Very Good")
    case marks if marks >= 50:
        print("Pass")
    case _:
        print("Fail")

#Match-case with Lists: The real power can be understood here
data = [1, 2, 3]

match data:
    case[]:
        print("Empty list")
    case [x]:
        print(f"One element: {x}")
    case [x, y]:
        print(f"Two elements: {x}, {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y}, {z}")
    case _:
        print("Other list")
#Here the values are not only compared, python is checking structure/pattern.

#Example:
a = int(input("Enter first number: "))
operator = input("Enter operator: ")
b = int(input("Enter second number: "))

match operator:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        print(f"Result: {a / b}")
    case _:
        print("Invalid Operator")

#Example:
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

#Match-case with function
#Example:
def http_status(status):

    match status:
        case 200:
            return "OK"

        case 400:
            return "Not found"

        case 500:
            return "Internal server error"

        case _:
            return "Unknown status"

print(http_status(280))

#Example:
def get_grade(marks):
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

#Match-case with class:
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):

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