# __name__ == "__main__": if __name__ == "__main__": is used to ensure that a block of code runs only when the Python file is executed directly, not when it is imported as a module.
#__name__ is a special built-in variable in Python that tells us how the current Python file is being used.

print(__name__) #Output: __main__ ->When we directly run any python file, python gives a special name to that file

# if __name__ =="__main__": #if we run directly then this will be true
#     print("Hello!")

#Simple Example:
# print("Before")

if __name__ == "__main__": #Run this code only when this file is executed directly, not when it is imported.
    print("This file is running directly")

# print("After")

#Example:
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    result = add(10, 20)
    print("Result:", result)

#Direct run → testing/demo code chalega.

#Import → functions/classes available honge, testing code automatically nahi chalega.

#Example:
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


if __name__ == "__main__":
    print("Testing calculator module...")

    print("Addition:", add(10, 20))
    print("Multiplication:", multiply(5, 4))
    print("Division:", divide(10, 2))


#Example:
def calculate_average(marks: list[int]) -> float:
    return sum(marks)/ len(marks)

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