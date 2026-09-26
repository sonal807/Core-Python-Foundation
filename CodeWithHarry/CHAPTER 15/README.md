# 📘 Chapter 15 — Robust & Professional Python

## 🎯 Objective

The goal of this chapter is to learn how to write Python code that is:

- **Robust** — able to handle unexpected situations safely.
- **Defensive** — prepared for invalid or unexpected input.
- **Reliable** — behaves predictably when something goes wrong.
- **Maintainable** — easy to understand and modify.
- **Testable** — easy to verify and debug.
- **Production-ready** — follows practices used in real-world applications.
- **AI Engineering-ready** — suitable as a foundation for AI APIs, RAG systems, AI agents, and other AI applications.

Throughout this chapter, we will move beyond simply making code "work" and learn how to make code **safe, readable, reliable, and easier to maintain**.

---

# 📌 Topics Covered

This chapter covers the following topics:

1. Robust Code
2. Defensive Programming
3. Input Validation
4. Type Hinting & `typing` Module
5. Pydantic & `BaseModel`
6. Advanced Exception Handling
7. Custom Exceptions
8. `assert`
9. Logging
10. Proper Error Messages
11. Resource Management
12. Configuration Handling
13. Retry Logic
14. Timeouts
15. Graceful Failure
16. Edge Cases
17. Clean & Maintainable Code
18. Testing Fundamentals
19. Unit Testing
20. Pytest
21. AI Engineer Practical Examples

---

# 1️⃣ Robust Code

## 📖 Definition

> **Robust code is code that can handle unexpected inputs, errors, and unusual situations without crashing or producing incorrect results.**

In simple words:

> Robust code sirf normal situation mein nahi, balki unexpected situations mein bhi safely kaam karta hai.

For example, consider this code:

    age = int(input("Enter your age: "))
    print("Your age is:", age)

This works if the user enters:

    25

But what happens if the user enters:

    twenty-five

Python will raise:

    ValueError

The program may terminate unexpectedly.

This makes the code relatively **fragile**.

---

## ❌ Fragile Code

    age = int(input("Enter your age: "))

The code assumes that the user will always enter a valid integer.

But real applications cannot always make this assumption.

---

## ✅ Robust Code

    while True:
        try:
            age = int(input("Enter your age: "))
            break

        except ValueError:
            print("Please enter a valid number.")

    print("Your age is:", age)

Now the program:

1. Takes input.
2. Attempts conversion.
3. Detects invalid input.
4. Shows a meaningful message.
5. Allows the user to try again.
6. Continues only after valid input is received.

---

## 🔹 Characteristics of Robust Code

Good robust code generally:

- Handles unexpected input.
- Handles possible exceptions.
- Validates data.
- Handles edge cases.
- Gives meaningful feedback.
- Avoids unnecessary crashes.
- Produces predictable behavior.
- Protects important operations.
- Separates error handling from normal logic where appropriate.

---

## 🔹 Robust Code vs Fragile Code

| Fragile Code | Robust Code |
|---|---|
| Assumes input is always valid | Validates input |
| May crash unexpectedly | Handles expected failures |
| Limited error handling | Appropriate exception handling |
| Ignores edge cases | Considers edge cases |
| Difficult to use safely | Predictable behavior |
| Harder to maintain | Easier to maintain |

---

## 🤖 Robust Code in AI Engineering

Robustness is especially important in AI applications because AI systems often interact with:

- Users
- External APIs
- Databases
- Files
- Web services
- LLM providers
- RAG pipelines
- AI agents
- Third-party services
- Unstructured or unexpected data

For example, an AI application may receive:

    prompt = ""

or:

    max_tokens = -100

or:

    temperature = 10

A reliable application should not blindly send such data to the next stage.

Instead:

    User Input
        ↓
    Validation
        ↓
    Error Handling
        ↓
    AI Processing
        ↓
    Response

---

## 🔹 Example: Robust AI Input

    prompt = input("Enter your question: ")

    if not prompt.strip():
        print("Please enter a valid question.")
    else:
        print("Processing:", prompt)

Here we are handling an important unexpected situation:

    User enters only spaces

Instead of processing an invalid prompt, we reject it safely.

---

## 🔑 Key Takeaways

- Robust code handles unexpected situations safely.
- Robustness is more than just using `try-except`.
- Input validation, error handling, and edge-case handling all contribute to robustness.
- Robust code behaves predictably when something goes wrong.
- Robustness is extremely important in AI applications because AI systems depend on external inputs and services.

---

# 2️⃣ Defensive Programming

## 📖 Definition

> **Defensive programming is a coding approach in which we anticipate possible errors, invalid inputs, and unexpected situations and handle them before they cause problems.**

In simple words:

> Defensive programming ka matlab hai problems hone ka wait na karna, balki possible problems ko pehle se identify karke handle karna.

---

## 🔹 Why Defensive Programming?

Suppose we write:

    marks = int(input("Enter marks: "))

We assume that the user will enter something like:

    85

But the user could enter:

    abc

or:

    -50

or:

    150

All of these situations need to be considered.

Defensive programming asks:

> "What could go wrong here?"

and then prepares the program accordingly.

---

## 🔹 Defensive Programming Approach

A common defensive approach is:

    Receive Input
         ↓
    Check Type
         ↓
    Check Format
         ↓
    Check Range
         ↓
    Check Edge Cases
         ↓
    Process Data

---

## 🔹 Example

    while True:
        try:
            marks = int(input("Enter your marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks. Enter marks between 0 and 100.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print("Marks:", marks)

This program is defensive because it handles multiple possible problems:

### Case 1 — Valid input

    85

Result:

    Marks: 85

### Case 2 — Non-numeric input

    abc

Result:

    Please enter a valid number.

### Case 3 — Negative marks

    -10

Result:

    Invalid marks. Enter marks between 0 and 100.

### Case 4 — Marks greater than 100

    150

Result:

    Invalid marks. Enter marks between 0 and 100.

---

## 🔹 Defensive Programming Principles

### 1. Never blindly trust input

Input can come from:

- Users
- APIs
- Files
- Databases
- Network requests
- External services

Always consider whether the data is valid.

---

### 2. Validate before processing

Instead of:

    process(data)

Prefer:

    validate(data)
    process(data)

when validation is necessary.

---

### 3. Handle expected failures

If an operation can reasonably fail, consider how the program should respond.

For example:

    API request
         ↓
    Could timeout
         ↓
    Handle timeout

---

### 4. Consider boundary values

For example, if valid temperature is:

    0 to 2

Then test:

    0
    2

and invalid boundaries:

    -1
    2.1

---

### 5. Provide meaningful feedback

Instead of:

    Invalid input

Prefer:

    Temperature must be between 0 and 2.

The second message tells the user exactly what needs to be corrected.

---

## 🤖 Defensive Programming in AI Engineering

AI applications often receive data that cannot be assumed to be perfect.

For example:

    User
      ↓
    Prompt
      ↓
    API Request
      ↓
    LLM
      ↓
    Response

At the request stage, defensive programming can check:

- Is the prompt empty?
- Is the prompt too long?
- Is `temperature` within the allowed range?
- Is `max_tokens` valid?
- Is the API key available?
- Is the requested model configured?
- Is the external API reachable?

This prevents invalid data from unnecessarily reaching later parts of the system.

---

## 🔑 Key Takeaways

- Defensive programming anticipates possible problems.
- Validate data before using it.
- Handle expected failures appropriately.
- Check boundary values and edge cases.
- Give clear feedback.
- Defensive programming is particularly useful in APIs and AI applications.
- Robust code and defensive programming are closely related, but defensive programming focuses specifically on anticipating and preventing failures before they cause problems.

---

# 📌 Part 1 Summary

In this part, we learned:

    Robust Code
        ↓
    Handles unexpected situations

    Defensive Programming
        ↓
    Anticipates unexpected situations before they cause problems

The overall goal is:

    Normal Code
        ↓
    Working Code
        ↓
    Robust Code
        ↓
    Reliable & Maintainable Code
        ↓
    Production-Ready Code

# 3️⃣ Input Validation

## 📖 Definition

> **Input validation is the process of checking whether input data is valid, safe, and in the expected format before using it in a program.**

In simple words:

> Input validation ka matlab hai kisi bhi input ko process karne se pehle check karna ki woh expected format, type, range aur rules ke according hai ya nahi.

Input validation is an important part of writing **robust and defensive code**.

---

## 🔹 Why Input Validation Is Important

A program may receive data from many different sources:

- User input
- Forms
- APIs
- Databases
- Files
- Network requests
- External services
- AI model responses

We cannot always assume that this data is correct.

For example:

    age = -10

or:

    temperature = 10

or:

    username = ""

These values may be syntactically valid Python values but logically invalid for the application.

Therefore:

    Input
      ↓
    Validate
      ↓
    Process

is safer than:

    Input
      ↓
    Process directly

---

# 🔹 Types of Input Validation

Input validation can involve several different checks.

### 1. Type Validation

Checking whether the input has the expected data type.

Example:

    age = int(input("Enter your age: "))

If the user enters:

    abc

Python cannot convert it into an integer and raises `ValueError`.

A safer approach:

    while True:
        try:
            age = int(input("Enter your age: "))
            break

        except ValueError:
            print("Please enter a valid integer.")

    print("Age:", age)

---

### 2. Range Validation

Checking whether a numerical value falls within an allowed range.

Example:

    marks = 85

Valid range:

    0 <= marks <= 100

Implementation:

    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks.")
    else:
        print("Valid marks:", marks)

---

### 3. Length Validation

Checking whether text contains an acceptable number of characters.

For example, a username may require at least 3 characters.

    username = input("Enter username: ")

    if len(username.strip()) < 3:
        print("Username must contain at least 3 characters.")
    else:
        print("Valid username:", username)

The `strip()` method removes leading and trailing whitespace.

For example:

    "   Sonal   "

becomes:

    "Sonal"

This prevents whitespace from being incorrectly counted as meaningful input.

---

### 4. Empty Input Validation

An input may technically be a string but still contain no useful information.

Example:

    username = input("Enter username: ")

    if not username.strip():
        print("Username is required.")
    else:
        print("Valid username:", username)

The condition:

    not username.strip()

detects:

- Empty string
- Only spaces
- Only tabs
- Other whitespace-only input

---

# 🔹 Complete Username Validation Example

    while True:
        username = input("Enter username: ")

        # Check whether the input is empty or contains only whitespace.
        if not username.strip():
            print("Username is required.")

        # Check whether the username has at least 3 characters.
        elif len(username.strip()) < 3:
            print("Username must contain at least 3 characters.")

        else:
            print("Valid username:", username)
            break

### Possible inputs

    ""
    
Result:

    Username is required.

---

    "  "

Result:

    Username is required.

---

    "ab"

Result:

    Username must contain at least 3 characters.

---

    "Sonal"

Result:

    Valid username: Sonal

---

# 🔹 Format Validation

Sometimes checking only the type and length is not enough.

For example, an email address should follow an expected format.

Conceptually:

    user@example.com

should be treated differently from:

    hello

Format validation can be implemented using appropriate rules, parsing libraries, or regular expressions depending on the requirement.

The important idea is:

    Input
      ↓
    Expected Format
      ↓
    Valid / Invalid

---

# 🔹 Multiple Validation Rules

Real applications often require multiple validation rules at the same time.

For example, a password may require:

- Minimum length
- Uppercase character
- Lowercase character
- Number
- Special character

The validation process can therefore be:

    Password Input
         ↓
    Check Empty
         ↓
    Check Length
         ↓
    Check Required Characters
         ↓
    Valid / Invalid

---

# 🔹 Validation Before Processing

One important principle is:

> **Validate data before performing important operations with it.**

Bad approach:

    temperature = float(input("Enter temperature: "))

    send_to_ai_api(temperature)

Here we are assuming that the value is valid.

Better approach:

    temperature = float(input("Enter temperature: "))

    if temperature < 0 or temperature > 2:
        print("Temperature must be between 0 and 2.")
    else:
        send_to_ai_api(temperature)

The AI API is called only after validation succeeds.

---

# 🤖 Input Validation in AI Engineering

Input validation is especially important when building AI applications.

Consider an AI chat API receiving:

    {
        "prompt": "Explain Machine Learning.",
        "temperature": 0.7,
        "max_tokens": 200
    }

Before processing the request, we may need to verify:

### Prompt

    prompt != ""

### Temperature

    0 <= temperature <= 2

### Maximum Tokens

    1 <= max_tokens <= 4096

Conceptually:

    User Request
         ↓
    Validate Prompt
         ↓
    Validate Temperature
         ↓
    Validate max_tokens
         ↓
    Valid Request
         ↓
    AI Model / API

If validation fails:

    User Request
         ↓
    Validation
         ↓
    ❌ Invalid
         ↓
    Meaningful Error
         ↓
    Do not call AI API

This prevents unnecessary API calls and makes the application more reliable.

---

# 🔹 AI Prompt Validation Example

    prompt = input("Enter your question: ")

    # Check whether the prompt is empty or contains only whitespace.
    if not prompt.strip():
        print("Cannot process an empty prompt.")

    else:
        print("Processing prompt:", prompt)

This simple validation prevents an empty prompt from reaching the AI system.

---

# 🔹 AI Parameter Validation Example

    temperature = 5

    # Temperature must be between 0 and 2.
    if temperature < 0 or temperature > 2:
        print(
            "Invalid temperature. "
            "Temperature must be between 0 and 2."
        )

    else:
        print("Temperature is valid.")

Here:

    temperature = 5

is rejected because:

    5 > 2

---

# 🔹 Combining Multiple AI Validations

    prompt = "Explain AI."
    temperature = 0.7
    max_tokens = 200

    # Validate prompt.
    if not prompt.strip():
        print("Prompt cannot be empty.")

    # Validate temperature.
    elif temperature < 0 or temperature > 2:
        print("Temperature must be between 0 and 2.")

    # Validate maximum tokens.
    elif max_tokens < 1 or max_tokens > 4096:
        print("max_tokens must be between 1 and 4096.")

    else:
        print("AI request is valid.")

This follows a clear validation pipeline:

    Prompt
      ↓
    Temperature
      ↓
    max_tokens
      ↓
    All valid
      ↓
    Process request

---

# 🔹 Validation and Security

Input validation is also an important security practice.

Untrusted input should not be blindly used in:

- Database queries
- File paths
- Shell commands
- API requests
- HTML output
- Configuration values

Validation helps ensure that data follows the expected rules before it reaches sensitive operations.

However, validation alone is not a complete security strategy. Applications should also use appropriate security mechanisms such as parameterized database queries, safe APIs, authentication, authorization, and output encoding where applicable.

---

# 🔹 Client-Side vs Server-Side Validation

In applications with a frontend and backend, validation can happen in multiple places.

### Client-side validation

Validation happens in the user's browser or application interface.

Advantages:

- Fast feedback
- Better user experience

But it should not be trusted as the only validation layer.

### Server-side validation

Validation happens on the backend/server.

This is essential because users can bypass client-side checks.

Typical flow:

    Frontend
       ↓
    Client-side validation
       ↓
    Backend
       ↓
    Server-side validation
       ↓
    Business Logic
       ↓
    Database / API / AI Model

For AI APIs, backend validation is particularly important.

---

# 🔹 Input Validation Best Practices

### 1. Validate early

Check input before performing important operations.

### 2. Validate according to actual requirements

Do not create unnecessary restrictions.

### 3. Give meaningful error messages

Prefer:

    Temperature must be between 0 and 2.

instead of:

    Invalid input.

### 4. Handle invalid input safely

Do not allow expected invalid input to crash the application.

### 5. Consider edge cases

Test:

- Empty values
- Minimum values
- Maximum values
- Negative values
- Very large values
- Whitespace
- Unexpected formats

### 6. Do not trust external data

Data coming from APIs, users, files, or other systems should be treated as untrusted until validated according to the application's requirements.

---

# 🔹 Input Validation Tools in Python

Different situations can use different approaches:

| Requirement | Possible Approach |
|---|---|
| Basic validation | `if` statements |
| Type conversion | `int()`, `float()`, etc. |
| Exception-based validation | `try-except` |
| String format | String methods / Regex |
| Structured validation | Pydantic |
| API request validation | Pydantic + FastAPI |
| Complex application validation | Dedicated validation logic |

Later in this chapter, we will use **Pydantic** for structured data validation.

---

# 🤖 AI Engineering Connection

Input validation is directly useful in:

- LLM APIs
- FastAPI applications
- RAG systems
- AI Agents
- Chatbots
- Model configuration
- User authentication systems
- Data preprocessing
- External API integration

For example:

    Chatbot Request
          ↓
    Validate Prompt
          ↓
    Validate Model
          ↓
    Validate Temperature
          ↓
    Validate Token Limit
          ↓
    Process Request
          ↓
    LLM
          ↓
    Response

This prevents invalid data from unnecessarily reaching the AI system.

---

# 🔑 Key Takeaways

- Input validation checks whether data is acceptable before processing.
- Validation can check type, format, length, range, and required fields.
- Empty and whitespace-only input should be considered when appropriate.
- Validation should happen before important operations.
- External input should not automatically be trusted.
- AI applications require validation for prompts, parameters, API requests, and configuration values.
- Server-side validation is essential even when client-side validation exists.
- Pydantic provides a powerful way to perform structured validation in Python.

# 4️⃣ Type Hinting & `typing` Module

## 📖 Definition

> **Type hinting is a Python feature that allows us to specify the expected data types of variables, function parameters, and return values.**

In simple words:

> Type hints code ko batate hain ki kisi variable, function parameter, ya return value mein kis type ka data expected hai.

Type hinting Python code ko:

- Easier to understand
- Easier to maintain
- Easier to debug
- Better supported by IDEs
- Better suited for large projects
- More readable

banata hai.

---

# 🔹 Why Type Hinting?

Without type hints:

    def calculate_total(price, quantity):
        return price * quantity

Function ko dekhkar immediately clear nahi hota ki:

- `price` ka type kya hona chahiye?
- `quantity` ka type kya hona chahiye?
- Function kya return karega?

With type hints:

    def calculate_total(price: float, quantity: int) -> float:
        return price * quantity

Ab clearly samajh aa raha hai:

    price
       ↓
    float expected

    quantity
       ↓
    int expected

    return value
       ↓
    float expected

---

# 🔹 Basic Variable Type Hints

## String

    name: str = "Sonal"

## Integer

    age: int = 25

## Float

    temperature: float = 0.7

## Boolean

    is_active: bool = True

The general syntax is:

    variable_name: type = value

---

# 🔹 Function Parameter Type Hints

Example:

    def greet(name: str):
        return f"Hello, {name}"

Here:

    name: str

means that `name` is expected to contain a string.

Another example:

    def add(a: int, b: int):
        return a + b

Both parameters are expected to be integers.

---

# 🔹 Return Type Hints

Return type can be specified using `->`.

    def add(a: int, b: int) -> int:
        return a + b

Here:

    a: int
    b: int
    -> int

means:

    Input:
        int
        int

    Output:
        int

---

# 🔹 Complete Function Example

    def calculate_average(marks: list[int]) -> float:
        return sum(marks) / len(marks)


    marks = [80, 75, 90, 85]

    average = calculate_average(marks)

    print("Average:", average)

Here:

    marks: list[int]

means the function expects a list containing integers.

And:

    -> float

means the function is expected to return a float.

---

# ⚠️ Type Hints Do Not Automatically Validate Data

This is a very important point.

Consider:

    def add(a: int, b: int) -> int:
        return a + b

The type hints say:

    a → int
    b → int

But Python normally does not automatically enforce these annotations at runtime.

Type hints mainly provide information to:

- Developers
- IDEs
- Linters
- Static type checkers
- Documentation tools

For example:

    add("Hello", "World")

may still execute because Python's runtime does not generally enforce the `int` annotation itself.

This is one reason tools such as **Pydantic** are useful when runtime validation is required.

---

# 🔹 The `typing` Module

Python provides the `typing` module for advanced type hints.

Example:

    from typing import List, Dict, Tuple, Set, Optional, Union

The `typing` module provides tools for describing more complex data structures.

---

# 4.1️⃣ `List`

## 📖 Definition

> **`List` is used to specify the expected type of elements inside a list.**

Example:

    from typing import List

    marks: List[int] = [80, 75, 90, 85]

Here:

    List[int]

means:

> The variable should be a list containing integers.

---

## 🔹 List of Strings

    from typing import List

    languages: List[str] = [
        "Python",
        "Java",
        "C++"
    ]

Here:

    List[str]

means:

> A list containing strings.

---

## 🔹 Function with `List`

    from typing import List


    def calculate_average(marks: List[int]) -> float:
        # List ke numbers ka average calculate kar rahe hain.
        return sum(marks) / len(marks)


    marks = [80, 75, 90, 85]

    average = calculate_average(marks)

    print("Average:", average)

The function expects:

    List[int]

and returns:

    float

---

# 4.2️⃣ `Dict`

## 📖 Definition

> **`Dict` is used to specify the expected types of keys and values inside a dictionary.**

Example:

    from typing import Dict

    subject_marks: Dict[str, int] = {
        "Python": 90,
        "DBMS": 85,
        "Java": 80
    }

Here:

    Dict[str, int]

means:

    Key   → str
    Value → int

---

## 🔹 Function with `Dict`

    from typing import Dict


    def get_total_marks(subject_marks: Dict[str, int]) -> int:
        # Dictionary ki values ka total calculate kar rahe hain.
        return sum(subject_marks.values())


    subject_marks = {
        "Python": 90,
        "DBMS": 85,
        "Java": 80
    }

    total_marks = get_total_marks(subject_marks)

    print("Total Marks:", total_marks)

---

# 4.3️⃣ `Tuple`

## 📖 Definition

> **`Tuple` is used to specify the expected types and structure of elements inside a tuple.**

Example:

    from typing import Tuple

    student: Tuple[str, int] = ("Sonal", 25)

Here:

    Tuple[str, int]

means:

    First element  → str
    Second element → int

---

## 🔹 Function with `Tuple`

    from typing import Tuple


    def get_student() -> Tuple[str, int]:
        # Student ka naam aur age tuple ke form mein return kar rahe hain.
        return ("Sonal", 25)


    student = get_student()

    print("Name:", student[0])
    print("Age:", student[1])

---

# 4.4️⃣ `Set`

## 📖 Definition

> **`Set` is used to specify the expected type of elements inside a set.**

Example:

    from typing import Set

    numbers: Set[int] = {10, 20, 30, 40}

Here:

    Set[int]

means:

> A set containing integers.

Sets automatically remove duplicate values.

Example:

    numbers = {10, 20, 20, 30}

Result:

    {10, 20, 30}

---

# 4.5️⃣ `Optional`

## 📖 Definition

> **`Optional` is used when a value can either contain a specific type or be `None`.**

Example:

    from typing import Optional

    email: Optional[str] = None

This means:

    email
      ↓
    str
      OR
    None

---

## 🔹 Function with `Optional`

    from typing import Optional


    def get_email(email: Optional[str]) -> str:

        # Check kar rahe hain ki email provide hua hai ya nahi.
        if email is None:
            return "Email not provided."

        return email


    print(get_email("sonal@example.com"))
    print(get_email(None))

Possible output:

    sonal@example.com
    Email not provided.

---

# 4.6️⃣ `Union`

## 📖 Definition

> **`Union` is used when a value can contain one of multiple specified types.**

Example:

    from typing import Union

    price: Union[int, float]

This means:

    price
      ↓
    int
      OR
    float

Example:

    from typing import Union


    def calculate_price(price: Union[int, float]) -> float:
        # Price ko float mein convert karke return kar rahe hain.
        return float(price)


    print(calculate_price(100))
    print(calculate_price(99.5))

Both are valid because the function accepts:

    int OR float

---

# 🔹 Modern Type Hint Syntax

Modern Python versions provide shorter syntax for many type hints.

Instead of:

    from typing import List

    numbers: List[int]

we can write:

    numbers: list[int]

Instead of:

    from typing import Dict

    marks: Dict[str, int]

we can write:

    marks: dict[str, int]

Instead of:

    from typing import Optional

    email: Optional[str]

we can write:

    email: str | None

Instead of:

    from typing import Union

    value: Union[int, float]

we can write:

    value: int | float

---

# 🔹 Comparison

| Older / Traditional Syntax | Modern Syntax |
|---|---|
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Tuple[str, int]` | `tuple[str, int]` |
| `Set[int]` | `set[int]` |
| `Optional[str]` | `str \| None` |
| `Union[int, float]` | `int \| float` |

The `typing` module remains important because you will encounter it in existing Python projects and libraries.

---

# 🤖 Type Hinting in AI Engineering

Type hints become increasingly useful as AI projects become larger.

For example:

    def generate_response(
        prompt: str,
        temperature: float,
        max_tokens: int
    ) -> str:

        # AI response ko simulate kar rahe hain.
        return f"AI response for: {prompt}"

This clearly communicates the expected structure of the function.

---

# 🔹 AI API Example

    def generate_response(
        prompt: str,
        temperature: float,
        max_tokens: int,
        stream: bool
    ) -> str:

        # AI request parameters ko display kar rahe hain.
        print("Prompt:", prompt)
        print("Temperature:", temperature)
        print("Max Tokens:", max_tokens)
        print("Streaming:", stream)

        # Actual AI API ke instead response simulate kar rahe hain.
        return "AI response generated."


    response = generate_response(
        "Explain Artificial Intelligence.",
        0.7,
        200,
        False
    )

    print("Response:", response)

Here:

    prompt: str
    temperature: float
    max_tokens: int
    stream: bool

and:

    -> str

make the expected data flow clear.

---

# 🔹 Complex AI Data Structure

Type hints can also describe structured data.

For example:

    from typing import Dict, List


    model_config: Dict[str, float] = {
        "temperature": 0.7,
        "top_p": 0.9
    }


    supported_languages: List[str] = [
        "English",
        "Hindi",
        "French"
    ]

This becomes useful when working with:

- Model configuration
- API parameters
- RAG metadata
- Search results
- Agent tools
- Dataset structures
- Configuration objects

---

# 🔹 Type Hints and IDE Support

Modern IDEs such as VS Code and PyCharm can use type hints to provide:

- Better autocomplete
- Better code navigation
- Warnings
- Parameter information
- Easier refactoring
- Better readability

For example:

    def calculate_total(price: float, quantity: int) -> float:
        return price * quantity

When another developer uses this function, the expected parameter types are immediately visible.

---

# 🔹 Type Hints and Static Analysis

Type hints can also be used by static type checking tools.

Examples include:

- MyPy
- Pyright
- IDE type checking

These tools can analyze code without necessarily executing it and identify potential type-related problems.

For example:

    def add(a: int, b: int) -> int:
        return a + b

A static type checker can help identify suspicious calls such as:

    add("Hello", 10)

This provides an additional layer of code quality checking.

---

# 🔹 Type Hints vs Runtime Validation

These two concepts should not be confused.

### Type Hinting

    age: int

Main purpose:

> Communicate the expected type.

### Runtime Validation

Main purpose:

> Actually check whether incoming data satisfies required rules while the program runs.

Pydantic is one tool that provides runtime data validation.

Conceptually:

    Type Hint
       ↓
    Expected structure

    Pydantic
       ↓
    Runtime validation
       ↓
    Validated data

This distinction becomes extremely important when building APIs and AI applications.

---

# 🤖 AI Engineering Applications

Type hinting is useful in:

### 1. AI APIs

    def chat(prompt: str) -> str:
        ...

### 2. RAG Systems

    documents: list[str]

### 3. Search Results

    results: list[dict[str, str]]

### 4. Model Configuration

    config: dict[str, float]

### 5. Agent Tools

    def search_web(query: str) -> list[str]:
        ...

### 6. Structured Responses

    response: dict[str, str]

### 7. FastAPI

FastAPI heavily uses Python type hints to understand:

- Request parameters
- Response structures
- Data types
- API documentation
- Validation through associated models

Pydantic is commonly used alongside FastAPI for structured request and response data.

---

# 🔹 Best Practices

### 1. Use meaningful types

Prefer:

    age: int

instead of unclear code where the expected type is difficult to determine.

### 2. Add return type hints to important functions

Prefer:

    def calculate_total(price: float, quantity: int) -> float:
        ...

### 3. Use complex type hints when they improve clarity

For example:

    documents: list[str]

is clearer than simply:

    documents: list

### 4. Do not add unnecessary complexity

Type hints should improve readability, not make simple code unnecessarily complicated.

### 5. Remember that type hints are not complete runtime validation

If external data must be validated at runtime, use appropriate validation logic or a validation library such as Pydantic.

---

# 🔑 Key Takeaways

- Type hints communicate expected data types.
- They improve readability and maintainability.
- Function parameters can have type hints.
- Return values can be documented with `->`.
- The `typing` module provides advanced type-hinting tools.
- Important tools include `List`, `Dict`, `Tuple`, `Set`, `Optional`, and `Union`.
- Modern Python provides shorter syntax such as `list[int]` and `str | None`.
- Type hints do not normally perform runtime validation by themselves.
- Static type checkers can detect potential type-related problems.
- Type hints are widely useful in AI APIs, RAG systems, agents, FastAPI applications, and structured AI projects.
- Pydantic can be used when runtime validation and structured data handling are required.

# 5️⃣ Pydantic & `BaseModel`

## 📖 Definition

> **Pydantic is a Python library used for data validation, parsing, and structured data handling using Python type hints.**

In simple words:

> **Pydantic ka use incoming data ko expected structure aur rules ke according validate aur manage karne ke liye kiya jata hai.**

Pydantic is especially useful when working with:

- APIs
- FastAPI
- AI applications
- LLM applications
- RAG systems
- AI agents
- Configuration data
- Structured user input

---

# 🔹 Why Pydantic?

Suppose an application receives this data:

    {
        "name": "Sonal",
        "age": 25,
        "email": "sonal@example.com"
    }

A normal Python dictionary does not automatically define a strict structure for this data.

We could access:

    data["name"]
    data["age"]
    data["email"]

But we may also receive:

    {
        "name": "Sonal",
        "age": "hello"
    }

Now the application needs to determine whether this data is valid.

Pydantic allows us to define a model that describes:

- What fields are required
- What types they should have
- What default values they have
- What validation rules apply

---

# 🔹 Installing Pydantic

Pydantic is an external package.

Install it using:

    pip install pydantic

Or:

    python -m pip install pydantic

To verify the installation:

    pip show pydantic

---

# 5.1️⃣ `BaseModel`

## 📖 Definition

> **`BaseModel` is the main Pydantic class used to define structured data models with validation and type information.**

We normally create our own model by inheriting from `BaseModel`.

Basic structure:

    from pydantic import BaseModel


    class User(BaseModel):
        name: str
        age: int

Now `User` describes the expected structure of user data.

---

# 🔹 Basic `BaseModel` Example

    from pydantic import BaseModel


    # User data ka structured model define kar rahe hain.
    class User(BaseModel):

        # User ka naam string hona chahiye.
        name: str

        # User ki age integer honi chahiye.
        age: int


    # Pydantic model ka object create kar rahe hain.
    user = User(
        name="Sonal",
        age=25
    )


    # Validated data ko access kar rahe hain.
    print("Name:", user.name)
    print("Age:", user.age)

Output:

    Name: Sonal
    Age: 25

---

# 🔹 Pydantic Model vs Dictionary

Normal dictionary:

    user = {
        "name": "Sonal",
        "age": 25
    }

Access:

    print(user["name"])

Pydantic model:

    user = User(
        name="Sonal",
        age=25
    )

Access:

    print(user.name)

The Pydantic model gives the data a defined structure.

---

# 5.2️⃣ Type Validation

Pydantic uses the type information defined in the model.

Example:

    from pydantic import BaseModel


    class User(BaseModel):
        name: str
        age: int


    user = User(
        name="Sonal",
        age="hello"
    )

Here:

    age = "hello"

cannot be interpreted as a valid integer, so Pydantic raises a `ValidationError`.

Conceptually:

    age: int
        ↓
    "hello"
        ↓
    ❌ Invalid
        ↓
    ValidationError

---

# 5.3️⃣ Type Conversion

Pydantic can parse some compatible input values into the expected type.

Example:

    from pydantic import BaseModel


    class User(BaseModel):
        name: str
        age: int


    user = User(
        name="Sonal",
        age="25"
    )


    print("Age:", user.age)
    print("Type:", type(user.age))

Possible output:

    Age: 25
    Type: <class 'int'>

The input was:

    "25"

but the resulting value can be represented as:

    25

with type:

    int

This behavior is useful when receiving data from external sources where values may arrive in compatible string representations.

However, applications should still define appropriate validation rules for their specific requirements.

---

# 5.4️⃣ Required Fields

A field without a default value is required.

Example:

    from pydantic import BaseModel


    class User(BaseModel):
        name: str
        age: int


    user = User(
        name="Sonal"
    )

The `age` field was not provided.

Therefore, Pydantic raises a validation error because:

    age

is required.

Conceptually:

    name → Required
    age  → Required

---

# 5.5️⃣ Default Values

## 📖 Definition

> **A default value is a predefined value that Pydantic uses when a field is not explicitly provided.**

Example:

    from pydantic import BaseModel


    class ChatRequest(BaseModel):

        # User ka question required hai.
        question: str

        # max_tokens provide na karne par 200 use hoga.
        max_tokens: int = 200

        # temperature provide na karne par 0.7 use hoga.
        temperature: float = 0.7

        # Model provide na karne par default model use hoga.
        model: str = "default-model"


    request = ChatRequest(
        question="What is Machine Learning?"
    )


    print("Question:", request.question)
    print("Max Tokens:", request.max_tokens)
    print("Temperature:", request.temperature)
    print("Model:", request.model)

Output:

    Question: What is Machine Learning?
    Max Tokens: 200
    Temperature: 0.7
    Model: default-model

---

# 5.6️⃣ Optional Fields

A field may be allowed to contain either a specific type or `None`.

Modern syntax:

    from pydantic import BaseModel


    class User(BaseModel):

        # Name required hai.
        name: str

        # Email optional hai.
        email: str | None = None


    user = User(
        name="Sonal"
    )


    print("Name:", user.name)
    print("Email:", user.email)

Output:

    Name: Sonal
    Email: None

The field:

    email: str | None = None

means:

    email
       ↓
    str
      OR
    None

The traditional syntax is:

    from typing import Optional

    email: Optional[str] = None

Both express the idea that the value may be a string or `None`.

---

# 5.7️⃣ `Field`

## 📖 Definition

> **`Field` is used to provide additional metadata, defaults, and validation constraints for Pydantic model fields.**

Import:

    from pydantic import BaseModel, Field

Example:

    class ChatRequest(BaseModel):

        prompt: str = Field(min_length=1)

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )

---

# 🔹 Common `Field` Constraints

### `ge`

Means:

> Greater than or equal to.

Example:

    age: int = Field(ge=18)

Allowed:

    18
    19
    20

Not allowed:

    17

---

### `gt`

Means:

> Greater than.

Example:

    amount: float = Field(gt=0)

Allowed:

    0.1
    10
    100

Not allowed:

    0

---

### `le`

Means:

> Less than or equal to.

Example:

    temperature: float = Field(le=2)

Allowed:

    2
    1
    0

Not allowed:

    2.1

---

### `lt`

Means:

> Less than.

Example:

    score: int = Field(lt=100)

Allowed:

    99
    50
    0

Not allowed:

    100

---

### `min_length`

Used for minimum string length.

    username: str = Field(min_length=3)

This means the username must contain at least 3 characters.

---

### `max_length`

Used for maximum string length.

    username: str = Field(max_length=20)

This means the username cannot contain more than 20 characters.

---

# 5.8️⃣ Complete Validation Example

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        # Prompt empty nahi hona chahiye.
        prompt: str = Field(min_length=1)

        # max_tokens 1 se 4096 ke beech hona chahiye.
        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        # temperature 0 se 2 ke beech hona chahiye.
        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    # Valid request create kar rahe hain.
    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=200,
        temperature=0.7
    )


    print("Prompt:", request.prompt)
    print("Max Tokens:", request.max_tokens)
    print("Temperature:", request.temperature)

Output:

    Prompt: Explain Machine Learning.
    Max Tokens: 200
    Temperature: 0.7

---

# 🔹 Invalid `max_tokens`

Suppose:

    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=5000,
        temperature=0.7
    )

The rule is:

    1 <= max_tokens <= 4096

But:

    5000 > 4096

Therefore Pydantic raises a `ValidationError`.

---

# 5.9️⃣ `ValidationError`

## 📖 Definition

> **`ValidationError` is the exception raised by Pydantic when provided data does not satisfy the model's validation requirements.**

Example:

    from pydantic import BaseModel, Field, ValidationError


    class ChatRequest(BaseModel):

        prompt: str = Field(min_length=1)

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    try:

        # Invalid max_tokens intentionally provide kar rahe hain.
        request = ChatRequest(
            prompt="Explain AI.",
            max_tokens=5000,
            temperature=0.7
        )

    except ValidationError as e:

        # Pydantic validation error ko safely handle kar rahe hain.
        print("Validation failed.")
        print(e)

The important concept is:

    Invalid Data
         ↓
    Pydantic
         ↓
    ValidationError
         ↓
    Error Handling

---

# 🔟 Pydantic Model Data Access

Pydantic model fields can be accessed using dot notation.

    request.prompt

    request.max_tokens

    request.temperature

Example:

    print(request.prompt)
    print(request.max_tokens)
    print(request.temperature)

---

# 🔹 Converting a Pydantic Model to a Dictionary

Pydantic models can be converted into dictionary-like data.

For modern Pydantic versions:

    request.model_dump()

Example:

    data = request.model_dump()

    print(data)

Possible result:

    {
        "prompt": "Explain Machine Learning.",
        "max_tokens": 200,
        "temperature": 0.7
    }

This is useful when structured model data needs to be passed to another part of an application.

---

# 🔹 JSON Representation

Pydantic models can also be serialized into JSON.

For modern Pydantic versions:

    json_data = request.model_dump_json()

    print(json_data)

Possible result:

    {"prompt":"Explain Machine Learning.","max_tokens":200,"temperature":0.7}

This is particularly useful when working with APIs.

---

# 🤖 Pydantic in AI Engineering

Pydantic is highly useful in AI Engineering because AI applications frequently exchange structured data.

Examples include:

- Chat requests
- Model configuration
- RAG documents
- Agent tool inputs
- Agent tool outputs
- API requests
- API responses
- Structured LLM outputs
- Application configuration

---

# 🔹 AI Chat Request Model

A typical AI request can be represented as:

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        # User ka prompt required hai.
        prompt: str = Field(min_length=1)

        # Maximum tokens ki allowed range define kar rahe hain.
        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        # Temperature ki allowed range define kar rahe hain.
        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )

        # Model optional hai.
        model: str | None = None


    request = ChatRequest(
        prompt="Explain Artificial Intelligence.",
        max_tokens=200,
        temperature=0.7,
        model="default-model"
    )


    print("Prompt:", request.prompt)
    print("Model:", request.model)

---

# 🔹 AI Request Validation Flow

A typical AI API request can follow this architecture:

    User Input
         ↓
    ChatRequest
         ↓
    Pydantic Validation
         ↓
    Valid Data
         ↓
    AI Processing
         ↓
    Response

If the request is invalid:

    User Input
         ↓
    ChatRequest
         ↓
    Validation
         ↓
    ❌ ValidationError
         ↓
    Error Handling
         ↓
    Meaningful Response

This prevents invalid data from unnecessarily reaching the AI processing layer.

---

# 🔹 Type Hinting + Pydantic

Type hints and Pydantic work particularly well together.

Example:

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        prompt: str = Field(min_length=1)

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    def generate_response(request: ChatRequest) -> str:

        # Validated request ko process kar rahe hain.
        return f"AI response for: {request.prompt}"


    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=200,
        temperature=0.7
    )


    response = generate_response(request)

    print(response)

Here:

    ChatRequest
        ↓
    Pydantic structured model

and:

    request: ChatRequest
        ↓
    Function expects a ChatRequest object

and:

    -> str
        ↓
    Function returns a string

This combines:

    Type Hints
        +
    Runtime Validation
        +
    Structured Data

---

# 🔹 Pydantic with FastAPI

Pydantic becomes particularly important when working with FastAPI.

A simplified API structure can look like:

    from fastapi import FastAPI
    from pydantic import BaseModel


    app = FastAPI()


    class ChatRequest(BaseModel):
        prompt: str
        temperature: float = 0.7


    @app.post("/chat")
    def chat(request: ChatRequest):

        return {
            "message": f"Received: {request.prompt}"
        }

Here:

    ChatRequest

defines the expected request structure.

FastAPI can use the Pydantic model for:

- Request parsing
- Data validation
- Structured data
- API documentation
- Type-aware development

FastAPI and Pydantic will be covered more deeply later when API development becomes part of the AI Engineering roadmap.

---

# 🔹 Pydantic in RAG Systems

RAG applications often work with structured information such as:

    document_id
    content
    source
    metadata
    score

A model can represent such data:

    from pydantic import BaseModel


    class Document(BaseModel):

        document_id: str
        content: str
        source: str
        score: float

This gives the application a defined structure for retrieved documents.

---

# 🔹 Pydantic in AI Agents

Agents may use tools that expect structured input.

For example:

    class SearchRequest(BaseModel):

        query: str
        max_results: int = 5

An agent tool can then receive validated structured data instead of arbitrary values.

Conceptually:

    AI Agent
       ↓
    Tool Request
       ↓
    Pydantic Model
       ↓
    Validation
       ↓
    Tool Execution

This makes tool interfaces more predictable.

---

# 🔹 Pydantic Best Practices

### 1. Define clear models

Use meaningful model names:

    ChatRequest

    UserProfile

    SearchRequest

    Document

instead of generic names such as:

    Data

---

### 2. Use type hints

Define the expected type for every important field.

---

### 3. Add constraints where required

For example:

    temperature: float = Field(ge=0, le=2)

---

### 4. Use defaults carefully

Defaults should represent sensible application behavior.

---

### 5. Validate external data

Data from:

- Users
- APIs
- Files
- Databases
- AI tools

should be validated according to the application's requirements.

---

### 6. Keep models focused

A model should represent a clear concept.

For example:

    ChatRequest

should describe a chat request rather than trying to represent the entire application.

---

# 🔹 Pydantic vs Normal Dictionary

| Normal Dictionary | Pydantic Model |
|---|---|
| Flexible structure | Defined structure |
| No built-in schema | Explicit schema |
| Manual validation often needed | Validation built into model |
| Manual type handling | Type-aware parsing/validation |
| Simple data storage | Structured application data |
| Useful for simple data | Useful for APIs and structured systems |

This does not mean dictionaries are bad. Dictionaries remain useful for many situations. Pydantic becomes particularly valuable when **data structure and validation matter**.

---

# 🔹 Type Hints vs Pydantic

These concepts solve related but different problems.

### Type Hinting

    temperature: float

Communicates:

> A float is expected.

### Pydantic

    temperature: float = Field(
        ge=0,
        le=2
    )

Adds runtime validation rules:

> The value must be a float-compatible value and must satisfy the specified constraints.

Therefore:

    Type Hinting
         ↓
    Expected structure

    Pydantic
         ↓
    Runtime validation + structured data

---

# 🤖 AI Engineering Connection

Pydantic is especially useful for:

### LLM APIs

    ChatRequest
        ↓
    Validate prompt and parameters
        ↓
    LLM API

### RAG

    Document
        ↓
    Validate document structure
        ↓
    Embedding / Retrieval

### AI Agents

    ToolRequest
        ↓
    Validate tool arguments
        ↓
    Tool execution

### FastAPI

    HTTP Request
        ↓
    Pydantic Model
        ↓
    Validation
        ↓
    API Logic

### Configuration

    ModelConfig
        ↓
    Validate AI model parameters
        ↓
    Application

---

# 🔑 Key Takeaways

- Pydantic is used for data validation and structured data handling.
- `BaseModel` is the main class used to define Pydantic models.
- Pydantic uses Python type hints to understand expected data.
- Required fields must be provided.
- Default values are used when fields are not provided.
- Optional fields can contain a value or `None`.
- `Field` allows additional validation constraints.
- `ge`, `gt`, `le`, and `lt` define numerical boundaries.
- `min_length` and `max_length` define string length constraints.
- Invalid data can raise `ValidationError`.
- Pydantic can parse compatible input values.
- Models can be converted into dictionaries and JSON.
- Pydantic works particularly well with FastAPI.
- Pydantic is highly useful in AI APIs, RAG systems, agents, and structured LLM applications.
- Type hints describe expected data, while Pydantic provides runtime validation and structured data handling.

# 6️⃣ Advanced Exception Handling

## 📖 Definition

> **Advanced exception handling is the practice of handling different types of errors precisely, preserving useful error information, and controlling how failures propagate through an application.**

In simple words:

> Advanced exception handling ka matlab hai errors ko sirf catch karna nahi, balki unhe properly identify, handle, log, re-raise, aur zarurat padne par meaningful custom errors mein convert karna.

Basic `try-except` se aage badhkar hum seekhenge:

- Specific exceptions
- Multiple `except` blocks
- Exception objects
- `raise`
- Re-raising exceptions
- Exception chaining
- `raise ... from ...`
- `else`
- `finally`
- AI application error handling

---

# 🔹 Why Advanced Exception Handling?

Real applications mein different errors ke different causes ho sakte hain.

For example:

    number = int(input("Enter a number: "))
    result = 100 / number

Yahan at least do common errors ho sakte hain:

    "hello"
        ↓
    ValueError

    0
        ↓
    ZeroDivisionError

Agar hum dono errors ko same way handle karenge, to error handling less precise ho sakti hai.

Better approach:

    ValueError
        ↓
    Input-related message

    ZeroDivisionError
        ↓
    Division-related message

---

# 6.1️⃣ Specific Exception Handling

## 🔹 Multiple `except` Blocks

    try:
        number = int(input("Enter a number: "))
        result = 100 / number

    except ValueError as e:
        print("Please enter a valid integer:", e)

    except ZeroDivisionError as e:
        print("Cannot divide by zero:", e)

    else:
        print("Result:", result)

Here:

    ValueError
        ↓
    First except

    ZeroDivisionError
        ↓
    Second except

This is better than catching every error with a broad exception when we already know the expected failure types.

---

# 🔹 Why Specific Exceptions Are Better

Consider:

    try:
        number = int(input("Enter a number: "))

    except Exception:
        print("Something went wrong.")

This catches many different exceptions, but the message does not tell us what actually happened.

A more precise approach:

    try:
        number = int(input("Enter a number: "))

    except ValueError:
        print("Please enter a valid integer.")

Now the error handling directly communicates the expected problem.

---

# 6.2️⃣ Exception Object with `as e`

## 📖 Definition

> **The `as` syntax stores the exception object in a variable so that its message and other available information can be inspected or logged.**

Example:

    try:
        number = int("hello")

    except ValueError as e:
        print("Error:", e)

Output will contain information about the conversion error.

Here:

    e

contains the exception object.

---

## 🔹 Why Use `as e`?

It is useful when we need to:

- Display the original error
- Log the error
- Debug the application
- Add context
- Re-raise the exception
- Chain it to another exception

Example:

    try:
        number = int("hello")

    except ValueError as e:
        print("Input processing failed:", e)

---

# 6.3️⃣ `else` with Exception Handling

## 📖 Definition

> **The `else` block runs only when the `try` block completes successfully without raising an exception.**

Example:

    try:
        number = int(input("Enter a number: "))
        result = 100 / number

    except ValueError:
        print("Please enter a valid integer.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Calculation successful.")
        print("Result:", result)

Flow:

    try
      ↓
    Error?
     ↙   ↘
    Yes   No
     ↓     ↓
    except else

The `else` block is useful for keeping successful-operation logic separate from error-handling logic.

---

# 6.4️⃣ `finally`

## 📖 Definition

> **The `finally` block is used for code that should execute regardless of whether an exception occurs.**

Example:

    try:
        number = int(input("Enter a number: "))
        result = 100 / number

    except ValueError:
        print("Invalid number.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    finally:
        print("Execution completed.")

The `finally` block runs whether:

- The operation succeeds
- A handled exception occurs
- An exception propagates further

---

# 🔹 Why `finally` Is Useful

`finally` is commonly useful for cleanup operations.

Examples:

- Closing resources
- Releasing locks
- Closing connections
- Cleaning temporary state
- Recording final status

Conceptually:

    Acquire Resource
         ↓
    Use Resource
         ↓
    Success / Failure
         ↓
    finally
         ↓
    Cleanup

However, for many resources such as files, Python's `with` statement is generally preferred because context managers handle cleanup automatically.

---

# 6.5️⃣ Complete `try-except-else-finally`

    try:
        number = int(input("Enter a number: "))
        result = 100 / number

    except ValueError as e:
        print("Invalid input:", e)

    except ZeroDivisionError as e:
        print("Division error:", e)

    else:
        print("Calculation successful.")
        print("Result:", result)

    finally:
        print("Calculation process finished.")

This provides a complete structure:

    try
      ↓
    Main operation
      ↓
    ┌───────────────┐
    │               │
    Error         Success
      ↓               ↓
    except          else
    │               │
    └───────┬───────┘
            ↓
         finally

---

# 6.6️⃣ `raise`

## 📖 Definition

> **The `raise` statement is used to manually trigger an exception when a specific condition occurs.**

Python automatically raises many exceptions.

But sometimes the program itself needs to decide that a condition is invalid.

Example:

    age = -5

Python may not automatically consider a negative integer a programming error.

But our application may define:

> Age cannot be negative.

We can explicitly raise an exception:

    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative.")

---

# 🔹 AI Example with `raise`

AI model parameters often have valid ranges.

Suppose temperature must be between `0` and `2`.

    def validate_temperature(temperature: float) -> float:

        # Temperature allowed range check kar rahe hain.
        if temperature < 0 or temperature > 2:

            # Invalid value hone par manually exception raise kar rahe hain.
            raise ValueError(
                "Temperature must be between 0 and 2."
            )

        return temperature


    temperature = validate_temperature(1.5)

    print("Valid temperature:", temperature)

If:

    temperature = 5

then:

    5 > 2

so:

    ValueError

will be raised.

---

# 6.7️⃣ Re-Raising an Exception

Sometimes a function catches an exception only to:

- Log it
- Add context
- Perform cleanup
- Then allow the caller to handle it

In such situations, we can re-raise the exception.

Example:

    def validate_temperature(temperature: float) -> float:

        try:

            if temperature < 0 or temperature > 2:
                raise ValueError(
                    "Temperature must be between 0 and 2."
                )

            return temperature

        except ValueError as e:

            # Error ko log/display kar rahe hain.
            print("Validation error:", e)

            # Same exception ko caller ke paas re-raise kar rahe hain.
            raise


    try:

        temperature = validate_temperature(5)

    except ValueError as e:

        print("Main program handled the error:", e)

Important:

    raise

without an exception object inside an `except` block means:

> Re-raise the currently handled exception.

Flow:

    Function
       ↓
    Exception occurs
       ↓
    Function catches it
       ↓
    Log / inspect
       ↓
    raise
       ↓
    Caller handles it

---

# 6.8️⃣ Exception Chaining

## 📖 Definition

> **Exception chaining is the process of raising a new exception while preserving the original exception as its cause.**

This is useful when a low-level error needs to be converted into a higher-level application error.

Example:

    try:
        number = int("hello")

    except ValueError as e:

        raise RuntimeError(
            "Failed to process user input."
        ) from e

Here there are two errors:

    Original:
    ValueError

        ↓

    New application-level error:
    RuntimeError

The `from e` part preserves the relationship between them.

---

# 🔹 Why Exception Chaining Matters

Suppose an AI application receives invalid configuration data.

Low-level error:

    ValueError

But the application wants to expose a more meaningful application-level error:

    RuntimeError:
    Failed to initialize AI configuration.

With chaining:

    Low-level Error
         ↓
    ValueError
         ↓
    Application Context
         ↓
    RuntimeError

The original cause is still available for debugging.

---

# 6.9️⃣ `raise ... from ...`

General syntax:

    try:
        ...
    except SomeError as e:
        raise NewError("Meaningful message") from e

Example:

    try:
        number = int("hello")

    except ValueError as e:

        raise RuntimeError(
            "Failed to process user input."
        ) from e

Here:

    ValueError

is the original cause, while:

    RuntimeError

provides higher-level context.

---

# 🔹 `raise` vs `raise ... from ...`

| Syntax | Purpose |
|---|---|
| `raise ValueError(...)` | Create a new exception |
| `raise` | Re-raise current exception |
| `raise NewError(...) from e` | Create a new exception while preserving the original cause |

---

# 🤖 Advanced Exception Handling in AI Engineering

AI systems interact with many components that can fail.

For example:

    User Input
         ↓
    Validation
         ↓
    API Request
         ↓
    LLM Provider
         ↓
    Response Processing
         ↓
    Database / Vector Store
         ↓
    Final Response

Possible failures include:

- Invalid user input
- Invalid model parameters
- Network errors
- Authentication errors
- Timeout
- Rate limiting
- Invalid API response
- Database errors
- Parsing errors
- Tool execution errors

Each layer may need different error handling.

---

# 🔹 AI API Validation Example

    def validate_temperature(temperature: float) -> float:

        try:

            if temperature < 0 or temperature > 2:
                raise ValueError(
                    "Temperature must be between 0 and 2."
                )

            return temperature

        except ValueError as e:

            print("AI parameter validation failed:", e)

            raise


    try:

        temperature = validate_temperature(5)

    except ValueError as e:

        print("Request rejected:", e)

This allows the lower-level validation function to identify the error while the higher-level application decides how to respond.

---

# 🔹 Converting Low-Level Errors into AI Application Errors

Suppose an internal operation fails:

    try:
        model_name = int("invalid")

    except ValueError as e:

        raise RuntimeError(
            "Failed to load AI model configuration."
        ) from e

This gives the application a more meaningful context while preserving the original cause.

---

# 🔹 Exception Handling Best Practices

### 1. Catch specific exceptions

Prefer:

    except ValueError:

when you specifically expect a `ValueError`.

Avoid unnecessarily using:

    except Exception:

for every operation.

---

### 2. Do not silently ignore errors

Avoid:

    try:
        ...
    except:
        pass

This hides failures and makes debugging difficult.

---

### 3. Give meaningful messages

Prefer:

    Temperature must be between 0 and 2.

instead of:

    Error.

---

### 4. Preserve useful error information

Use:

    except ValueError as e:

when the original error information is useful.

---

### 5. Use exception chaining when changing abstraction levels

Use:

    raise RuntimeError("...") from e

when a lower-level exception needs to be represented as a higher-level application error.

---

### 6. Do not use exceptions for normal program flow unnecessarily

Exceptions should represent exceptional situations, not every ordinary decision.

---

### 7. Log important failures

In production applications, logging is usually preferable to relying only on `print()`.

---

# 🔹 Complete Example

    def process_temperature(temperature: float) -> float:

        try:

            # Temperature ki valid range check kar rahe hain.
            if temperature < 0 or temperature > 2:
                raise ValueError(
                    "Temperature must be between 0 and 2."
                )

            return temperature

        except ValueError as e:

            # Original validation error ko display kar rahe hain.
            print("Validation error:", e)

            # Same error ko caller ke paas re-raise kar rahe hain.
            raise


    try:

        # Invalid temperature intentionally provide kar rahe hain.
        temperature = process_temperature(5)

        print("Valid temperature:", temperature)

    except ValueError as e:

        # Main application level par error handle kar rahe hain.
        print("Request rejected:", e)

Possible output:

    Validation error: Temperature must be between 0 and 2.
    Request rejected: Temperature must be between 0 and 2.

---

# 🔑 Key Takeaways

- Advanced exception handling gives precise control over failures.
- Use specific exception types whenever practical.
- `as e` provides access to the exception object.
- `else` runs when the `try` block succeeds.
- `finally` runs regardless of whether an exception occurs.
- `raise` manually triggers an exception.
- A bare `raise` re-raises the currently handled exception.
- Exception chaining connects a new exception with its original cause.
- `raise ... from ...` preserves the original error context.
- Re-raising is useful when lower-level code logs or inspects an error but the caller should still decide how to handle it.
- AI applications benefit from precise exception handling because multiple external and internal components can fail.
- Good exception handling should provide useful context without hiding the original cause.

# 7️⃣ Custom Exceptions

## 📖 Definition

> **A custom exception is a user-defined exception class created to represent a specific type of error in an application.**

In simple words:

> Jab normal built-in exceptions application ke specific error ko clearly represent nahi kar paate, tab hum apni custom exception class create kar sakte hain.

Python already provides many built-in exceptions:

- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `KeyError`
- `IndexError`
- `ConnectionError`
- `TimeoutError`

Lekin large applications, especially AI applications, mein domain-specific errors ko clearly represent karna useful hota hai.

For example:

    InvalidPromptError
    TokenLimitError
    InvalidAIRequestError
    ModelNotFoundError
    AIServiceError

---

# 7.1️⃣ Why Custom Exceptions?

Suppose an AI application receives:

    max_tokens = 5000

and application ki allowed limit hai:

    1 <= max_tokens <= 4096

Hum simply:

    ValueError

raise kar sakte hain.

But a larger application may benefit from a more specific error:

    TokenLimitError

Now the meaning of the error is immediately clear.

Conceptually:

    Invalid AI Request
          ↓
    TokenLimitError
          ↓
    Token limit exceeded

---

# 7.2️⃣ Creating a Custom Exception

Custom exceptions are normally created by inheriting from `Exception`.

Basic syntax:

    class MyCustomError(Exception):
        pass

Example:

    class InvalidAgeError(Exception):
        pass

Now `InvalidAgeError` is a custom exception.

---

# 🔹 Basic Custom Exception Example

    class InvalidAgeError(Exception):
        pass


    def validate_age(age: int) -> int:

        # Negative age ko invalid maan rahe hain.
        if age < 0:
            raise InvalidAgeError(
                "Age cannot be negative."
            )

        return age


    try:

        age = validate_age(-5)

        print("Valid age:", age)

    except InvalidAgeError as e:

        print("Validation Error:", e)

Output:

    Validation Error: Age cannot be negative.

---

# 🔹 Understanding the Flow

    validate_age(-5)
          ↓
    age < 0
          ↓
    raise InvalidAgeError
          ↓
    except InvalidAgeError
          ↓
    Error handled

The important part is:

    raise InvalidAgeError(...)

We manually raise our custom exception when our application-specific condition is violated.

---

# 7.3️⃣ Custom Exception with AI Example

AI applications often have domain-specific rules.

For example, an AI model may have a maximum token limit.

    class TokenLimitError(Exception):
        pass


    def validate_tokens(tokens: int) -> int:

        # Maximum allowed tokens check kar rahe hain.
        if tokens > 4096:
            raise TokenLimitError(
                "Token limit exceeded. "
                "Maximum allowed tokens are 4096."
            )

        return tokens


    try:

        tokens = validate_tokens(5000)

        print("Valid token count:", tokens)

    except TokenLimitError as e:

        print("AI Error:", e)

Output:

    AI Error: Token limit exceeded. Maximum allowed tokens are 4096.

---

# 7.4️⃣ Custom Exception for Invalid Prompt

A chatbot may reject an empty prompt.

We can represent this condition using a custom exception.

    class InvalidPromptError(Exception):
        pass


    def validate_prompt(prompt: str) -> str:

        # Empty ya whitespace-only prompt ko invalid maan rahe hain.
        if not prompt.strip():

            raise InvalidPromptError(
                "The given prompt is invalid. "
                "Please enter a prompt."
            )

        return prompt


    try:

        prompt = validate_prompt(" ")

        print("Prompt:", prompt)

    except InvalidPromptError as e:

        print("Prompt error:", e)

Output:

    Prompt error: The given prompt is invalid. Please enter a prompt.

---

# 7.5️⃣ Custom Exception with Type Hints

Custom exceptions can be used together with type hints.

    class InvalidPromptError(Exception):
        pass


    def validate_prompt(prompt: str) -> str:

        if not prompt.strip():
            raise InvalidPromptError(
                "Prompt cannot be empty."
            )

        return prompt

Here:

    prompt: str

is a type hint, while:

    InvalidPromptError

represents an application-specific error.

---

# 7.6️⃣ Custom Exception with Multiple Conditions

A function can raise different custom exceptions depending on the problem.

Example:

    class InvalidPromptError(Exception):
        pass


    class TokenLimitError(Exception):
        pass


    def validate_request(
        prompt: str,
        max_tokens: int
    ) -> bool:

        # Prompt validation.
        if not prompt.strip():
            raise InvalidPromptError(
                "Prompt cannot be empty."
            )

        # Token limit validation.
        if max_tokens < 1 or max_tokens > 4096:
            raise TokenLimitError(
                "max_tokens must be between 1 and 4096."
            )

        return True


    try:

        validate_request(
            "Explain AI.",
            5000
        )

        print("Request is valid.")

    except InvalidPromptError as e:

        print("Prompt Error:", e)

    except TokenLimitError as e:

        print("Token Error:", e)

---

# 🔹 Why Multiple Custom Exceptions Are Useful

Different exceptions allow the application to react differently.

For example:

    InvalidPromptError
        ↓
    Ask user to enter a valid prompt

    TokenLimitError
        ↓
    Ask user to reduce token limit

    ModelNotFoundError
        ↓
    Check model configuration

    AIServiceError
        ↓
    Retry or show service-unavailable message

This is more precise than treating every problem as:

    ValueError

or:

    Exception

---

# 7.7️⃣ Custom Exception Hierarchy

Custom exceptions can also have parent-child relationships.

Example:

    class AIError(Exception):
        pass


    class InvalidPromptError(AIError):
        pass


    class TokenLimitError(AIError):
        pass


    class ModelNotFoundError(AIError):
        pass

Now:

    AIError

is the general parent exception.

And:

    InvalidPromptError
    TokenLimitError
    ModelNotFoundError

are specialized AI errors.

Conceptually:

    Exception
        │
        └── AIError
             ├── InvalidPromptError
             ├── TokenLimitError
             └── ModelNotFoundError

This structure becomes useful as an application grows.

---

# 🔹 Handling the Parent Exception

Because the specialized exceptions inherit from `AIError`, we can catch them individually or collectively.

Example:

    class AIError(Exception):
        pass


    class InvalidPromptError(AIError):
        pass


    class TokenLimitError(AIError):
        pass


    try:

        raise TokenLimitError(
            "Maximum token limit exceeded."
        )

    except TokenLimitError as e:

        print("Specific AI error:", e)

    except AIError as e:

        print("General AI error:", e)

The specific exception should generally be handled before the more general parent exception when both are possible.

---

# 7.8️⃣ Custom Exception with Additional Information

A custom exception can store additional information.

Example:

    class TokenLimitError(Exception):

        def __init__(self, requested_tokens, max_tokens):
            self.requested_tokens = requested_tokens
            self.max_tokens = max_tokens

            message = (
                f"Requested {requested_tokens} tokens, "
                f"but maximum allowed is {max_tokens}."
            )

            super().__init__(message)


    try:

        raise TokenLimitError(
            requested_tokens=5000,
            max_tokens=4096
        )

    except TokenLimitError as e:

        print("Error:", e)
        print("Requested:", e.requested_tokens)
        print("Maximum:", e.max_tokens)

Possible output:

    Error: Requested 5000 tokens, but maximum allowed is 4096.
    Requested: 5000
    Maximum: 4096

This can be useful when error handling needs structured information.

---

# 7.9️⃣ Custom Exceptions and Logging

Custom exceptions can be combined with logging.

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    class TokenLimitError(Exception):
        pass


    def validate_tokens(tokens: int) -> int:

        if tokens > 4096:
            raise TokenLimitError(
                "Maximum token limit is 4096."
            )

        return tokens


    try:

        tokens = validate_tokens(5000)

    except TokenLimitError as e:

        logging.error("Token validation failed: %s", e)
        print("Request failed:", e)

Output:

    ERROR - Token validation failed: Maximum token limit is 4096.
    Request failed: Maximum token limit is 4096.

Here:

    logging.error()

is useful for application logs, while:

    print()

can provide a simple user-facing message in a learning/demo application.

---

# 🔟 Custom Exceptions and Exception Chaining

Custom exceptions can be combined with exception chaining.

Suppose a lower-level validation operation raises `ValueError`.

We can convert it into an application-specific error.

    class InvalidAIRequestError(Exception):
        pass


    def process_request(data: str):

        try:

            # Low-level operation.
            number = int(data)

            return number

        except ValueError as e:

            # Low-level error ko AI-specific error mein
            # convert kar rahe hain.
            raise InvalidAIRequestError(
                "AI request contains invalid numeric data."
            ) from e


    try:

        process_request("hello")

    except InvalidAIRequestError as e:

        print("AI Request Error:", e)

The structure is:

    Original ValueError
           ↓
    Exception chaining
           ↓
    InvalidAIRequestError
           ↓
    Application handles AI-specific error

The original cause remains available for debugging.

---

# 7.1️⃣1️⃣ Custom Exceptions vs Built-in Exceptions

Custom exceptions do not replace built-in exceptions.

Use built-in exceptions when they accurately describe the problem.

For example:

    int("hello")

naturally produces:

    ValueError

But if the application wants to represent a domain-specific condition, a custom exception may be clearer.

For example:

    TokenLimitError

or:

    InvalidPromptError

---

# 🔹 Comparison

| Built-in Exception | Custom Exception |
|---|---|
| Provided by Python | Created by developer |
| General-purpose | Application-specific |
| Useful for common errors | Useful for domain-specific errors |
| Examples: `ValueError`, `TypeError` | Examples: `TokenLimitError`, `InvalidPromptError` |
| No custom definition required | Requires custom class |

---

# 7.1️⃣2️⃣ When Should You Create a Custom Exception?

Custom exceptions are useful when:

- The error represents a specific business/application rule.
- Different errors need different handling.
- The built-in exception does not communicate the domain clearly.
- The application has multiple related error types.
- You want a clear exception hierarchy.
- You want to attach additional error information.

Avoid creating custom exceptions for every tiny error.

For example, creating a new exception for a simple arithmetic mistake may add unnecessary complexity.

---

# 🤖 Custom Exceptions in AI Engineering

Custom exceptions are useful in many AI systems.

### LLM Applications

    InvalidPromptError

    TokenLimitError

    ModelNotFoundError

    AIServiceError

### RAG Systems

    DocumentNotFoundError

    RetrievalError

    EmbeddingError

### AI Agents

    ToolExecutionError

    InvalidToolInputError

    ToolTimeoutError

### Model Loading

    ModelLoadError

    InvalidModelConfigError

Conceptually:

    AI Application
          │
          ├── Prompt
          │     └── InvalidPromptError
          │
          ├── Model
          │     └── ModelNotFoundError
          │
          ├── Tokens
          │     └── TokenLimitError
          │
          ├── RAG
          │     └── RetrievalError
          │
          └── Tools
                └── ToolExecutionError

This makes the application's error system easier to understand and maintain.

---

# 🔹 Complete AI Request Example

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    class AIError(Exception):
        # Base exception for AI-specific errors.
        pass


    class InvalidPromptError(AIError):
        # Raised when the prompt is invalid.
        pass


    class TokenLimitError(AIError):
        # Raised when the token limit is invalid.
        pass


    def validate_request(
        prompt: str,
        max_tokens: int
    ) -> bool:

        # Prompt validation.
        if not prompt.strip():
            raise InvalidPromptError(
                "Prompt cannot be empty."
            )

        # Token validation.
        if max_tokens < 1 or max_tokens > 4096:
            raise TokenLimitError(
                "max_tokens must be between 1 and 4096."
            )

        return True


    try:

        # Request validation perform kar rahe hain.
        validate_request(
            prompt="Explain AI.",
            max_tokens=5000
        )

        logging.info("AI request is valid.")

    except InvalidPromptError as e:

        logging.error("Prompt validation failed: %s", e)
        print("Prompt Error:", e)

    except TokenLimitError as e:

        logging.error("Token validation failed: %s", e)
        print("Token Error:", e)

    except AIError as e:

        # Other AI-specific errors ko handle karne ke liye
        # parent exception use kar rahe hain.
        logging.error("AI application error: %s", e)
        print("AI Error:", e)

---

# 🔹 Complete Error Flow

    User Request
         ↓
    Validation
         ↓
    ┌───────────────────────────┐
    │                           │
    Valid                     Invalid
    │                           │
    ↓                           ↓
    AI Processing        Custom Exception
                                ↓
                         Specific Handler
                                ↓
                         Logging + Message
                                ↓
                         Graceful Response

---

# 🔹 Best Practices

### 1. Use meaningful names

Prefer:

    InvalidPromptError

instead of:

    Error1

---

### 2. Inherit from `Exception`

Most application-specific exceptions should ultimately inherit from `Exception`.

---

### 3. Keep exceptions focused

Each custom exception should represent a clear error condition.

---

### 4. Use an exception hierarchy when appropriate

For example:

    AIError
       ├── InvalidPromptError
       ├── TokenLimitError
       └── ModelNotFoundError

---

### 5. Add useful messages

Prefer:

    "max_tokens must be between 1 and 4096."

instead of:

    "Invalid."

---

### 6. Preserve the original cause when converting errors

Use:

    raise CustomError("...") from e

when appropriate.

---

### 7. Do not overuse custom exceptions

Use built-in exceptions when they already represent the situation clearly.

---

# 🔑 Key Takeaways

- A custom exception is a user-defined exception for application-specific errors.
- Custom exceptions inherit from `Exception` or another appropriate custom exception.
- `raise` is used to trigger a custom exception.
- Custom exceptions make error handling more precise and readable.
- AI applications can benefit from errors such as `InvalidPromptError`, `TokenLimitError`, and `ModelNotFoundError`.
- Related exceptions can be organized into an exception hierarchy.
- A parent exception can handle multiple related child exceptions.
- Custom exceptions can store additional information.
- Custom exceptions work well with logging and graceful failure.
- Exception chaining can preserve the original low-level cause.
- Custom exceptions should be created when they provide meaningful application-level context.
- Built-in exceptions should still be used when they accurately describe the problem.

# 8️⃣ `assert`

## 📖 Definition

> **`assert` is a debugging statement used to check whether a condition is true. If the condition is false, Python raises an `AssertionError`.**

In simple words:

> `assert` is used to verify an assumption or condition during development and debugging.

If the condition is:

    True

the program continues normally.

If the condition is:

    False

Python raises:

    AssertionError

---

# 8.1️⃣ Basic Syntax

General syntax:

    assert condition

Example:

    age = 25

    assert age >= 18

    print("Age is valid.")

Here:

    age >= 18

is:

    True

Therefore, the program continues.

Output:

    Age is valid.

---

# 8.2️⃣ When the Condition Is False

Example:

    age = 15

    assert age >= 18

    print("Age is valid.")

Here:

    age >= 18

becomes:

    False

Therefore, Python raises:

    AssertionError

The statement after `assert` will not execute.

---

# 8.3️⃣ Assertion with a Custom Message

We can provide a message along with the assertion.

Syntax:

    assert condition, "error message"

Example:

    age = 15

    assert age >= 18, "Age must be at least 18."

    print("Age is valid.")

If the condition is false, Python raises:

    AssertionError: Age must be at least 18.

A custom message makes the failure easier to understand.

---

# 8.4️⃣ Understanding the Flow

Example:

    temperature = 1.5

    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

    print("Temperature is valid.")

Flow:

    temperature = 1.5
           ↓
    0 <= temperature <= 2
           ↓
         True
           ↓
    Continue execution
           ↓
    Temperature is valid.

If:

    temperature = 5

then:

    0 <= 5 <= 2

is:

    False

Therefore:

    AssertionError

---

# 8.5️⃣ AI Example

AI applications often work with values that are expected to remain within certain ranges.

For example, suppose our internal code assumes that temperature is between `0` and `2`.

    temperature = 1.5

    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

    print("Temperature is valid.")

Output:

    Temperature is valid.

If:

    temperature = 5

the assertion fails.

This can help developers detect incorrect internal values during development.

---

# 8.6️⃣ `assert` for Internal Assumptions

One important use of `assert` is checking assumptions made by the programmer.

Example:

    numbers = [10, 20, 30]

    assert len(numbers) > 0, \
        "The list should not be empty."

    average = sum(numbers) / len(numbers)

    print("Average:", average)

Here the programmer expects:

    numbers

to contain at least one value.

The assertion checks that assumption.

---

# 8.7️⃣ `assert` with Functions

Example:

    def calculate_average(numbers):

        # Internal assumption:
        # The function should receive a non-empty list.
        assert numbers, "Numbers list cannot be empty."

        return sum(numbers) / len(numbers)


    numbers = [10, 20, 30]

    average = calculate_average(numbers)

    print("Average:", average)

Output:

    Average: 20.0

If an empty list is passed:

    numbers = []

then:

    assert numbers

becomes false and Python raises `AssertionError`.

---

# 8.8️⃣ Multiple Assertions

We can use multiple assertions when several internal assumptions need to be checked.

Example:

    temperature = 1.5
    max_tokens = 500

    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

    assert 1 <= max_tokens <= 4096, \
        "max_tokens must be between 1 and 4096."

    print("AI configuration is valid.")

Here two different assumptions are checked:

    temperature
         ↓
       0 to 2

    max_tokens
         ↓
      1 to 4096

---

# 8.9️⃣ `assert` vs `if`

Both can check conditions, but their purposes are different.

## Using `if`

    temperature = 5

    if temperature < 0 or temperature > 2:
        print("Invalid temperature.")

`if` is normal program logic.

The program can decide what to do when the condition is invalid.

For example:

    if invalid:
        show message
        ask user again
        use default value
        return error

---

## Using `assert`

    temperature = 5

    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

`assert` is mainly intended for checking assumptions during development and debugging.

---

# 🔹 Comparison

| `if` | `assert` |
|---|---|
| Normal program logic | Debugging/internal assumptions |
| Handles expected conditions | Checks programmer assumptions |
| Can provide alternative behavior | Raises `AssertionError` when false |
| Suitable for user input validation | Not the primary choice for user input validation |
| Suitable for runtime business logic | Best used for development/debugging checks |

---

# 🔟 `assert` vs `raise`

This distinction is very important.

## `raise`

`raise` is used when the application intentionally needs to generate an exception.

Example:

    def validate_temperature(temperature):

        if temperature < 0 or temperature > 2:
            raise ValueError(
                "Temperature must be between 0 and 2."
            )

        return temperature

Here the validation is part of normal application logic.

---

## `assert`

`assert` is mainly used to verify an internal assumption.

Example:

    temperature = 1.5

    assert 0 <= temperature <= 2, \
        "Internal temperature assumption failed."

---

# 🔹 Comparison

| `assert` | `raise` |
|---|---|
| Mainly for debugging and assumptions | For intentionally raising exceptions |
| Raises `AssertionError` | Can raise different exception types |
| Useful during development | Useful in production application logic |
| Not ideal for user input validation | Suitable for explicit validation |
| Checks programmer assumptions | Implements application rules |

---

# 1️⃣1️⃣ Why `assert` Should Not Replace Input Validation

Suppose a user enters a temperature.

Bad approach:

    temperature = float(input("Enter temperature: "))

    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

The problem is that user input validation is part of normal application behavior.

Better:

    temperature = float(input("Enter temperature: "))

    if temperature < 0 or temperature > 2:
        raise ValueError(
            "Temperature must be between 0 and 2."
        )

Here invalid input is handled explicitly as part of the application's logic.

---

# 1️⃣2️⃣ Why `assert` Is Not a Security Mechanism

`assert` should not be used as the only mechanism for:

- Authentication
- Authorization
- Security validation
- User input validation
- API security
- Production business rules

For example, do not rely on:

    assert user_is_admin

for authorization.

Instead, use explicit application logic:

    if not user_is_admin:
        raise PermissionError(
            "User is not authorized."
        )

Security and business rules should remain active regardless of how Python is executed.

---

# 1️⃣3️⃣ Assertions Can Be Disabled

Python can be run in optimized mode using:

    python -O program.py

In optimized mode, assertions can be removed.

Therefore, this is another reason why `assert` should not be used for essential runtime validation.

For example:

    assert user_age >= 18

should not be the only mechanism enforcing an important application rule.

Instead:

    if user_age < 18:
        raise ValueError(
            "User must be at least 18 years old."
        )

Use `assert` for assumptions that are useful during development and debugging.

---

# 1️⃣4️⃣ Assertions in AI Engineering

Assertions can help AI developers detect unexpected internal states.

Examples:

### Model Configuration

    temperature = 0.7

    assert 0 <= temperature <= 2

### Token Configuration

    max_tokens = 1000

    assert 1 <= max_tokens <= 4096

### Model Output

Suppose internal code expects a response to be a string.

    response = "Machine Learning is a field of AI."

    assert isinstance(response, str), \
        "Model response should be a string."

### Data Processing

Suppose a preprocessing step expects a non-empty dataset.

    data = [10, 20, 30]

    assert len(data) > 0, \
        "Dataset should not be empty."

---

# 1️⃣5️⃣ Assertions for AI Pipeline Assumptions

Consider a simplified AI pipeline:

    User Input
         ↓
    Validation
         ↓
    Preprocessing
         ↓
    Model
         ↓
    Postprocessing
         ↓
    Response

Suppose preprocessing is expected to produce a non-empty list.

    processed_data = [10, 20, 30]

    assert processed_data, \
        "Preprocessing should produce non-empty data."

    result = sum(processed_data)

The assertion checks whether the internal assumption is still valid.

If preprocessing unexpectedly returns:

    []

the assertion immediately highlights the problem during development.

---

# 1️⃣6️⃣ Assertions and Testing

Assertions are also fundamental to testing.

For example, a simple test can use:

    def add(a, b):
        return a + b


    def test_add():
        assert add(2, 3) == 5

Here:

    assert add(2, 3) == 5

checks that the function produces the expected result.

This style of assertion is commonly used in testing frameworks such as `pytest`.

So:

    assert

has two closely related uses:

    Development / Debugging
            +
          Testing

---

# 1️⃣7️⃣ Example: Detecting an Internal Bug

Suppose we have:

    def calculate_average(numbers):

        assert numbers, \
            "Internal error: numbers should not be empty."

        return sum(numbers) / len(numbers)


    numbers = [10, 20, 30]

    result = calculate_average(numbers)

    print("Average:", result)

Output:

    Average: 20.0

Now suppose another part of the program accidentally sends:

    numbers = []

The assertion immediately identifies the unexpected state.

This can help developers locate bugs earlier.

---

# 1️⃣8️⃣ Practical Example

    # Define the AI model configuration.
    temperature = 0.7
    max_tokens = 1000

    # Verify internal assumptions.
    assert 0 <= temperature <= 2, \
        "Temperature must be between 0 and 2."

    assert 1 <= max_tokens <= 4096, \
        "max_tokens must be between 1 and 4096."

    print("AI configuration is valid.")

Output:

    AI configuration is valid.

If:

    temperature = 5

then Python raises:

    AssertionError:
    Temperature must be between 0 and 2.

---

# 1️⃣9️⃣ `assert` Best Practices

### ✅ Use `assert` for:

- Development checks
- Debugging
- Internal assumptions
- Invariants
- Detecting unexpected internal states
- Test assertions

### ❌ Do not use `assert` as the primary mechanism for:

- User input validation
- Authentication
- Authorization
- Security checks
- Production business rules
- API parameter validation

---

# 🔹 Good Example

    def process_data(data):

        if not data:
            raise ValueError(
                "Data cannot be empty."
            )

        # Check an internal assumption after validation.
        assert isinstance(data, list), \
            "Internal assumption failed: data should be a list."

        return len(data)

Here:

    ValueError

handles an application-level validation rule.

And:

    assert

checks an internal assumption.

---

# 🔹 AI Engineering Example

    def process_ai_request(
        temperature: float,
        max_tokens: int
    ):

        # Runtime/application validation.
        if temperature < 0 or temperature > 2:
            raise ValueError(
                "Temperature must be between 0 and 2."
            )

        if max_tokens < 1 or max_tokens > 4096:
            raise ValueError(
                "max_tokens must be between 1 and 4096."
            )

        # Check internal assumptions after validation.
        assert isinstance(temperature, float), \
            "Temperature should be a float."

        assert isinstance(max_tokens, int), \
            "max_tokens should be an integer."

        return "AI request is valid."


    result = process_ai_request(
        temperature=0.7,
        max_tokens=1000
    )

    print(result)

Output:

    AI request is valid.

This demonstrates an important design principle:

    Runtime Validation
            ↓
        if / raise
            ↓
    Internal Assumptions
            ↓
          assert

---

# 🔄 Important Comparison

| Concept | Main Purpose | Example |
|---|---|---|
| `if` | Normal decision-making | `if age < 18:` |
| `raise` | Explicitly raise an exception | `raise ValueError(...)` |
| `assert` | Check internal assumption | `assert result is not None` |
| `try-except` | Handle exceptions | `except ValueError:` |
| `unittest` / `pytest` assertions | Verify test results | `assert add(2, 3) == 5` |

---

# 🤖 AI Engineer Relevance

`assert` is useful when developing:

- AI pipelines
- Data preprocessing
- Model inference code
- LLM applications
- RAG pipelines
- Agent workflows
- API integrations
- Data transformation functions

For example:

    Input Data
        ↓
    Preprocessing
        ↓
    assert expected state
        ↓
    Embedding
        ↓
    Vector Database
        ↓
    Retrieval
        ↓
    LLM
        ↓
    Response

Assertions can help developers identify unexpected internal states early.

---

# 🧠 Key Takeaways

- `assert` checks whether a condition is true.
- If the condition is false, Python raises `AssertionError`.
- A custom message can be provided with the assertion.
- `assert` is primarily useful for debugging and checking internal assumptions.
- `assert` is commonly used in tests.
- `assert` should not replace normal user input validation.
- `assert` should not be used as the primary security mechanism.
- `raise` is better for explicit application-level validation.
- Assertions can be disabled in optimized Python execution.
- AI Engineers can use assertions to detect unexpected internal states in pipelines and model-processing code.
- A good rule is:

      User / External Input
             ↓
      if + raise / validation
             ↓
      Internal Processing
             ↓
          assert
             ↓
      Continue Processing

---

# 9️⃣ Logging

## 📖 Definition

> **Logging is the process of recording information about what a program is doing, including normal operations, warnings, errors, and important events.**

Logging is an important part of building reliable and maintainable software.

Instead of only using `print()` statements, production applications usually use Python's built-in `logging` module.

Logging helps developers understand:

- What happened
- When it happened
- How serious the event was
- Where a problem occurred
- Whether an operation succeeded or failed

---

# 9.1️⃣ Why Logging Is Important

Consider an AI application:

    User Request
         ↓
    Input Validation
         ↓
    API Request
         ↓
    AI Model
         ↓
    Response
         ↓
    Database

Many things can happen during this process.

For example:

- User sends a request
- Request validation succeeds
- API request starts
- API response takes too long
- API request fails
- Model generates a response
- Database operation fails

Without logging, diagnosing these problems can become difficult.

With logging:

    INFO - Request received
    INFO - Validation successful
    INFO - API request started
    WARNING - API response is slow
    ERROR - API request failed

The application becomes much easier to monitor and debug.

---

# 9.2️⃣ `print()` vs Logging

A simple program may use:

    print("Application started.")

This is useful while learning and debugging small programs.

However, production applications often need more control.

Logging provides:

- Different severity levels
- Timestamps
- Structured messages
- File logging
- Error tracking
- Configurable output
- Better debugging
- Better monitoring

---

# 🔹 Comparison

| `print()` | Logging |
|---|---|
| Simple output | Structured application events |
| Mostly for direct console output | Console, files, and other handlers |
| No standard severity levels | Multiple logging levels |
| Limited configuration | Highly configurable |
| Useful for simple programs | Suitable for production applications |
| Difficult to manage at scale | Easier to manage at scale |

---

# 9.3️⃣ Python `logging` Module

Python provides a built-in module called:

    logging

We can import it using:

    import logging

Basic example:

    import logging

    logging.basicConfig(level=logging.INFO)

    logging.info("Application started.")

Output:

    INFO:root:Application started.

Here:

    logging.info()

records an informational event.

---

# 9.4️⃣ Basic Logging Functions

The logging module provides several commonly used functions:

    logging.debug()
    logging.info()
    logging.warning()
    logging.error()
    logging.critical()

Each represents a different severity level.

---

# 9.5️⃣ Logging Levels

Python's standard logging levels include:

| Level | Purpose |
|---|---|
| `DEBUG` | Detailed information useful for debugging |
| `INFO` | General information about normal application execution |
| `WARNING` | Something unexpected or potentially problematic |
| `ERROR` | A specific operation failed |
| `CRITICAL` | A serious failure that may affect the application |

Severity increases approximately like:

    DEBUG
      ↓
    INFO
      ↓
    WARNING
      ↓
    ERROR
      ↓
    CRITICAL

---

# 9.6️⃣ DEBUG

## 📖 Definition

> **`DEBUG` is used for detailed information that is mainly useful when diagnosing problems during development.**

Example:

    import logging

    logging.basicConfig(level=logging.DEBUG)

    logging.debug("Starting data preprocessing.")
    logging.debug("Loading configuration.")
    logging.debug("Preparing model input.")

These messages provide detailed information about internal program execution.

---

# 9.7️⃣ INFO

## 📖 Definition

> **`INFO` is used to record normal application events and successful operations.**

Example:

    import logging

    logging.basicConfig(level=logging.INFO)

    logging.info("Application started.")
    logging.info("User logged in.")
    logging.info("Request received.")

Possible output:

    INFO:root:Application started.
    INFO:root:User logged in.
    INFO:root:Request received.

AI applications can use `INFO` for events such as:

    INFO - AI request received
    INFO - Model loaded
    INFO - Response generated
    INFO - Database connection established

---

# 9.8️⃣ WARNING

## 📖 Definition

> **`WARNING` is used when something unexpected or potentially problematic occurs, but the application can continue operating.**

Example:

    import logging

    logging.basicConfig(level=logging.INFO)

    logging.warning("API response is taking longer than expected.")

Possible output:

    WARNING:root:API response is taking longer than expected.

Other examples:

    logging.warning("Memory usage is high.")
    logging.warning("Retry attempt started.")
    logging.warning("Configuration value is missing; using default.")

A warning does not necessarily mean the application has failed.

---

# 9.9️⃣ ERROR

## 📖 Definition

> **`ERROR` is used when an operation fails and the application cannot complete that particular operation successfully.**

Example:

    import logging

    logging.basicConfig(level=logging.INFO)

    logging.error("API request failed.")

Possible output:

    ERROR:root:API request failed.

Other examples:

    logging.error("Database connection failed.")
    logging.error("Failed to load model.")
    logging.error("Invalid API response.")

The application itself may still continue running after an error.

---

# 🔟 CRITICAL

## 📖 Definition

> **`CRITICAL` is used for very serious problems that may prevent the application or an important component from continuing normally.**

Example:

    import logging

    logging.basicConfig(level=logging.INFO)

    logging.critical("Database service is unavailable.")

Possible output:

    CRITICAL:root:Database service is unavailable.

Examples:

- Critical database failure
- Application configuration failure
- Important service unavailable
- System-level failure

The exact meaning of a critical event depends on the application.

---

# 1️⃣1️⃣ Logging Level Configuration

Consider:

    import logging

    logging.basicConfig(level=logging.INFO)

Now messages with severity `INFO` and above are normally displayed.

That means:

    DEBUG
        ↓
    Hidden

    INFO
        ↓
    Displayed

    WARNING
        ↓
    Displayed

    ERROR
        ↓
    Displayed

    CRITICAL
        ↓
    Displayed

If we use:

    logging.basicConfig(level=logging.DEBUG)

then debug messages can also be displayed.

---

# 1️⃣2️⃣ Logging with a Custom Format

The default logging output may not contain all the information we want.

We can customize the format.

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Application started.")
    logging.warning("API response is slow.")
    logging.error("API request failed.")

Possible output:

    2026-09-26 14:30:00,123 - INFO - Application started.
    2026-09-26 14:30:01,456 - WARNING - API response is slow.
    2026-09-26 14:30:02,789 - ERROR - API request failed.

---

# 1️⃣3️⃣ Understanding the Format

The format:

    %(asctime)s - %(levelname)s - %(message)s

contains three important fields.

### `%(asctime)s`

Records the time when the log was created.

Example:

    2026-09-26 14:30:00,123

---

### `%(levelname)s`

Records the logging level.

Examples:

    INFO
    WARNING
    ERROR
    CRITICAL

---

### `%(message)s`

Contains the actual message written by the developer.

Example:

    Application started.

So:

    2026-09-26 14:30:00 - INFO - Application started.

contains:

    Timestamp
        +
    Level
        +
    Message

---

# 1️⃣4️⃣ Logging a Realistic Application Flow

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Application started.")
    logging.info("User request received.")
    logging.info("Request validation successful.")
    logging.info("Sending API request.")
    logging.warning("API response is taking longer than expected.")
    logging.info("Response received.")
    logging.info("Application completed successfully.")

This creates a readable record of the application's execution flow.

---

# 1️⃣5️⃣ Logging Errors

Logging becomes especially useful when exceptions occur.

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )

    try:

        result = 10 / 0

    except ZeroDivisionError as e:

        logging.error("Division failed: %s", e)

Output:

    ERROR - Division failed: division by zero

Here:

    %s

allows the exception message to be included in the log.

---

# 1️⃣6️⃣ Logging Exception Information

Python logging also provides:

    logging.exception()

This is especially useful inside an `except` block because it records the error and traceback.

Example:

    import logging

    logging.basicConfig(
        level=logging.ERROR,
        format="%(levelname)s - %(message)s"
    )

    try:

        result = 10 / 0

    except ZeroDivisionError:

        logging.exception("An error occurred during calculation.")

The log can include the traceback, which helps developers identify where the error occurred.

---

# 1️⃣7️⃣ `logging.error()` vs `logging.exception()`

| `logging.error()` | `logging.exception()` |
|---|---|
| Records an error message | Records an error message and traceback |
| Can be used generally | Intended for exception handling |
| Useful for simple error messages | Useful for debugging exceptions |
| Does not automatically provide the current traceback | Includes traceback when used inside `except` |

Example:

    except ValueError as e:
        logging.error("Validation failed: %s", e)

versus:

    except ValueError:
        logging.exception("Validation failed.")

---

# 1️⃣8️⃣ Logging to a File

Logs do not have to be displayed only in the terminal.

They can also be stored in a file.

Example:

    import logging

    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Application started.")
    logging.info("User request received.")
    logging.warning("API response is slow.")
    logging.error("API request failed.")

This creates:

    app.log

The log file can contain records such as:

    2026-09-26 14:30:00 - INFO - Application started.
    2026-09-26 14:30:01 - INFO - User request received.
    2026-09-26 14:30:02 - WARNING - API response is slow.
    2026-09-26 14:30:03 - ERROR - API request failed.

---

# 1️⃣9️⃣ Logging a File Example

A simple banking application can record important events.

    import logging

    logging.basicConfig(
        filename="bank.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    logging.info("User logged in.")
    logging.info("Balance checked.")
    logging.info("₹5,000 transfer initiated.")
    logging.info("Transaction successful.")
    logging.warning("Wrong OTP entered.")
    logging.warning("Wrong OTP entered.")
    logging.error("Account temporarily locked.")

The resulting file may contain:

    INFO - User logged in.
    INFO - Balance checked.
    INFO - ₹5,000 transfer initiated.
    INFO - Transaction successful.
    WARNING - Wrong OTP entered.
    WARNING - Wrong OTP entered.
    ERROR - Account temporarily locked.

---

# 2️⃣0️⃣ The `force=True` Parameter

Sometimes Python's logging system has already been configured earlier in the same process.

In such cases:

    logging.basicConfig()

may not change the existing configuration.

Using:

    force=True

can force the logging configuration to be applied again.

Example:

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )

This is particularly useful in scripts, notebooks, and learning environments where logging may already have been configured.

---

# 2️⃣1️⃣ Logging Variables

We can include variable values in log messages.

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )

    username = "Sonal"

    logging.info("User logged in: %s", username)

Output:

    INFO - User logged in: Sonal

Another example:

    response_time = 2.5

    logging.info(
        "API response received in %s seconds.",
        response_time
    )

---

# 2️⃣2️⃣ Logging AI Application Events

Logging is especially useful in AI applications because AI systems often contain multiple components.

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    logging.info("AI application started.")
    logging.info("User query received.")
    logging.info("Prompt validation successful.")
    logging.info("Sending request to model.")
    logging.info("Model response received.")
    logging.info("Response returned to user.")

This provides a basic execution trail.

---

# 2️⃣3️⃣ Logging an AI API Failure

Example:

    import logging

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    def call_ai_api(prompt: str):

        logging.info("AI API request started.")

        try:

            # Simulating an API failure.
            raise ConnectionError(
                "AI service is temporarily unavailable."
            )

        except ConnectionError:

            logging.exception(
                "AI API request failed."
            )

            return None


    response = call_ai_api(
        "Explain Machine Learning."
    )

    if response is None:
        logging.warning(
            "No AI response was returned."
        )

This demonstrates a useful pattern:

    API Request
        ↓
    Exception
        ↓
    Log Error
        ↓
    Graceful Handling

---

# 2️⃣4️⃣ Logging and Debugging

Suppose an AI application produces an unexpected result.

Without logs:

    Something is wrong.

With logs:

    INFO - User request received.
    INFO - Input validation successful.
    INFO - Query preprocessing started.
    INFO - Query preprocessing completed.
    INFO - Embedding generation started.
    ERROR - Embedding API request failed.

Now the developer can identify where the problem occurred.

This is one of the most important reasons logging is used in production systems.

---

# 2️⃣5️⃣ Logging in a RAG Pipeline

A Retrieval-Augmented Generation system can contain several stages.

Example:

    User Query
         ↓
    Query Validation
         ↓
    Embedding Generation
         ↓
    Vector Search
         ↓
    Context Retrieval
         ↓
    Prompt Construction
         ↓
    LLM Request
         ↓
    Response Generation

Each stage can produce logs.

Example:

    logging.info("User query received.")
    logging.info("Generating query embedding.")
    logging.info("Searching vector database.")
    logging.info("Relevant documents retrieved.")
    logging.info("Building final prompt.")
    logging.info("Sending request to LLM.")
    logging.info("LLM response received.")

If something fails:

    logging.error("Vector database search failed.")

This makes debugging a RAG system much easier.

---

# 2️⃣6️⃣ Logging in AI Agents

AI agents may perform multiple steps:

    User Request
         ↓
    Agent
         ↓
    Tool Selection
         ↓
    Tool Execution
         ↓
    Result Processing
         ↓
    Next Action
         ↓
    Final Response

Logging can record important events such as:

    INFO - Agent started.
    INFO - Tool selected: web_search.
    INFO - Tool execution started.
    INFO - Tool execution completed.
    WARNING - Tool response was empty.
    ERROR - Tool execution failed.

This can help developers understand the agent's execution flow.

---

# 2️⃣7️⃣ What Should Be Logged?

Useful things to log include:

- Application startup
- Application shutdown
- Important operations
- API requests
- API failures
- Validation failures
- Database errors
- Retry attempts
- Timeouts
- Model loading
- Model inference events
- Important pipeline stages
- Unexpected states

However, not everything should be logged.

---

# 2️⃣8️⃣ What Should Not Be Logged?

Avoid logging sensitive information such as:

- Passwords
- API keys
- Access tokens
- Authentication secrets
- Private personal information
- Sensitive user data
- Confidential application data

For example, avoid:

    logging.info(
        "API key: %s",
        api_key
    )

This can expose credentials in log files.

Instead:

    logging.info("API key loaded successfully.")

The event is recorded without exposing the secret.

---

# 2️⃣9️⃣ Logging Best Practices

### 1. Use meaningful messages

Prefer:

    logging.info("User authentication successful.")

instead of:

    logging.info("Done.")

---

### 2. Choose the correct level

Use:

    DEBUG

for detailed debugging information.

Use:

    INFO

for normal application events.

Use:

    WARNING

for potentially problematic situations.

Use:

    ERROR

for failed operations.

Use:

    CRITICAL

for serious failures.

---

### 3. Include useful context

Instead of:

    logging.error("Request failed.")

prefer:

    logging.error(
        "AI API request failed for model: %s",
        model_name
    )

Do not include sensitive information.

---

### 4. Use `logging.exception()` for exceptions

Inside an `except` block:

    except Exception:
        logging.exception("Unexpected error occurred.")

This preserves useful traceback information.

---

### 5. Do not log secrets

Never expose:

    API keys
    Passwords
    Access tokens
    Secret credentials

in logs.

---

### 6. Avoid excessive logging

Logging every small operation can make logs difficult to read.

Focus on important events.

---

# 3️⃣0️⃣ Complete Practical Example

    import logging


    # Configure application logging.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )


    def process_request(prompt: str):

        logging.info("AI request received.")

        if not prompt.strip():

            logging.warning(
                "Empty prompt received."
            )

            return None

        logging.info(
            "Prompt validation successful."
        )

        try:

            logging.info(
                "Sending request to AI service."
            )

            # Simulating an AI service response.
            response = (
                f"AI response for: {prompt}"
            )

            logging.info(
                "AI response received successfully."
            )

            return response

        except Exception:

            logging.exception(
                "AI request processing failed."
            )

            return None


    response = process_request(
        "Explain Machine Learning."
    )

    if response is not None:

        print("Response:", response)

    else:

        print(
            "Unable to process the request."
        )

Possible output:

    INFO - AI request received.
    INFO - Prompt validation successful.
    INFO - Sending request to AI service.
    INFO - AI response received successfully.

    Response: AI response for: Explain Machine Learning.

This is only a simulation. No real AI API is being called.

---

# 🔄 Logging Levels Summary

| Level | Meaning | Typical Use |
|---|---|---|
| `DEBUG` | Detailed diagnostic information | Development/debugging |
| `INFO` | Normal application events | Startup, requests, success |
| `WARNING` | Potential problem | Slow API, retry, fallback |
| `ERROR` | Operation failed | API/database/model failure |
| `CRITICAL` | Very serious failure | Major system/component failure |

---

# 🔄 `print()` vs `logging`

| Feature | `print()` | `logging` |
|---|---|---|
| Simple output | ✅ | ✅ |
| Severity levels | ❌ | ✅ |
| Timestamp support | Manual | Built-in |
| File output | Manual | Built-in configuration |
| Exception traceback | ❌ | `logging.exception()` |
| Production monitoring | Limited | Suitable |
| Configuration | Limited | Extensive |
| Large applications | Less suitable | More suitable |

---

# 🤖 AI Engineer Relevance

Logging is important for:

- AI APIs
- LLM applications
- RAG systems
- AI agents
- Model inference
- Data pipelines
- Vector databases
- Embedding systems
- FastAPI applications
- Background workers
- Production AI systems
- Debugging model pipelines

A production AI system may look like:

    User Request
         ↓
    Validation
         ↓
    logging.info()
         ↓
    Preprocessing
         ↓
    logging.info()
         ↓
    Model / API
         ↓
    logging.info()
         ↓
    Response
         ↓
    logging.info()

If something fails:

    Exception
       ↓
    logging.exception()
       ↓
    Error Handling
       ↓
    Graceful Response

---

# 🧠 Key Takeaways

- Logging records important events and information about program execution.
- Python provides the built-in `logging` module.
- Logging is more flexible and powerful than simple `print()` statements.
- The main logging levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- `INFO` is commonly used for normal application events.
- `WARNING` indicates a potentially problematic situation.
- `ERROR` indicates that an operation failed.
- `CRITICAL` indicates a very serious problem.
- `logging.exception()` is useful inside exception handlers because it records traceback information.
- Logs can be written to files using `filename`.
- Custom formats can include timestamps, levels, and messages.
- Logs should never expose passwords, API keys, access tokens, or other sensitive information.
- Logging is extremely useful for debugging AI pipelines, APIs, RAG systems, and AI agents.
- Good logging provides a clear execution trail that helps developers understand what happened and where a failure occurred.

# 🔟 Proper Error Messages

## 📖 Definition

> **A proper error message is a clear and meaningful message that explains what went wrong and, when useful, how the problem can be fixed.**

A good error message should help the developer or user understand:

- What went wrong
- Which value caused the problem
- What the expected value or format was
- How the problem can be corrected

A vague message such as:

    Error.

does not provide enough information.

A better message is:

    Temperature must be between 0 and 2.

---

# 10.1️⃣ Why Proper Error Messages Matter

Consider this:

    raise ValueError("Invalid input.")

The message tells us that something is wrong, but it does not explain:

- Which input is invalid
- Why it is invalid
- What values are allowed
- What the user should do

Compare it with:

    raise ValueError(
        "Temperature must be between 0 and 2."
    )

This immediately communicates the expected range.

---

# 10.2️⃣ Poor vs Proper Error Messages

| Poor Message | Better Message |
|---|---|
| `Error` | `Invalid temperature.` |
| `Invalid input` | `Temperature must be between 0 and 2.` |
| `Failed` | `Failed to connect to the AI service.` |
| `Wrong value` | `max_tokens must be between 1 and 4096.` |
| `Something went wrong` | `Unable to load the requested model.` |

A proper message provides context instead of simply announcing that something failed.

---

# 10.3️⃣ Basic Example

Poor:

    temperature = 5

    if temperature < 0 or temperature > 2:
        raise ValueError("Invalid input.")

Better:

    temperature = 5

    if temperature < 0 or temperature > 2:
        raise ValueError(
            "Temperature must be between 0 and 2."
        )

The second message clearly communicates the expected range.

---

# 10.4️⃣ Proper Error Messages with `raise`

Example:

    age = -5

    if age < 0:
        raise ValueError(
            "Age cannot be negative."
        )

The error message explains exactly why the value is invalid.

Another example:

    max_tokens = 10000

    if max_tokens < 1 or max_tokens > 4096:
        raise ValueError(
            "max_tokens must be between 1 and 4096."
        )

---

# 10.5️⃣ AI Example: Temperature Validation

AI model parameters often have defined ranges.

Example:

    temperature = 5

    if temperature < 0 or temperature > 2:
        raise ValueError(
            "Invalid temperature. "
            "Temperature must be between 0 and 2."
        )

This message provides:

    Invalid parameter
          ↓
    Parameter name
          ↓
    Allowed range

So the developer immediately understands the problem.

---

# 10.6️⃣ AI Example: Token Limit

Example:

    max_tokens = 10000

    if max_tokens > 4096:
        raise ValueError(
            "Invalid max_tokens. "
            "The value must be between 1 and 4096."
        )

This is much more useful than:

    raise ValueError("Invalid input.")

---

# 10.7️⃣ Include the Actual Value When Useful

Sometimes it is useful to include the received value.

Example:

    temperature = 5

    if temperature < 0 or temperature > 2:
        raise ValueError(
            f"Invalid temperature: {temperature}. "
            "Expected a value between 0 and 2."
        )

Possible error:

    ValueError:
    Invalid temperature: 5. Expected a value between 0 and 2.

This can be especially useful during debugging.

However, sensitive information should never be included in error messages or logs.

---

# 10.8️⃣ Error Messages for Missing Input

Suppose a prompt is required.

Poor:

    raise ValueError("Error.")

Better:

    raise ValueError(
        "Prompt is required."
    )

Even better when appropriate:

    raise ValueError(
        "Prompt cannot be empty. "
        "Please provide a valid question."
    )

This tells the user both:

- What is wrong
- What should be done

---

# 10.9️⃣ Error Messages for Incorrect Types

Suppose a function expects an integer.

Example:

    max_tokens = "hello"

We can provide a clear error:

    if not isinstance(max_tokens, int):
        raise TypeError(
            "max_tokens must be an integer."
        )

The message identifies the expected type.

Another example:

    if not isinstance(prompt, str):
        raise TypeError(
            "prompt must be a string."
        )

---

# 🔟 Error Messages for File Operations

Suppose a required file does not exist.

Instead of:

    File error.

A better application-level message could be:

    raise FileNotFoundError(
        "Configuration file 'config.json' was not found."
    )

This identifies:

- The type of problem
- The file involved
- What resource is missing

---

# 1️⃣1️⃣ Error Messages for API Failures

AI applications frequently communicate with external APIs.

A vague message:

    API failed.

is not very useful.

A more meaningful message:

    "AI API request failed. Please try again later."

For internal debugging, additional context can be logged separately.

For example:

    logging.error(
        "AI API request failed for model: %s",
        model_name
    )

The user-facing message does not need to expose internal implementation details.

---

# 1️⃣2️⃣ User-Facing vs Developer-Facing Messages

An important distinction in production applications is that the message shown to the user does not always need to be the same as the internal log.

For example:

    Internal log:
    ERROR - Database connection failed:
    connection refused on port 5432.

User-facing message:

    "The service is temporarily unavailable.
    Please try again later."

This prevents unnecessary technical details from being exposed to users.

The developer can still investigate the detailed log.

---

# 1️⃣3️⃣ Error Message Design

A useful error message often follows this structure:

    What went wrong
           +
    Relevant context
           +
    Expected value / action

For example:

    "Invalid temperature. "
    "Expected a value between 0 and 2."

Breakdown:

    What went wrong:
    Invalid temperature.

    Expected:
    A value between 0 and 2.

---

# 1️⃣4️⃣ Error Messages Should Be Specific

Avoid:

    raise ValueError("Invalid value.")

Prefer:

    raise ValueError(
        "max_tokens must be between 1 and 4096."
    )

Avoid:

    raise RuntimeError("Failed.")

Prefer:

    raise RuntimeError(
        "Failed to load the AI model."
    )

Specific messages reduce debugging time.

---

# 1️⃣5️⃣ Error Messages and Custom Exceptions

Proper error messages work well with custom exceptions.

Example:

    class InvalidPromptError(Exception):
        pass


    def validate_prompt(prompt: str):

        if not prompt.strip():
            raise InvalidPromptError(
                "Prompt cannot be empty. "
                "Please provide a valid question."
            )

        return prompt

Now the exception type communicates:

    InvalidPromptError

and the message communicates:

    Prompt cannot be empty.
    Please provide a valid question.

Together they provide useful context.

---

# 1️⃣6️⃣ Error Messages with Pydantic

Pydantic can automatically generate detailed validation errors.

Example:

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        prompt: str = Field(min_length=1)

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )

If we provide:

    max_tokens = 5000

Pydantic can report that the value must be less than or equal to `4096`.

This is one reason structured validation libraries are useful in AI applications.

---

# 1️⃣7️⃣ Error Messages Should Be Actionable

An actionable error message helps the user or developer know what to do next.

Less useful:

    "Invalid configuration."

More useful:

    "Invalid configuration: temperature must be between 0 and 2."

Even more actionable:

    "Invalid temperature. "
    "Set temperature to a value between 0 and 2."

The goal is not to make every error message extremely long.

The goal is to make it useful.

---

# 1️⃣8️⃣ Avoid Unnecessary Technical Details

Not every internal detail should be exposed to users.

For example, avoid showing users:

    ConnectionError:
    socket.gaierror:
    [Errno 11001] getaddrinfo failed

Instead, a user-facing message could be:

    "Unable to connect to the AI service.
    Please try again later."

The detailed technical information can be recorded in logs for developers.

---

# 1️⃣9️⃣ Avoid Sensitive Information

Error messages should not expose:

- Passwords
- API keys
- Access tokens
- Secret credentials
- Private user information
- Internal security information

Bad example:

    raise ValueError(
        f"Invalid API key: {api_key}"
    )

This can expose a secret.

Better:

    raise ValueError(
        "The configured API key is invalid."
    )

The same principle applies to logging.

---

# 2️⃣0️⃣ Error Message for Retryable Failures

Suppose an external AI service temporarily fails.

A useful message could be:

    "AI service is temporarily unavailable.
    Please try again later."

Internally, the application could log:

    logging.warning(
        "AI service unavailable. Retry attempt: %s",
        attempt
    )

This separates:

    User Communication
          +
    Internal Diagnostics

---

# 2️⃣1️⃣ Error Messages and Graceful Failure

Proper error messages are an important part of graceful failure.

Example:

    def divide_numbers(a, b):

        try:

            return a / b

        except ZeroDivisionError:

            print(
                "Cannot divide by zero. "
                "Please provide a non-zero denominator."
            )

            return None


    result = divide_numbers(10, 0)

Output:

    Cannot divide by zero.
    Please provide a non-zero denominator.

The program communicates the problem instead of simply crashing with an unexplained message.

---

# 2️⃣2️⃣ Error Messages in AI Applications

Consider an AI request:

    prompt = ""
    max_tokens = 5000
    temperature = 5

There are multiple possible validation errors.

A good application can communicate them clearly:

    Prompt cannot be empty.

    max_tokens must be between 1 and 4096.

    Temperature must be between 0 and 2.

This is much easier to understand than:

    Invalid request.

---

# 2️⃣3️⃣ Combining Validation and Proper Messages

Example:

    def validate_temperature(temperature: float) -> float:

        if temperature < 0 or temperature > 2:
            raise ValueError(
                f"Invalid temperature: {temperature}. "
                "Expected a value between 0 and 2."
            )

        return temperature


    try:

        temperature = validate_temperature(5)

        print("Valid temperature:", temperature)

    except ValueError as e:

        print("Validation error:", e)

Possible output:

    Validation error:
    Invalid temperature: 5.
    Expected a value between 0 and 2.

---

# 2️⃣4️⃣ Proper Error Messages with Logging

Example:

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    temperature = 5

    try:

        if temperature < 0 or temperature > 2:
            raise ValueError(
                "Invalid temperature. "
                "Temperature must be between 0 and 2."
            )

    except ValueError as e:

        logging.error(
            "Temperature validation failed: %s",
            e
        )

        print(
            "Unable to process the request. "
            "Please check the temperature value."
        )

Here:

    Log
      ↓
    Detailed technical information

while:

    User message
      ↓
    Clear and appropriate explanation

---

# 2️⃣5️⃣ Good Error Message Checklist

Before creating an error message, ask:

### 1. Is the problem clear?

Instead of:

    Error.

Use:

    Invalid temperature.

---

### 2. Is the relevant value or parameter identified?

Example:

    Invalid max_tokens value.

---

### 3. Is the expected value explained?

Example:

    max_tokens must be between 1 and 4096.

---

### 4. Is the message actionable?

Example:

    Please provide a value between 1 and 4096.

---

### 5. Does it avoid sensitive information?

Never expose:

    API keys
    Passwords
    Tokens
    Secrets

---

### 6. Is it appropriate for the audience?

Developers may need detailed technical information.

Users generally need a clear and safe explanation.

---

# 2️⃣6️⃣ Poor vs Professional Example

### Poor

    try:
        process_request()

    except Exception:
        print("Something went wrong.")

### Better

    try:
        process_request()

    except ConnectionError:
        print(
            "Unable to connect to the AI service. "
            "Please try again later."
        )

The second approach provides useful information while remaining understandable.

---

# 2️⃣7️⃣ AI Engineering Example

    class InvalidTemperatureError(Exception):
        pass


    def validate_temperature(
        temperature: float
    ) -> float:

        if temperature < 0 or temperature > 2:

            raise InvalidTemperatureError(
                f"Invalid temperature: {temperature}. "
                "Temperature must be between 0 and 2."
            )

        return temperature


    try:

        temperature = validate_temperature(5)

        print(
            "Temperature:",
            temperature
        )

    except InvalidTemperatureError as e:

        print(
            "Request validation failed:",
            e
        )

Possible output:

    Request validation failed:
    Invalid temperature: 5.
    Temperature must be between 0 and 2.

This combines:

    Type Hinting
         +
    Custom Exception
         +
    Validation
         +
    Proper Error Message

---

# 2️⃣8️⃣ Best Practices

### 1. Be specific

Explain exactly what went wrong.

### 2. Mention expected values when useful

For example:

    Expected 0 to 2.

### 3. Make messages actionable

Tell the user or developer what can be corrected.

### 4. Do not expose secrets

Never include credentials or sensitive information.

### 5. Separate user-facing messages from internal diagnostics

Users should receive clear and safe messages.

Developers can receive detailed logs.

### 6. Use the correct exception type

For example:

    ValueError
    TypeError
    FileNotFoundError
    ConnectionError
    CustomException

### 7. Avoid vague messages

Avoid:

    Error
    Failed
    Invalid

without additional context.

### 8. Keep messages concise

A useful error message does not need to be extremely long.

---

# 🔄 Error Handling Flow

A well-designed application can follow this pattern:

    Operation
        ↓
    Validation
        ↓
    Error?
      ↙   ↘
    Yes    No
     ↓      ↓
    Raise   Continue
     ↓
    Catch
     ↓
    Log detailed information
     ↓
    Provide clear user-facing message
     ↓
    Recover / Retry / Stop gracefully

---

# 🤖 AI Engineer Relevance

Proper error messages are especially important in:

- LLM applications
- RAG systems
- AI agents
- FastAPI applications
- Model inference
- Data pipelines
- Vector databases
- API integrations
- Production AI systems

For example, an AI API may fail because:

    Invalid input
        ↓
    Invalid model parameter
        ↓
    Authentication failure
        ↓
    Rate limit
        ↓
    Timeout
        ↓
    Server error

Each situation should have an appropriate error type and meaningful message.

---

# 🧠 Key Takeaways

- A proper error message clearly explains what went wrong.
- Good error messages provide useful context.
- When appropriate, include the expected value or valid range.
- Error messages should help users or developers take the next step.
- Avoid vague messages such as `Error`, `Failed`, or `Invalid input`.
- Use specific exception types together with meaningful messages.
- Custom exceptions can make application-specific errors clearer.
- User-facing messages and developer-facing logs may contain different levels of detail.
- Never expose passwords, API keys, access tokens, or other sensitive information.
- Pydantic can automatically provide detailed validation errors.
- Proper error messages are an important part of graceful failure.
- Clear error messages make AI applications easier to debug, maintain, and use.

# 1️⃣1️⃣ Resource Management

## 📖 Definition

> **Resource management is the practice of properly acquiring, using, and releasing resources such as files, database connections, network connections, and other system resources.**

Resources are limited and often need to be released after use.

Examples include:

- Files
- Database connections
- Network connections
- Locks
- Sockets
- Temporary resources
- External service connections

If resources are not properly released, applications can experience:

- Memory or resource leaks
- Locked files
- Too many open connections
- Reduced performance
- Unexpected failures

---

# 11.1️⃣ Why Resource Management Matters

Consider a program that opens a file:

    file = open("data.txt", "r")

If the file is never closed, the operating system may keep the resource open.

The general lifecycle is:

    Acquire Resource
          ↓
       Use Resource
          ↓
    Release Resource

For a file:

    Open File
       ↓
    Read File
       ↓
    Close File

For a database:

    Connect
       ↓
    Execute Query
       ↓
    Close Connection

For a network connection:

    Connect
       ↓
    Send / Receive Data
       ↓
    Close Connection

---

# 11.2️⃣ File Resource Management

A file is a resource that should be properly closed after use.

Basic approach:

    file = open("data.txt", "r")

    try:
        content = file.read()
        print(content)

    finally:
        file.close()

The `finally` block ensures that the file is closed even if an exception occurs.

---

# 11.3️⃣ The `with` Statement

Python provides a cleaner way to manage resources using the `with` statement.

Example:

    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

After the `with` block finishes, Python automatically handles the resource cleanup.

Conceptually:

    with
      ↓
    Acquire Resource
      ↓
    Use Resource
      ↓
    Automatic Cleanup

This is one of the most important patterns for safe resource management in Python.

---

# 11.4️⃣ Context Managers

## 📖 Definition

> **A context manager is an object that manages the setup and cleanup of a resource around a block of code.**

The `with` statement is commonly used with context managers.

Example:

    with open("data.txt", "r") as file:
        content = file.read()

The context manager handles:

    Resource Acquisition
            ↓
       Code Execution
            ↓
       Resource Cleanup

---

# 11.5️⃣ `__enter__()` and `__exit__()`

A custom context manager can be created using:

    __enter__()

and:

    __exit__()

Example:

    class MyContext:

        def __enter__(self):
            print("Resource acquired.")
            return self

        def __exit__(
            self,
            exc_type,
            exc_value,
            traceback
        ):
            print("Resource released.")


    with MyContext():
        print("Using resource.")

Output:

    Resource acquired.
    Using resource.
    Resource released.

The flow is:

    with MyContext()
          ↓
    __enter__()
          ↓
    Code inside with
          ↓
    __exit__()

---

# 11.6️⃣ Why `__exit__()` Is Important

`__exit__()` is responsible for cleanup when the context ends.

For example, it can:

- Close a connection
- Release a lock
- Close a file
- Clean temporary resources
- Perform final cleanup

Even when an exception occurs inside the `with` block, the context manager gets an opportunity to perform cleanup.

---

# 11.7️⃣ `try/finally` vs `with`

Both approaches can ensure cleanup.

### `try/finally`

    file = open("data.txt", "r")

    try:
        content = file.read()
        print(content)

    finally:
        file.close()

### `with`

    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

The `with` approach is generally cleaner and easier to maintain for resources that support context management.

---

# 11.8️⃣ Database Connections

Database connections are another important resource.

Conceptual flow:

    Connect to Database
           ↓
      Execute Query
           ↓
      Process Result
           ↓
      Close Connection

If connections are not released properly, an application can eventually run out of available connections.

A context manager or equivalent cleanup mechanism can help ensure proper resource handling.

---

# 11.9️⃣ Network Connections

AI applications frequently communicate with external services.

For example:

    AI Application
         ↓
    Network Connection
         ↓
    AI API
         ↓
    Response
         ↓
    Connection Cleanup

Network resources should be managed carefully, especially in applications that handle many requests.

---

# 🔟 Resource Management in AI Engineering

AI systems frequently use external resources.

Examples:

- LLM API connections
- Database connections
- Vector database connections
- File handles
- Network connections
- Model files
- Temporary files
- Locks
- HTTP sessions

A typical RAG application may use:

    User Query
         ↓
    Embedding Service
         ↓
    Vector Database
         ↓
    Retrieved Documents
         ↓
    LLM API
         ↓
    Final Response

Several external resources may be involved.

Proper cleanup helps keep the system reliable.

---

# 1️⃣1️⃣ Resource Management and Error Handling

Resource management and exception handling often work together.

Example:

    try:
        resource = acquire_resource()

        try:
            use_resource(resource)

        finally:
            release_resource(resource)

    except Exception as e:
        print("Operation failed:", e)

The general idea is:

    Acquire
       ↓
    Use
       ↓
    Failure / Success
       ↓
    Cleanup
       ↓
    Continue / Handle Error

---

# 1️⃣2️⃣ Why the `with` Statement Is Preferred

The `with` statement reduces the chance of forgetting cleanup.

Without `with`:

    file = open("data.txt", "r")

    try:
        content = file.read()

    finally:
        file.close()

With `with`:

    with open("data.txt", "r") as file:
        content = file.read()

The second version is shorter and communicates the resource lifecycle more clearly.

---

# 1️⃣3️⃣ Custom Context Manager

A custom context manager can manage application-specific resources.

Example:

    class DatabaseConnection:

        def __enter__(self):
            print("Database connection opened.")
            return self

        def __exit__(
            self,
            exc_type,
            exc_value,
            traceback
        ):
            print("Database connection closed.")


    with DatabaseConnection() as db:
        print("Executing database operation.")

Output:

    Database connection opened.
    Executing database operation.
    Database connection closed.

This is a simplified simulation of resource management.

---

# 1️⃣4️⃣ Resource Management with `contextlib`

Python also provides the `contextlib` module for creating context managers more conveniently.

Example:

    from contextlib import contextmanager


    @contextmanager
    def managed_resource():

        print("Resource acquired.")

        try:
            yield

        finally:
            print("Resource released.")


    with managed_resource():
        print("Using resource.")

Output:

    Resource acquired.
    Using resource.
    Resource released.

The `finally` block ensures cleanup.

---

# 1️⃣5️⃣ Resource Management in File Processing

AI and data-processing applications frequently process files.

Example workflow:

    Open Dataset
         ↓
    Read Data
         ↓
    Process Data
         ↓
    Close Dataset

Using:

    with open("dataset.txt", "r") as file:
        data = file.read()

the file is automatically managed by the context manager.

This is useful when processing:

- Text datasets
- CSV files
- Configuration files
- JSON files
- Training data
- Prompt templates

---

# 1️⃣6️⃣ Resource Management in Model Loading

AI applications may work with large model files.

Conceptually:

    Model File
        ↓
    Load Model
        ↓
    Use Model
        ↓
    Release Temporary Resources

Large resources should be managed carefully because they may consume significant memory or system resources.

---

# 1️⃣7️⃣ Resource Management Best Practices

### 1. Release resources after use

Do not leave files, connections, or locks open unnecessarily.

### 2. Prefer context managers

Use:

    with

when a resource supports context management.

### 3. Use `finally` when appropriate

For resources that cannot conveniently be managed with a context manager, `finally` can guarantee cleanup.

### 4. Keep resource lifetimes controlled

Acquire resources as close as practical to where they are needed.

### 5. Avoid unnecessary open connections

Long-lived connections should be used intentionally.

### 6. Consider exceptions

Cleanup should still happen if an operation fails.

### 7. Avoid resource leaks

Repeatedly opening resources without releasing them can eventually cause failures.

---

# 1️⃣8️⃣ Resource Leak

## 📖 Definition

> **A resource leak occurs when a program acquires a resource but fails to release it properly after use.**

Example:

    for i in range(10000):
        file = open("data.txt", "r")
        content = file.read()

If the file is repeatedly opened without being properly closed, resources can accumulate.

A safer pattern is:

    for i in range(10000):

        with open("data.txt", "r") as file:
            content = file.read()

Each context automatically handles the file lifecycle.

---

# 1️⃣9️⃣ AI Engineering Example

A simplified AI document-processing pipeline might look like:

    Document
       ↓
    Open File
       ↓
    Read Content
       ↓
    Split Text
       ↓
    Generate Embeddings
       ↓
    Store in Vector Database
       ↓
    Close File

The file should not remain open after its contents have been processed.

Using:

    with open("document.txt", "r") as file:
        text = file.read()

helps ensure proper file management.

---

# 🧠 Key Takeaways

- Resource management means properly acquiring, using, and releasing resources.
- Common resources include files, database connections, network connections, locks, and sockets.
- Resources should be released even when errors occur.
- `try/finally` can be used to guarantee cleanup.
- The `with` statement provides a cleaner approach for resources that support context management.
- Context managers commonly use `__enter__()` and `__exit__()`.
- `contextlib` provides tools for creating context managers.
- Resource leaks can cause performance problems and application failures.
- Proper resource management is especially important in applications that handle many files, connections, or requests.
- AI systems frequently interact with files, APIs, databases, vector stores, and other resources.
- Good resource management improves reliability, maintainability, and system stability.


# 1️⃣2️⃣ Configuration Handling

## 📖 Definition

> **Configuration handling is the practice of storing and managing application settings separately from the main program code.**

Configuration may include:

- API endpoints
- Model names
- Temperature values
- Token limits
- Database URLs
- Feature flags
- Application settings
- Environment-specific values

Instead of placing every setting directly inside the program, configuration can be managed separately.

---

# 12.1️⃣ Why Configuration Handling Matters

Consider an AI application:

    model = "some-model"
    temperature = 0.7
    max_tokens = 200
    api_key = "secret-key"

Putting all these values directly into the source code can create problems.

For example:

- Changing configuration requires modifying code.
- Secrets may accidentally be committed to GitHub.
- Different environments may require different settings.
- Configuration becomes harder to manage as the project grows.

A better structure is:

    Application Code
          +
    Configuration
          +
    Environment Variables

---

# 12.2️⃣ Hard-Coded Configuration

Example:

    MODEL_NAME = "some-model"
    TEMPERATURE = 0.7
    MAX_TOKENS = 200

This works for small programs, but larger applications benefit from separating configuration from application logic.

---

# 12.3️⃣ Configuration File

A simple Python configuration file could contain:

    MODEL_NAME = "some-model"
    TEMPERATURE = 0.7
    MAX_TOKENS = 200

For example, a project could have:

    project/
    │
    ├── config.py
    └── main.py

`config.py`:

    MODEL_NAME = "some-model"
    TEMPERATURE = 0.7
    MAX_TOKENS = 200

`main.py`:

    import config

    print("Model:", config.MODEL_NAME)
    print("Temperature:", config.TEMPERATURE)
    print("Max tokens:", config.MAX_TOKENS)

This keeps configuration values separate from the main application logic.

---

# 12.4️⃣ Environment Variables

## 📖 Definition

> **An environment variable is a value stored outside the Python source code that an application can read while it is running.**

Environment variables are especially useful for sensitive configuration.

Examples:

    API_KEY
    DATABASE_URL
    SECRET_KEY
    ENVIRONMENT

Python can access environment variables using the `os` module.

Example:

    import os

    api_key = os.getenv("API_KEY")

    print(api_key)

If `API_KEY` is not configured, `os.getenv()` returns:

    None

---

# 12.5️⃣ Checking Whether an API Key Exists

Example:

    import os

    api_key = os.getenv("API_KEY")

    if api_key:

        print("API key loaded successfully.")

    else:

        print("API key is missing.")

This verifies whether the environment variable is available without printing the secret itself.

---

# 12.6️⃣ Why API Keys Should Not Be Hard-Coded

Avoid:

    API_KEY = "my-secret-api-key"

Especially in a Git repository.

If the repository becomes public or the secret is accidentally shared, the API key may be exposed.

A better approach is:

    import os

    api_key = os.getenv("API_KEY")

The actual secret remains outside the source code.

---

# 12.7️⃣ Configuration for AI Applications

An AI application may have:

    MODEL_NAME
    TEMPERATURE
    MAX_TOKENS
    API_KEY

For example:

    import os

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "default-model"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", "0.7")
    )

    MAX_TOKENS = int(
        os.getenv("MAX_TOKENS", "200")
    )

    API_KEY = os.getenv("API_KEY")

Here:

- `MODEL_NAME` has a default value.
- `TEMPERATURE` is converted to `float`.
- `MAX_TOKENS` is converted to `int`.
- `API_KEY` is loaded from the environment.

---

# 12.8️⃣ Default Configuration Values

Environment variables may not always exist.

We can provide defaults.

Example:

    import os

    model_name = os.getenv(
        "MODEL_NAME",
        "default-model"
    )

If `MODEL_NAME` exists:

    MODEL_NAME

is used.

If it does not exist:

    default-model

is used.

Conceptually:

    Environment Variable Available
              ↓
          Use its value

    Environment Variable Missing
              ↓
          Use default

---

# 12.9️⃣ Configuration Validation

Configuration should also be validated.

Example:

    import os

    temperature = float(
        os.getenv("TEMPERATURE", "0.7")
    )

    if temperature < 0 or temperature > 2:
        raise ValueError(
            "TEMPERATURE must be between 0 and 2."
        )

This prevents invalid configuration from entering the application.

---

# 🔟 Configuration and Pydantic

Pydantic can also be used to represent and validate structured configuration.

Example:

    from pydantic import BaseModel


    class AIConfig(BaseModel):

        model_name: str
        temperature: float
        max_tokens: int


    config = AIConfig(
        model_name="default-model",
        temperature=0.7,
        max_tokens=200
    )

    print("Model:", config.model_name)
    print("Temperature:", config.temperature)
    print("Max tokens:", config.max_tokens)

This combines:

    Configuration
         +
    Type Hints
         +
    Validation

---

# 10.1️⃣1️⃣ Configuration by Environment

Different environments may need different settings.

For example:

    Development
         ↓
    Local configuration

    Testing
         ↓
    Test configuration

    Production
         ↓
    Production configuration

An application may use different environment variables for each environment.

Example:

    ENVIRONMENT=development

or:

    ENVIRONMENT=production

The application can then load appropriate settings.

---

# 1️⃣2️⃣ Environment Variables and Git

Environment variables are useful for keeping secrets outside source code.

A project may contain:

    .env

with sensitive values in local development.

The `.env` file should generally not be committed to a public repository when it contains secrets.

A common practice is to include it in:

    .gitignore

For example:

    .env

The exact setup depends on the project and environment.

---

# 1️⃣3️⃣ Configuration Best Practices

### 1. Keep configuration separate from application logic

Avoid scattering configuration values throughout the code.

### 2. Never hard-code secrets

Keep API keys and credentials outside source code.

### 3. Use environment variables for sensitive values

Examples:

    API_KEY
    DATABASE_URL
    SECRET_KEY

### 4. Validate configuration

Invalid configuration should be detected early.

### 5. Provide sensible defaults where appropriate

Defaults can simplify local development.

### 6. Do not print secrets

Even debugging output should not expose credentials.

### 7. Use different configuration for different environments

Development, testing, and production may have different requirements.

---

# 🤖 AI Engineering Relevance

Configuration handling is essential for:

- LLM applications
- AI APIs
- RAG systems
- AI agents
- FastAPI applications
- Database integrations
- Vector databases
- Model configuration
- Deployment

A production AI application may separate:

    Application Code
          ↓
    Configuration
          ↓
    Environment Variables
          ↓
    Secrets Management

This makes the application easier to configure, deploy, and maintain.

---

# 🧠 Key Takeaways

- Configuration handling separates application settings from core program logic.
- Configuration may include model names, API endpoints, token limits, and application settings.
- Environment variables store values outside the Python source code.
- `os.getenv()` can be used to read environment variables.
- Sensitive values such as API keys should not be hard-coded.
- Default values can be provided when an environment variable is missing.
- Configuration values should be validated before use.
- Pydantic can be used to represent and validate structured configuration.
- Different environments may require different configuration values.
- Secrets should never be printed or accidentally committed to a public repository.
- Proper configuration handling makes AI applications easier to deploy, maintain, and scale.

# 1️⃣3️⃣ Retry Logic

## 📖 Definition

> **Retry logic is a mechanism that automatically attempts an operation again when it temporarily fails.**

In real applications, some failures are temporary.

For example:

- Temporary network failure
- Temporary API failure
- Service overload
- Connection interruption
- Temporary database issue
- Rate limiting

Instead of immediately giving up, the application can try the operation again.

Basic flow:

    Operation
        ↓
      Fails
        ↓
    Retry
        ↓
      Fails
        ↓
    Retry
        ↓
    Success / Final Failure

---

# 13.1️⃣ Why Retry Logic Is Important

Consider an AI application that calls an external API.

    Application
         ↓
      AI API
         ↓
    Temporary Failure

A temporary network problem does not necessarily mean the request can never succeed.

Without retry logic:

    Request
      ↓
    Failure
      ↓
    Stop

With retry logic:

    Request
      ↓
    Failure
      ↓
    Wait
      ↓
    Retry
      ↓
    Success

Retry logic can improve reliability when failures are temporary.

---

# 13.2️⃣ Simple Retry Example

Example:

    import time

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        print(
            f"Attempt {attempt}: "
            "Sending API request..."
        )

        try:

            # Simulating a temporary API failure.
            raise ConnectionError(
                "Temporary network error."
            )

        except ConnectionError as e:

            print("Request failed:", e)

            if attempt < max_retries:

                print("Retrying...\n")

                # Wait before the next attempt.
                time.sleep(2)

            else:

                print(
                    "Maximum retry attempts reached."
                )

Possible output:

    Attempt 1: Sending API request...
    Request failed: Temporary network error.
    Retrying...

    Attempt 2: Sending API request...
    Request failed: Temporary network error.
    Retrying...

    Attempt 3: Sending API request...
    Request failed: Temporary network error.
    Maximum retry attempts reached.

This example simulates failure every time.

---

# 13.3️⃣ Understanding `max_retries`

Consider:

    max_retries = 3

This controls how many attempts the application is allowed to make in this example.

The loop:

    for attempt in range(1, max_retries + 1):

produces:

    1
    2
    3

So the application gets three attempts.

---

# 13.4️⃣ Retry Only When Attempts Remain

Consider:

    if attempt < max_retries:
        print("Retrying...")

This prevents the program from retrying after the final attempt.

Flow:

    Attempt 1
       ↓
    Failed
       ↓
    Retry

    Attempt 2
       ↓
    Failed
       ↓
    Retry

    Attempt 3
       ↓
    Failed
       ↓
    Stop

---

# 13.5️⃣ Successful Retry

Not every attempt has to fail.

Example:

    import time

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        print(
            f"Attempt {attempt}: "
            "Sending API request..."
        )

        try:

            if attempt < 3:

                # Simulate temporary failures
                # on the first two attempts.
                raise ConnectionError(
                    "Temporary network error."
                )

            # Simulate a successful request.
            response = "API response received."

            print(response)

            break

        except ConnectionError as e:

            print("Request failed:", e)

            if attempt < max_retries:

                print("Retrying...\n")
                time.sleep(1)

            else:

                print(
                    "Maximum retry attempts reached."
                )

Output:

    Attempt 1: Sending API request...
    Request failed: Temporary network error.
    Retrying...

    Attempt 2: Sending API request...
    Request failed: Temporary network error.
    Retrying...

    Attempt 3: Sending API request...
    API response received.

The important idea is:

    Temporary Failure
          ↓
       Retry
          ↓
       Success
          ↓
       Continue

---

# 13.6️⃣ Retry Delay

Immediately retrying an operation repeatedly may not be a good idea.

For example:

    Request
      ↓
    Failure
      ↓
    Immediate Retry
      ↓
    Failure
      ↓
    Immediate Retry
      ↓
    Failure

This can generate unnecessary load.

Instead, the application can wait:

    Failure
      ↓
    Wait
      ↓
    Retry

Example:

    import time

    time.sleep(2)

This waits for approximately two seconds before continuing.

---

# 13.7️⃣ Why a Delay Helps

A temporary problem may resolve itself after a short period.

For example:

    Network interruption
          ↓
       Wait
          ↓
    Network restored
          ↓
       Retry
          ↓
      Success

A delay can also reduce repeated pressure on an already struggling service.

---

# 13.8️⃣ Exponential Backoff

## 📖 Definition

> **Exponential backoff is a retry strategy in which the delay between attempts increases after each failure.**

Instead of:

    Attempt 1 → Wait 1 second
    Attempt 2 → Wait 1 second
    Attempt 3 → Wait 1 second

we can use:

    Attempt 1 → Wait 1 second
    Attempt 2 → Wait 2 seconds
    Attempt 3 → Wait 4 seconds
    Attempt 4 → Wait 8 seconds

A simple formula is:

    delay = base_delay * (2 ** (attempt - 1))

Example:

    base_delay = 1

    Attempt 1:
    1 * 2^0 = 1 second

    Attempt 2:
    1 * 2^1 = 2 seconds

    Attempt 3:
    1 * 2^2 = 4 seconds

    Attempt 4:
    1 * 2^3 = 8 seconds

---

# 13.9️⃣ Exponential Backoff Example

    import time

    max_retries = 4
    base_delay = 1

    for attempt in range(1, max_retries + 1):

        print(
            f"Attempt {attempt}: "
            "Sending API request..."
        )

        try:

            # Simulating a temporary failure.
            raise ConnectionError(
                "Temporary network error."
            )

        except ConnectionError as e:

            print("Request failed:", e)

            if attempt < max_retries:

                delay = base_delay * (
                    2 ** (attempt - 1)
                )

                print(
                    f"Waiting {delay} seconds "
                    "before retrying..."
                )

                time.sleep(delay)

            else:

                print(
                    "Maximum retry attempts reached."
                )

The delays increase after each failure.

---

# 🔟 Jitter

## 📖 Definition

> **Jitter is a small random variation added to a retry delay to prevent many clients from retrying at exactly the same time.**

Suppose thousands of applications receive a temporary service failure.

Without jitter:

    Client 1 → Retry at 5 seconds
    Client 2 → Retry at 5 seconds
    Client 3 → Retry at 5 seconds
    Client 4 → Retry at 5 seconds

Many clients may send requests simultaneously.

With jitter:

    Client 1 → Retry at 4.7 seconds
    Client 2 → Retry at 5.2 seconds
    Client 3 → Retry at 5.8 seconds
    Client 4 → Retry at 4.9 seconds

The retry traffic becomes more distributed.

---

# 10.1️⃣1️⃣ Retryable vs Non-Retryable Errors

This is one of the most important concepts in retry logic.

Not every error should be retried.

### Potentially Retryable

Examples:

- Temporary network failure
- Temporary connection failure
- Service temporarily unavailable
- Temporary timeout
- Some rate-limit situations

### Usually Not Retryable

Examples:

- Invalid API key
- Invalid request format
- Invalid parameter
- Missing required input
- Permanent authentication failure
- Invalid model name

Conceptually:

    Error
      ↓
    Retryable?
     ↙     ↘
   Yes      No
    ↓        ↓
  Retry    Handle failure

---

# 1️⃣2️⃣ Invalid Input Should Not Usually Be Retried

Consider:

    temperature = 5

Suppose the valid range is:

    0 to 2

Retrying the same invalid value will not fix the problem.

Bad pattern:

    Invalid temperature
          ↓
       Retry
          ↓
    Invalid temperature
          ↓
       Retry
          ↓
    Invalid temperature

Better:

    Invalid temperature
          ↓
    Return validation error
          ↓
    Ask for corrected input

This is why retry logic should be combined with proper validation.

---

# 1️⃣3️⃣ Retry Logic with Logging

Retry attempts should often be logged.

Example:

    import logging
    import time


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    max_retries = 3

    for attempt in range(1, max_retries + 1):

        logging.info(
            "API request attempt %s.",
            attempt
        )

        try:

            # Simulating a temporary failure.
            raise ConnectionError(
                "Temporary network error."
            )

        except ConnectionError as e:

            logging.warning(
                "API request failed: %s",
                e
            )

            if attempt < max_retries:

                logging.info(
                    "Retrying API request."
                )

                time.sleep(1)

            else:

                logging.error(
                    "Maximum retry attempts reached."
                )

This creates a useful execution history.

---

# 1️⃣4️⃣ Retry Logic with a Function

Instead of writing retry logic repeatedly, it can be placed inside a function.

Example:

    import time


    def request_with_retry(
        max_retries: int = 3
    ):

        for attempt in range(
            1,
            max_retries + 1
        ):

            print(
                f"Attempt {attempt}: "
                "Sending request..."
            )

            try:

                # Simulating a temporary failure.
                raise ConnectionError(
                    "Temporary network error."
                )

            except ConnectionError as e:

                print("Request failed:", e)

                if attempt < max_retries:

                    print("Retrying...")
                    time.sleep(1)

                else:

                    print(
                        "Request failed permanently."
                    )


    request_with_retry()

This makes retry behavior reusable.

---

# 1️⃣5️⃣ Retry Logic in AI Applications

AI applications frequently depend on external services.

For example:

    User
      ↓
    AI Application
      ↓
    Embedding API
      ↓
    Vector Database
      ↓
    LLM API
      ↓
    Response

Any external service may temporarily fail.

Retry logic can be useful for appropriate transient failures.

Example:

    LLM Request
        ↓
    Temporary Network Failure
        ↓
    Wait
        ↓
    Retry
        ↓
    LLM Response

---

# 1️⃣6️⃣ Retry Logic in RAG Systems

A RAG pipeline may involve:

    User Query
         ↓
    Generate Embedding
         ↓
    Vector Database
         ↓
    Retrieve Documents
         ↓
    LLM Request
         ↓
    Final Response

Potential temporary failures include:

    Embedding API timeout
    Vector database connection failure
    LLM API temporary failure

A carefully designed system can retry appropriate operations.

However, retrying should depend on the type of error.

---

# 1️⃣7️⃣ Retry Logic in AI Agents

AI agents may execute external tools.

Example:

    Agent
      ↓
    Select Tool
      ↓
    Execute Tool
      ↓
    Temporary Failure?
       ↙       ↘
     Yes        No
      ↓          ↓
    Retry      Continue
      ↓
    Success

For example, a temporary network failure while calling a web API may be retryable.

A malformed tool input may not be retryable without changing the input.

---

# 1️⃣8️⃣ Retry Logic and Idempotency

## 📖 Definition

> **An operation is idempotent when repeating it produces the same intended final effect as performing it once.**

This is important when designing retries.

For example, repeatedly requesting data is generally different from repeatedly performing a financial transaction.

Consider:

    GET request
       ↓
    Retry
       ↓
    GET request

The operation usually only retrieves information.

But consider:

    Transfer ₹5,000
          ↓
       Retry
          ↓
    Transfer ₹5,000 again

If the operation is not safely designed for retries, the same transaction could potentially be processed more than once.

Therefore, retry logic should consider whether the operation is safe to repeat.

---

# 1️⃣9️⃣ Retry Logic and Rate Limits

External APIs may impose rate limits.

For example:

    Too Many Requests
          ↓
    Wait
          ↓
    Retry

The application should respect the API's retry guidance when available.

Repeatedly sending requests without waiting can make the situation worse.

---

# 2️⃣0️⃣ Retry Logic and Timeouts

Retry logic and timeouts solve different problems.

### Timeout

> Determines how long an operation is allowed to wait.

Example:

    Wait at most 5 seconds.

### Retry

> Determines how many times an operation should be attempted again.

Example:

    Try up to 3 times.

They can work together:

    Request
       ↓
    Timeout after 5 seconds
       ↓
    Retry
       ↓
    Timeout after 5 seconds
       ↓
    Retry
       ↓
    Final failure

---

# 🔄 Retry vs Timeout

| Retry | Timeout |
|---|---|
| Controls repeated attempts | Controls waiting duration |
| Used after a failure | Used when an operation takes too long |
| Example: retry 3 times | Example: wait maximum 5 seconds |
| Can improve reliability | Prevents indefinite waiting |

---

# 2️⃣1️⃣ Retry Logic with Timeout

A production-style request may use both.

Conceptually:

    Start Request
         ↓
    Wait up to 5 seconds
         ↓
    ┌───────────────┐
    │               │
  Success         Timeout
    │               │
    ↓               ↓
  Return          Retry
                    ↓
              Another Request

This prevents the application from waiting indefinitely while still allowing temporary failures to recover.

---

# 2️⃣2️⃣ Maximum Retry Limit

Always consider a maximum number of attempts.

Avoid:

    while True:
        retry_request()

unless there is a very specific reason and a separate termination mechanism.

Otherwise, the application could retry indefinitely.

Prefer:

    max_retries = 3

or another appropriate limit based on the application.

---

# 2️⃣3️⃣ Retry Logic Best Practices

### 1. Retry only appropriate failures

Do not retry every exception automatically.

### 2. Use a maximum retry count

Avoid infinite retry loops.

### 3. Add a delay

Give temporary problems time to recover.

### 4. Consider exponential backoff

Increase the delay between repeated failures.

### 5. Consider jitter

Spread retry attempts when many clients may retry simultaneously.

### 6. Log retry attempts

This makes behavior easier to diagnose.

### 7. Do not retry invalid input

Fix the input instead.

### 8. Consider idempotency

Make sure repeating an operation is safe.

### 9. Combine retry logic with timeouts

Avoid waiting indefinitely on each attempt.

### 10. Provide graceful failure after final retry

When all attempts fail, return a meaningful result or error.

---

# 2️⃣4️⃣ Complete Practical Example

    import time
    import logging


    # Configure application logging.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    # Maximum number of request attempts.
    max_retries = 3


    for attempt in range(
        1,
        max_retries + 1
    ):

        logging.info(
            "API request attempt %s.",
            attempt
        )

        try:

            # Simulate a temporary API failure.
            raise ConnectionError(
                "Temporary network error."
            )

        except ConnectionError as e:

            logging.warning(
                "API request failed: %s",
                e
            )

            if attempt < max_retries:

                # Wait before making another attempt.
                logging.info(
                    "Retrying API request..."
                )

                time.sleep(2)

            else:

                # No attempts remain.
                logging.error(
                    "Maximum retry attempts reached."
                )

Output:

    INFO - API request attempt 1.
    WARNING - API request failed: Temporary network error.
    INFO - Retrying API request...

    INFO - API request attempt 2.
    WARNING - API request failed: Temporary network error.
    INFO - Retrying API request...

    INFO - API request attempt 3.
    WARNING - API request failed: Temporary network error.
    ERROR - Maximum retry attempts reached.

This example demonstrates:

    Exception Handling
          +
    Retry Logic
          +
    Delay
          +
    Logging
          +
    Maximum Attempts

---

# 🤖 AI Engineer Relevance

Retry logic is important for:

- LLM APIs
- Embedding APIs
- Vector databases
- Web APIs
- AI agents
- RAG pipelines
- Database operations
- External model services
- Distributed AI systems

A production AI system may use:

    Request
       ↓
    Timeout
       ↓
    Retryable Error?
      ↙       ↘
    Yes        No
     ↓          ↓
   Backoff    Handle Error
     ↓
   Retry
     ↓
   Success / Final Failure

---

# 🧠 Key Takeaways

- Retry logic automatically attempts a failed operation again.
- It is mainly useful for temporary or transient failures.
- Not every error should be retried.
- Invalid input and permanent authentication errors generally should not be blindly retried.
- A maximum retry count prevents infinite loops.
- A delay between attempts can give temporary problems time to recover.
- Exponential backoff increases the delay between repeated attempts.
- Jitter adds randomness to retry delays and can reduce synchronized retry traffic.
- Retry logic should consider whether an operation is safe to repeat.
- Logging retry attempts makes system behavior easier to diagnose.
- Retry logic and timeout are different but can work together.
- After all retries fail, the application should fail gracefully with a meaningful error or fallback.
- Retry logic is highly relevant to AI applications because they frequently depend on external APIs and services.


# 1️⃣4️⃣ Timeouts

## 📖 Definition

> **A timeout is a limit placed on how long a program will wait for an operation to complete before stopping the wait or handling the delay as an error.**

Without a timeout, an application may wait indefinitely for a slow or unresponsive operation.

Basic idea:

    Start Operation
          ↓
       Wait
          ↓
    Time Limit Reached?
       ↙       ↘
     No         Yes
      ↓          ↓
   Continue    Timeout

---

# 14.1️⃣ Why Timeouts Are Important

Consider an AI application calling an external service.

    AI Application
          ↓
       AI API
          ↓
      No Response

Without a timeout:

    Request
      ↓
    Wait
      ↓
    Wait
      ↓
    Wait
      ↓
    Wait...

The application may remain blocked for an unpredictable amount of time.

With a timeout:

    Request
      ↓
    Wait 5 seconds
      ↓
    No response
      ↓
    Timeout
      ↓
    Handle failure

Timeouts help prevent indefinite waiting.

---

# 14.2️⃣ Real-Life Example

Imagine ordering food.

    Order placed
        ↓
    Restaurant prepares food
        ↓
    Wait maximum 60 minutes
        ↓
    Food arrives → Success
        ↓
    No delivery → Handle delay

The 60-minute limit is similar to a timeout.

In software:

    Operation
        ↓
    Maximum waiting time
        ↓
    Timeout if exceeded

---

# 14.3️⃣ Timeout vs Retry

These concepts are related but different.

### Timeout

Controls:

> How long should we wait?

Example:

    Wait maximum 5 seconds.

### Retry

Controls:

> How many times should we try again?

Example:

    Try up to 3 times.

Together:

    Request
       ↓
    Wait 5 seconds
       ↓
    Timeout
       ↓
    Retry
       ↓
    Wait 5 seconds
       ↓
    Timeout
       ↓
    Final Failure

---

# 🔄 Comparison

| Timeout | Retry |
|---|---|
| Limits waiting time | Controls repeated attempts |
| Prevents indefinite waiting | Can recover from temporary failures |
| Example: 5-second limit | Example: 3 attempts |
| Applies to an individual operation | Applies across multiple attempts |

---

# 14.4️⃣ Simulating a Timeout

Python's `concurrent.futures` can be used to demonstrate timeout behavior.

Example:

    import time
    from concurrent.futures import (
        ThreadPoolExecutor,
        TimeoutError
    )


    def api_request():

        # Simulate an API request that takes 5 seconds.
        time.sleep(5)

        return "API response received"


    with ThreadPoolExecutor() as executor:

        # Start the API request in a separate thread.
        future = executor.submit(api_request)

        try:

            # Wait for the result for a maximum of 2 seconds.
            result = future.result(timeout=2)

            print(result)

        except TimeoutError:

            print("Request timed out.")

Output:

    Request timed out.

The request takes approximately five seconds, but the caller waits only two seconds for the result.

---

# 14.5️⃣ Understanding `future.result(timeout=...)`

The expression:

    future.result(timeout=2)

means:

> Wait for the result for at most approximately two seconds.

If the operation completes within that time:

    result

is returned.

If it does not complete within the allowed waiting period:

    TimeoutError

is raised.

---

# 14.6️⃣ Timeout Flow

    API Request
        ↓
    Start Operation
        ↓
    Wait up to 2 seconds
        ↓
    ┌───────────────┐
    │               │
  Response       No Response
    │               │
    ↓               ↓
  Return          Timeout
  Result            ↓
                 Handle Error

---

# 14.7️⃣ Timeout Does Not Always Mean the Operation Stops Immediately

This distinction is important.

When:

    future.result(timeout=2)

raises `TimeoutError`, it means the caller stopped waiting for the result after the timeout.

It does not necessarily mean that the underlying operation was immediately terminated.

For example, the worker function may still be running.

Therefore:

    Timeout

and:

    Cancellation / Termination

are different concepts.

---

# 14.8️⃣ Timeout with Exception Handling

Example:

    import time
    from concurrent.futures import (
        ThreadPoolExecutor,
        TimeoutError
    )


    def slow_operation():

        time.sleep(5)

        return "Operation completed."


    with ThreadPoolExecutor() as executor:

        future = executor.submit(
            slow_operation
        )

        try:

            result = future.result(
                timeout=2
            )

            print(result)

        except TimeoutError:

            print(
                "Operation timed out. "
                "Please try again later."
            )

Output:

    Operation timed out.
    Please try again later.

This combines:

    Timeout
        +
    Exception Handling
        +
    Proper Error Message

---

# 14.9️⃣ Timeouts in AI APIs

AI applications often depend on external APIs.

For example:

    User
      ↓
    AI Application
      ↓
    LLM API
      ↓
    Response

The LLM service may experience:

- High traffic
- Network problems
- Temporary service issues
- Slow processing
- Connection problems

A timeout prevents the application from waiting forever.

Conceptually:

    LLM Request
        ↓
    Wait maximum 10 seconds
        ↓
    ┌───────────────┐
    │               │
  Response       Timeout
    │               │
    ↓               ↓
  Return          Retry /
  Response        Fallback

---

# 1️⃣5️⃣ Timeout in RAG Systems

A RAG pipeline may involve multiple operations:

    User Query
         ↓
    Generate Embedding
         ↓
    Vector Search
         ↓
    Retrieve Context
         ↓
    LLM Request
         ↓
    Final Response

Each external operation may have its own timeout.

For example:

    Embedding API
        ↓
    Timeout: 5 seconds

    Vector Database
        ↓
    Timeout: 3 seconds

    LLM API
        ↓
    Timeout: 20 seconds

This prevents one slow component from blocking the entire pipeline indefinitely.

---

# 1️⃣5️⃣1️⃣ Timeout in AI Agents

AI agents may use external tools.

Example:

    Agent
      ↓
    Select Tool
      ↓
    Call Tool
      ↓
    Tool Response
      ↓
    Continue Agent Execution

If a tool becomes unresponsive:

    Tool Request
        ↓
    Timeout
        ↓
    Tool failed
        ↓
    Agent handles failure
        ↓
    Alternative action / response

This is especially important for agents that depend on multiple external services.

---

# 1️⃣6️⃣ Timeout and Graceful Failure

A timeout should usually be handled gracefully.

Poor behavior:

    API timeout
        ↓
    Application crashes

Better behavior:

    API timeout
        ↓
    Catch timeout
        ↓
    Log failure
        ↓
    Retry / fallback / user message

Example:

    try:

        response = call_api()

    except TimeoutError:

        logging.warning(
            "AI API request timed out."
        )

        print(
            "The AI service is taking too long "
            "to respond. Please try again later."
        )

---

# 1️⃣7️⃣ Timeout and Retry Together

A common production pattern is:

    Request
       ↓
    Timeout
       ↓
    Retryable?
      ↙       ↘
    Yes        No
     ↓          ↓
   Retry      Failure
     ↓
    Timeout
     ↓
    Retry
     ↓
    Success / Final Failure

For example:

    Maximum Attempts = 3
    Timeout Per Attempt = 5 seconds

Possible behavior:

    Attempt 1
       ↓
    Wait 5 seconds
       ↓
    Timeout

    Attempt 2
       ↓
    Wait 5 seconds
       ↓
    Success

The total time depends on the implementation and retry delays.

---

# 1️⃣8️⃣ Choosing a Timeout

The appropriate timeout depends on the operation.

Examples:

    Fast API request
        ↓
    Short timeout

    Large model inference
        ↓
    Longer timeout

    Database query
        ↓
    Depends on expected query duration

    File operation
        ↓
    Depends on file size and storage

There is no single timeout value that is correct for every application.

---

# 1️⃣9️⃣ Timeout Too Short

A timeout that is too short can cause unnecessary failures.

Example:

    Actual API response time:
    3 seconds

    Configured timeout:
    1 second

Result:

    Timeout
        ↓
    Unnecessary retry

The service may have responded successfully if the application had waited slightly longer.

---

# 2️⃣0️⃣ Timeout Too Long

A timeout that is too long can cause the application to remain blocked for too long.

Example:

    API timeout:
    10 minutes

If the service is unavailable, users may have to wait for a very long time before receiving a failure response.

Therefore, timeout values should be selected based on realistic application requirements.

---

# 2️⃣1️⃣ Timeout Best Practices

### 1. Set timeouts for external operations

Do not allow external calls to wait indefinitely when a timeout can reasonably be applied.

### 2. Choose realistic timeout values

Avoid both extremely short and unnecessarily long timeouts.

### 3. Handle timeout errors explicitly

Provide a meaningful fallback or error response.

### 4. Log important timeouts

Timeouts can reveal performance or availability problems.

### 5. Combine with retry logic when appropriate

Temporary failures may recover after a retry.

### 6. Consider operation type

Different operations may need different timeout values.

### 7. Do not assume timeout means cancellation

The caller may stop waiting while the underlying operation continues.

---

# 2️⃣2️⃣ Complete Practical Example

    import time
    import logging

    from concurrent.futures import (
        ThreadPoolExecutor,
        TimeoutError
    )


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    def api_request():

        logging.info(
            "AI API request started."
        )

        # Simulating a slow API request.
        time.sleep(5)

        return "AI response received."


    with ThreadPoolExecutor() as executor:

        future = executor.submit(
            api_request
        )

        try:

            logging.info(
                "Waiting for API response."
            )

            result = future.result(
                timeout=2
            )

            print("Response:", result)

        except TimeoutError:

            logging.warning(
                "AI API request timed out."
            )

            print(
                "The AI service took too long "
                "to respond. Please try again later."
            )

Output:

    INFO - AI API request started.
    INFO - Waiting for API response.
    WARNING - AI API request timed out.

    The AI service took too long to respond.
    Please try again later.

This example demonstrates:

    API Simulation
          +
    ThreadPoolExecutor
          +
    Timeout
          +
    Logging
          +
    Graceful Failure

---

# 🔄 Important Comparison

| Concept | Purpose |
|---|---|
| Exception Handling | Handle failures |
| Retry Logic | Attempt an operation again |
| Timeout | Limit how long to wait |
| Logging | Record what happened |
| Graceful Failure | Prevent unexpected application failure |

A reliable application can combine all of them:

    Operation
        ↓
    Timeout
        ↓
    Error?
      ↙    ↘
    Yes     No
     ↓       ↓
    Retry   Success
     ↓
    Logging
     ↓
    Final Failure
     ↓
    Graceful Response

---

# 🤖 AI Engineer Relevance

Timeouts are important for:

- LLM APIs
- Embedding APIs
- Vector databases
- Web APIs
- AI agents
- RAG pipelines
- Database operations
- Model inference
- Distributed AI systems
- FastAPI services

In production AI systems, timeouts help control latency and prevent slow external services from blocking the entire application.

---

# 🧠 Key Takeaways

- A timeout limits how long an application waits for an operation.
- Without appropriate timeouts, external operations may wait indefinitely.
- `future.result(timeout=...)` can demonstrate timeout behavior with `concurrent.futures`.
- A timeout does not necessarily terminate the underlying operation immediately.
- Timeout and cancellation are different concepts.
- Timeout and retry solve different problems.
- A timeout controls waiting time.
- Retry controls repeated attempts.
- Timeouts are especially important when working with external APIs and services.
- Timeout values should be chosen according to the expected behavior of the operation.
- A timeout should usually be handled gracefully.
- AI systems can combine timeout, retry, logging, and graceful failure to become more reliable.

# 1️⃣5️⃣ Graceful Failure

## 📖 Definition

> **Graceful failure is the practice of handling errors or failures safely so that an application does not crash unexpectedly and can provide a meaningful response or continue operating when possible.**

In simple terms, graceful failure means:

    Failure occurs
         ↓
    Detect the failure
         ↓
    Handle the failure
         ↓
    Log the problem
         ↓
    Provide a meaningful response
         ↓
    Continue / Retry / Stop safely

The goal is not to hide errors.

The goal is to make sure that failures are handled in a controlled way.

---

# 15.1️⃣ Why Graceful Failure Is Important

Consider an application that calls an external AI service.

Without graceful failure:

    User Request
         ↓
    AI API
         ↓
    Connection Error
         ↓
    Application Crashes

With graceful failure:

    User Request
         ↓
    AI API
         ↓
    Connection Error
         ↓
    Catch Error
         ↓
    Log Error
         ↓
    Provide Fallback Message
         ↓
    Application Continues

This creates a better user experience and makes the system more reliable.

---

# 15.2️⃣ Simple Example

Example:

    def divide_numbers(a, b):

        try:

            # Perform the division operation.
            return a / b

        except ZeroDivisionError:

            # Handle division by zero safely.
            print("Cannot divide by zero.")

            # Return None to indicate that
            # the operation was not successful.
            return None


    # Call the function with an invalid denominator.
    result = divide_numbers(10, 0)


    # Check whether the operation succeeded.
    if result is not None:

        print("Result:", result)

    else:

        print(
            "Operation could not be completed."
        )

Output:

    Cannot divide by zero.
    Operation could not be completed.

The application does not terminate unexpectedly.

---

# 15.3️⃣ Why Return `None`?

In the previous example:

    return None

is used to indicate that the operation did not produce a valid result.

The caller can then decide what to do:

    if result is not None:
        process_result(result)
    else:
        handle_failure()

This is one possible graceful-failure strategy.

The exact strategy depends on the application.

---

# 15.4️⃣ Graceful Failure Is Not Ignoring Errors

A bad approach is:

    try:
        process_data()

    except Exception:
        pass

This silently ignores the failure.

Problems with this approach:

- The error disappears.
- Debugging becomes difficult.
- The application may continue with invalid state.
- Developers may not know that something failed.

Graceful failure should instead:

    Detect
       ↓
    Understand
       ↓
    Log / Report
       ↓
    Recover or Stop Safely

---

# 15.5️⃣ Graceful Failure with Logging

Example:

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    def divide_numbers(a, b):

        try:

            return a / b

        except ZeroDivisionError:

            logging.error(
                "Division failed because the denominator was zero."
            )

            return None


    result = divide_numbers(10, 0)


    if result is not None:

        print("Result:", result)

    else:

        print(
            "Unable to complete the calculation."
        )

Output:

    ERROR - Division failed because the denominator was zero.
    Unable to complete the calculation.

Here:

    logging.error()

records the technical problem.

The user-facing message provides a simpler explanation.

---

# 15.6️⃣ Graceful Failure in an AI API

Consider a simplified AI API function.

    def call_ai_api(prompt):

        try:

            # Simulating an AI API failure.
            raise ConnectionError(
                "AI API is temporarily unavailable."
            )

        except ConnectionError as e:

            print("AI service error:", e)

            return None


    prompt = "Explain Machine Learning."

    response = call_ai_api(prompt)


    if response is not None:

        print("AI Response:", response)

    else:

        print(
            "Sorry, the AI service is currently "
            "unavailable. Please try again later."
        )

Output:

    AI service error: AI API is temporarily unavailable.
    Sorry, the AI service is currently unavailable.
    Please try again later.

The actual API is not being called here. The failure is simulated.

---

# 15.7️⃣ User-Facing vs Developer-Facing Information

Graceful failure often involves two different messages.

### Developer-facing information

Useful for debugging:

    ConnectionError:
    AI API is temporarily unavailable.

### User-facing information

Clear and safe:

    "The AI service is currently unavailable.
    Please try again later."

The developer may need detailed technical information, while the user usually needs a concise explanation and possible next step.

---

# 15.8️⃣ Graceful Failure with Fallback

## 📖 Definition

> **A fallback is an alternative behavior used when the primary operation cannot be completed successfully.**

Example:

    Primary AI Service
           ↓
        Failure
           ↓
      Fallback
           ↓
    Alternative Response

A fallback could be:

- A cached response
- A default value
- A secondary service
- A local model
- A simpler operation
- A user-friendly message

---

# 15.9️⃣ Simple Fallback Example

    def get_weather():

        try:

            # Simulating a failed external service.
            raise ConnectionError(
                "Weather API unavailable."
            )

        except ConnectionError:

            # Return a fallback response.
            return "Weather information is temporarily unavailable."


    response = get_weather()

    print(response)

Output:

    Weather information is temporarily unavailable.

The application provides a meaningful result instead of crashing.

---

# 🔟 Graceful Failure with Retry

Graceful failure can work together with retry logic.

Example flow:

    API Request
        ↓
    Temporary Failure
        ↓
    Retry
        ↓
    Success?
      ↙     ↘
    Yes      No
     ↓        ↓
  Continue  Graceful Failure

Example:

    Attempt 1
       ↓
    Failure
       ↓
    Retry

    Attempt 2
       ↓
    Failure
       ↓
    Retry

    Attempt 3
       ↓
    Failure
       ↓
    Final Failure
       ↓
    Graceful Response

This prevents the application from retrying forever.

---

# 1️⃣1️⃣ Graceful Failure with Timeout

Timeouts and graceful failure also work together.

Example:

    AI API Request
         ↓
    Wait for response
         ↓
    Timeout
         ↓
    Catch TimeoutError
         ↓
    Log failure
         ↓
    Retry / Fallback
         ↓
    User response

This prevents a slow external service from blocking the application indefinitely.

---

# 1️⃣2️⃣ Graceful Failure in RAG Systems

A RAG system may contain:

    User Query
         ↓
    Query Validation
         ↓
    Embedding Generation
         ↓
    Vector Search
         ↓
    Document Retrieval
         ↓
    Prompt Construction
         ↓
    LLM
         ↓
    Final Response

Many components can fail.

For example:

    Embedding API
          ↓
       Failure

or:

    Vector Database
          ↓
       Failure

or:

    LLM API
          ↓
       Timeout

A graceful system can handle these failures without unnecessarily crashing the entire application.

---

# 1️⃣3️⃣ RAG Fallback Example

Suppose vector search fails.

A possible strategy could be:

    Vector Search
         ↓
      Failure
         ↓
    Log Error
         ↓
    Fallback Strategy
         ↓
    Return Safe Response

For example:

    "I could not retrieve the required information.
    Please try again later."

The exact fallback depends on the application's requirements.

---

# 1️⃣4️⃣ Graceful Failure in AI Agents

AI agents may call multiple tools.

Example:

    User Request
         ↓
       Agent
         ↓
    Tool Selection
         ↓
    Tool Execution
         ↓
    Tool Failure
         ↓
    Handle Failure
         ↓
    Alternative Tool / Retry / Final Response

Suppose a web-search tool fails.

The agent might:

- Retry the tool
- Use another available tool
- Continue with existing information
- Ask the user to try again
- Return a controlled failure message

The appropriate strategy depends on the application.

---

# 1️⃣5️⃣ Graceful Failure and Custom Exceptions

Custom exceptions can make graceful failure easier to structure.

Example:

    class AIServiceError(Exception):
        pass


    def call_ai_service():

        try:

            raise ConnectionError(
                "Temporary AI service failure."
            )

        except ConnectionError as e:

            raise AIServiceError(
                "Unable to communicate with the AI service."
            ) from e


    try:

        call_ai_service()

    except AIServiceError as e:

        print(
            "AI service error:",
            e
        )

This converts a low-level error into an application-specific error.

---

# 1️⃣6️⃣ Graceful Failure and Proper Error Messages

A graceful application should communicate failure clearly.

Poor:

    Something went wrong.

Better:

    "The AI service is temporarily unavailable."

Even better when appropriate:

    "The AI service is temporarily unavailable.
    Please try again later."

A good message should:

- Explain the problem
- Avoid unnecessary technical details
- Avoid sensitive information
- Provide a useful next step when possible

---

# 1️⃣7️⃣ Graceful Failure and Logging

A production application should usually record important failures.

Example:

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    def call_ai_service():

        try:

            raise ConnectionError(
                "AI service unavailable."
            )

        except ConnectionError:

            logging.exception(
                "AI service request failed."
            )

            return None


    response = call_ai_service()


    if response is None:

        print(
            "The AI service is currently unavailable."
        )

Here:

    logging.exception()

records technical information.

The user receives a simpler message.

---

# 1️⃣8️⃣ Graceful Failure Does Not Mean Hiding Failures

This distinction is important.

### Hiding failure

    try:
        process_request()

    except Exception:
        pass

The application hides the problem.

### Graceful failure

    try:
        process_request()

    except Exception as e:

        logging.exception(
            "Request processing failed."
        )

        print(
            "The request could not be completed."
        )

The second approach:

- Detects the failure
- Records the failure
- Communicates the failure
- Prevents an uncontrolled crash

---

# 1️⃣9️⃣ Graceful Failure and Application State

A failure should not leave the application in an invalid state.

For example:

    Start Transaction
         ↓
    Update Data
         ↓
    Failure
         ↓
    Partial State

A robust application may need to:

- Roll back changes
- Release resources
- Reset state
- Preserve data consistency
- Notify the user

The exact mechanism depends on the system.

---

# 2️⃣0️⃣ Graceful Failure with Resource Cleanup

Resource cleanup should still occur when an operation fails.

For example:

    resource = acquire_resource()

    try:

        use_resource(resource)

    except Exception as e:

        print(
            "Operation failed:",
            e
        )

    finally:

        release_resource(resource)

The important principle is:

    Failure
       ↓
    Handle Error
       ↓
    Cleanup Resource
       ↓
    Continue / Stop Safely

This connects graceful failure with resource management.

---

# 2️⃣1️⃣ Graceful Failure in Production AI Systems

A production AI system may have many failure points:

    User Input
        ↓
    Validation
        ↓
    Authentication
        ↓
    API Request
        ↓
    Model
        ↓
    Database
        ↓
    Response Processing

Any stage may fail.

A robust architecture should decide what happens when each stage fails.

For example:

    Validation Failure
        ↓
    Return validation message

    API Timeout
        ↓
    Retry

    API Permanent Failure
        ↓
    Fallback / Error Response

    Database Failure
        ↓
    Log + Controlled Failure

    Unexpected Exception
        ↓
    Log + Safe Response

---

# 2️⃣2️⃣ Complete AI API Example

    import logging


    # Configure logging.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    def call_ai_api(prompt: str):

        logging.info(
            "AI request received."
        )

        try:

            # Simulate an AI service failure.
            raise ConnectionError(
                "AI service is temporarily unavailable."
            )

        except ConnectionError:

            # Record technical information for debugging.
            logging.exception(
                "AI API request failed."
            )

            # Return None to signal controlled failure.
            return None


    # User prompt.
    prompt = "Explain Machine Learning."


    # Call the AI service.
    response = call_ai_api(prompt)


    # Handle the result safely.
    if response is not None:

        print(
            "AI Response:",
            response
        )

    else:

        print(
            "Sorry, the AI service is currently "
            "unavailable. Please try again later."
        )

Possible output:

    INFO - AI request received.
    ERROR - AI API request failed.

    Traceback ...
    ConnectionError: AI service is temporarily unavailable.

    Sorry, the AI service is currently unavailable.
    Please try again later.

The traceback details are useful for developers, while the final message is appropriate for the user.

---

# 2️⃣3️⃣ Complete Failure-Handling Flow

A production-style AI operation can follow this general pattern:

    User Request
         ↓
    Input Validation
         ↓
    Valid?
      ↙    ↘
    No      Yes
     ↓        ↓
    Error   API Request
    Message    ↓
            Timeout?
            ↙    ↘
          Yes     No
           ↓       ↓
         Retry   Response
           ↓
       Retryable?
         ↙    ↘
       Yes     No
        ↓       ↓
      Retry   Graceful
                Failure
                   ↓
                Logging
                   ↓
              User Response

---

# 2️⃣4️⃣ Graceful Failure Best Practices

### 1. Catch expected failures

Handle errors that the application knows how to handle.

### 2. Do not silently ignore exceptions

Always consider whether an error should be logged, returned, retried, or propagated.

### 3. Provide meaningful messages

Users should understand what happened without being exposed to unnecessary technical details.

### 4. Log important failures

Logs help developers investigate production problems.

### 5. Use retries for temporary failures

Do not retry permanent failures unnecessarily.

### 6. Use timeouts

Avoid waiting indefinitely for external operations.

### 7. Provide fallbacks where appropriate

A fallback can allow the application to continue operating.

### 8. Clean up resources

Files, connections, locks, and other resources should still be released.

### 9. Preserve application consistency

Avoid leaving the system in an invalid or partially updated state.

### 10. Do not expose sensitive information

Never include secrets in user-facing error messages or logs.

---

# 🔄 Important Comparison

| Concept | Purpose |
|---|---|
| Exception Handling | Detect and handle errors |
| Retry Logic | Attempt temporary failures again |
| Timeout | Limit waiting time |
| Logging | Record important events and failures |
| Fallback | Provide alternative behavior |
| Graceful Failure | Handle failure safely and in a controlled manner |
| Resource Management | Ensure resources are properly released |

These concepts often work together.

---

# 🤖 AI Engineer Relevance

Graceful failure is important for:

- LLM applications
- RAG systems
- AI agents
- AI APIs
- Vector databases
- Embedding services
- Model inference
- FastAPI applications
- Distributed AI systems
- Production AI applications

A reliable AI application should not assume that every external service will always work.

Instead:

    External Dependency
          ↓
    Success → Continue
          ↓
    Failure → Detect
          ↓
    Retry / Fallback / Error Handling
          ↓
    Log
          ↓
    Safe Response

---

# 🧠 Key Takeaways

- Graceful failure means handling failures in a controlled and safe way.
- It prevents applications from crashing unexpectedly.
- Graceful failure does not mean ignoring or hiding errors.
- Important failures should be logged.
- Users should receive clear and appropriate messages.
- Retry logic can be used for temporary failures.
- Timeouts can prevent indefinite waiting.
- Fallbacks can provide alternative behavior when the primary operation fails.
- Resource cleanup should still happen when failures occur.
- Custom exceptions can help organize application-specific failures.
- AI systems need graceful failure because they often depend on external APIs, databases, models, and tools.
- A robust system should define what happens when each important component fails.

# 1️⃣6️⃣ Edge Cases

## 📖 Definition

> **An edge case is an unusual or extreme situation that occurs at the boundary of normal expected input or behavior and can cause unexpected results if it is not handled properly.**

Most programs are designed around normal situations.

For example:

    numbers = [10, 20, 30, 40]

This is a normal input.

But what happens when:

    numbers = []

This is an edge case.

A robust program should consider such situations before they cause errors.

---

# 16.1️⃣ Normal Cases vs Edge Cases

### Normal Case

    User enters:
    25

    Program:
    Calculates the result

### Edge Case

    User enters:
    0

    Program:
    Must determine whether 0 is valid.

Another example:

    Normal:
    "Explain Machine Learning"

    Edge Case:
    ""

    Edge Case:
    "     "

    Edge Case:
    Extremely long prompt

The correct behavior depends on the application's requirements.

---

# 16.2️⃣ Why Edge Cases Matter

Consider this code:

    numbers = [10, 20, 30]

    average = sum(numbers) / len(numbers)

This works correctly.

But if:

    numbers = []

then:

    len(numbers)

is:

    0

Therefore:

    sum(numbers) / len(numbers)

becomes:

    0 / 0

which raises:

    ZeroDivisionError

The problem is not with the normal case.

The problem is that the program did not consider an edge case.

---

# 16.3️⃣ Handling an Empty List

A safer implementation is:

    # Normal case:
    # The list contains numbers.
    numbers = [10, 20, 30, 40, 50]


    # Check whether the list is empty.
    if not numbers:

        # Handle the edge case safely.
        print(
            "Cannot calculate average. "
            "The list is empty."
        )

    else:

        # Calculate the average when numbers are available.
        average = sum(numbers) / len(numbers)

        print(
            "Average:",
            average
        )

Output:

    Average: 30.0

If the list is:

    numbers = []

Output:

    Cannot calculate average. The list is empty.

---

# 16.4️⃣ Why `if not numbers` Works

In Python, an empty list is considered falsy.

Therefore:

    numbers = []

    if not numbers:
        print("List is empty.")

The condition becomes true.

Examples of other commonly falsy values include:

    False
    None
    0
    ""
    []
    {}
    ()

This behavior can be useful for checking empty collections.

---

# 16.5️⃣ Edge Cases in User Input

Suppose a program asks for a username.

A normal input might be:

    Sonal

But users might enter:

    ""

or:

    "   "

or:

    "So"

or a very long string.

The program should define what is considered valid.

Example:

    while True:

        username = input(
            "Enter username: "
        )

        # Remove leading and trailing whitespace.
        username = username.strip()


        # Check for empty input.
        if not username:

            print(
                "Username is required."
            )

        # Check minimum length.
        elif len(username) < 3:

            print(
                "Username must contain "
                "at least 3 characters."
            )

        else:

            print(
                "Valid username:",
                username
            )

            break

This handles multiple possible edge cases.

---

# 16.6️⃣ Common Input Edge Cases

When accepting user input, consider:

| Edge Case | Example |
|---|---|
| Empty input | `""` |
| Whitespace | `"   "` |
| Zero | `0` |
| Negative number | `-10` |
| Very large number | `999999999999` |
| Wrong type | `"hello"` instead of `25` |
| Very long input | Huge text |
| Unexpected characters | `"12abc"` |
| Duplicate input | Same value entered twice |
| Boundary value | Minimum or maximum allowed value |

Not every edge case is invalid.

Some may be perfectly valid depending on the application's requirements.

---

# 16.7️⃣ Boundary Values

## 📖 Definition

> **A boundary value is a value located at or near the limit of an allowed range.**

Suppose an AI API allows:

    temperature = 0 to 2

Important values include:

    0
    0.1
    1
    1.9
    2
    2.1

The values:

    0

and:

    2

are boundary values.

The value:

    2.1

is outside the allowed range.

---

# 16.8️⃣ Boundary Validation Example

    temperature = 2


    if temperature < 0 or temperature > 2:

        print(
            "Invalid temperature."
        )

    else:

        print(
            "Temperature is valid."
        )

Output:

    Temperature is valid.

Now:

    temperature = 2.1

Output:

    Invalid temperature.

Boundary testing is especially important when dealing with:

- API parameters
- Model configuration
- User limits
- File sizes
- Token limits
- Numerical ranges

---

# 16.9️⃣ Empty String vs Whitespace

These two values look similar but are technically different:

    ""

and:

    "     "

The first contains no characters.

The second contains whitespace characters.

Therefore, this check:

    if not prompt:

may not reject:

    "     "

A better validation can be:

    if not prompt.strip():

This treats whitespace-only input as empty.

Example:

    prompt = "   "


    if not prompt.strip():

        print(
            "Prompt cannot be empty."
        )

Output:

    Prompt cannot be empty.

---

# 🔟 AI Prompt Edge Cases

AI applications receive user-generated text, so prompts can have many unusual cases.

Examples:

    ""
    
    " "
    
    "Hello"
    
    Very long prompt
    
    Repeated text
    
    Unexpected characters
    
    Extremely large input

A basic validation example:

    prompt = " "


    # Remove leading and trailing whitespace.
    cleaned_prompt = prompt.strip()


    # Check whether anything remains.
    if not cleaned_prompt:

        print(
            "Cannot process an empty prompt."
        )

    else:

        print(
            "Processing prompt:",
            cleaned_prompt
        )

Output:

    Cannot process an empty prompt.

---

# 1️⃣1️⃣ Long Input as an Edge Case

AI models often have input limits.

Suppose an application expects a reasonably sized prompt.

A user could provide an extremely large input.

Possible flow:

    User Input
         ↓
    Check Length
         ↓
    Within Limit?
       ↙    ↘
     Yes     No
      ↓       ↓
    Process  Reject /
             Truncate /
             Summarize

Example:

    prompt = input(
        "Enter your prompt: "
    )


    max_length = 1000


    if len(prompt) > max_length:

        print(
            "Prompt is too long. "
            "Maximum length is 1000 characters."
        )

    else:

        print(
            "Prompt accepted."
        )

The exact limit should be determined by the application's requirements.

---

# 1️⃣2️⃣ Numeric Edge Cases

Numbers have many possible edge cases.

For example:

    age = -5

A person's age cannot normally be negative.

Another example:

    quantity = 0

Whether this is valid depends on the application.

For an order system:

    quantity = 0

may be invalid.

For another calculation:

    0

may be completely valid.

Therefore, edge-case handling must be based on the program's actual requirements.

---

# 1️⃣3️⃣ Division Edge Case

Consider:

    def divide(a, b):

        return a / b

The edge case is:

    b = 0

A safer version:

    def divide(a, b):

        if b == 0:

            return None

        return a / b


    result = divide(10, 0)


    if result is None:

        print(
            "Division cannot be performed."
        )

    else:

        print(
            "Result:",
            result
        )

This prevents the operation from crashing.

---

# 1️⃣4️⃣ Empty Dictionary Edge Case

Consider:

    user = {}

Trying to access a required key directly:

    print(user["name"])

can raise:

    KeyError

A safer approach is:

    user = {}


    name = user.get("name")


    if name is None:

        print(
            "Name is not available."
        )

    else:

        print(
            "Name:",
            name
        )

The `.get()` method can be useful when a key may not exist.

---

# 1️⃣5️⃣ Missing Data in AI Applications

AI applications frequently work with incomplete data.

For example:

    {
        "question": "What is AI?"
    }

The application may expect:

    question
    user_id
    model
    temperature

But some fields may be missing.

A structured validation system such as Pydantic can help detect these cases.

Example:

    from pydantic import BaseModel


    class ChatRequest(BaseModel):

        question: str
        temperature: float = 0.7

Here:

    question

is required.

While:

    temperature

has a default value.

This provides a structured way of handling missing data.

---

# 1️⃣6️⃣ None as an Edge Case

`None` represents the absence of a value.

Example:

    response = None


    if response is None:

        print(
            "No response was received."
        )

Always distinguish:

    None

from:

    0

and:

    ""

and:

    False

They represent different concepts.

Example:

    value = None

    if value is None:
        print("No value available.")

Using:

    if value is None

is generally clearer when specifically checking for `None`.

---

# 1️⃣7️⃣ List Index Edge Case

Consider:

    numbers = [10, 20, 30]

    print(numbers[5])

Index `5` does not exist.

Python raises:

    IndexError

A safer approach can be:

    numbers = [10, 20, 30]

    index = 5


    if 0 <= index < len(numbers):

        print(
            numbers[index]
        )

    else:

        print(
            "Invalid list index."
        )

This explicitly checks the boundary.

---

# 1️⃣8️⃣ File-Related Edge Cases

File operations can have many edge cases.

Examples:

- File does not exist
- File is empty
- File contains invalid data
- File is too large
- File has unexpected encoding
- Permission is denied
- Required data is missing

Example:

    try:

        with open(
            "data.txt",
            "r"
        ) as file:

            content = file.read()


        if not content.strip():

            print(
                "The file is empty."
            )

        else:

            print(
                "File loaded successfully."
            )

    except FileNotFoundError:

        print(
            "The requested file was not found."
        )

Here both an exception and an edge case are handled.

---

# 1️⃣9️⃣ API Response Edge Cases

An API may not always return the expected response.

Expected:

    {
        "status": "success",
        "data": "..."
    }

Possible edge cases:

    {}
    
    {"status": "error"}
    
    {"status": "success"}
    
    Missing "data"
    
    Unexpected data type

A robust application should validate external data before using it.

Example:

    response = {
        "status": "success"
    }


    if "data" not in response:

        print(
            "API response does not contain data."
        )

    else:

        print(
            "Data:",
            response["data"]
        )

---

# 2️⃣0️⃣ Edge Cases in RAG Systems

A RAG system can encounter:

- Empty query
- Very long query
- No retrieved documents
- Irrelevant retrieved documents
- Duplicate documents
- Empty document
- Missing metadata
- Vector database failure
- Embedding failure
- LLM timeout

Example:

    query = "Python"


    retrieved_documents = []


    if not retrieved_documents:

        print(
            "No relevant documents were found."
        )

    else:

        print(
            "Retrieved documents:",
            len(retrieved_documents)
        )

The system should define what to do when retrieval returns nothing.

---

# 2️⃣1️⃣ Edge Cases in AI Agents

AI agents may encounter:

    User Request
         ↓
    Tool Selection
         ↓
    Tool Execution
         ↓
    Unexpected Result

Possible edge cases:

- Tool returns no result
- Tool returns invalid data
- Tool times out
- Tool is unavailable
- Tool returns duplicate information
- Tool requires missing parameters
- Agent receives an empty result
- Agent exceeds a step limit

A production agent should have limits and validation around these situations.

---

# 2️⃣2️⃣ Edge Case Testing

Testing should include more than normal inputs.

For example, for:

    divide(a, b)

test:

    divide(10, 2)
    divide(10, 1)
    divide(10, 0)
    divide(0, 10)
    divide(-10, 2)

The purpose is to discover behavior at unusual or boundary conditions.

---

# 2️⃣3️⃣ Normal Case + Edge Case Testing

| Test Type | Example |
|---|---|
| Normal case | `divide(10, 2)` |
| Boundary case | `divide(10, 1)` |
| Zero case | `divide(0, 10)` |
| Error case | `divide(10, 0)` |
| Negative case | `divide(-10, 2)` |
| Large input | Very large number |
| Missing input | `None` |

Good testing considers different categories of behavior.

---

# 2️⃣4️⃣ Edge Cases and Defensive Programming

Defensive programming and edge-case handling are closely related.

    Defensive Programming
            ↓
    Anticipate Problems
            ↓
    Identify Edge Cases
            ↓
    Validate Input
            ↓
    Handle Unexpected Situations
            ↓
    Produce Safe Behavior

The goal is to make the program behave predictably.

---

# 2️⃣5️⃣ Edge Case Checklist

Before considering a function reliable, ask:

    ✓ What happens with normal input?

    ✓ What happens with empty input?

    ✓ What happens with None?

    ✓ What happens with zero?

    ✓ What happens with negative values?

    ✓ What happens at the minimum boundary?

    ✓ What happens at the maximum boundary?

    ✓ What happens with extremely large input?

    ✓ What happens with invalid types?

    ✓ What happens when required data is missing?

    ✓ What happens when an external service fails?

    ✓ What happens when a file is empty?

    ✓ What happens when an API response is incomplete?

    ✓ What happens when a database returns no data?

---

# 🤖 AI Engineer Relevance

Edge-case handling is extremely important in AI Engineering because AI applications often process unpredictable real-world data.

Common areas include:

### LLM Applications

    Empty prompts
    Huge prompts
    Invalid parameters
    Model limits

### RAG

    No documents
    Missing metadata
    Duplicate documents
    Poor retrieval

### AI Agents

    Tool failures
    Missing parameters
    Empty results
    Infinite loops

### AI APIs

    Invalid requests
    Missing fields
    Timeouts
    Unexpected responses

### Data Processing

    Empty datasets
    Missing values
    Wrong data types
    Outliers
    Duplicate records

---

# 🧠 Key Takeaways

- An edge case is an unusual or boundary situation that a program must handle correctly.
- Edge cases are not necessarily errors.
- Some edge cases are valid inputs.
- Empty collections are common edge cases.
- `None`, `0`, empty strings, and empty collections have different meanings.
- Boundary values should be tested carefully.
- User input should be validated before processing.
- External API responses should not be trusted blindly.
- AI systems must handle empty, incomplete, large, and unexpected data.
- RAG systems should define behavior when no relevant documents are retrieved.
- AI agents should handle tool failures and unexpected tool results.
- Testing should include normal cases, boundary cases, invalid cases, and unusual cases.
- Defensive programming helps identify and safely handle edge cases.
- Good edge-case handling makes applications more robust and predictable.

# 1️⃣7️⃣ Clean & Maintainable Code

## 📖 Definition

> **Clean and maintainable code is code that is easy to read, understand, modify, test, debug, and reuse.**

Writing code that simply works is not always enough.

A program can produce the correct output and still be difficult to maintain.

For example:

    x = 10
    y = 20
    z = x + y

This code works, but the purpose of `x`, `y`, and `z` is unclear.

A clearer version is:

    first_number = 10
    second_number = 20
    total = first_number + second_number

The second version communicates the intention more clearly.

---

# 17.1️⃣ Why Clean Code Matters

As projects become larger, code becomes harder to manage.

A small program may contain:

    50 lines

A real AI application may contain:

    Thousands of lines
         ↓
    Multiple files
         ↓
    Multiple modules
         ↓
    APIs
         ↓
    Databases
         ↓
    Models
         ↓
    Tests

If the code is poorly organized, changing one part can become difficult.

Clean code helps developers:

- Understand the code quickly
- Find bugs
- Add new features
- Modify existing functionality
- Reuse functions
- Write tests
- Work with other developers
- Maintain production systems

---

# 17.2️⃣ Characteristics of Clean Code

Clean code generally has:

- Meaningful names
- Small and focused functions
- Clear structure
- Consistent formatting
- Minimal unnecessary complexity
- Useful comments
- Proper error handling
- Reusable components
- Clear responsibilities
- Good testability

---

# 17.3️⃣ Meaningful Variable Names

Poor:

    x = 500
    y = 0.7
    z = "Python"

Better:

    max_tokens = 500
    temperature = 0.7
    language = "Python"

The second version makes the purpose of each variable obvious.

---

# 17.4️⃣ Meaningful Function Names

Poor:

    def process(data):
        ...

The name `process()` is too generic.

Better:

    def calculate_average(marks):
        ...

or:

    def validate_chat_request(request):
        ...

A function name should communicate what the function does.

---

# 17.5️⃣ Meaningful Class Names

Poor:

    class Data:
        ...

Better:

    class ChatRequest:
        ...

or:

    class DocumentRetriever:
        ...

or:

    class AIResponse:
        ...

Class names should normally describe the object or responsibility represented by the class.

---

# 17.6️⃣ Functions Should Have a Clear Responsibility

A function should ideally perform one clearly defined task.

Poor design:

    def process_student():
        # Take input
        # Validate input
        # Calculate marks
        # Save file
        # Send email
        # Print result

This function is doing many unrelated tasks.

A cleaner design can separate responsibilities:

    def get_student_data():
        ...


    def validate_student_data(data):
        ...


    def calculate_result(marks):
        ...


    def save_student_data(data):
        ...


    def send_notification(data):
        ...

Now each function has a more focused responsibility.

---

# 17.7️⃣ Example: Refactoring a Function

### Less Maintainable

    def calculate(marks):

        total = sum(marks)
        avg = total / len(marks)

        print("Total:", total)
        print("Average:", avg)

        return avg

The function calculates data and also handles output.

### More Focused

    def calculate_average(marks):

        return sum(marks) / len(marks)


    marks = [80, 90, 70]

    average = calculate_average(marks)

    print(
        "Average:",
        average
    )

The calculation logic is separated from displaying the result.

This also makes testing easier.

---

# 17.8️⃣ Avoid Repeated Code

Repeated code can make maintenance difficult.

Example:

    temperature = 1.5

    if temperature < 0 or temperature > 2:
        print("Invalid temperature.")


    another_temperature = 3

    if another_temperature < 0 or another_temperature > 2:
        print("Invalid temperature.")

The same validation logic is repeated.

A reusable function is better:

    def validate_temperature(temperature):

        if temperature < 0 or temperature > 2:

            return False

        return True


    temperature = 1.5

    if validate_temperature(temperature):

        print("Temperature is valid.")


    another_temperature = 3

    if validate_temperature(another_temperature):

        print("Temperature is valid.")

This reduces duplication.

---

# 17.9️⃣ DRY Principle

## 📖 Definition

> **DRY stands for "Don't Repeat Yourself."**

The principle encourages developers to avoid unnecessary duplication of logic.

Instead of:

    Same logic
    Same logic
    Same logic

Prefer:

    Reusable function
          ↓
    Call whenever required

However, DRY should not be taken to an extreme.

Sometimes a small amount of repetition can be clearer than creating an unnecessarily complicated abstraction.

---

# 🔟 Comments in Clean Code

Comments should explain things that are not immediately obvious.

Good comment:

    # Convert the temperature from Celsius to Fahrenheit.
    fahrenheit = (celsius * 9 / 5) + 32

Bad comment:

    # Add two numbers.
    result = a + b

The second comment simply repeats what the code already clearly shows.

---

# 10.1️⃣ When Comments Are Useful

Comments can explain:

- Why something is done
- Important business rules
- Complex algorithms
- Non-obvious decisions
- External limitations
- Temporary workarounds

Example:

    # The API requires temperature to remain between 0 and 2.
    temperature = 0.7

The comment provides useful context.

---

# 10.2️⃣ Comments Should Not Replace Good Code

Instead of:

    # Store user's name
    x = name

Prefer:

    user_name = name

The variable name itself explains the purpose.

Good code should be understandable without excessive comments.

---

# 1️⃣1️⃣ Consistent Formatting

Consider:

    def add(a,b):
        return a+b


    def subtract(a, b):
        return a - b

The second function is formatted more clearly.

Consistent formatting improves readability.

Python projects commonly follow established style conventions such as:

- Consistent indentation
- Meaningful spacing
- Clear line breaks
- Consistent naming
- Reasonable line lengths

---

# 1️⃣2️⃣ Naming Conventions in Python

Common Python conventions include:

### Variables and Functions

Use `snake_case`.

    user_name = "Sonal"

    def calculate_average():
        ...


### Classes

Use `PascalCase`.

    class ChatRequest:
        ...


### Constants

Often use uppercase with underscores.

    MAX_TOKENS = 4096

    DEFAULT_TEMPERATURE = 0.7

Following consistent naming conventions makes projects easier to understand.

---

# 1️⃣3️⃣ Avoid Unnecessary Complexity

Compare:

    if is_valid == True:
        print("Valid")

with:

    if is_valid:
        print("Valid")

The second version is simpler.

Another example:

    if not user:
        print("User not found.")

is easier to understand than unnecessarily complicated conditions.

The goal is not to make code clever.

The goal is to make code understandable.

---

# 1️⃣4️⃣ Readability Over Cleverness

A developer may write highly compressed code:

    result = [x * 2 for x in numbers if x > 5]

This is valid Python.

But if the logic becomes complicated, multiple simple steps may be easier to understand.

Clean code prioritizes:

    Readability
         ↓
    Maintainability
         ↓
    Correctness
         ↓
    Performance where needed

Performance still matters, but unnecessary complexity should be avoided.

---

# 1️⃣5️⃣ Avoid Giant Functions

A very large function may contain:

    Input handling
    Validation
    Database operations
    API calls
    Model inference
    Logging
    Error handling
    Output formatting

This makes the function difficult to understand and test.

Instead, divide responsibilities:

    main()
       ↓
    validate_request()
       ↓
    retrieve_data()
       ↓
    generate_response()
       ↓
    format_response()

This creates a clearer structure.

---

# 1️⃣6️⃣ Modular Code

## 📖 Definition

> **Modular code is code divided into separate, focused components that can be developed, tested, and maintained independently.**

Instead of one huge Python file:

    main.py
        ↓
    Everything

A project can be organized as:

    project/
    │
    ├── main.py
    ├── config.py
    ├── validation.py
    ├── models.py
    ├── services.py
    ├── utils.py
    └── tests/

The exact structure depends on the project.

---

# 1️⃣7️⃣ AI Project Example

A simple AI application might be organized as:

    ai_app/
    │
    ├── main.py
    │
    ├── config.py
    │
    ├── models.py
    │
    ├── validation.py
    │
    ├── llm_service.py
    │
    ├── retrieval.py
    │
    ├── logging_config.py
    │
    └── tests/
        ├── test_validation.py
        └── test_retrieval.py

Possible responsibilities:

| File | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `config.py` | Configuration |
| `models.py` | Data models |
| `validation.py` | Input validation |
| `llm_service.py` | LLM-related operations |
| `retrieval.py` | Document retrieval |
| `logging_config.py` | Logging setup |
| `tests/` | Automated tests |

This is an example structure, not a mandatory structure for every project.

---

# 1️⃣8️⃣ Separation of Concerns

## 📖 Definition

> **Separation of concerns means dividing a program into components where each component is responsible for a distinct part of the application.**

For example:

    User Input
        ↓
    Validation
        ↓
    Business Logic
        ↓
    Database / API
        ↓
    Response

Instead of putting all of these responsibilities into one function, separate them.

---

# 1️⃣9️⃣ AI Example of Separation of Concerns

A RAG application might separate:

    Query Validation
          ↓
    Embedding Generation
          ↓
    Vector Retrieval
          ↓
    Context Preparation
          ↓
    Prompt Construction
          ↓
    LLM Generation
          ↓
    Response Processing

Each component can have its own function or module.

This makes the system easier to modify.

For example, changing the vector database should ideally require changes mainly in the retrieval component rather than throughout the entire application.

---

# 2️⃣0️⃣ Avoid Hard-Coded Configuration

Poor:

    temperature = 0.7
    max_tokens = 4096

If these values are used throughout the project, changing them becomes difficult.

A configuration system can centralize them:

    DEFAULT_TEMPERATURE = 0.7
    MAX_TOKENS = 4096

For production applications, configuration may come from environment variables or configuration files.

This connects clean code with the configuration-handling concepts from this chapter.

---

# 2️⃣1️⃣ Error Handling in Clean Code

Error handling should also be organized.

Poor:

    try:
        ...
    except:
        print("Error")

Problems:

- Catches everything
- Hides the actual problem
- Makes debugging difficult
- Provides little information

Better:

    try:

        result = divide(10, 0)

    except ZeroDivisionError as e:

        print(
            "Division failed:",
            e
        )

Catch the exceptions that you actually expect to handle.

---

# 2️⃣2️⃣ Clean Code and Type Hints

Type hints improve readability.

Without type hints:

    def calculate_average(marks):
        return sum(marks) / len(marks)

With type hints:

    def calculate_average(
        marks: list[int]
    ) -> float:

        return sum(marks) / len(marks)

The second version communicates:

    marks → list of integers
    return value → float

This can make larger projects easier to understand.

---

# 2️⃣3️⃣ Clean Code and Pydantic

Pydantic models can make data structures explicit.

Example:

    from pydantic import BaseModel


    class ChatRequest(BaseModel):

        prompt: str

        max_tokens: int = 200

        temperature: float = 0.7

Now developers can immediately see the expected structure of a chat request.

This is especially useful in AI APIs.

---

# 2️⃣4️⃣ Clean Code and Testing

Clean code is easier to test.

For example:

    def calculate_average(marks):

        return sum(marks) / len(marks)

This function has a clear input and output.

It can easily be tested:

    def test_calculate_average():

        assert calculate_average(
            [10, 20, 30]
        ) == 20

A large function containing many unrelated operations would be harder to test.

---

# 2️⃣5️⃣ Clean Code and Reusability

Reusable functions reduce duplication.

Example:

    def validate_temperature(
        temperature: float
    ) -> bool:

        return 0 <= temperature <= 2

The same function can be used by:

- Chat API
- RAG application
- AI agent
- Testing code
- Configuration validation

Instead of rewriting the same logic.

---

# 2️⃣6️⃣ Practical Example

Consider:

    marks = [80, 90, 70]


    def calculate_average(marks):

        return sum(marks) / len(marks)


    average = calculate_average(marks)


    print(
        "Average:",
        average
    )

Output:

    Average: 80.0

This example demonstrates:

- Meaningful variable name
- Meaningful function name
- Single responsibility
- Reusable function
- Simple structure
- Easy testing

---

# 2️⃣7️⃣ Improving the Example with Type Hints

A slightly more explicit version:

    marks: list[int] = [80, 90, 70]


    def calculate_average(
        marks: list[int]
    ) -> float:

        return sum(marks) / len(marks)


    average = calculate_average(marks)


    print(
        "Average:",
        average
    )

The type hints communicate the expected data types.

---

# 2️⃣8️⃣ Improving the Example with Edge-Case Handling

The previous function has one important edge case:

    marks = []

A safer version:

    def calculate_average(
        marks: list[int]
    ) -> float:

        if not marks:

            raise ValueError(
                "Marks list cannot be empty."
            )

        return sum(marks) / len(marks)


    marks = [80, 90, 70]

    average = calculate_average(marks)

    print(
        "Average:",
        average
    )

Now the function handles an invalid state explicitly.

This demonstrates how multiple Chapter 15 concepts can work together:

    Type Hints
         +
    Edge Cases
         +
    Proper Error Messages
         +
    Clean Code

---

# 2️⃣9️⃣ Clean Code and Documentation

Documentation explains how a component should be used.

For reusable functions, a docstring can be useful.

Example:

    def calculate_average(
        marks: list[int]
    ) -> float:
        """
        Calculate the average of a list of marks.
        """

        if not marks:

            raise ValueError(
                "Marks list cannot be empty."
            )

        return sum(marks) / len(marks)

A docstring is especially useful when:

- A function is reused
- A module is shared
- The behavior is not obvious
- The function has important constraints

---

# 3️⃣0️⃣ Avoid Over-Engineering

Clean code does not mean creating dozens of files and classes for a tiny program.

For example, this is unnecessary for a simple calculation:

    calculator/
        core/
            services/
                calculation/
                    arithmetic/
                        addition.py

A simple function may be enough:

    def add(a, b):
        return a + b

The goal is appropriate structure, not maximum structure.

---

# 3️⃣1️⃣ Simplicity vs Complexity

| Simple Approach | Over-Complicated Approach |
|---|---|
| Easy to understand | Hard to understand |
| Easy to test | Difficult to test |
| Fewer dependencies | Many unnecessary dependencies |
| Easy to modify | Difficult to modify |
| Clear responsibility | Too many abstractions |

Use the simplest design that properly solves the problem.

---

# 3️⃣2️⃣ Maintainability

## 📖 Definition

> **Maintainability is the ease with which software can be understood, modified, fixed, tested, and extended over time.**

Imagine you build an AI project today.

Six months later, you need to:

- Change the model
- Change the API
- Add authentication
- Replace the vector database
- Add logging
- Add tests

If the code is well structured, these changes are easier.

If everything is written inside one giant file, changes become much harder.

---

# 3️⃣3️⃣ Clean Code Review Checklist

Before considering code complete, ask:

    ✓ Are variable names meaningful?

    ✓ Are function names descriptive?

    ✓ Does each function have a clear responsibility?

    ✓ Is unnecessary repetition avoided?

    ✓ Are comments useful?

    ✓ Is the code formatted consistently?

    ✓ Are edge cases handled?

    ✓ Are errors handled properly?

    ✓ Are sensitive values kept out of source code?

    ✓ Is the code easy to test?

    ✓ Can another developer understand it?

    ✓ Can the code be modified without breaking unrelated components?

---

# 3️⃣4️⃣ AI Engineer Practical Structure

A small AI application could eventually evolve into:

    ai_project/
    │
    ├── main.py
    │
    ├── config.py
    │
    ├── models.py
    │
    ├── validation.py
    │
    ├── services/
    │   ├── llm_service.py
    │   ├── embedding_service.py
    │   └── retrieval_service.py
    │
    ├── utils/
    │   └── logging_utils.py
    │
    └── tests/
        ├── test_validation.py
        ├── test_llm_service.py
        └── test_retrieval.py

This kind of organization can help separate responsibilities as an AI project grows.

The exact structure should be adapted to the project's size and requirements.

---

# 🤖 AI Engineer Relevance

Clean and maintainable code is especially important in AI Engineering because AI applications often combine many components:

    Python
      ↓
    Data Processing
      ↓
    APIs
      ↓
    Embeddings
      ↓
    Vector Database
      ↓
    LLM
      ↓
    RAG
      ↓
    Agents
      ↓
    Deployment

If everything is tightly coupled, maintaining the system becomes difficult.

Clean architecture helps developers:

- Replace models
- Add new AI providers
- Change retrieval systems
- Add validation
- Add tests
- Debug API failures
- Improve reliability
- Scale applications
- Collaborate with other developers

---

# 🔄 Important Concepts Together

Chapter 15 concepts can work together:

    Type Hints
         ↓
    Clear Data Expectations
         ↓
    Pydantic
         ↓
    Runtime Validation
         ↓
    Exception Handling
         ↓
    Logging
         ↓
    Retry / Timeout
         ↓
    Graceful Failure
         ↓
    Edge-Case Handling
         ↓
    Clean Code
         ↓
    Maintainable AI Application

These concepts are not isolated.

They support each other when building reliable Python and AI systems.

---

# 🧠 Key Takeaways

- Clean code is easy to read, understand, test, and modify.
- Meaningful names make code easier to understand.
- Functions should have clear responsibilities.
- Avoid unnecessary duplication.
- DRY means "Don't Repeat Yourself."
- Comments should explain useful context rather than obvious code.
- Consistent formatting improves readability.
- Python commonly uses `snake_case` for variables and functions and `PascalCase` for classes.
- Modular code separates an application into focused components.
- Separation of concerns keeps different responsibilities independent.
- Type hints improve code clarity.
- Pydantic can make data structures explicit and validated.
- Clean code is easier to test.
- Avoid unnecessary complexity and over-engineering.
- Maintainability becomes increasingly important as projects grow.
- AI applications benefit from clean architecture because they combine APIs, models, databases, retrieval systems, and other components.

# 1️⃣8️⃣ Testing Fundamentals

## 📖 Definition

> **Testing is the process of checking whether a program behaves correctly under expected and unexpected conditions.**

Testing helps us determine whether:

- The program produces the expected output
- Functions behave correctly
- Invalid inputs are handled properly
- Edge cases are handled
- Errors are detected
- Changes have not broken existing functionality

Testing is especially important in AI Engineering because AI applications often contain many interconnected components.

---

# 18.1️⃣ Why Testing Is Important

Consider a simple function:

    def add(a, b):
        return a + b

We expect:

    add(2, 3)

to return:

    5

Testing verifies this expectation.

Without testing, a bug can remain unnoticed until the application is used.

With testing:

    Code
      ↓
    Test
      ↓
    Expected Result
      ↓
    Compare
      ↓
    Pass / Fail

---

# 18.2️⃣ Testing vs Debugging

These concepts are related but different.

### Testing

Testing checks whether the program behaves correctly.

    Input
      ↓
    Program
      ↓
    Output
      ↓
    Compare with Expected Output

### Debugging

Debugging is the process of finding and fixing the cause of a problem.

    Test Fails
        ↓
    Investigate
        ↓
    Find Bug
        ↓
    Fix Bug
        ↓
    Test Again

Therefore:

    Testing → Detects problems

    Debugging → Finds and fixes problems

---

# 18.3️⃣ Simple Manual Test

Consider:

    def add(a, b):

        return a + b


    result = add(2, 3)


    if result == 5:

        print("Test passed.")

    else:

        print("Test failed.")

Output:

    Test passed.

Here:

    Expected result = 5

    Actual result = 5

Therefore:

    Test passed.

---

# 18.4️⃣ What Happens When the Code Contains a Bug?

Suppose the function is incorrectly written:

    def multiply(a, b):

        return a + b

Now:

    result = multiply(5, 4)

The actual result is:

    9

But the expected result is:

    20

A test can detect the problem:

    if result == 20:

        print("Test passed.")

    else:

        print("Test failed.")

Output:

    Test failed.

The test has successfully identified that the implementation does not behave as expected.

---

# 18.5️⃣ Expected vs Actual Result

Testing commonly involves comparing two values.

    Expected Result
          ↓
        20

    Actual Result
          ↓
         20

Comparison:

    20 == 20

Result:

    Test Passed

If:

    Expected = 20

    Actual = 15

Then:

    20 != 15

Result:

    Test Failed

---

# 18.6️⃣ Test Cases

## 📖 Definition

> **A test case is a specific input, condition, or scenario used to verify a particular behavior of a program.**

For:

    def add(a, b):
        return a + b

Possible test cases:

    add(2, 3)
    add(0, 0)
    add(-2, -3)
    add(10, 0)

Each test checks a different situation.

---

# 18.7️⃣ Normal Test Cases

A normal test checks expected input.

Example:

    def add(a, b):

        return a + b


    result = add(2, 3)

    assert result == 5

This checks normal behavior.

---

# 18.8️⃣ Edge-Case Testing

Testing should also include edge cases.

For example:

    def divide(a, b):

        return a / b

Possible tests:

    divide(10, 2)
    divide(0, 10)
    divide(-10, 2)
    divide(10, 0)

The last case checks division by zero.

Testing should not focus only on ideal input.

---

# 18.9️⃣ Invalid Input Testing

Suppose a function accepts a temperature between `0` and `2`.

Possible tests:

    0
    0.7
    2
    -1
    3

Here:

    0       → Boundary value
    0.7     → Normal value
    2       → Boundary value
    -1      → Invalid
    3       → Invalid

This verifies both valid and invalid behavior.

---

# 🔟 Assertions

## 📖 Definition

> **An assertion is a statement used to check whether a condition is true. If the condition is false, Python raises an `AssertionError`.**

Example:

    result = 2 + 3

    assert result == 5

If the condition is true:

    result == 5

the program continues.

If the condition is false:

    assert result == 10

Python raises:

    AssertionError

---

# 10.1️⃣ Assertions in Testing

Assertions are commonly used to express expected behavior.

Example:

    def add(a, b):

        return a + b


    assert add(2, 3) == 5

This means:

    "I expect add(2, 3) to return 5."

If the function returns `5`, the assertion passes.

If it returns another value, the assertion fails.

---

# 10.2️⃣ Multiple Assertions

A function can have multiple tests.

    def add(a, b):

        return a + b


    assert add(2, 3) == 5

    assert add(0, 0) == 0

    assert add(-2, -3) == -5

These test different inputs.

If all assertions pass, the program finishes without an `AssertionError`.

---

# 10.3️⃣ Assertion with a Message

You can provide a message:

    result = 2 + 3

    assert result == 5, "Addition result is incorrect."

If the assertion fails, the message helps explain the problem.

---

# 10.4️⃣ Assertions vs `if`

An `if` statement is commonly used for normal program logic.

Example:

    if temperature > 2:

        print(
            "Invalid temperature."
        )

An assertion is commonly used to check an assumption:

    assert temperature <= 2

These have different purposes.

For user input validation, normal validation logic or explicit exceptions are generally more appropriate than relying on `assert`.

---

# 10.5️⃣ Unit Testing

## 📖 Definition

> **Unit testing is the practice of testing individual units of code, such as functions or methods, independently to verify that they work correctly.**

A unit is usually a small, logically independent part of a program.

For example:

    Application
        ↓
    ┌───────────────┐
    │ validate()    │
    ├───────────────┤
    │ calculate()   │
    ├───────────────┤
    │ format()      │
    └───────────────┘

Each function can be tested separately.

---

# 10.6️⃣ Real-Life Analogy

Imagine a car.

Instead of testing only the entire car at once, you can separately check:

    Engine
    Brakes
    Lights
    Steering
    Seat belts

Similarly, software can test individual components.

    AI Application
         ↓
    ┌──────────────────┐
    │ Input Validation  │
    ├──────────────────┤
    │ Retrieval         │
    ├──────────────────┤
    │ API Call          │
    ├──────────────────┤
    │ Response Format   │
    └──────────────────┘

Each component can have its own tests.

---

# 10.7️⃣ Basic Unit Test

Consider:

    def add(a, b):

        return a + b


    def test_add():

        assert add(2, 3) == 5

The function:

    test_add()

checks one specific behavior.

The test passes if:

    add(2, 3)

returns:

    5

---

# 10.8️⃣ Multiple Unit Tests

    def add(a, b):

        return a + b


    def test_positive_numbers():

        assert add(2, 3) == 5


    def test_negative_numbers():

        assert add(-2, -3) == -5


    def test_zero():

        assert add(0, 0) == 0

Now the same function is tested under multiple conditions.

---

# 10.9️⃣ Python's `unittest`

## 📖 Definition

> **`unittest` is Python's built-in unit testing framework used to create, organize, and run automated tests for individual parts of a program.**

It is included with Python, so no separate installation is required.

Basic structure:

    import unittest


    def add(a, b):

        return a + b


    class TestAddFunction(unittest.TestCase):

        def test_add(self):

            self.assertEqual(
                add(2, 3),
                5
            )


    if __name__ == "__main__":

        unittest.main()

---

# 11.0️⃣ `unittest.TestCase`

A test class usually inherits from:

    unittest.TestCase

Example:

    class TestAddFunction(
        unittest.TestCase
    ):

        ...

This provides testing features and assertion methods.

---

# 11.1️⃣ Test Method Naming

Test methods should normally begin with:

    test_

Example:

    def test_add(self):

        ...

`unittest` uses this naming convention to discover test methods automatically.

---

# 11.2️⃣ `assertEqual()`

## 📖 Definition

> **`assertEqual()` checks whether two values are equal.**

Example:

    self.assertEqual(
        add(2, 3),
        5
    )

This checks:

    Actual result == Expected result

If both are equal, the test passes.

---

# 11.3️⃣ Multiple `unittest` Tests

    import unittest


    def add(a, b):

        return a + b


    class TestAddFunction(
        unittest.TestCase
    ):

        def test_positive_numbers(self):

            self.assertEqual(
                add(2, 3),
                5
            )


        def test_negative_numbers(self):

            self.assertEqual(
                add(-2, -3),
                -5
            )


        def test_zero(self):

            self.assertEqual(
                add(0, 0),
                0
            )


    if __name__ == "__main__":

        unittest.main()

This creates three separate test cases.

---

# 11.4️⃣ Common `unittest` Assertions

| Assertion | Purpose |
|---|---|
| `assertEqual(a, b)` | Checks `a == b` |
| `assertNotEqual(a, b)` | Checks `a != b` |
| `assertTrue(x)` | Checks whether `x` is true |
| `assertFalse(x)` | Checks whether `x` is false |
| `assertIsNone(x)` | Checks whether `x is None` |
| `assertIsNotNone(x)` | Checks whether `x is not None` |
| `assertIn(a, b)` | Checks whether `a` is inside `b` |
| `assertNotIn(a, b)` | Checks whether `a` is not inside `b` |
| `assertRaises(...)` | Checks whether an expected exception is raised |

---

# 11.5️⃣ Testing Exceptions

Testing should also verify that errors are raised when expected.

Example:

    import unittest


    def divide(a, b):

        return a / b


    class TestDivideFunction(
        unittest.TestCase
    ):

        def test_divide_by_zero(self):

            with self.assertRaises(
                ZeroDivisionError
            ):

                divide(10, 0)


    if __name__ == "__main__":

        unittest.main()

This test checks that:

    divide(10, 0)

raises:

    ZeroDivisionError

---

# 11.6️⃣ Why Test Exceptions?

Suppose a function is expected to reject invalid input.

For example:

    def validate_temperature(
        temperature
    ):

        if temperature < 0 or temperature > 2:

            raise ValueError(
                "Temperature must be between 0 and 2."
            )

A test can verify this behavior:

    import unittest


    class TestTemperature(
        unittest.TestCase
    ):

        def test_invalid_temperature(self):

            with self.assertRaises(
                ValueError
            ):

                validate_temperature(5)

This confirms that invalid input is handled as expected.

---

# 11.7️⃣ `if __name__ == "__main__"`

In a `unittest` file, you will often see:

    if __name__ == "__main__":

        unittest.main()

This means the test runner is executed when the file is run directly.

For example:

    python test_example.py

will execute:

    unittest.main()

The condition also prevents the test runner from automatically executing when the file is imported by another module.

---

# 11.8️⃣ What Is Automated Testing?

Manual testing:

    Run Program
       ↓
    Enter Input
       ↓
    Check Output
       ↓
    Repeat Manually

Automated testing:

    Write Tests
       ↓
    Run Test Suite
       ↓
    All Tests Execute
       ↓
    Pass / Fail Results

Automated tests save time when a project becomes larger.

---

# 11.9️⃣ Test Suite

## 📖 Definition

> **A test suite is a collection of tests that are executed together.**

For example:

    Test Validation
    Test API Request
    Test Retrieval
    Test Response
    Test Error Handling

Together:

    Test Suite

A test suite can contain many test cases.

---

# 1️⃣2️⃣ Test Isolation

Unit tests should ideally test one component independently.

For example:

    test_calculate_average()

should primarily test the calculation logic.

It should not unnecessarily depend on:

    Database
    Network
    External API
    LLM

If the calculation function depends on all of these components, the test becomes harder to control.

---

# 1️⃣2️⃣1️⃣ Deterministic vs Non-Deterministic Testing

A deterministic function produces predictable output for the same input.

Example:

    def add(a, b):

        return a + b

For:

    add(2, 3)

the result should always be:

    5

This is easy to test.

AI systems can be more complicated because model outputs may vary.

For example:

    User Prompt
         ↓
       LLM
         ↓
    Generated Text

The exact response may not always be identical.

Therefore, AI testing often focuses on properties and expected behavior rather than exact text matching.

---

# 1️⃣2️⃣2️⃣ Testing AI Components

AI applications can still have many deterministic components.

For example:

- Input validation
- Data preprocessing
- Text cleaning
- Chunking
- Metadata handling
- Database operations
- API request construction
- Response parsing
- Token-limit validation

These components can be tested with normal unit tests.

---

# 1️⃣2️⃣3️⃣ Testing a RAG Pipeline

A simplified RAG system:

    User Query
        ↓
    Validation
        ↓
    Embedding
        ↓
    Retrieval
        ↓
    Context
        ↓
    Prompt
        ↓
    LLM
        ↓
    Response

Possible unit tests:

    Test query validation

    Test document chunking

    Test metadata extraction

    Test retrieval formatting

    Test prompt construction

    Test response parsing

Each component can be tested independently.

---

# 1️⃣2️⃣4️⃣ Testing API Request Validation

Suppose:

    class ChatRequest(BaseModel):

        prompt: str
        max_tokens: int = 200
        temperature: float = 0.7

Tests can verify:

    Valid prompt
    Empty prompt
    Valid temperature
    Invalid temperature
    Valid token count
    Excessive token count

This combines:

    Pydantic
       +
    Validation
       +
    Unit Testing

---

# 1️⃣2️⃣5️⃣ Testing Edge Cases

Testing should include the edge cases discussed earlier.

For example:

    Empty list
    Empty string
    None
    Zero
    Negative number
    Boundary values
    Very large input
    Missing data

Example:

    def calculate_average(
        numbers
    ):

        if not numbers:

            raise ValueError(
                "List cannot be empty."
            )

        return sum(numbers) / len(numbers)

Tests can include:

    calculate_average(
        [10, 20, 30]
    )

and:

    calculate_average([])

The first tests normal behavior.

The second tests an edge case.

---

# 1️⃣2️⃣6️⃣ Regression Testing

## 📖 Definition

> **Regression testing is the process of checking that existing functionality still works after code changes.**

Example:

    Version 1
       ↓
    Feature works

    Developer changes code
       ↓
    Version 2
       ↓
    Existing feature breaks

Regression tests help detect this.

A test suite can be run after changes:

    Code Change
         ↓
    Run Tests
         ↓
    Existing Tests Pass?
       ↙       ↘
     Yes        No
      ↓          ↓
    Continue   Investigate

---

# 1️⃣2️⃣7️⃣ Why Regression Testing Matters in AI Projects

AI projects change frequently.

For example:

- Model provider changes
- Prompt changes
- Retrieval logic changes
- Database changes
- API changes
- Configuration changes

A change in one component can accidentally affect another component.

Automated tests help detect these regressions.

---

# 1️⃣2️⃣8️⃣ Testing Pyramid

A common testing concept is the testing pyramid:

    ┌───────────────────┐
    │   End-to-End      │
    │      Tests        │
    └───────────────────┘
             ▲
             │
    ┌───────────────────┐
    │  Integration      │
    │      Tests        │
    └───────────────────┘
             ▲
             │
    ┌───────────────────┐
    │    Unit Tests     │
    └───────────────────┘

The general idea is to have many fast, focused tests and fewer expensive end-to-end tests.

---

# 1️⃣2️⃣9️⃣ Unit vs Integration vs End-to-End

| Type | Main Purpose |
|---|---|
| Unit Test | Test one small component |
| Integration Test | Test multiple components working together |
| End-to-End Test | Test the complete application flow |

Example AI application:

### Unit

    validate_prompt()

### Integration

    Retrieval + Database

### End-to-End

    User Query
       ↓
    RAG
       ↓
    LLM
       ↓
    Final Response

Each level provides different information.

---

# 3️⃣0️⃣ Testing Best Practices

### 1. Test important behavior

Focus on behavior that matters to the application.

### 2. Test normal cases

Verify expected functionality.

### 3. Test edge cases

Check unusual and boundary conditions.

### 4. Test invalid input

Verify that incorrect input is handled properly.

### 5. Keep tests focused

A test should ideally verify one specific behavior.

### 6. Use meaningful test names

Example:

    test_invalid_temperature()

is clearer than:

    test_1()

### 7. Keep tests repeatable

A test should ideally produce consistent results.

### 8. Test exceptions

If a function should raise an exception, test that behavior.

### 9. Run tests after changes

This helps detect regressions.

### 10. Avoid unnecessary external dependencies

Unit tests should be as isolated as practical.

---

# 🤖 AI Engineer Relevance

Testing is an essential part of building reliable AI applications.

Important areas include:

    Input Validation
         ↓
    Data Processing
         ↓
    Embeddings
         ↓
    Retrieval
         ↓
    Prompt Construction
         ↓
    API Integration
         ↓
    Model Output
         ↓
    Response Processing

Each layer can introduce bugs.

Testing helps detect these problems before they reach users.

---

# 🧠 Key Takeaways

- Testing checks whether software behaves as expected.
- Testing and debugging are different activities.
- A test case checks a specific behavior or scenario.
- Expected and actual results are commonly compared.
- Assertions can express expected behavior.
- Unit testing focuses on individual functions or methods.
- Python provides the built-in `unittest` framework.
- `unittest.TestCase` provides testing functionality.
- Test methods normally begin with `test_`.
- `assertEqual()` checks whether two values are equal.
- `assertRaises()` checks whether an expected exception occurs.
- Automated tests can execute many test cases consistently.
- Test suites group multiple tests together.
- Edge cases and invalid inputs should be tested.
- Regression testing checks that existing functionality still works after changes.
- AI applications contain many components that can be tested independently.
- RAG systems can test validation, chunking, retrieval, prompt construction, and response processing separately.
- Clean, modular code is easier to test.
- Good testing improves reliability and maintainability of AI applications.

# 1️⃣9️⃣ Unit Testing

## 📖 Definition

> **Unit testing is the practice of testing individual units of code, such as functions or methods, independently to verify that they work correctly.**

A unit is usually a small and logically independent part of a program.

For example:

    Application
         ↓
    ┌────────────────────┐
    │ validate_input()   │
    ├────────────────────┤
    │ calculate_total()  │
    ├────────────────────┤
    │ format_response()  │
    └────────────────────┘

Each function can be tested independently.

---

# 19.1️⃣ Why Unit Testing?

Without unit testing:

    Write Code
       ↓
    Run Application
       ↓
    Something Fails
       ↓
    Find the Problem Manually

With unit testing:

    Write Code
       ↓
    Write Tests
       ↓
    Run Tests
       ↓
    Test Fails
       ↓
    Identify the Problem
       ↓
    Fix the Code
       ↓
    Run Tests Again

Unit testing helps detect problems early.

---

# 19.2️⃣ Unit Testing vs Manual Testing

### Manual Testing

A developer manually checks the program.

    Input
      ↓
    Run Program
      ↓
    Observe Output
      ↓
    Decide Whether It Is Correct

This can become repetitive.

### Unit Testing

The expected behavior is written as a test.

    Test Case
       ↓
    Run Automatically
       ↓
    Pass / Fail

The same test can be executed many times.

---

# 19.3️⃣ Simple Function

Consider:

    def add(a, b):

        return a + b

We can test it manually:

    result = add(2, 3)

    print(result)

Output:

    5

But printing the result does not automatically verify that it is correct.

A test should explicitly check the expected behavior.

---

# 19.4️⃣ Basic Unit Test with `assert`

    def add(a, b):

        return a + b


    def test_add():

        assert add(2, 3) == 5


    test_add()

If:

    add(2, 3)

returns:

    5

the assertion passes.

If it returns another value, Python raises:

    AssertionError

---

# 19.5️⃣ Multiple Unit Tests

A function can have multiple test cases.

    def add(a, b):

        return a + b


    def test_positive_numbers():

        assert add(2, 3) == 5


    def test_negative_numbers():

        assert add(-2, -3) == -5


    def test_zero():

        assert add(0, 0) == 0


    test_positive_numbers()
    test_negative_numbers()
    test_zero()

Each function tests a different scenario.

---

# 19.6️⃣ Unit Test Structure

A simple unit test can be understood as:

    Arrange
       ↓
    Act
       ↓
    Assert

This is commonly called the **AAA pattern**.

### Arrange

Prepare the required data.

    numbers = [10, 20, 30]

### Act

Call the function being tested.

    result = calculate_average(numbers)

### Assert

Check the expected result.

    assert result == 20

Complete example:

    def calculate_average(numbers):

        return sum(numbers) / len(numbers)


    def test_calculate_average():

        # Arrange
        numbers = [10, 20, 30]

        # Act
        result = calculate_average(numbers)

        # Assert
        assert result == 20

---

# 19.7️⃣ Why the AAA Pattern Is Useful

The AAA pattern makes tests easier to understand.

    Arrange
    → What data are we using?

    Act
    → What are we testing?

    Assert
    → What result do we expect?

This structure is useful with both `unittest` and `pytest`.

---

# 19.8️⃣ Testing a Validation Function

Consider:

    def validate_temperature(
        temperature
    ):

        if temperature < 0 or temperature > 2:

            raise ValueError(
                "Temperature must be between 0 and 2."
            )

        return temperature

We can test a valid value:

    def test_valid_temperature():

        result = validate_temperature(0.7)

        assert result == 0.7

And an invalid value:

    def test_invalid_temperature():

        try:

            validate_temperature(5)

        except ValueError:

            assert True

        else:

            assert False

The second test verifies that invalid input produces an exception.

---

# 19.9️⃣ Testing Exceptions with `unittest`

The built-in `unittest` framework provides:

    assertRaises()

Example:

    import unittest


    def divide(a, b):

        return a / b


    class TestDivideFunction(
        unittest.TestCase
    ):

        def test_divide_by_zero(self):

            with self.assertRaises(
                ZeroDivisionError
            ):

                divide(10, 0)


    if __name__ == "__main__":

        unittest.main()

This test passes only if:

    ZeroDivisionError

is raised.

---

# 🔟 `unittest` Framework

## 📖 Definition

> **`unittest` is Python's built-in unit testing framework used to create, organize, and run automated tests.**

It is part of Python's standard library.

No additional installation is required.

Basic structure:

    import unittest


    def add(a, b):

        return a + b


    class TestAddFunction(
        unittest.TestCase
    ):

        def test_add(self):

            self.assertEqual(
                add(2, 3),
                5
            )


    if __name__ == "__main__":

        unittest.main()

---

# 10.1️⃣ `unittest.TestCase`

Test classes normally inherit from:

    unittest.TestCase

Example:

    class TestAddFunction(
        unittest.TestCase
    ):

        ...

This gives the class access to methods such as:

    self.assertEqual()

    self.assertNotEqual()

    self.assertTrue()

    self.assertFalse()

    self.assertRaises()

---

# 10.2️⃣ Test Method Naming

`unittest` automatically discovers methods whose names begin with:

    test_

Example:

    def test_add(self):

        ...

    def test_subtract(self):

        ...

    def test_divide(self):

        ...

A method such as:

    def check_add(self):

        ...

will not normally be discovered as a test by `unittest`.

---

# 10.3️⃣ `assertEqual()`

## 📖 Definition

> **`assertEqual()` verifies that two values are equal.**

Example:

    self.assertEqual(
        add(2, 3),
        5
    )

This means:

    Actual Result == Expected Result

If:

    5 == 5

the test passes.

---

# 10.4️⃣ `assertNotEqual()`

## 📖 Definition

> **`assertNotEqual()` verifies that two values are different.**

Example:

    self.assertNotEqual(
        add(2, 3),
        10
    )

The test passes because:

    5 != 10

---

# 10.5️⃣ `assertTrue()`

## 📖 Definition

> **`assertTrue()` verifies that a value or condition is true.**

Example:

    def is_positive(number):

        return number > 0


    self.assertTrue(
        is_positive(10)
    )

The test passes because:

    10 > 0

is true.

---

# 10.6️⃣ `assertFalse()`

## 📖 Definition

> **`assertFalse()` verifies that a value or condition is false.**

Example:

    def is_positive(number):

        return number > 0


    self.assertFalse(
        is_positive(-10)
    )

The condition:

    -10 > 0

is false.

Therefore, the test passes.

---

# 10.7️⃣ `assertIsNone()`

## 📖 Definition

> **`assertIsNone()` verifies that a value is exactly `None`.**

Example:

    def get_response():

        return None


    self.assertIsNone(
        get_response()
    )

This is useful when a function uses `None` to indicate that no result was available.

---

# 10.8️⃣ `assertIsNotNone()`

## 📖 Definition

> **`assertIsNotNone()` verifies that a value is not `None`.**

Example:

    def get_response():

        return "AI response"


    self.assertIsNotNone(
        get_response()
    )

The test passes because the function returns a value.

---

# 10.9️⃣ `assertIn()`

## 📖 Definition

> **`assertIn()` verifies that a value exists inside another collection.**

Example:

    models = [
        "GPT",
        "Gemini",
        "Claude"
    ]


    self.assertIn(
        "GPT",
        models
    )

The test passes because `"GPT"` exists in the list.

---

# 1️⃣1️⃣ `assertNotIn()`

## 📖 Definition

> **`assertNotIn()` verifies that a value does not exist inside another collection.**

Example:

    models = [
        "GPT",
        "Gemini",
        "Claude"
    ]


    self.assertNotIn(
        "Llama",
        models
    )

The test passes because `"Llama"` is not in the list.

---

# 1️⃣1️⃣1️⃣ `assertRaises()`

## 📖 Definition

> **`assertRaises()` verifies that a specific exception is raised when code is executed.**

Example:

    import unittest


    def divide(a, b):

        return a / b


    class TestDivideFunction(
        unittest.TestCase
    ):

        def test_divide_by_zero(self):

            with self.assertRaises(
                ZeroDivisionError
            ):

                divide(10, 0)


    if __name__ == "__main__":

        unittest.main()

This is important because testing is not only about successful operations.

We should also test expected failures.

---

# 1️⃣1️⃣2️⃣ Complete `unittest` Example

    import unittest


    def add(a, b):

        # Return the sum of two numbers.
        return a + b


    class TestAddFunction(
        unittest.TestCase
    ):

        def test_positive_numbers(self):

            # Test addition using positive numbers.
            self.assertEqual(
                add(2, 3),
                5
            )


        def test_negative_numbers(self):

            # Test addition using negative numbers.
            self.assertEqual(
                add(-2, -3),
                -5
            )


        def test_zero(self):

            # Test addition using zero.
            self.assertEqual(
                add(0, 0),
                0
            )


        def test_different_values(self):

            # Verify that the result is not an incorrect value.
            self.assertNotEqual(
                add(2, 3),
                10
            )


    if __name__ == "__main__":

        # Discover and execute all test methods.
        unittest.main()

---

# 1️⃣1️⃣3️⃣ Running the Test

Suppose the file is:

    test_add.py

Run:

    python test_add.py

A successful run produces output similar to:

    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK

The exact execution time may differ.

Each:

    .

represents a successful test.

---

# 1️⃣1️⃣4️⃣ What Happens When a Test Fails?

Suppose the implementation contains a bug:

    def add(a, b):

        return a - b

But the test expects:

    add(2, 3) == 5

The test will fail.

The test framework provides information about:

- Which test failed
- Expected value
- Actual value
- Location of the failure

This helps developers debug the implementation.

---

# 1️⃣1️⃣5️⃣ Unit Tests Should Be Independent

Consider:

    test_login()

and:

    test_generate_response()

The second test should ideally not depend on the first test having been executed successfully unless such dependency is explicitly required.

Independent tests are easier to:

- Run
- Debug
- Reorder
- Maintain
- Execute repeatedly

---

# 1️⃣1️⃣6️⃣ Test Isolation

Suppose a function uses a database.

A unit test should ideally not require a real production database.

Instead, the external dependency can be isolated or replaced with a controlled test dependency.

General idea:

    Unit Under Test
          ↓
    Controlled Dependency
          ↓
    Predictable Test

This keeps unit tests focused on the component being tested.

---

# 1️⃣1️⃣7️⃣ External API Testing

Suppose:

    def get_ai_response(prompt):

        return call_external_api(prompt)

Calling a real external API in every unit test can be:

- Slow
- Expensive
- Unreliable
- Dependent on network availability
- Difficult to reproduce

For unit testing, external dependencies are often isolated or mocked.

The exact mocking techniques will be explored separately when working with testing tools.

---

# 1️⃣1️⃣8️⃣ Unit Testing AI Components

AI applications contain many components that can be unit tested.

For example:

    validate_prompt()
    validate_temperature()
    calculate_token_limit()
    clean_text()
    split_documents()
    format_context()
    build_prompt()
    parse_response()

These functions can often be tested without calling an actual LLM.

---

# 1️⃣1️⃣9️⃣ Testing Prompt Construction

Suppose:

    def build_prompt(
        question,
        context
    ):

        return (
            f"Context: {context}\n"
            f"Question: {question}"
        )

A unit test can verify the generated structure:

    def test_build_prompt():

        prompt = build_prompt(
            "What is AI?",
            "AI stands for Artificial Intelligence."
        )

        assert "What is AI?" in prompt

        assert (
            "Artificial Intelligence"
            in prompt
        )

This tests the deterministic prompt-building logic.

---

# 1️⃣2️⃣0️⃣ Testing Data Processing

Suppose:

    def clean_text(text):

        return text.strip().lower()

A unit test can check:

    def test_clean_text():

        result = clean_text(
            "  HELLO WORLD  "
        )

        assert result == "hello world"

This is a good candidate for unit testing because the function is deterministic.

---

# 1️⃣2️⃣1️⃣ Testing RAG Components

A RAG system may contain:

    Query Processing
          ↓
    Document Chunking
          ↓
    Embedding
          ↓
    Retrieval
          ↓
    Context Formatting
          ↓
    Prompt Construction

Many of these components can be tested independently.

For example:

    test_chunking()

    test_metadata_extraction()

    test_context_formatting()

    test_prompt_construction()

This makes debugging a larger RAG system easier.

---

# 1️⃣2️⃣2️⃣ Testing Pydantic Models

Suppose:

    from pydantic import BaseModel


    class ChatRequest(BaseModel):

        prompt: str

        max_tokens: int = 200

        temperature: float = 0.7

Tests can verify valid data:

    def test_valid_chat_request():

        request = ChatRequest(
            prompt="Explain AI",
            max_tokens=200,
            temperature=0.7
        )

        assert request.prompt == "Explain AI"

They can also verify invalid data.

---

# 1️⃣2️⃣3️⃣ Testing Invalid AI Parameters

Suppose temperature must be between `0` and `2`.

A test can check invalid input:

    import unittest
    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        prompt: str

        temperature: float = Field(
            ge=0,
            le=2
        )


    class TestChatRequest(
        unittest.TestCase
    ):

        def test_invalid_temperature(self):

            with self.assertRaises(
                ValueError
            ):

                ChatRequest(
                    prompt="Explain AI",
                    temperature=5
                )


    if __name__ == "__main__":

        unittest.main()

This verifies that invalid AI configuration is rejected.

---

# 1️⃣2️⃣4️⃣ Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
|---|---|
| Tests one component | Tests multiple components |
| Usually fast | Usually slower |
| More isolated | Components interact |
| Easier to debug | More complex |
| Often no external services | May use external systems |

Example:

### Unit

    test_prompt_builder()

### Integration

    Prompt Builder
         +
    Retrieval System
         +
    Database

Both are useful, but they answer different questions.

---

# 1️⃣2️⃣5️⃣ Unit Testing vs End-to-End Testing

### Unit Test

Tests one small component.

    validate_prompt()

### End-to-End Test

Tests the complete workflow.

    User Query
        ↓
    API
        ↓
    Validation
        ↓
    Retrieval
        ↓
    LLM
        ↓
    Response

End-to-end tests can provide confidence in the complete system but are generally more expensive and slower than unit tests.

---

# 1️⃣2️⃣6️⃣ Test Naming

Good:

    test_empty_prompt_is_rejected()

    test_valid_temperature_is_accepted()

    test_invalid_temperature_raises_error()

Poor:

    test1()

    test2()

    test3()

Good names explain what behavior is being tested.

---

# 1️⃣2️⃣7️⃣ Arrange → Act → Assert

A good unit test often follows:

    Arrange
       ↓
    Prepare test data

       ↓

    Act
       ↓
    Execute function

       ↓

    Assert
       ↓
    Verify expected behavior

Example:

    def test_calculate_average():

        # Arrange
        marks = [80, 90, 70]

        # Act
        result = calculate_average(marks)

        # Assert
        assert result == 80

This structure makes tests easier to read.

---

# 1️⃣2️⃣8️⃣ Unit Testing Best Practices

### 1. Test one behavior at a time

Keep the purpose of each test clear.

### 2. Use meaningful test names

The test name should explain the scenario.

### 3. Include normal cases

Verify expected behavior.

### 4. Include edge cases

Test empty, zero, boundary, and unusual values.

### 5. Test invalid inputs

Verify that invalid data is rejected appropriately.

### 6. Test expected exceptions

Use `assertRaises()` when using `unittest`.

### 7. Keep tests independent

Avoid unnecessary dependencies between tests.

### 8. Keep tests deterministic where possible

The same input should ideally produce predictable results.

### 9. Avoid unnecessary external dependencies

Unit tests should remain fast and isolated.

### 10. Run tests regularly

Running tests after changes helps detect regressions early.

---

# 1️⃣2️⃣9️⃣ AI Engineer Testing Strategy

A practical AI project may use several layers of testing:

    ┌────────────────────────────┐
    │     End-to-End Tests       │
    └────────────────────────────┘
                 ↑
    ┌────────────────────────────┐
    │    Integration Tests       │
    └────────────────────────────┘
                 ↑
    ┌────────────────────────────┐
    │       Unit Tests           │
    └────────────────────────────┘

Unit tests can cover:

    Input Validation
    Data Processing
    Text Cleaning
    Chunking
    Prompt Construction
    Response Parsing
    Configuration Validation

Integration tests can cover:

    Database + Retrieval
    API + Service
    Retrieval + Prompt Pipeline

End-to-end tests can cover:

    User
      ↓
    API
      ↓
    RAG
      ↓
    LLM
      ↓
    Final Response

---

# 🤖 AI Engineer Relevance

Unit testing is highly useful when building:

- AI APIs
- RAG applications
- AI agents
- Data pipelines
- LLM applications
- Embedding pipelines
- Vector search systems
- FastAPI applications
- Production AI systems

Not every part of an AI system behaves like a deterministic mathematical function.

However, many supporting components are deterministic and can be tested thoroughly.

For example:

    Input Validation
          ↓
    Unit Test

    Text Cleaning
          ↓
    Unit Test

    Chunking
          ↓
    Unit Test

    Prompt Construction
          ↓
    Unit Test

    Response Parsing
          ↓
    Unit Test

This provides a reliable foundation for the larger AI system.

---

# 🧠 Key Takeaways

- Unit testing tests individual functions or methods independently.
- A unit should generally represent a small, logically focused component.
- Unit tests help detect bugs early.
- The AAA pattern means Arrange, Act, and Assert.
- Python provides the built-in `unittest` framework.
- `unittest.TestCase` provides useful assertion methods.
- Test methods normally begin with `test_`.
- `assertEqual()` checks equality.
- `assertNotEqual()` checks inequality.
- `assertTrue()` checks truth.
- `assertFalse()` checks falseness.
- `assertIsNone()` checks for `None`.
- `assertIsNotNone()` checks that a value is not `None`.
- `assertIn()` checks membership.
- `assertNotIn()` checks that a value is absent.
- `assertRaises()` verifies expected exceptions.
- Unit tests should generally be independent and focused.
- External APIs and databases should usually be isolated when writing unit tests.
- AI applications have many deterministic components that can be unit tested.
- Unit testing works together with edge-case handling, validation, exception handling, and clean code.
- Unit tests provide a foundation for integration and end-to-end testing.

# 2️⃣0️⃣ Pytest

## 📖 Definition

> **Pytest is a popular Python testing framework that makes it easy to write, run, and maintain automated tests.**

Unlike `unittest`, which uses classes and methods such as `TestCase` and `assertEqual()`, pytest allows us to write simple test functions using Python's normal `assert` statement.

Pytest is widely used because it provides:

- Simple test syntax
- Less boilerplate code
- Automatic test discovery
- Clear failure reports
- Fixtures
- Parameterized testing
- Plugin support
- Integration with larger Python projects

---

# 20.1️⃣ Why Pytest?

Compare the basic structure.

### Using `unittest`

    import unittest


    def add(a, b):

        return a + b


    class TestAdd(unittest.TestCase):

        def test_add(self):

            self.assertEqual(
                add(2, 3),
                5
            )


    if __name__ == "__main__":

        unittest.main()

### Using pytest

    def add(a, b):

        return a + b


    def test_add():

        assert add(2, 3) == 5

The pytest version is shorter and easier to read.

---

# 20.2️⃣ Installing Pytest

Pytest is not part of Python's standard library, so it usually needs to be installed separately.

Use:

    pip install pytest

After installation, verify it with:

    pytest --version

Example output:

    pytest 9.x.x

The exact version depends on the installed package.

---

# 20.3️⃣ Creating a Pytest File

Pytest follows naming conventions for automatic test discovery.

Common test file names include:

    test_example.py

or:

    example_test.py

For this chapter, we can use:

    20_pytest.py

However, when working on larger projects, names such as:

    test_calculator.py

are generally clearer.

---

# 20.4️⃣ Basic Pytest Example

Create a function:

    def add(a, b):

        # Add two numbers.
        return a + b


    def test_add():

        # Verify that 2 + 3 produces 5.
        assert add(2, 3) == 5

The important part is:

    assert add(2, 3) == 5

Pytest uses Python's normal `assert` statement.

---

# 20.5️⃣ Running Pytest

From the terminal, run:

    pytest

Pytest searches for test files and test functions according to its discovery rules.

You can also specify a particular file:

    pytest 20_pytest.py

A successful test run may look similar to:

    ================= test session starts =================
    collected 1 item

    20_pytest.py .                              [100%]

    ================== 1 passed in 0.02s ==================

The exact output and execution time may vary.

---

# 20.6️⃣ Understanding the Output

Suppose pytest displays:

    collected 1 item

This means:

    1 test

was discovered.

Then:

    .

represents a passing test.

Therefore:

    1 passed

means the test completed successfully.

---

# 20.7️⃣ Multiple Tests

Example:

    def add(a, b):

        return a + b


    def test_positive_numbers():

        assert add(2, 3) == 5


    def test_negative_numbers():

        assert add(-2, -3) == -5


    def test_zero():

        assert add(0, 0) == 0

Running:

    pytest 20_pytest.py

will discover all three test functions.

Possible output:

    collected 3 items

    20_pytest.py ...                         [100%]

    3 passed

Each:

    .

represents a successful test.

---

# 20.8️⃣ Pytest Test Discovery

Pytest automatically discovers tests based on naming conventions.

Common patterns include:

    test_*.py

and:

    *_test.py

Test functions generally begin with:

    test_

Example:

    def test_add():
        ...


    def test_subtract():
        ...

These can be automatically discovered.

A function such as:

    def check_add():
        ...

will not normally be discovered as a pytest test.

---

# 20.9️⃣ Test Classes in Pytest

Pytest can also use test classes.

Example:

    class TestCalculator:

        def test_add(self):

            assert 2 + 3 == 5


        def test_subtract(self):

            assert 5 - 3 == 2

Unlike `unittest`, the class does not need to inherit from:

    unittest.TestCase

This reduces boilerplate.

---

# 🔟 Pytest Uses Normal `assert`

One of the main advantages of pytest is its simple assertion syntax.

Example:

    result = 2 + 3

    assert result == 5

You do not need:

    self.assertEqual(
        result,
        5
    )

Pytest analyzes the failed assertion and provides useful information.

---

# 10.1️⃣ Failed Assertion

Suppose:

    def add(a, b):

        return a + b


    def test_add():

        assert add(2, 3) == 10

The actual result is:

    5

but the expected result is:

    10

Pytest reports the assertion failure and shows useful information about the comparison.

This makes debugging easier.

---

# 10.2️⃣ Pytest and AAA Pattern

The Arrange → Act → Assert pattern works naturally with pytest.

Example:

    def calculate_average(numbers):

        return sum(numbers) / len(numbers)


    def test_calculate_average():

        # Arrange
        numbers = [10, 20, 30]

        # Act
        result = calculate_average(numbers)

        # Assert
        assert result == 20

This makes the test structure clear.

---

# 10.3️⃣ Testing Edge Cases with Pytest

Consider:

    def calculate_average(numbers):

        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        return sum(numbers) / len(numbers)

Tests can cover both normal and edge cases.

    def test_average():

        assert calculate_average(
            [10, 20, 30]
        ) == 20


    def test_empty_list():

        try:

            calculate_average([])

        except ValueError:

            assert True

        else:

            assert False

However, pytest provides a cleaner way to test exceptions.

---

# 10.4️⃣ `pytest.raises()`

## 📖 Definition

> **`pytest.raises()` verifies that a specific exception is raised by the code being tested.**

Example:

    import pytest


    def calculate_average(numbers):

        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        return sum(numbers) / len(numbers)


    def test_empty_list():

        with pytest.raises(
            ValueError
        ):

            calculate_average([])

This is the pytest equivalent of testing expected exceptions with `unittest`.

---

# 10.5️⃣ Comparing Exception Testing

### `unittest`

    with self.assertRaises(
        ValueError
    ):

        calculate_average([])

### Pytest

    with pytest.raises(
        ValueError
    ):

        calculate_average([])

Both verify that:

    ValueError

is raised.

Pytest simply provides a lightweight syntax.

---

# 10.6️⃣ Checking the Exception Message

Pytest can also inspect the exception.

Example:

    import pytest


    def validate_temperature(
        temperature
    ):

        if temperature < 0 or temperature > 2:

            raise ValueError(
                "Temperature must be between 0 and 2."
            )


    def test_invalid_temperature():

        with pytest.raises(
            ValueError,
            match="Temperature must be between 0 and 2."
        ):

            validate_temperature(5)

This verifies both:

    Exception Type
         +
    Expected Message

---

# 10.7️⃣ Pytest Fixtures

## 📖 Definition

> **A pytest fixture is a reusable piece of setup or test data that can be provided to test functions.**

Fixtures are useful when multiple tests need the same preparation.

For example:

    Test 1 → needs user data
    Test 2 → needs user data
    Test 3 → needs user data

Instead of recreating the same setup repeatedly, a fixture can provide it.

---

# 10.8️⃣ Basic Fixture

    import pytest


    @pytest.fixture
    def sample_numbers():

        return [10, 20, 30]


    def test_average(sample_numbers):

        result = sum(
            sample_numbers
        ) / len(sample_numbers)

        assert result == 20

Here:

    @pytest.fixture

marks:

    sample_numbers()

as a fixture.

Pytest automatically provides the fixture value to:

    test_average(sample_numbers)

---

# 10.9️⃣ Why Fixtures Are Useful

Without a fixture:

    def test_one():

        numbers = [10, 20, 30]

        ...


    def test_two():

        numbers = [10, 20, 30]

        ...

With a fixture:

    @pytest.fixture
    def sample_numbers():

        return [10, 20, 30]


    def test_one(sample_numbers):

        ...


    def test_two(sample_numbers):

        ...

The setup logic is centralized.

---

# 1️⃣0️⃣ Fixture Flow

The general flow is:

    Test Function
         ↓
    Requests Fixture
         ↓
    Pytest Executes Fixture
         ↓
    Fixture Provides Data
         ↓
    Test Runs

For example:

    sample_numbers
          ↓
    [10, 20, 30]
          ↓
    test_average()
          ↓
    assert result == 20

---

# 1️⃣1️⃣ Parameterized Testing

## 📖 Definition

> **Parameterized testing allows the same test logic to run with multiple sets of input values.**

Suppose we want to test:

    add(2, 3)
    add(5, 5)
    add(-2, -3)

Instead of writing separate test functions, pytest can parameterize the test.

Example:

    import pytest


    def add(a, b):

        return a + b


    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),
            (5, 5, 10),
            (-2, -3, -5),
            (0, 0, 0)
        ]
    )
    def test_add(
        a,
        b,
        expected
    ):

        assert add(a, b) == expected

The same test logic runs with multiple inputs.

---

# 1️⃣2️⃣ Why Parameterization Is Useful

Without parameterization:

    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()

With parameterization:

    One Test
       +
    Multiple Inputs

This is especially useful for:

- Validation
- Mathematical functions
- Text processing
- Data transformation
- AI configuration testing

---

# 1️⃣3️⃣ Parameterized AI Validation

Suppose:

    def validate_temperature(
        temperature
    ):

        return 0 <= temperature <= 2

We can test multiple values:

    import pytest


    @pytest.mark.parametrize(
        "temperature, expected",
        [
            (0, True),
            (0.7, True),
            (2, True),
            (-1, False),
            (3, False)
        ]
    )
    def test_temperature(
        temperature,
        expected
    ):

        assert (
            validate_temperature(
                temperature
            )
            == expected
        )

This efficiently tests normal and boundary values.

---

# 1️⃣4️⃣ Testing AI Prompt Validation

Consider:

    def validate_prompt(prompt):

        return bool(prompt.strip())

We can test several inputs:

    import pytest


    @pytest.mark.parametrize(
        "prompt, expected",
        [
            ("Hello", True),
            ("Explain AI", True),
            ("", False),
            ("   ", False)
        ]
    )
    def test_prompt_validation(
        prompt,
        expected
    ):

        assert (
            validate_prompt(prompt)
            == expected
        )

This covers:

    Normal Input
    Empty Input
    Whitespace Input

---

# 1️⃣5️⃣ Test Fixtures and AI Applications

Fixtures are particularly useful for AI projects.

For example, multiple tests may require:

    Sample Documents
    Sample Prompts
    Sample API Responses
    Sample User Data
    Sample Embeddings

A fixture can provide these reusable test inputs.

Example:

    import pytest


    @pytest.fixture
    def sample_documents():

        return [
            "Python is a programming language.",
            "Machine Learning is a field of AI.",
            "RAG combines retrieval with generation."
        ]


    def test_document_count(
        sample_documents
    ):

        assert len(
            sample_documents
        ) == 3

---

# 1️⃣6️⃣ Testing RAG Components with Fixtures

Suppose a retrieval function expects documents.

A fixture can provide sample documents:

    @pytest.fixture
    def sample_documents():

        return [
            "Python basics",
            "Machine Learning basics",
            "Deep Learning basics"
        ]

Then:

    def test_document_retrieval(
        sample_documents
    ):

        result = retrieve_documents(
            sample_documents,
            "Machine Learning"
        )

        assert len(result) > 0

This avoids depending on a real vector database for every unit test.

---

# 1️⃣7️⃣ Pytest Markers

## 📖 Definition

> **Pytest markers allow tests to be categorized or labeled so that specific groups of tests can be selected.**

For example:

    @pytest.mark.slow
    def test_large_dataset():

        ...

A project may contain:

    Unit Tests
    Integration Tests
    Slow Tests
    API Tests

Markers can help organize them.

---

# 1️⃣8️⃣ Example Marker

    import pytest


    @pytest.mark.slow
    def test_large_dataset():

        result = process_large_dataset()

        assert result is not None

The exact marker configuration depends on the project.

In larger projects, custom markers are normally registered in the pytest configuration.

---

# 1️⃣9️⃣ Running Specific Tests

Run the complete test suite:

    pytest

Run one file:

    pytest 20_pytest.py

Run a specific test:

    pytest 20_pytest.py::test_add

Run tests matching a keyword:

    pytest -k add

These commands become useful as the number of tests increases.

---

# 2️⃣0️⃣ Verbose Output

Pytest can provide more detailed output using:

    pytest -v

The `-v` option means:

    verbose

This can show individual test names and their results.

Example:

    pytest -v

Possible output:

    test_add PASSED
    test_subtract PASSED
    test_divide PASSED

---

# 2️⃣1️⃣ Quiet Output

Pytest also supports:

    pytest -q

The `-q` option means:

    quiet

It reduces the amount of output displayed.

This can be useful when you want a shorter test summary.

---

# 2️⃣2️⃣ Running a Test File

Suppose your project contains:

    project/
    │
    ├── calculator.py
    └── test_calculator.py

You can run:

    pytest test_calculator.py

Pytest will discover the tests inside the file.

---

# 2️⃣3️⃣ Example Project Structure

A small Python project may look like:

    project/
    │
    ├── calculator.py
    │
    └── tests/
        └── test_calculator.py

`calculator.py`:

    def add(a, b):

        return a + b


    def subtract(a, b):

        return a - b

`test_calculator.py`:

    from calculator import add
    from calculator import subtract


    def test_add():

        assert add(2, 3) == 5


    def test_subtract():

        assert subtract(5, 3) == 2

Run:

    pytest

Pytest discovers the test file and executes the tests.

---

# 2️⃣4️⃣ Testing AI Project Structure

A larger AI project may eventually look like:

    ai_project/
    │
    ├── app/
    │   ├── validation.py
    │   ├── retrieval.py
    │   ├── llm_service.py
    │   └── prompt_builder.py
    │
    └── tests/
        ├── test_validation.py
        ├── test_retrieval.py
        ├── test_llm_service.py
        └── test_prompt_builder.py

This keeps production code and tests organized separately.

---

# 2️⃣5️⃣ Testing Input Validation

Example:

    def validate_age(age):

        if age < 0:

            raise ValueError(
                "Age cannot be negative."
            )

        return age

Pytest:

    import pytest


    def test_valid_age():

        assert validate_age(25) == 25


    def test_invalid_age():

        with pytest.raises(
            ValueError
        ):

            validate_age(-5)

Two behaviors are tested:

    Valid Input
         +
    Invalid Input

---

# 2️⃣6️⃣ Testing Clean Functions

Clean and maintainable functions are easier to test.

Example:

    def calculate_average(
        numbers: list[int]
    ) -> float:

        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        return sum(numbers) / len(numbers)

Tests:

    def test_average():

        assert calculate_average(
            [10, 20, 30]
        ) == 20


    def test_empty_list():

        with pytest.raises(
            ValueError
        ):

            calculate_average([])

This combines:

    Type Hints
    Edge Cases
    Proper Error Messages
    Exception Handling
    Unit Testing
    Pytest

---

# 2️⃣7️⃣ Pytest vs `unittest`

| Feature | `unittest` | `pytest` |
|---|---|---|
| Included with Python | Yes | No |
| Installation | Not required | `pip install pytest` |
| Test style | Classes commonly used | Functions commonly used |
| Assertions | `self.assertEqual()` | Normal `assert` |
| Test discovery | Built-in | Automatic |
| Fixtures | `setUp()` / `tearDown()` and others | Powerful fixture system |
| Parameterization | More verbose | `pytest.mark.parametrize` |
| Syntax | More boilerplate | More concise |
| Plugins | Available | Large plugin ecosystem |

Both are valid testing tools.

Pytest is often preferred when developers want concise syntax and a flexible testing ecosystem.

---

# 2️⃣8️⃣ Pytest vs Manual Testing

| Manual Testing | Pytest |
|---|---|
| Human executes checks | Tests execute automatically |
| Repetitive | Repeatable |
| Easy for quick experiments | Better for larger test suites |
| Results may depend on manual checking | Results are programmatically verified |
| Difficult to run hundreds of checks manually | Can execute many tests quickly |

Manual testing still has value, but automated testing is important for maintainable software.

---

# 2️⃣9️⃣ Pytest and Regression Testing

Suppose an AI application originally has:

    50 tests

All tests pass.

Later, you modify:

    retrieval.py

Run:

    pytest

If an existing retrieval test fails, you may have introduced a regression.

General workflow:

    Change Code
        ↓
    Run Pytest
        ↓
    Tests Pass?
       ↙     ↘
     Yes      No
      ↓        ↓
    Continue  Investigate
               ↓
             Fix
               ↓
             Test Again

---

# 3️⃣0️⃣ Pytest and AI Engineering

Pytest is useful for testing:

### Data Processing

    Text Cleaning
    Chunking
    Data Transformation

### AI Validation

    Prompt Validation
    Token Limits
    Temperature Limits

### RAG

    Retrieval Logic
    Context Formatting
    Metadata Processing

### APIs

    Request Validation
    Response Parsing
    Error Handling

### AI Agents

    Tool Input Validation
    Tool Output Processing
    Agent State Handling

---

# 3️⃣1️⃣ Testing Deterministic AI Components

Not every AI operation needs exact output comparison.

For deterministic components, exact assertions are useful.

Example:

    def clean_text(text):

        return text.strip().lower()


    def test_clean_text():

        assert (
            clean_text(
                "  HELLO  "
            )
            == "hello"
        )

For an LLM response, exact text may vary.

Instead, testing may check properties such as:

    Response is not empty

    Response has expected structure

    Required fields exist

    Response satisfies validation rules

    No forbidden data is present

The exact testing strategy depends on the AI system.

---

# 3️⃣2️⃣ Pytest Best Practices

### 1. Use descriptive test names

Good:

    test_empty_prompt_is_rejected()

### 2. Keep tests focused

One test should ideally verify one behavior.

### 3. Use fixtures for reusable setup

Avoid repeating the same setup code unnecessarily.

### 4. Use parameterization for multiple inputs

It reduces duplicated test logic.

### 5. Test edge cases

Include:

    Empty
    Zero
    Negative
    Boundary
    Invalid
    Missing

### 6. Test expected exceptions

Use:

    pytest.raises()

### 7. Keep tests independent

Avoid unnecessary test-to-test dependencies.

### 8. Keep unit tests fast

Avoid unnecessary network or external service calls.

### 9. Run tests after code changes

This helps detect regressions.

### 10. Organize tests clearly

Keep tests grouped by functionality or module.

---

# 3️⃣3️⃣ Complete Pytest Example

    import pytest


    def calculate_average(
        numbers: list[int]
    ) -> float:

        # Reject an empty list.
        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        # Calculate and return the average.
        return sum(numbers) / len(numbers)


    def test_average():

        # Test normal input.
        assert calculate_average(
            [10, 20, 30]
        ) == 20


    def test_single_value():

        # Test a list containing one value.
        assert calculate_average(
            [50]
        ) == 50


    def test_empty_list():

        # Verify that empty input raises ValueError.
        with pytest.raises(
            ValueError
        ):

            calculate_average([])

Running:

    pytest

will execute all discovered tests.

Possible result:

    collected 3 items

    ...                                      [100%]

    3 passed

---

# 3️⃣4️⃣ Pytest Learning Flow

The important progression is:

    Basic Test
         ↓
    assert
         ↓
    Multiple Tests
         ↓
    Exception Testing
         ↓
    Fixtures
         ↓
    Parameterization
         ↓
    Markers
         ↓
    Test Organization
         ↓
    AI Project Testing

This provides a foundation for writing maintainable automated tests.

---

# 🤖 AI Engineer Relevance

Pytest becomes particularly useful when your AI projects grow beyond simple Python scripts.

A future AI project may contain:

    API
     ↓
    Validation
     ↓
    Data Processing
     ↓
    Embeddings
     ↓
    Vector Database
     ↓
    Retrieval
     ↓
    Prompt Construction
     ↓
    LLM
     ↓
    Response Processing

Pytest can help verify individual components before testing the complete system.

For example:

    test_validation.py
        ↓
    test_retrieval.py
        ↓
    test_prompt_builder.py
        ↓
    test_response_parser.py

This reduces the chance that a small change silently breaks existing functionality.

---

# 🧠 Key Takeaways

- Pytest is a popular Python testing framework.
- It usually requires installation with `pip install pytest`.
- Pytest supports simple test functions.
- Test functions normally begin with `test_`.
- Pytest uses Python's normal `assert` statement.
- It automatically discovers tests using naming conventions.
- `pytest.raises()` verifies expected exceptions.
- Fixtures provide reusable test data and setup.
- Parameterization allows one test to run with multiple inputs.
- Markers can categorize tests.
- `pytest -v` provides verbose output.
- `pytest -q` provides quieter output.
- Specific files and individual tests can be executed directly.
- Pytest can be used for both small Python programs and large applications.
- Pytest is especially useful for AI projects because many AI-supporting components are deterministic and testable.
- Validation, preprocessing, retrieval, prompt construction, response parsing, and configuration logic can all be tested.
- Pytest works well with the other Chapter 15 concepts such as type hints, Pydantic, exception handling, edge cases, logging, and clean code.

# 2️⃣1️⃣ AI Engineer Practical Examples

## 🎯 Objective

This section connects the concepts learned throughout Chapter 15 with practical AI Engineering scenarios.

The goal is to understand how concepts such as:

- Type Hinting
- Pydantic
- Input Validation
- Custom Exceptions
- Logging
- Proper Error Messages
- Graceful Failure
- Configuration Handling
- Retry Logic
- Timeouts
- Edge-Case Handling
- Clean Code
- Unit Testing
- Pytest

can work together in an AI application.

The examples in this section simulate AI application behavior. They do not make real AI API calls unless an actual API integration is added later.

---

# 21.1️⃣ AI Engineer Practical Architecture

A simple AI application can be represented as:

    User Request
         ↓
    Input Validation
         ↓
    Structured Data
         ↓
    Error Handling
         ↓
    AI Service
         ↓
    Logging
         ↓
    Response
         ↓
    Graceful Failure

Each stage can use concepts learned in this chapter.

---

# 21.2️⃣ Practical Example 1 — Type Hints

Type hints make the expected data types clear.

Example:

    def generate_response(
        prompt: str
    ) -> str:

        return f"AI response for: {prompt}"

Here:

    prompt: str

means the function expects a string.

And:

    -> str

means the function is expected to return a string.

Example:

    response = generate_response(
        "Explain Machine Learning."
    )

    print(response)

Output:

    AI response for: Explain Machine Learning.

---

# 21.3️⃣ Practical Example 2 — Pydantic Model

AI APIs commonly receive structured request data.

For example:

    {
        "prompt": "Explain Machine Learning",
        "max_tokens": 200,
        "temperature": 0.7
    }

Pydantic can represent this structure.

    from pydantic import BaseModel


    class ChatRequest(BaseModel):

        prompt: str

        max_tokens: int = 200

        temperature: float = 0.7

Now the application has a clear data model.

---

# 21.4️⃣ Pydantic Validation

We can add constraints using `Field`.

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        prompt: str = Field(
            min_length=1
        )

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )

This means:

    prompt
    → Cannot be empty

    max_tokens
    → 1 to 4096

    temperature
    → 0 to 2

These rules protect the application from invalid request data.

---

# 21.5️⃣ Practical Example 3 — Custom Exception

A custom exception can represent an application-specific failure.

Example:

    class InvalidAIRequestError(
        Exception
    ):
        pass

This exception can be raised when an AI request cannot be processed.

Example:

    raise InvalidAIRequestError(
        "Invalid AI request."
    )

The application can then catch this specific exception.

---

# 21.6️⃣ Practical Example 4 — Logging

Logging records important application events.

Example:

    import logging


    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    logging.info(
        "AI request received."
    )

Output:

    INFO - AI request received.

Logging can be used to record:

- Request received
- Validation failure
- API request
- API response
- Retry attempt
- Timeout
- Error
- Application shutdown

---

# 21.7️⃣ Practical Example 5 — Proper Error Messages

Compare:

    raise ValueError(
        "Invalid input."
    )

with:

    raise ValueError(
        "Invalid temperature. "
        "Temperature must be between 0 and 2."
    )

The second message provides more useful information.

For an AI application, a meaningful error can make debugging much easier.

---

# 21.8️⃣ Practical Example 6 — Graceful Failure

Suppose an AI service becomes unavailable.

A production application should avoid an uncontrolled crash.

Example:

    def call_ai_service(
        prompt: str
    ) -> str | None:

        try:

            # Simulate an AI service failure.
            raise ConnectionError(
                "AI service unavailable."
            )

        except ConnectionError:

            logging.exception(
                "AI service request failed."
            )

            return None

The caller can then handle the failure:

    response = call_ai_service(
        "Explain Machine Learning."
    )


    if response is not None:

        print(
            "AI Response:",
            response
        )

    else:

        print(
            "The AI service is currently "
            "unavailable."
        )

---

# 21.9️⃣ Practical Example 7 — Complete Request Model

Now combine:

    Pydantic
    +
    Type Hints
    +
    Validation

Example:

    from pydantic import BaseModel, Field


    class ChatRequest(BaseModel):

        prompt: str = Field(
            min_length=1
        )

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=200,
        temperature=0.7
    )


    print(
        "Prompt:",
        request.prompt
    )

    print(
        "Max Tokens:",
        request.max_tokens
    )

    print(
        "Temperature:",
        request.temperature
    )

Output:

    Prompt: Explain Machine Learning.
    Max Tokens: 200
    Temperature: 0.7

---

# 2️⃣1️⃣0️⃣ Practical Example 8 — Validation Failure

Now provide invalid data.

    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=5000,
        temperature=0.7
    )

The model rejects the request because:

    max_tokens > 4096

Pydantic raises a validation error.

The application can catch it:

    from pydantic import ValidationError


    try:

        request = ChatRequest(
            prompt="Explain Machine Learning.",
            max_tokens=5000,
            temperature=0.7
        )

    except ValidationError as e:

        print(
            "Invalid AI request."
        )

This demonstrates:

    Input
      ↓
    Pydantic
      ↓
    Validation
      ↓
    Invalid
      ↓
    Controlled Error

---

# 2️⃣1️⃣1️⃣ Practical Example 9 — Combining Pydantic and Custom Exceptions

A production-style application can convert low-level validation errors into an application-specific exception.

    from pydantic import (
        BaseModel,
        Field,
        ValidationError
    )


    class InvalidAIRequestError(
        Exception
    ):
        pass


    class ChatRequest(BaseModel):

        prompt: str = Field(
            min_length=1
        )

        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    def create_chat_request(
        prompt: str,
        max_tokens: int = 200,
        temperature: float = 0.7
    ) -> ChatRequest:

        try:

            return ChatRequest(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )

        except ValidationError as e:

            raise InvalidAIRequestError(
                "Invalid AI request. "
                "Please check prompt, max_tokens, "
                "and temperature."
            ) from e

Now the rest of the application does not need to directly handle every Pydantic validation detail.

---

# 21.12️⃣ Practical Example 10 — AI Response Simulation

We can now create a function that simulates an AI response.

    def generate_response(
        request: ChatRequest
    ) -> str:

        logging.info(
            "AI request received."
        )

        # Simulate an AI response.
        response = (
            f"AI response for: "
            f"{request.prompt}"
        )

        return response

This is not a real LLM call.

It only simulates the structure of an AI service.

---

# 21.13️⃣ Calling the Simulated AI Service

    request = ChatRequest(
        prompt="Explain Machine Learning.",
        max_tokens=200,
        temperature=0.7
    )


    response = generate_response(
        request
    )


    print(
        "Response:",
        response
    )

Output:

    INFO - AI request received.
    Response: AI response for: Explain Machine Learning.

---

# 21.14️⃣ Practical Example 11 — Retry Logic

External AI services can temporarily fail.

Retry logic can handle temporary failures.

Example:

    import time


    def call_ai_api_with_retry(
        prompt: str,
        max_retries: int = 3
    ):

        for attempt in range(
            1,
            max_retries + 1
        ):

            try:

                logging.info(
                    "AI API attempt %s",
                    attempt
                )

                # Simulate a temporary failure.
                raise ConnectionError(
                    "Temporary network error."
                )

            except ConnectionError as e:

                logging.warning(
                    "Attempt %s failed: %s",
                    attempt,
                    e
                )

                if attempt < max_retries:

                    time.sleep(1)

                else:

                    logging.error(
                        "Maximum retries reached."
                    )

                    return None

This prevents unlimited retries.

---

# 21.15️⃣ Retry Flow

The process is:

    AI API Request
         ↓
      Failure
         ↓
      Retry?
       ↙   ↘
     Yes    No
      ↓      ↓
    Retry   Failure
      ↓
    Success?
      ↙   ↘
    Yes    No
     ↓      ↓
  Response Retry Again

Retry logic is especially useful for temporary failures.

---

# 21.16️⃣ Practical Example 12 — Timeout

External services may also take too long.

A timeout limits how long the application waits.

Example:

    import time

    from concurrent.futures import (
        ThreadPoolExecutor,
        TimeoutError
    )


    def api_request():

        # Simulate a slow API request.
        time.sleep(5)

        return "API response received"


    with ThreadPoolExecutor() as executor:

        future = executor.submit(
            api_request
        )

        try:

            result = future.result(
                timeout=2
            )

            print(result)

        except TimeoutError:

            print(
                "Request timed out."
            )

Output:

    Request timed out.

The application does not wait indefinitely for the result.

---

# 21.17️⃣ Retry vs Timeout

These concepts solve different problems.

| Concept | Purpose |
|---|---|
| Retry | Try an operation again |
| Timeout | Limit how long to wait |
| Graceful Failure | Handle failure safely |

They can work together:

    Request
       ↓
    Timeout
       ↓
    Retry
       ↓
    Timeout
       ↓
    Retry
       ↓
    Final Failure
       ↓
    Graceful Response

---

# 21.18️⃣ Practical Example 13 — Edge Cases

AI systems should handle unusual inputs.

Example:

    prompt = "   "


    if not prompt.strip():

        print(
            "Prompt cannot be empty."
        )

Output:

    Prompt cannot be empty.

Other AI-related edge cases include:

- Empty prompt
- Extremely long prompt
- Missing parameters
- Invalid temperature
- Invalid token count
- Empty API response
- Missing response fields
- No retrieved documents
- Tool failure

---

# 21.19️⃣ Practical Example 14 — Clean Code

Instead of putting everything into one large function:

    def process_everything():
        ...

Separate responsibilities:

    def validate_request():
        ...


    def retrieve_context():
        ...


    def build_prompt():
        ...


    def generate_response():
        ...


    def format_response():
        ...

This creates a modular application.

---

# 21.20️⃣ Practical Example 15 — Testing

Suppose we have:

    def calculate_average(
        numbers: list[int]
    ) -> float:

        if not numbers:

            raise ValueError(
                "Numbers list cannot be empty."
            )

        return sum(numbers) / len(numbers)

A pytest test can be:

    import pytest


    def test_average():

        assert calculate_average(
            [10, 20, 30]
        ) == 20


    def test_empty_list():

        with pytest.raises(
            ValueError
        ):

            calculate_average([])

This combines:

    Clean Code
         +
    Type Hints
         +
    Edge Cases
         +
    Exception Handling
         +
    Unit Testing
         +
    Pytest

---

# 21.21️⃣ Complete Integrated AI Example

The following example combines many concepts learned throughout Chapter 15.

    import logging

    from pydantic import (
        BaseModel,
        Field,
        ValidationError
    )


    # Configure application logging.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
        force=True
    )


    # Custom exception for invalid AI requests.
    class InvalidAIRequestError(
        Exception
    ):
        pass


    # Structured AI chat request model.
    class ChatRequest(BaseModel):

        # User prompt must contain at least one character.
        prompt: str = Field(
            min_length=1
        )

        # Token limit must remain within the allowed range.
        max_tokens: int = Field(
            default=200,
            ge=1,
            le=4096
        )

        # Temperature must remain between 0 and 2.
        temperature: float = Field(
            default=0.7,
            ge=0,
            le=2
        )


    def generate_response(
        request: ChatRequest
    ) -> str:

        # Record that a valid AI request was received.
        logging.info(
            "AI request received."
        )

        # Simulate an AI response.
        response = (
            f"AI response for: "
            f"{request.prompt}"
        )

        return response


    def process_chat_request(
        prompt: str,
        max_tokens: int = 200,
        temperature: float = 0.7
    ) -> str:

        # Validate the incoming AI request.
        try:

            request = ChatRequest(
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )

        except ValidationError as e:

            # Record the validation failure.
            logging.error(
                "AI request validation failed."
            )

            # Convert the validation error into
            # an application-specific exception.
            raise InvalidAIRequestError(
                "Invalid AI request. "
                "Please check prompt, max_tokens, "
                "and temperature."
            ) from e


        # Generate and return the AI response.
        return generate_response(
            request
        )


    # Process the request safely.
    try:

        response = process_chat_request(
            prompt="Explain Machine Learning.",
            max_tokens=200,
            temperature=0.7
        )

        print(
            "Response:",
            response
        )

    except InvalidAIRequestError as e:

        # Handle the application-specific failure.
        logging.error(
            "Request failed: %s",
            e
        )

        print(
            "Request failed:",
            e
        )

Output:

    INFO - AI request received.
    Response: AI response for: Explain Machine Learning.

The response is simulated.

---

# 21.22️⃣ Testing the Integrated Example

The integrated application can be tested using pytest.

For example, we can test a valid request:

    def test_valid_request():

        response = process_chat_request(
            prompt="Explain Machine Learning.",
            max_tokens=200,
            temperature=0.7
        )

        assert (
            response
            == "AI response for: Explain Machine Learning."
        )

We can also test invalid input:

    def test_invalid_max_tokens():

        with pytest.raises(
            InvalidAIRequestError
        ):

            process_chat_request(
                prompt="Explain AI.",
                max_tokens=5000,
                temperature=0.7
            )

This verifies that invalid AI configuration is rejected.

---

# 21.23️⃣ Integrated Architecture

The complete flow can be visualized as:

    User Input
         ↓
    Type Hints
         ↓
    Pydantic Validation
         ↓
    Invalid?
      ↙     ↘
    Yes      No
     ↓        ↓
    Custom   AI Service
    Error       ↓
       ↓     Logging
    Error       ↓
    Message   Response
                ↓
             User


For external services:

    AI Service
         ↓
    Timeout?
      ↙    ↘
    Yes     No
     ↓       ↓
    Retry   Response
     ↓
    Failure?
      ↓
    Graceful Failure

---

# 21.24️⃣ Chapter 15 Concepts in One AI Application

| Chapter Concept | AI Engineering Application |
|---|---|
| Robust Code | Reliable AI applications |
| Defensive Programming | Prevent invalid operations |
| Input Validation | Validate prompts and API data |
| Type Hinting | Clear data expectations |
| `typing` | Complex type definitions |
| Pydantic | Structured request validation |
| Exception Handling | Handle application failures |
| Custom Exceptions | Represent AI-specific errors |
| `assert` | Check internal assumptions |
| Logging | Monitor application behavior |
| Proper Error Messages | Clear failure information |
| Resource Management | Safely handle files/connections |
| Configuration | Manage models and settings |
| Retry Logic | Recover from temporary API failures |
| Timeouts | Prevent indefinite waiting |
| Graceful Failure | Safe failure behavior |
| Edge Cases | Handle unusual input |
| Clean Code | Maintainable architecture |
| Testing | Verify application behavior |
| Unit Testing | Test individual components |
| Pytest | Automate Python tests |

---

# 21.25️⃣ AI Engineer Production Flow

A more realistic AI application may eventually follow:

    User
      ↓
    API Endpoint
      ↓
    Authentication
      ↓
    Input Validation
      ↓
    Pydantic Model
      ↓
    Business Logic
      ↓
    ┌────────────────────────┐
    │                        │
    ↓                        ↓
    Retrieval             External API
    ↓                        ↓
    Vector DB              Timeout
    ↓                        ↓
    Context                Retry
    │                        ↓
    └──────────┬─────────────┘
               ↓
          Prompt Builder
               ↓
              LLM
               ↓
        Response Validation
               ↓
            Logging
               ↓
          Final Response
               ↓
             User

Testing can exist around many of these components.

---

# 21.26️⃣ What You Have Learned in Chapter 15

This chapter started with writing code that simply works.

It then moved toward writing code that is:

    Reliable
       ↓
    Validated
       ↓
    Typed
       ↓
    Testable
       ↓
    Maintainable
       ↓
    Production-Oriented

The major progression was:

    Robust Code
         ↓
    Defensive Programming
         ↓
    Input Validation
         ↓
    Type Hinting
         ↓
    Pydantic
         ↓
    Exception Handling
         ↓
    Custom Exceptions
         ↓
    assert
         ↓
    Logging
         ↓
    Proper Error Messages
         ↓
    Resource Management
         ↓
    Configuration
         ↓
    Retry
         ↓
    Timeouts
         ↓
    Graceful Failure
         ↓
    Edge Cases
         ↓
    Clean Code
         ↓
    Testing
         ↓
    Unit Testing
         ↓
    Pytest
         ↓
    AI Engineering Applications

---

# 🧠 Key Takeaways

- AI applications require more than just model calls.
- Reliable AI systems need validation, error handling, logging, testing, and clean architecture.
- Type hints make AI application code easier to understand.
- Pydantic provides structured runtime validation.
- Custom exceptions make application-specific failures easier to handle.
- Logging helps developers understand what happens inside an application.
- Retry logic can recover from temporary failures.
- Timeouts prevent applications from waiting indefinitely.
- Graceful failure prevents uncontrolled application crashes.
- Edge-case handling makes systems more robust.
- Clean code makes AI applications easier to maintain and extend.
- Unit testing verifies individual components.
- Pytest makes automated Python testing simpler.
- Many AI components can be tested without calling a real LLM.
- Validation, preprocessing, retrieval, prompt construction, and response parsing are good candidates for automated testing.
- These concepts form an important foundation for building production-oriented AI applications.

# 📊 Important Comparisons

This section summarizes the major concepts covered throughout Chapter 15 and highlights the differences between concepts that are easy to confuse.

---

# 1️⃣ Robust Code vs Defensive Programming

| Robust Code | Defensive Programming |
|---|---|
| Focuses on reliable behavior | Focuses on anticipating problems |
| Handles unexpected situations | Prevents problems before they occur |
| Broader concept | Specific programming approach |
| Includes validation and error handling | Uses validation, checks, and safeguards |
| Goal is predictable behavior | Goal is to protect the program from invalid situations |

Relationship:

    Defensive Programming
           ↓
    Helps Build Robust Code

---

# 2️⃣ Input Validation vs Pydantic

| Input Validation | Pydantic |
|---|---|
| General concept | Python library |
| Can be written manually | Provides structured validation |
| Can use `if`, `try`, `raise`, etc. | Uses models and type hints |
| Flexible | Useful for structured data |
| Can become repetitive | Reduces validation boilerplate |

Example manual validation:

    if temperature < 0 or temperature > 2:

        raise ValueError(
            "Temperature must be between 0 and 2."
        )

Pydantic approach:

    temperature: float = Field(
        ge=0,
        le=2
    )

---

# 3️⃣ Type Hints vs Runtime Validation

| Type Hints | Runtime Validation |
|---|---|
| Describe expected types | Checks actual data |
| Mainly improve readability and tooling | Protects the application at runtime |
| Do not automatically reject invalid values | Can reject invalid values |
| Example: `age: int` | Example: Pydantic validation |

Example:

    age: int

This tells developers and tools that `age` is expected to be an integer.

It does not by itself provide complete runtime validation.

Pydantic can provide runtime validation.

---

# 4️⃣ `raise` vs `assert`

| `raise` | `assert` |
|---|---|
| Explicitly raises an exception | Checks an assumption |
| Suitable for application validation | Mainly useful for debugging/internal assumptions |
| Should not be disabled for normal validation | Can be disabled with Python optimization |
| Example: `raise ValueError(...)` | Example: `assert temperature <= 2` |

For user input validation, explicit validation and exceptions are generally more appropriate.

---

# 5️⃣ Exception Handling vs Graceful Failure

| Exception Handling | Graceful Failure |
|---|---|
| Mechanism for handling exceptions | Overall failure-handling strategy |
| Uses `try`, `except`, `finally`, etc. | May include exceptions, logging, fallback, retry, and user communication |
| Focuses on errors | Focuses on safe application behavior |
| Can be a part of graceful failure | Can use multiple techniques together |

Relationship:

    Exception Handling
          +
    Logging
          +
    Retry
          +
    Timeout
          +
    Fallback
          ↓
    Graceful Failure

---

# 6️⃣ Retry vs Timeout

| Retry | Timeout |
|---|---|
| Attempts an operation again | Limits waiting time |
| Useful for temporary failures | Useful for slow operations |
| Controls number of attempts | Controls maximum waiting period |
| Example: retry API request 3 times | Example: wait only 5 seconds |

They can be combined:

    API Request
         ↓
      Timeout
         ↓
      Failure
         ↓
       Retry
         ↓
      Timeout
         ↓
    Final Failure
         ↓
    Graceful Failure

---

# 7️⃣ Logging vs `print()`

| `print()` | Logging |
|---|---|
| Mainly for direct console output | Designed for application event recording |
| Limited control | Supports log levels |
| Less suitable for production monitoring | Better suited for applications |
| No built-in severity levels | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| Basic output | Can write to files and other handlers |

Example:

    logging.info(
        "AI request received."
    )

is generally more useful for application logging than:

    print(
        "AI request received."
    )

---

# 8️⃣ Custom Exception vs Built-in Exception

| Built-in Exception | Custom Exception |
|---|---|
| Provided by Python | Created by the developer |
| General error categories | Application-specific error categories |
| Examples: `ValueError`, `TypeError` | Example: `InvalidAIRequestError` |
| Useful for common errors | Useful for domain-specific failures |

Example:

    class InvalidAIRequestError(
        Exception
    ):
        pass

---

# 9️⃣ Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
|---|---|
| Tests individual components | Tests multiple components together |
| Usually fast | Usually slower |
| More isolated | Components interact |
| Easier to debug | More complex |
| Example: test `build_prompt()` | Example: retrieval + database |

---

# 🔟 Unit Testing vs End-to-End Testing

| Unit | End-to-End |
|---|---|
| Small component | Complete workflow |
| Fast | Usually slower |
| Highly focused | Broad |
| Easier to isolate failures | Failure may occur anywhere |
| Example: `validate_prompt()` | User → API → RAG → LLM → Response |

---

# 1️⃣1️⃣ `unittest` vs Pytest

| `unittest` | Pytest |
|---|---|
| Built into Python | Installed separately |
| Uses `TestCase` commonly | Simple test functions are common |
| Uses methods such as `assertEqual()` | Uses normal `assert` |
| More boilerplate | More concise |
| `assertRaises()` | `pytest.raises()` |
| Supports test organization | Provides fixtures and parameterization |
| Standard library framework | Extensive plugin ecosystem |

Both are valid Python testing frameworks.

---

# 1️⃣2️⃣ Edge Cases vs Invalid Inputs

An edge case is not necessarily invalid.

Example:

    temperature = 0

This may be a valid boundary value.

An invalid value might be:

    temperature = 5

if the allowed range is:

    0 to 2

Therefore:

    Edge Case
       ↓
    Unusual / Boundary Situation

while:

    Invalid Input
       ↓
    Data That Violates Requirements

Sometimes an edge case can also be invalid.

---

# 1️⃣3️⃣ Clean Code vs Over-Engineering

| Clean Code | Over-Engineering |
|---|---|
| Clear | Unnecessarily complicated |
| Maintainable | Difficult to maintain |
| Appropriate abstraction | Excessive abstraction |
| Simple where possible | Complexity without sufficient benefit |
| Focused responsibilities | Too many unnecessary components |

Clean code does not mean creating the maximum number of classes and files.

The goal is appropriate structure.

---

# 🤖 AI Engineering Relevance

Chapter 15 is important because AI Engineering is not only about calling an LLM.

A real AI application may contain:

    User
      ↓
    API
      ↓
    Authentication
      ↓
    Input Validation
      ↓
    Pydantic Model
      ↓
    Business Logic
      ↓
    Data Processing
      ↓
    Retrieval
      ↓
    Vector Database
      ↓
    Prompt Construction
      ↓
    LLM
      ↓
    Response Processing
      ↓
    Logging
      ↓
    Final Response

Every stage can introduce errors.

---

# 1️⃣4️⃣ Where Chapter 15 Concepts Fit in AI Engineering

## Input Validation

Used for:

- User prompts
- API requests
- Model parameters
- Configuration
- Tool inputs

Example:

    temperature: float

with a valid range.

---

## Type Hinting

Used for:

- Function parameters
- Return values
- Data structures
- API models
- Internal application logic

Example:

    def generate_response(
        prompt: str
    ) -> str:
        ...

---

## Pydantic

Useful for:

- API request models
- API response models
- Configuration models
- Agent tool inputs
- Structured AI data

Example:

    class ChatRequest(BaseModel):

        prompt: str

        max_tokens: int = 200

        temperature: float = 0.7

---

## Exception Handling

Used for:

- API failures
- Database errors
- File errors
- Validation errors
- Network failures
- Unexpected application conditions

---

## Custom Exceptions

Useful for application-specific failures.

Example:

    class AIServiceError(
        Exception
    ):
        pass

---

## Logging

Useful for observing:

    Request Received
    Validation
    Retrieval
    API Call
    Retry
    Timeout
    Error
    Response

This becomes particularly important when debugging deployed AI applications.

---

## Retry Logic

Useful when an external service experiences temporary failures.

Examples:

- AI API
- Embedding API
- Vector database
- External tools

---

## Timeouts

Useful when an external operation takes too long.

Examples:

- LLM API
- Database request
- Web request
- Tool execution

---

## Graceful Failure

Useful when an AI system cannot complete an operation.

Possible responses:

    Retry
    ↓
    Fallback
    ↓
    Safe Error Response

---

## Edge Cases

AI systems must consider:

- Empty prompts
- Very large prompts
- Missing data
- Invalid parameters
- No retrieved documents
- Empty API responses
- Tool failures
- Unexpected model responses

---

## Clean Code

Useful for organizing:

    API
    Services
    Models
    Retrieval
    Configuration
    Validation
    Testing

into manageable components.

---

## Testing

Used to verify:

- Validation
- Data processing
- Retrieval logic
- Prompt construction
- Response parsing
- Error handling
- API behavior

---

# 1️⃣5️⃣ AI Engineer Practical Architecture

A maintainable AI application can follow a structure such as:

    ai_project/
    │
    ├── app/
    │   ├── main.py
    │   ├── config.py
    │   ├── models.py
    │   ├── validation.py
    │   │
    │   ├── services/
    │   │   ├── llm_service.py
    │   │   ├── embedding_service.py
    │   │   └── retrieval_service.py
    │   │
    │   └── utils/
    │       └── logging_utils.py
    │
    └── tests/
        ├── test_validation.py
        ├── test_retrieval.py
        ├── test_prompt_builder.py
        └── test_response_parser.py

This is only an example structure.

The appropriate structure depends on the size and requirements of the project.

---

# 1️⃣6️⃣ AI Application Reliability Flow

A reliable AI application can be thought of as:

    Input
      ↓
    Validate
      ↓
    Structure
      ↓
    Process
      ↓
    External Service
      ↓
    Timeout / Retry
      ↓
    Response Validation
      ↓
    Logging
      ↓
    Safe Response

If something goes wrong:

    Failure
      ↓
    Detect
      ↓
    Log
      ↓
    Recover / Retry / Fallback
      ↓
    Respond Safely

---

# 📋 Final Chapter Checklist

Use this checklist to review Chapter 15.

## Robustness

    [ ] I understand what robust code means.
    [ ] I understand how fragile code differs from robust code.
    [ ] I can design code that handles unexpected situations.

## Defensive Programming

    [ ] I understand defensive programming.
    [ ] I can anticipate invalid inputs.
    [ ] I can add safeguards before risky operations.

## Input Validation

    [ ] I can validate user input.
    [ ] I can validate ranges.
    [ ] I can validate empty input.
    [ ] I can validate input length.
    [ ] I can validate expected formats.

## Type Hinting

    [ ] I understand basic type hints.
    [ ] I can add parameter type hints.
    [ ] I can add return type hints.
    [ ] I understand the `typing` module.
    [ ] I understand `List`, `Dict`, `Tuple`, `Set`, `Optional`, and `Union`.
    [ ] I understand modern type-hint syntax.

## Pydantic

    [ ] I understand `BaseModel`.
    [ ] I can create a Pydantic model.
    [ ] I understand required and default fields.
    [ ] I understand `Field`.
    [ ] I can apply validation constraints.
    [ ] I understand `ValidationError`.
    [ ] I can use Pydantic for structured AI request data.

## Exception Handling

    [ ] I can handle specific exceptions.
    [ ] I understand `as e`.
    [ ] I understand `else` and `finally`.
    [ ] I understand `raise`.
    [ ] I understand re-raising.
    [ ] I understand exception chaining.

## Custom Exceptions

    [ ] I can create a custom exception.
    [ ] I understand when custom exceptions are useful.
    [ ] I can handle custom exceptions.

## `assert`

    [ ] I understand what `assert` does.
    [ ] I understand how `assert` differs from `raise`.
    [ ] I understand why `assert` should not be the primary mechanism for user-input validation.

## Logging

    [ ] I understand why logging is useful.
    [ ] I can use the `logging` module.
    [ ] I understand DEBUG, INFO, WARNING, ERROR, and CRITICAL.
    [ ] I can configure a logging format.
    [ ] I can log to a file.
    [ ] I understand `logging.exception()`.

## Error Messages

    [ ] I can write meaningful error messages.
    [ ] I can include useful context.
    [ ] I understand user-facing vs developer-facing messages.
    [ ] I avoid exposing sensitive information.

## Resource Management

    [ ] I understand resource management.
    [ ] I understand the `with` statement.
    [ ] I understand context managers.
    [ ] I understand `__enter__()` and `__exit__()`.
    [ ] I understand why resources should be released properly.

## Configuration

    [ ] I understand configuration handling.
    [ ] I understand environment variables.
    [ ] I know why API keys should not be hard-coded.
    [ ] I understand separating configuration from application logic.

## Retry Logic

    [ ] I understand retry logic.
    [ ] I can limit the number of retries.
    [ ] I understand retry delays.
    [ ] I understand exponential backoff conceptually.
    [ ] I understand that not every error should be retried.

## Timeouts

    [ ] I understand what a timeout is.
    [ ] I understand timeout vs retry.
    [ ] I can handle timeout failures.

## Graceful Failure

    [ ] I understand graceful failure.
    [ ] I can handle failures without uncontrolled crashes.
    [ ] I understand fallback behavior.
    [ ] I understand graceful failure in AI applications.

## Edge Cases

    [ ] I can identify edge cases.
    [ ] I can test boundary values.
    [ ] I can handle empty input.
    [ ] I can handle `None`.
    [ ] I can handle missing data.
    [ ] I can consider unusual API responses.

## Clean Code

    [ ] I use meaningful variable names.
    [ ] I use meaningful function names.
    [ ] I keep functions focused.
    [ ] I avoid unnecessary duplication.
    [ ] I understand DRY.
    [ ] I understand separation of concerns.
    [ ] I can organize code into modules.
    [ ] I avoid unnecessary complexity.

## Testing

    [ ] I understand testing fundamentals.
    [ ] I understand test cases.
    [ ] I understand expected vs actual results.
    [ ] I understand assertions.
    [ ] I understand unit testing.
    [ ] I understand `unittest`.
    [ ] I understand common `unittest` assertions.
    [ ] I understand `assertRaises()`.

## Pytest

    [ ] I know how to install pytest.
    [ ] I can create pytest tests.
    [ ] I can run pytest from the terminal.
    [ ] I understand pytest test discovery.
    [ ] I understand fixtures.
    [ ] I understand parameterization.
    [ ] I understand `pytest.raises()`.
    [ ] I understand basic markers.
    [ ] I can organize tests for a project.

## AI Engineering

    [ ] I can connect these concepts to AI applications.
    [ ] I understand validation of AI requests.
    [ ] I understand structured AI request models.
    [ ] I understand AI API failure handling.
    [ ] I understand retry and timeout strategies.
    [ ] I understand testing deterministic AI components.
    [ ] I understand how these concepts contribute to production-oriented AI systems.

---

# 🎯 Chapter 15 Final Summary

Chapter 15 focused on writing Python code that is not only functional but also reliable, maintainable, testable, and suitable as a foundation for AI Engineering.

The complete progression was:

    Robust Code
         ↓
    Defensive Programming
         ↓
    Input Validation
         ↓
    Type Hinting & typing
         ↓
    Pydantic & BaseModel
         ↓
    Advanced Exception Handling
         ↓
    Custom Exceptions
         ↓
    assert
         ↓
    Logging
         ↓
    Proper Error Messages
         ↓
    Resource Management
         ↓
    Configuration Handling
         ↓
    Retry Logic
         ↓
    Timeouts
         ↓
    Graceful Failure
         ↓
    Edge Cases
         ↓
    Clean & Maintainable Code
         ↓
    Testing Fundamentals
         ↓
    Unit Testing
         ↓
    Pytest
         ↓
    AI Engineer Practical Applications

---

# 🧠 Final Chapter Takeaways

The major lesson of Chapter 15 is:

> **Good Python code should not only work; it should also handle failure, validate data, remain understandable, and be testable.**

For AI Engineering, this becomes even more important because AI applications often depend on multiple external components.

A reliable AI application should be prepared for:

    Invalid Input
    Missing Data
    API Failure
    Timeout
    Temporary Network Error
    Unexpected Response
    Empty Retrieval Result
    Tool Failure
    Configuration Error
    Application Bug

The concepts learned in this chapter provide the foundation for handling these situations systematically.

---

# 🚀 Chapter 15 → AI Engineering Connection

The Python foundation now looks like:

    Python Fundamentals
          ↓
    OOP
          ↓
    Advanced Python
          ↓
    Concurrency
          ↓
    Robust Python Code
          ↓
    NumPy
          ↓
    Pandas
          ↓
    Matplotlib / Seaborn
          ↓
    Mathematics for ML
          ↓
    Machine Learning
          ↓
    Deep Learning
          ↓
    NLP / Transformers
          ↓
    LLMs
          ↓
    RAG
          ↓
    AI Agents
          ↓
    APIs / FastAPI
          ↓
    Deployment / MLOps
          ↓
    Production AI Systems

Chapter 15 strengthens the Python foundation required before moving deeper into data science and machine learning.

---

# 📚 Course Information

**Course:** Python for AI Engineering  
**Chapter:** 15  
**Topic:** Robust Python Code  
**Language:** Python

---

# 👨‍💻 Author

**Sonal Rai**