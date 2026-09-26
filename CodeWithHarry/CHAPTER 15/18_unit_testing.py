# Unit testing is the practice of testing individual units of code,
# such as functions or methods, independently to verify that they work correctly.
def add(a, b):
    # Two numbers ko add karke result return kar rahe hain.
    return a + b


# Unit test:
# Check kar rahe hain ki add(2, 3) ka expected result 5 hai.
result = add(2, 3)

if result == 5:
    print("Test passed.")
else:
    print("Test failed.")


#Example: multiple test case
def add(a, b):
    return a + b


# Test Case 1
if add(2, 3) == 5:
    print("Test 1 passed.")
else:
    print("Test 1 failed.")


# Test Case 2
if add(-2, 5) == 3:
    print("Test 2 passed.")
else:
    print("Test 2 failed.")


# Test Case 3
if add(0, 0) == 0:
    print("Test 3 passed.")
else:
    print("Test 3 failed.")


#unittest module: unittest is Python's built-in unit testing framework used to create, organize,
#and run automated tests for individual parts of a program.

import unittest


def add(a, b):
    # Do numbers ko add karke result return kar rahe hain.
    return a + b


class TestAddFunction(unittest.TestCase):
    # TestAddFunction ek test class hai.
    # unittest.TestCase se inherit karke hum unittest ke
    # testing features aur assertion methods use kar sakte hain.

    def test_add(self):
        # Test method ka naam `test_` se start kiya hai.
        # unittest automatically is method ko test ke roop mein identify karega.

        # add(2, 3) ka expected result 5 hai.
        # assertEqual() actual result aur expected result ko compare karta hai.
        self.assertEqual(add(2, 3), 5)


# Ye check karta hai ki file directly run ho rahi hai ya
# kisi doosri file ke through import hui hai.
if __name__ == "__main__":

    # unittest ke test cases ko discover karke execute karta hai.
    unittest.main()

#Example: unittest with multiple test cases
import unittest


def add(a, b):
    # Do numbers ko add karke result return kar rahe hain.
    return a + b


class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        # Positive numbers ka test.
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        # Negative number ke saath addition test.
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        # Zero ke saath addition test.
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    # Saare test methods ko automatically run karta hai.
    unittest.main()


#assertRaises(): It is a unittest assertion used to verify that a
#specific exception is raised when a piece of code is executed.

import unittest


def divide(a, b):
    # Do numbers ko divide karke result return kar rahe hain.
    # Agar b = 0 hua, to Python ZeroDivisionError raise karega.
    return a / b


class TestDivideFunction(unittest.TestCase):

    def test_divide_by_zero(self):
        # Check kar rahe hain ki zero se divide karne par
        # ZeroDivisionError actually raise hota hai ya nahi.
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    # Saare test methods ko run karta hai.
    unittest.main()