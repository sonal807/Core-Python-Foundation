#Pytest is a popular Python testing framework used to write
#simple, readable, and powerful automated tests.

#For using it first we need to install: pip install pytest

def add(a, b):
    # Do numbers ko add karke result return kar rahe hain.
    return a + b


def test_add():
    # Check kar rahe hain ki expected result 5 hai.
    assert add(2, 3) == 5