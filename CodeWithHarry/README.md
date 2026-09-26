# 🐍 CodeWithHarry — Python Programming

<p align="center">
  <img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AI%2FML-Foundation-green?style=for-the-badge" alt="AI/ML Foundation">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Completed">
  <img src="https://img.shields.io/badge/Chapters-15-orange?style=for-the-badge" alt="15 Chapters">
  <img src="https://img.shields.io/badge/Projects-2-purple?style=for-the-badge" alt="2 Projects">
</p>

<p align="center">
  <b>Building a Strong Python Foundation for AI/ML and AI Engineering</b>
</p>

---

## 🎯 Objective

This repository documents my Python learning journey through the **CodeWithHarry Python course**, along with additional self-learning beyond the core course.

The main goal of this journey is not only to learn Python syntax, but to build a strong programming foundation for my future path in:

- 🤖 Artificial Intelligence
- 🧠 Machine Learning
- 📊 Data Analysis
- 🔬 Data Science
- ⚙️ AI Engineering
- 🚀 Generative AI

Python is one of the major programming languages used throughout the AI/ML ecosystem. Therefore, this repository focuses on developing strong Python fundamentals before moving toward libraries, frameworks, and real-world AI/ML applications.

---

# 📚 About This Folder

This folder contains:

- 📖 **13 chapters** completed from the CodeWithHarry Python learning path
- 🚀 **2 additional chapters** studied independently
- 💻 **2 Python projects**
- 📝 Chapter-wise README documentation
- 🧪 Practice programs
- 🐍 Python concepts from beginner to advanced level
- 🤖 AI/ML-oriented examples and concepts wherever relevant

The purpose of maintaining this repository is to keep my learning structured, revision-friendly, and connected to my long-term goal of becoming an **AI/ML Engineer**.

---

# 🗂️ Folder Structure

```text
CodeWithHarry/
│
├── CHAPTER 01/
├── CHAPTER 02/
├── CHAPTER 03/
├── CHAPTER 04/
├── CHAPTER 05/
├── CHAPTER 06/
├── CHAPTER 07/
├── CHAPTER 08/
├── CHAPTER 09/
├── CHAPTER 10/
├── CHAPTER 11/
├── CHAPTER 12/
├── CHAPTER 13/
│
├── CHAPTER 14/              ← Additional Self-Learning
├── CHAPTER 15/              ← Additional Self-Learning
│
└── PROJECTS/
    ├── PROJECT 01 - Snake Water Gun Game
    └── PROJECT 02 - The Perfect Guess
```

Each chapter contains Python source files, practice material where applicable, and a dedicated `README.md` for revision and documentation.

---

# 📖 Core Course — Chapters 01–13

## 🟢 Chapter 01 — Modules & pip

### Topics Covered

- Python modules
- Importing modules
- Creating custom modules
- Using functions from modules
- Module-based code organization
- Introduction to `pip`
- Using external Python packages

### Why It Matters

Modules and packages are essential when building larger Python applications.

As I move toward AI/ML, I will work with many external libraries such as:

```text
NumPy
Pandas
Matplotlib
Scikit-learn
PyTorch
TensorFlow
```

Understanding imports, modules, and packages provides the foundation for working with these libraries.

---

## 🟢 Chapter 02 — Variables, Data Types & Operators

### Topics Covered

- Variables
- Python data types
- Integers
- Floating-point numbers
- Strings
- Booleans
- Type checking
- Type conversion
- User input
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Other Python operators

### Why It Matters

Almost every AI/ML program involves working with data.

Understanding basic types such as:

```python
int
float
str
bool
```

and knowing how operators work is essential before moving toward numerical computing and data analysis.

---

## 🟢 Chapter 03 — Strings

### Topics Covered

- String creation
- String indexing
- String slicing
- Escape characters
- String methods
- String manipulation
- String formatting
- Working with textual data

### Why It Matters

String manipulation is useful in many areas of AI and software development, including:

- Natural Language Processing
- Generative AI
- Prompt Engineering
- Data Cleaning
- Text Processing
- Feature Engineering

Strong string fundamentals are especially useful when dealing with real-world text data.

---

## 🟢 Chapter 04 — Lists & Tuples

### Topics Covered

### Lists

- Creating lists
- Indexing
- Slicing
- Updating elements
- Adding elements
- Removing elements
- List methods
- Iterating through lists

### Tuples

- Creating tuples
- Indexing
- Slicing
- Tuple methods
- Tuple immutability
- Lists vs Tuples

### Why It Matters

Lists and tuples are fundamental Python data structures.

They are commonly used for:

- Storing collections of data
- Iteration
- Data processing
- Algorithm implementation
- Preparing data before using specialized libraries

Understanding these structures also helps build the conceptual foundation for working with more advanced data-processing tools.

---

## 🟢 Chapter 05 — Dictionaries & Sets

### Topics Covered

### Dictionaries

- Dictionary creation
- Key-value pairs
- Accessing values
- Updating dictionaries
- Dictionary methods
- Iterating through dictionaries

### Sets

- Set creation
- Unique elements
- Set methods
- Set operations
- Adding and removing elements

### Why It Matters

Dictionaries are extremely useful when working with structured information.

Example:

```python
student = {
    "name": "Sonal",
    "age": 21,
    "course": "B.Tech CSE"
}
```

Key-value structures are commonly encountered in:

- JSON
- APIs
- Configuration files
- Metadata
- Data preprocessing
- AI applications

Sets are useful when uniqueness and mathematical set operations are required.

---

## 🟢 Chapter 06 — Conditional Statements

### Topics Covered

- `if`
- `elif`
- `else`
- Nested conditions
- Conditional expressions
- Decision-making logic
- Combining conditions with logical operators

### Why It Matters

Conditional logic is one of the fundamental building blocks of programming.

Example:

```python
if accuracy >= 90:
    print("Excellent model")
elif accuracy >= 70:
    print("Acceptable model")
else:
    print("Model needs improvement")
```

The same fundamental decision-making concepts are used throughout larger programs and AI/ML applications.

---

## 🟢 Chapter 07 — Loops

### Topics Covered

- `for` loops
- `while` loops
- `range()`
- Iteration
- Iterating through lists
- `break`
- `continue`
- `pass`
- `for` loop with `else`
- `while` loop concepts
- Building lists using loops

### Why It Matters

Loops are fundamental for repetitive operations and data processing.

They are useful for:

- Processing collections
- Iterating through records
- File processing
- Algorithm implementation
- Repetitive calculations
- Model evaluation logic

Understanding loops also makes it easier to understand how higher-level data-processing operations work.

---

## 🟢 Chapter 08 — Functions & Recursion

### Topics Covered

- Defining functions
- Calling functions
- Function arguments
- Different types of arguments
- Return values
- `print()` vs `return`
- Reusable functions
- Recursion
- Recursive functions

### Why It Matters

Functions allow programs to be divided into reusable and manageable components.

Example:

```python
def calculate_accuracy(correct, total):
    return correct / total
```

Functions are important when building:

- Data preprocessing utilities
- Feature engineering functions
- Model evaluation functions
- AI pipelines
- Reusable application logic

---

## 🟢 Chapter 09 — File Input/Output

### Topics Covered

- Introduction to File I/O
- Opening files
- Reading files
- Writing files
- Appending data
- File modes
- `with` statement
- `seek()`
- `tell()`
- Working with file paths
- Working with text files

### Why It Matters

Real-world applications frequently need to read and write external data.

Examples include:

```text
Text files
Datasets
Configuration files
Logs
JSON files
```

File handling provides an important foundation before moving toward specialized data-analysis libraries.

---

## 🟢 Chapter 10 — OOP Basics

### Topics Covered

- Classes
- Objects
- Instance attributes
- Class attributes
- `self`
- Constructors
- `__init__()`
- Object-oriented program structure

### Why It Matters

Object-Oriented Programming becomes increasingly useful as applications become larger.

Understanding OOP helps when working with:

- Machine Learning models
- Data processing components
- AI pipelines
- APIs
- Frameworks
- Larger Python projects

Many Python libraries and frameworks are designed around classes and objects.

---

# 🟢 Chapter 11 — OOP Advanced

Chapter 11 focuses on advanced Object-Oriented Programming concepts.

## 🔹 Inheritance

- Basic inheritance
- Single inheritance
- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance
- Hybrid inheritance

The different inheritance types were practiced separately to understand how each form works.

---

## 🔹 `super()` & Method Resolution Order

- `super()`
- Calling parent methods
- Calling parent constructors
- Passing arguments through `super()`
- Method Resolution Order (MRO)
- MRO in multiple inheritance
- C3 linearization
- Cooperative inheritance
- `super()` with MRO

---

## 🔹 Class Methods

- `@classmethod`
- `cls`
- Class attributes
- Class-level operations
- Alternative constructors

---

## 🔹 Property Decorators

- `@property`
- Getter
- Setter
- Deleter
- Getter + Setter + Deleter
- Read-only properties
- Property-based validation

---

## 🔹 Operator Overloading

- Magic / dunder methods
- Arithmetic operators
- Comparison operators
- `__str__()`
- `__len__()`
- Custom object behavior

---

## 🔹 Encapsulation

- Public members
- Protected members
- Private members
- Private variables
- Name mangling
- Getters
- Setters
- Setter validation
- Property decorators with encapsulation

---

## 🔹 Polymorphism

- Method overriding
- Method overriding with `super()`
- Duck typing
- Method overloading concepts
- Default arguments
- `*args`
- `**kwargs`
- Built-in function polymorphism

---

## 🔹 Abstraction

- Abstract classes
- `ABC`
- `@abstractmethod`
- Abstract methods
- Abstract properties
- `raise NotImplementedError`
- Practical abstraction

---

## 🔹 Composition

- HAS-A relationship
- Object composition
- Composition vs inheritance
- Component-based design
- Dependency injection
- Building larger systems from smaller components

### Why It Matters for AI/ML

Advanced OOP becomes useful when developing larger AI systems.

For example:

```text
AI Pipeline
│
├── Data Loader
├── Preprocessor
├── Model
├── Evaluator
└── Predictor
```

Each component can be represented by a separate class with a clear responsibility.

This makes larger AI/ML applications easier to organize, maintain, test, and extend.

---

# 🟢 Chapter 12 — Advanced Python Features

### Topics Covered

- Walrus operator `:=`
- Type definitions / type annotations
- `match-case`
- Dictionary merging
- Multiple context managers
- Exception handling
- Raising errors
- `try-except`
- `try-except-else`
- `try-except-finally`
- Global and local scope
- `enumerate()`
- List comprehensions
- JSON handling

### Supporting Files

This chapter also includes practical files and data such as:

```text
file1.txt
file2.txt
student.json
main.py
test.py
```

### Why It Matters

These features help in writing cleaner and more robust Python programs.

JSON handling is particularly useful because JSON is widely used for:

- Configuration
- API responses
- Metadata
- Data exchange
- AI application data

Exception handling is also essential for dealing with unexpected situations safely.

---

# 🟢 Chapter 13 — Python Tools & Functional Programming

### Virtual Environments

- Virtual environments
- Environment isolation

### Package Management

- `pip`
- Installing packages
- `pip freeze`
- `requirements.txt`

### Functional Programming

- Lambda functions
- `map()`
- `filter()`
- `reduce()`
- Combining `map()`, `filter()` and `lambda`

### Useful Python Features

- `join()`
- String formatting
- `*args`
- `**kwargs`
- `zip()`
- `sorted()`
- `any()`
- `all()`
- `pathlib`
- `os`
- Environment variables
- `.env`
- Modules and packages

### Supporting Files

```text
pip_freeze.txt
requirements.txt
```

### Why It Matters for AI Engineering

This chapter connects Python programming with real project environments.

Virtual environments and dependency management become especially important in AI/ML because different projects can require different versions of libraries.

For example:

```text
Project A
├── NumPy version X
└── Other dependencies

Project B
├── NumPy version Y
└── Different dependencies
```

Virtual environments help keep these projects isolated.

---

# 🚀 Additional Self-Learning

Chapters 14 and 15 were studied **independently beyond the core CodeWithHarry course**.

They are included to strengthen Python knowledge for future software development and AI Engineering work.

---

# 🔵 Chapter 14 — Concurrency & Asynchronous Programming

### Topics Covered

- Concurrency basics
- Sequential vs concurrent execution
- Process vs thread
- Threading
- Starting and joining threads
- Multiple threads
- Race conditions
- Locks
- Thread safety
- Multiprocessing
- Processes
- Process pools
- Queues
- `concurrent.futures`
- `ThreadPoolExecutor`
- `ProcessPoolExecutor`
- `asyncio`
- `async`
- `await`
- Asyncio tasks
- `asyncio.gather()`
- I/O-bound vs CPU-bound tasks
- AI Engineer concurrency concepts

### Why It Matters for AI Engineering

AI applications often involve tasks such as:

```text
API calls
File operations
Database operations
Network requests
Data loading
Model serving
Multiple independent tasks
```

Understanding concurrency and asynchronous programming can help when building applications that need to manage multiple operations efficiently.

---

# 🔵 Chapter 15 — Robust, Defensive & Maintainable Python

### Topics Covered

### Robust & Defensive Programming

- Robust code
- Defensive programming
- Input validation
- Type hinting
- Pydantic `BaseModel`

### Exception Handling

- Advanced exception handling
- Custom exceptions
- Assertions
- Proper error messages
- Graceful failure

### Logging & Configuration

- Logging
- Configuration handling
- Retry logic
- Timeouts

### Code Quality

- Edge cases
- Clean code
- Maintainable code

### Testing

- Testing fundamentals
- Unit testing
- `pytest`

### Why It Matters for AI Engineering

When moving from learning projects to production-oriented AI systems, code needs to handle more than the ideal case.

Real applications may encounter:

```text
Invalid input
Missing data
API failure
Timeout
Model failure
Unexpected values
Incorrect configuration
External service failure
```

Therefore, concepts such as validation, logging, exception handling, retries, timeouts, graceful failure, and testing are important foundations for building reliable AI applications.

# 💻 Projects

The learning journey also includes two Python projects that were created to apply the concepts learned throughout the course.

Projects are an important part of learning because they help convert individual programming concepts into a complete working application.

---

## 🎮 Project 01 — Snake Water Gun Game

A command-line based implementation of the classic **Snake, Water, Gun** game.

### 🔹 Concepts Applied

- Python variables
- User input
- Conditional statements
- Loops
- Functions
- Random module
- Game logic
- Score tracking
- Repeated gameplay
- External package usage
- Basic program structure

### 🔹 Core Game Logic

The game follows the relationship:

```text
Snake  → defeats Water
Water  → defeats Gun
Gun    → defeats Snake
```

The program accepts the player's choice, generates a computer choice, determines the winner, and maintains the score.

### 🔹 Why This Project Matters

This project combines multiple basic Python concepts into one complete application.

Instead of learning concepts individually:

```text
Variables
   +
Conditions
   +
Loops
   +
Functions
   +
Randomization
   ↓
Complete Python Application
```

It helped strengthen problem-solving and program-structuring skills.

---

# 🎯 Project 02 — The Perfect Guess

A number-guessing game in which the user attempts to guess a randomly generated number.

### 🔹 Concepts Applied

- Variables
- User input
- Conditional statements
- Loops
- Random numbers
- Comparison operators
- Attempt tracking
- Game logic

### 🔹 Basic Working

The general flow of the program is:

```text
Generate Random Number
        ↓
Take User Guess
        ↓
Compare Guess
        ↓
Too High / Too Low / Correct
        ↓
Continue Until Correct
```

### 🔹 Why This Project Matters

The project provides practical experience with:

- Control flow
- User interaction
- Comparisons
- Loops
- Randomization
- Building logic from scratch

It demonstrates how simple Python concepts can be combined to create an interactive program.

---

# 🧠 Skills Developed

Through the complete learning journey, I developed a foundation across several areas of Python.

## 🐍 Python Fundamentals

- Variables
- Data Types
- Operators
- Input and Output
- Type Casting
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Conditional Statements
- Loops
- Functions
- Recursion

---

## 📂 File & Data Handling

- File Input/Output
- Reading and Writing Files
- File Modes
- `with`
- `seek()`
- `tell()`
- JSON
- File Paths
- `pathlib`
- Environment Variables
- Configuration Handling

---

## 🏗️ Object-Oriented Programming

- Classes
- Objects
- Instance Attributes
- Class Attributes
- Constructors
- Inheritance
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance
- `super()`
- MRO
- Class Methods
- Property Decorators
- Operator Overloading
- Encapsulation
- Polymorphism
- Abstraction
- Composition

---

## ⚙️ Advanced Python

- Lambda Functions
- `map()`
- `filter()`
- `reduce()`
- `*args`
- `**kwargs`
- `zip()`
- `sorted()`
- `any()`
- `all()`
- Virtual Environments
- `pip`
- Modules
- Packages
- Exception Handling
- Custom Exceptions
- Type Hints
- Pydantic
- Logging
- Retry Logic
- Timeouts
- Testing
- `pytest`
- Threading
- Multiprocessing
- Concurrency
- `asyncio`
- `async`
- `await`

---

# 🛡️ Production-Oriented Python Concepts

The additional self-learning chapters introduced concepts that are useful when moving from simple learning programs toward reliable applications.

### Areas Covered

```text
Input Validation
      ↓
Type Hinting
      ↓
Exception Handling
      ↓
Custom Exceptions
      ↓
Logging
      ↓
Configuration
      ↓
Retry Logic
      ↓
Timeouts
      ↓
Graceful Failure
      ↓
Testing
```

These concepts are particularly useful when building applications that interact with external APIs, databases, models, or other services.

---

# 🤖 Python → AI/ML Learning Roadmap

Completing Python is the first major foundation stage of my AI/ML journey.

The planned progression is:

```text
                 🐍 PYTHON
                     │
                     ▼
        Core Python Foundation
                     │
                     ▼
                 🔢 NumPy
                     │
                     ▼
                 🐼 Pandas
                     │
                     ▼
          📊 Data Visualization
          Matplotlib / Seaborn
                     │
                     ▼
                   EDA
      Exploratory Data Analysis
                     │
                     ▼
          🤖 Machine Learning
                     │
                     ▼
           🧠 Deep Learning
                     │
                     ▼
        ✨ Generative AI / LLMs
                     │
                     ▼
             ⚙️ AI Engineering
```

The purpose of completing Python first is to build enough programming understanding to use AI/ML libraries effectively instead of treating them as black boxes.

---

# 📊 Learning Progression

| Stage | Focus | Status |
|---|---|---|
| Python Basics | Core syntax and programming | ✅ Completed |
| Data Structures | Lists, Tuples, Dictionaries, Sets | ✅ Completed |
| Functions | Functions and Recursion | ✅ Completed |
| File Handling | File I/O and JSON | ✅ Completed |
| OOP | Basic and Advanced OOP | ✅ Completed |
| Advanced Python | Modern and functional Python | ✅ Completed |
| Concurrency | Threading, Multiprocessing, Asyncio | ✅ Completed |
| Robust Python | Validation, Logging, Testing | ✅ Completed |
| NumPy | Numerical Computing | 🔜 Next |
| Pandas | Data Analysis | 🔜 Upcoming |
| Matplotlib / Seaborn | Data Visualization | 🔜 Upcoming |
| EDA | Exploratory Data Analysis | 🎯 Upcoming |
| Machine Learning | ML Algorithms & Projects | 🎯 Future |
| Deep Learning | Neural Networks & DL | 🎯 Future |
| Generative AI | LLMs & AI Applications | 🎯 Future |
| AI Engineering | Production AI Systems | 🎯 Goal |

---

# 📌 Why Python is Important for My AI/ML Journey

Python will continue to be used throughout the next stages of my learning.

The foundation built in this repository will support future work with:

```text
NumPy
Pandas
Matplotlib
Seaborn
Scikit-learn
PyTorch
TensorFlow
Transformers
Generative AI
LLM Applications
RAG
AI Agents
```

For example, basic Python data structures will later lead to numerical and tabular data processing:

```text
Python Lists / Dictionaries
          ↓
        NumPy
          ↓
        Pandas
          ↓
        Data Analysis
          ↓
   Machine Learning
```

Similarly, Python functions and OOP concepts will help in building reusable components for AI applications.

---

# 🗂️ Complete Folder Structure

```text
CodeWithHarry/
│
├── CHAPTER 01/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 02/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 03/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 04/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 05/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 06/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 07/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 08/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 09/
│   ├── PRACTICE SET/
│   ├── README.md
│   ├── Python source files
│   └── Sample text files
│
├── CHAPTER 10/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 11/
│   ├── PRACTICE SET/
│   ├── README.md
│   └── Python source files
│
├── CHAPTER 12/
│   ├── PRACTICE SET/
│   ├── README.md
│   ├── Python source files
│   ├── JSON files
│   └── Text files
│
├── CHAPTER 13/
│   ├── PRACTICE SET/
│   ├── README.md
│   ├── requirements.txt
│   └── pip_freeze.txt
│
├── CHAPTER 14/
│   ├── README.md
│   └── Concurrency & Async Python files
│
├── CHAPTER 15/
│   ├── README.md
│   ├── Python source files
│   └── bank.log
│
└── PROJECTS/
    ├── PROJECT 01 - Snake Water Gun Game
    └── PROJECT 02 - The Perfect Guess
```

---

# ⭐ Key Takeaways

- Python fundamentals provide the base for my AI/ML journey.
- Data structures are essential for handling and processing information.
- Functions help create reusable and maintainable programs.
- File handling provides a foundation for working with external data.
- OOP helps structure larger software systems.
- Exception handling helps programs handle unexpected situations.
- Virtual environments and dependency management are important for real projects.
- Functional programming features can make certain operations concise and expressive.
- Concurrency and asynchronous programming are useful for suitable I/O-bound workloads.
- Validation, logging, retries, timeouts, and testing help make applications more robust.
- Python will remain an important tool throughout the upcoming AI/ML learning journey.

---

# 🚀 What's Next?

With the Python foundation completed, the next phase of my learning journey is **Data Analysis**.

```text
🐍 Python
   ↓
🔢 NumPy
   ↓
🐼 Pandas
   ↓
📊 Matplotlib
   ↓
🎨 Seaborn
   ↓
🔍 Exploratory Data Analysis
   ↓
🤖 Machine Learning
```

The next repository in this journey will focus on:

> **Data Analysis Mastery**

with a focus on:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Exploratory Data Analysis

---

# 📚 Course Information

**Course:** CodeWithHarry — Python Programming

**Core Course Coverage:** Chapters 01–13

**Additional Self-Learning:** Chapters 14–15

**Projects:** 2

**Primary Language:** Python

**Learning Focus:** Python → Data Analysis → AI/ML → AI Engineering

---

# 👨‍💻 Author

**Sonal Rai**

B.Tech CSE Student | Aspiring AI/ML Engineer

---

<p align="center">
  🐍 <b>Python Foundation Completed</b>
  <br><br>
  📊 <b>Next Stop: Data Analysis</b>
  <br><br>
  🤖 <b>Long-Term Goal: AI Engineering</b>
</p>