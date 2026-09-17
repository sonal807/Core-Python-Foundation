#Write a program to display a/b where a and b are integer.
#if b = 0, display infinite by handling ZeroDivisionError.

try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    result = a / b
    print(result)

except ValueError:
    print("Enter a valid number.")

except ZeroDivisionError:
    print("Infinite")

finally:
    print("Program executed successfully")