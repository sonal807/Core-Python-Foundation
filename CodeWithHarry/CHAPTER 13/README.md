# 🐍 Chapter 13 — Python Tools & Advanced Utilities

# 📖 Chapter Introduction

Chapter 13 focuses on several important Python tools, functions, utilities, and programming techniques that are useful for writing practical, reusable, maintainable, and real-world Python applications.

In the previous chapters, we learned Python fundamentals, Object-Oriented Programming, advanced Python features, exception handling, file handling, JSON handling, comprehensions, and other important concepts.

In this chapter, we move towards **real-world Python development**.

The main focus of this chapter is not only learning new syntax, but also understanding how Python projects are managed and how Python's built-in and third-party tools can be used effectively.

This chapter covers:

- Virtual Environments
- `pip` and Package Management
- `requirements.txt`
- `pip freeze`
- Lambda Functions
- `map()`
- `filter()`
- `reduce()`
- Combining `map()`, `filter()`, and `lambda`
- `join()`
- String Formatting
- `*args` and `**kwargs`
- `zip()`
- `sorted()` with `key=`
- `any()` and `all()`
- `pathlib`
- Environment Variables
- `.env` Files
- `python-dotenv`
- Modules and Packages

These concepts are useful for Python development, automation, APIs, data processing, backend development, and eventually AI/ML and AI Engineering projects.

---

# 🎯 Chapter Overview

The purpose of this chapter is to develop practical Python development skills beyond basic programming.

We will learn how to:

- Create isolated Python environments
- Install and manage external packages
- Understand package versions
- Save project dependencies
- Recreate a project's environment
- Write small anonymous functions
- Transform collections using `map()`
- Filter collections using `filter()`
- Reduce collections to a single result using `reduce()`
- Combine functional programming tools
- Combine strings using `join()`
- Format strings professionally
- Accept a variable number of function arguments
- Work with multiple iterables using `zip()`
- Sort data according to custom conditions
- Check whether any or all elements satisfy a condition
- Work with files and directories using `pathlib`
- Access operating-system environment variables
- Keep configuration outside Python source code
- Protect sensitive values such as API keys from being hardcoded
- Organize reusable Python code using modules and packages

---

# 🎯 Learning Objectives

After completing this chapter, you should be able to:

1. Understand the purpose of a virtual environment.
2. Create and activate a Python virtual environment.
3. Install and manage packages using `pip`.
4. Check installed packages and their versions.
5. Understand package version specifications.
6. Create and understand `requirements.txt`.
7. Understand the purpose of `pip freeze`.
8. Recreate project dependencies using `requirements.txt`.
9. Create and use lambda functions.
10. Use `map()`, `filter()`, and `reduce()`.
11. Combine `lambda`, `map()`, and `filter()`.
12. Join strings using `join()`.
13. Format strings using f-strings and `.format()`.
14. Use `*args` and `**kwargs`.
15. Combine multiple iterables using `zip()`.
16. Sort data using `sorted()` and custom `key=` functions.
17. Use `any()` and `all()` for condition checking.
18. Work with paths using `pathlib`.
19. Access environment variables using `os`.
20. Understand `.env` files and `python-dotenv`.
21. Organize code using modules and packages.
22. Understand how these tools are used in real-world Python and AI projects.

---

# 1️⃣ Virtual Environment

## 📌 Definition

> A **virtual environment** is an isolated Python environment that allows a project to have its own Python packages and dependencies without affecting the global Python installation.

---

## 📖 What is a Virtual Environment?

A virtual environment creates an isolated environment for a Python project.

Normally, when we install a package globally, it becomes available to the global Python installation.

For example:

```text
Global Python
    │
    ├── requests
    ├── numpy
    └── pandas
```

If multiple projects use the same global environment, they may require different versions of the same package.

This can create dependency conflicts.

A virtual environment solves this problem by allowing each project to maintain its own dependencies.

---

# ❓ Why Do We Need Virtual Environments?

Suppose we have two projects.

```text
Project A → requires NumPy 1.x
Project B → requires NumPy 2.x
```

If both projects use the same global environment, installing one version may affect the other project.

With virtual environments:

```text
Project A
└── .venv
    └── NumPy 1.x

Project B
└── .venv
    └── NumPy 2.x
```

Both projects can work independently.

---

## 🔑 Main Benefits

Virtual environments provide:

### 1. Dependency Isolation

Each project can have its own packages and package versions.

### 2. Prevention of Version Conflicts

Different projects can use different versions of the same package.

### 3. Cleaner Development Environment

The global Python installation does not become filled with project-specific packages.

### 4. Reproducible Projects

Dependencies can be recorded in a file such as `requirements.txt`.

### 5. Safer Experimentation

We can install, upgrade, or remove packages inside a project environment without unnecessarily affecting other projects.

---

# 🛠️ Creating a Virtual Environment

Python provides the built-in `venv` module for creating virtual environments.

The basic command is:

```bash
python -m venv .venv
```

### Explanation

```text
python
```

Runs Python.

```text
-m
```

Tells Python to run a module.

```text
venv
```

Python's built-in module for creating virtual environments.

```text
.venv
```

The name of the virtual environment directory.

`.venv` is a common naming convention, although another name can also be used.

---

# 📂 Typical Project Structure

After creating a virtual environment, a project may look like:

```text
MyProject/
│
├── .venv/
├── main.py
└── requirements.txt
```

The `.venv` directory contains the isolated environment.

---

# ▶️ Activating a Virtual Environment

The activation command depends on the operating system and terminal.

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## Linux / macOS

```bash
source .venv/bin/activate
```

---

# 🔍 How to Know Whether the Environment is Active?

After activation, the environment name usually appears at the beginning of the terminal prompt.

For example:

```text
(.venv) PS C:\Users\Sonal\MyProject>
```

The:

```text
(.venv)
```

indicates that the virtual environment is active.

---

# 🐍 Checking Python Version

After activating the environment, we can check the Python version:

```bash
python --version
```

Example output:

```text
Python 3.x.x
```

We can also check which Python executable is being used.

## Windows

```powershell
where python
```

## Linux / macOS

```bash
which python
```

This helps verify that Python is coming from the virtual environment.

---

# 📦 Installing Packages Inside the Virtual Environment

Once the environment is activated, packages can be installed using `pip`.

For example:

```bash
pip install requests
```

Another example:

```bash
pip install numpy
```

These packages are installed inside the active environment.

They do not need to be installed globally.

---

# 🔄 Virtual Environment Workflow

A typical workflow looks like:

```text
Create project
      ↓
Create virtual environment
      ↓
Activate virtual environment
      ↓
Install required packages
      ↓
Develop project
      ↓
Save dependencies
      ↓
Deactivate when finished
```

---

# ⏹️ Deactivating a Virtual Environment

To deactivate the active environment:

```bash
deactivate
```

After deactivation, the `(.venv)` indicator disappears from the terminal.

---

# 🗑️ Removing a Virtual Environment

A virtual environment is simply a directory.

After deactivating it, the `.venv` directory can be deleted if it is no longer required.

The project source code remains unaffected.

If the dependencies are recorded in `requirements.txt`, the environment can be recreated later.

For example:

```bash
python -m venv .venv
```

followed by:

```bash
pip install -r requirements.txt
```

This makes the project environment reproducible.

---

# ⚠️ Important Points About Virtual Environments

- A virtual environment is isolated from the global Python environment.
- It is normally created separately for each project.
- `.venv` is a common name for the environment directory.
- The environment should generally be activated before installing project dependencies.
- Packages installed inside the environment are available to that environment.
- Different projects can use different package versions.
- The `.venv` directory should generally not be uploaded to GitHub.
- Instead of uploading `.venv`, project dependencies should be recorded in `requirements.txt`.
- A deleted virtual environment can be recreated using the project's dependency file.

---

# 🤖 Virtual Environment in AI Engineering

Virtual environments are especially important in AI/ML projects because these projects often depend on many external libraries.

For example:

```text
numpy
pandas
matplotlib
scikit-learn
torch
transformers
fastapi
requests
```

Different AI projects may require different versions of these libraries.

For example:

```text
Project A
└── PyTorch Version A

Project B
└── PyTorch Version B
```

Separate environments prevent these projects from interfering with each other.

Therefore:

> Understanding virtual environments is a fundamental practical skill for an AI Engineer working with Python.

---

# 🧠 Virtual Environment — Quick Revision

```text
Virtual Environment
        ↓
Creates an isolated Python environment
        ↓
Keeps project dependencies separate
        ↓
Prevents package/version conflicts
        ↓
Makes projects easier to reproduce
        ↓
Very useful for Python and AI/ML projects
```

---

# 2️⃣ pip — Python Package Manager

## 📌 Definition

> **pip** is Python's package manager used to install, uninstall, upgrade, and manage Python packages and their dependencies.

`pip` is one of the most important tools used in practical Python development.

---

# 📖 Why Do We Need pip?

Python has a large standard library, but many real-world applications require additional packages.

For example:

```text
requests
numpy
pandas
matplotlib
scikit-learn
torch
transformers
fastapi
```

Instead of manually downloading and configuring these packages, we can use `pip`.

---

# 📦 Installing a Package

The basic syntax is:

```bash
pip install package_name
```

For example:

```bash
pip install requests
```

Another example:

```bash
pip install numpy
```

---

# 📋 Installing Multiple Packages

Multiple packages can be installed in a single command:

```bash
pip install requests numpy pandas
```

This is useful when a project requires several dependencies.

---

# 🔍 Checking Installed Packages

We can view installed packages using:

```bash
pip list
```

Example:

```text
Package       Version
------------  -------
numpy         2.x.x
requests      2.x.x
```

`pip list` provides a readable list of packages installed in the current Python environment.

---

# 🔎 Checking Information About a Package

We can use:

```bash
pip show package_name
```

For example:

```bash
pip show numpy
```

It can provide information such as:

- Package name
- Version
- Installation location
- Dependencies
- Package metadata

---

# 🗑️ Uninstalling a Package

To remove a package:

```bash
pip uninstall package_name
```

For example:

```bash
pip uninstall requests
```

pip will normally ask for confirmation before uninstalling the package.

---

# 🔄 Upgrading a Package

To upgrade a package:

```bash
pip install --upgrade package_name
```

For example:

```bash
pip install --upgrade numpy
```

This tells pip to install a newer available version of the package.

---

# 📌 Installing a Specific Package Version

Sometimes a project requires a particular package version.

We can specify the exact version using:

```bash
pip install package_name==version
```

For example:

```bash
pip install numpy==2.5.3
```

This requests exactly version `2.5.3`.

---

# 📌 Version Constraints

Python dependency specifications can use different operators.

## Exact Version

```text
numpy==2.5.3
```

Means:

> Use exactly version `2.5.3`.

---

## Minimum Version

```text
numpy>=2.0
```

Means:

> Use version `2.0` or newer.

---

## Maximum Version

```text
numpy<3.0
```

Means:

> Use a version lower than `3.0`.

---

## Combined Version Range

We can also specify a range:

```text
numpy>=2.0,<3.0
```

This means:

> Use a version greater than or equal to `2.0` but lower than `3.0`.

Version constraints become particularly useful when creating `requirements.txt`.

---

# 🧠 pip and Virtual Environment

`pip` works with the currently selected Python environment.

If a virtual environment is active:

```bash
pip install numpy
```

the package is installed into that environment.

Conceptually:

```text
Global Python
│
├── Package A
└── Package B

Project Virtual Environment
│
├── NumPy
├── Requests
└── Pandas
```

This is why it is important to know which environment is currently active.

---

# 🔍 Checking pip Version

We can check the installed pip version using:

```bash
pip --version
```

This can also help identify which Python environment's pip is being used.

---

# ⚠️ Important Points About pip

- `pip` is used to manage Python packages.
- `pip install` installs packages.
- `pip uninstall` removes packages.
- `pip list` displays installed packages.
- `pip show` displays detailed package information.
- `pip install --upgrade` upgrades packages.
- `==` can be used to specify an exact package version.
- `>=` can specify a minimum version.
- `<` can specify a maximum version.
- Package management should generally be performed inside a project-specific virtual environment.
- Dependencies can later be recorded in `requirements.txt`.

---

# 🤖 pip in AI Engineering

AI Engineers regularly install and manage third-party Python packages.

For example:

### Numerical Computing

```bash
pip install numpy
```

### Data Processing

```bash
pip install pandas
```

### Machine Learning

```bash
pip install scikit-learn
```

### Deep Learning

```bash
pip install torch
```

### API Development

```bash
pip install fastapi
```

### HTTP Requests

```bash
pip install requests
```

Therefore:

> Understanding `pip` is an essential practical Python skill for AI/ML and AI Engineering development.

---

# 🧠 pip — Quick Revision

```text
pip
 │
 ├── pip install package
 │       → Install package
 │
 ├── pip uninstall package
 │       → Remove package
 │
 ├── pip list
 │       → Show installed packages
 │
 ├── pip show package
 │       → Show package information
 │
 ├── pip install --upgrade package
 │       → Upgrade package
 │
 └── pip --version
         → Show pip version
```

---

# 🔗 Relationship Between Virtual Environment and pip

Virtual environments and `pip` are commonly used together.

```text
Create Virtual Environment
          ↓
Activate Virtual Environment
          ↓
Use pip to install packages
          ↓
Develop the project
          ↓
Record dependencies
          ↓
Recreate environment when required
```

This workflow is extremely common in professional Python development.

---

# 3️⃣ requirements.txt

## 📌 Definition

> `requirements.txt` is a text file used to record the Python packages and their required versions that a project depends on.

It provides a simple way to document and recreate a project's Python environment.

---

# 📖 Why Do We Need requirements.txt?

Suppose we create a Python project that uses:

```text
numpy
requests
pandas
```

If we share the project with another developer, simply sharing the Python files is not always enough.

The other developer also needs to install the required packages.

Instead of telling them individually:

```bash
pip install numpy
pip install requests
pip install pandas
```

we can create a:

```text
requirements.txt
```

file containing the dependencies.

Then they can install everything using:

```bash
pip install -r requirements.txt
```

---

# 📂 Example Project Structure

A typical Python project can look like:

```text
MyProject/
│
├── main.py
├── requirements.txt
└── README.md
```

The `requirements.txt` file contains the project's dependencies.

---

# 📝 Basic requirements.txt Format

A simple `requirements.txt` file can contain:

```text
numpy
requests
pandas
```

Each package is normally written on a separate line.

---

# 📌 Specifying Package Versions

We can also specify exact versions.

For example:

```text
numpy==2.5.3
requests==2.34.2
pandas==2.3.2
```

This tells pip to install those specific versions.

Version specifications are useful because package updates can sometimes change behavior or introduce compatibility issues.

---

# 🔢 Different Version Specifications

`requirements.txt` supports version constraints.

### Exact Version

```text
numpy==2.5.3
```

Means:

> Install exactly version `2.5.3`.

---

### Minimum Version

```text
numpy>=2.0
```

Means:

> Install version `2.0` or newer.

---

### Maximum Version

```text
numpy<3.0
```

Means:

> Install a version lower than `3.0`.

---

### Version Range

```text
numpy>=2.0,<3.0
```

Means:

> Install a version greater than or equal to `2.0` but lower than `3.0`.

---

# ⚙️ Installing Dependencies from requirements.txt

The most important command is:

```bash
pip install -r requirements.txt
```

Here:

```text
-r
```

means:

> Read and install the requirements listed in the specified file.

Therefore:

```bash
pip install -r requirements.txt
```

reads the file and installs its listed dependencies.

---

# 🔄 How requirements.txt Helps Recreate a Project

Suppose another developer gets our project.

They can create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

Now the required packages are installed in the new environment.

The general workflow is:

```text
Project Source Code
        +
requirements.txt
        ↓
Create Virtual Environment
        ↓
pip install -r requirements.txt
        ↓
Project Environment Recreated
```

---

# 🧠 Why Is This Important?

Without `requirements.txt`, someone may have to manually figure out:

- Which packages are required?
- Which versions are required?
- Which dependencies should be installed?
- Which package versions are compatible?

With `requirements.txt`, the project's dependencies are explicitly documented.

---

# 🧪 Example

Suppose our project uses:

```text
numpy==2.5.3
requests==2.34.2
```

Our `requirements.txt` would contain:

```text
numpy==2.5.3
requests==2.34.2
```

Another developer can simply run:

```bash
pip install -r requirements.txt
```

and pip will install the listed packages.

---

# 📌 Creating requirements.txt Manually

We can create the file manually.

For example:

```text
requirements.txt
```

Then write:

```text
numpy==2.5.3
requests==2.34.2
```

This approach is useful when we want to specify only the direct dependencies of a project.

---

# 🔄 Creating requirements.txt Using pip freeze

Instead of manually writing installed packages, we can use:

```bash
pip freeze > requirements.txt
```

This command takes the installed packages from the current Python environment and writes them into `requirements.txt`.

For example, the file may contain:

```text
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.19
numpy==2.5.3
requests==2.34.2
urllib3==2.8.0
```

The exact packages and versions depend on the current environment.

---

# ⚠️ Important: Current Environment Matters

The command:

```bash
pip freeze > requirements.txt
```

records packages installed in the environment from which the command is executed.

Therefore, it is important to make sure that the correct project environment is active before running it.

Conceptually:

```text
Correct Environment
       ↓
pip freeze
       ↓
requirements.txt
```

If the wrong environment is used, unrelated packages may also be recorded.

---

# 📥 Installing requirements Again

Suppose we already have:

```text
requirements.txt
```

We can recreate the dependencies using:

```bash
pip install -r requirements.txt
```

This is especially useful when:

- Setting up a project on another computer
- Recreating a deleted virtual environment
- Collaborating with other developers
- Cloning a project from GitHub
- Deploying a Python application

---

# 🔁 Complete Dependency Workflow

A common real-world workflow is:

```text
Create Project
      ↓
Create Virtual Environment
      ↓
Activate Environment
      ↓
Install Packages
      ↓
Develop Project
      ↓
Save Dependencies
      ↓
requirements.txt
      ↓
Share Project
      ↓
Create New Environment
      ↓
pip install -r requirements.txt
```

---

# 🤖 requirements.txt in AI Engineering

AI projects often contain many dependencies.

For example:

```text
numpy
pandas
scikit-learn
torch
transformers
fastapi
requests
```

A project can record these dependencies in:

```text
requirements.txt
```

This makes the AI project easier to:

- Share
- Reproduce
- Deploy
- Maintain
- Run on another machine
- Set up in development environments

For example, an ML project might have:

```text
numpy==2.5.3
pandas==2.3.2
scikit-learn==1.x.x
```

A deployment server can then install the required dependencies from the file.

---

# ⚠️ Important Points

- `requirements.txt` is normally a plain text file.
- Each dependency is usually written on a separate line.
- Package versions can be specified.
- `pip install -r requirements.txt` installs the listed dependencies.
- `pip freeze > requirements.txt` can generate the file from the current environment.
- The correct Python environment should be used when generating the file.
- `requirements.txt` is commonly committed to Git repositories.
- `.venv` itself should generally not be committed to Git.
- `requirements.txt` helps make Python projects reproducible.

---

# 🧠 requirements.txt — Quick Revision

```text
requirements.txt
       ↓
Records project dependencies
       ↓
Package names + optional versions
       ↓
Can be generated using pip freeze
       ↓
Can be installed using:
pip install -r requirements.txt
       ↓
Helps recreate the project environment
```

---

# 4️⃣ pip freeze

## 📌 Definition

> `pip freeze` is a pip command that displays the packages installed in the current Python environment along with their exact versions.

It is commonly used to generate a dependency list that can be saved into `requirements.txt`.

---

# 📖 Basic Syntax

```bash
pip freeze
```

It produces output similar to:

```text
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.19
numpy==2.5.3
requests==2.34.2
urllib3==2.8.0
```

Each package is shown in a format similar to:

```text
package_name==version
```

---

# 🔍 What Does pip freeze Actually Do?

`pip freeze` looks at the currently active Python environment and lists installed packages in a requirements-style format.

For example:

```text
numpy==2.5.3
requests==2.34.2
```

This means:

```text
numpy
Version → 2.5.3

requests
Version → 2.34.2
```

---

# 📋 pip list vs pip freeze

Both commands show installed packages, but their output is designed for different purposes.

| Command | Purpose |
|---|---|
| `pip list` | Human-readable list of installed packages |
| `pip freeze` | Dependency-style package list with versions |

### `pip list`

```bash
pip list
```

Typical output:

```text
Package       Version
------------  -------
numpy         2.5.3
requests      2.34.2
```

### `pip freeze`

```bash
pip freeze
```

Typical output:

```text
numpy==2.5.3
requests==2.34.2
```

The output of `pip freeze` is directly suitable for a requirements-style file.

---

# 💾 Saving pip freeze Output

We can redirect the output to a file:

```bash
pip freeze > requirements.txt
```

Here:

```text
pip freeze
```

generates the dependency list.

The:

```text
>
```

operator redirects the output into a file.

Therefore:

```text
pip freeze > requirements.txt
```

means:

> Take the output of `pip freeze` and save it into `requirements.txt`.

---

# 📄 Example

Running:

```bash
pip freeze
```

might produce:

```text
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.19
numpy==2.5.3
requests==2.34.2
urllib3==2.8.0
```

Running:

```bash
pip freeze > requirements.txt
```

stores that output inside:

```text
requirements.txt
```

---

# 🔄 Reinstalling Frozen Dependencies

If we have:

```text
requirements.txt
```

we can install all listed dependencies using:

```bash
pip install -r requirements.txt
```

Therefore:

```text
pip freeze
     ↓
Save dependencies
     ↓
requirements.txt
     ↓
pip install -r requirements.txt
     ↓
Dependencies recreated
```

---

# ⚠️ Important Environment Concept

`pip freeze` reports packages from the environment that pip is currently using.

Therefore, always make sure the intended project environment is active before running:

```bash
pip freeze
```

Otherwise, packages from another environment may be included.

---

# 🤖 pip freeze in AI Engineering

AI projects often depend on many packages.

For example:

```text
numpy
pandas
scikit-learn
torch
transformers
fastapi
```

Keeping track of their versions is important because different versions can behave differently or have compatibility requirements.

Using:

```bash
pip freeze > requirements.txt
```

allows us to record the environment's installed package versions.

This is useful when:

- Sharing an AI project
- Recreating an environment
- Deploying an application
- Collaborating with teammates
- Moving a project to another machine

---

# ⚠️ Important Points

- `pip freeze` displays installed packages and their versions.
- It works with the current Python environment.
- Its output uses a requirements-style format.
- `pip freeze > requirements.txt` saves the output.
- `pip install -r requirements.txt` can reinstall those dependencies.
- `pip list` is generally easier to read interactively.
- `pip freeze` is particularly useful for recording dependencies.
- Always use the correct project environment when generating dependency information.

---

# 🧠 pip freeze — Quick Revision

```text
pip freeze
     ↓
Shows installed packages
     ↓
Includes versions
     ↓
Can be redirected to requirements.txt
     ↓
pip freeze > requirements.txt
     ↓
Used for dependency reproduction
```

---

# 🔗 Virtual Environment + pip + requirements.txt + pip freeze

These concepts work together.

```text
Virtual Environment
        ↓
Creates isolated environment
        ↓
pip
        ↓
Installs and manages packages
        ↓
pip freeze
        ↓
Records installed package versions
        ↓
requirements.txt
        ↓
Stores project dependencies
        ↓
pip install -r requirements.txt
        ↓
Recreates dependencies
```

This workflow is one of the basic foundations of professional Python project management.

---

# 5️⃣ Lambda Functions

## 📌 Definition

> A **lambda function** is a small anonymous function that can take arguments and return a value in a single expression.

Lambda functions are useful when we need a short function for a simple operation and do not want to define a complete function using `def`.

---

# 📖 What is a Lambda Function?

Normally, we create a function using `def`:

```python
def square(number):
    return number * number

print(square(5))
```

Output:

```text
25
```

The same operation can be written using a lambda function:

```python
square = lambda number: number * number

print(square(5))
```

Output:

```text
25
```

Here:

```text
lambda
```

creates the anonymous function.

```text
number
```

is the parameter.

```text
number * number
```

is the expression whose result is returned.

---

# 🧩 Basic Syntax

The general syntax is:

```python
lambda arguments: expression
```

For example:

```python
lambda x: x * 2
```

This means:

> Take `x` as input and return `x * 2`.

---

# 🔍 Lambda Function Components

Consider:

```python
square = lambda number: number * number
```

It can be understood as:

```text
lambda
  ↓
Creates anonymous function

number
  ↓
Parameter

:
  ↓
Separates parameter from expression

number * number
  ↓
Expression / return value
```

The result of the expression is automatically returned.

---

# 🆚 Lambda vs Normal Function

### Normal Function

```python
def square(number):
    return number * number
```

### Lambda Function

```python
square = lambda number: number * number
```

Both perform the same operation.

---

# 📌 Important Difference

A normal function can contain multiple statements:

```python
def calculate(number):
    result = number * 2
    result = result + 10
    return result
```

A lambda is designed for a small expression:

```python
calculate = lambda number: number * 2 + 10
```

Therefore:

> Lambda functions are best suited for short and simple operations.

---

# 5.1️⃣ Lambda with One Argument

A lambda can accept one argument.

```python
square = lambda number: number * number

print(square(5))
```

Output:

```text
25
```

Another example:

```python
double = lambda number: number * 2

print(double(10))
```

Output:

```text
20
```

---

# 5.2️⃣ Lambda with Multiple Arguments

A lambda can accept multiple arguments.

For example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Another example:

```python
multiply = lambda a, b: a * b

print(multiply(5, 4))
```

Output:

```text
20
```

---

# 5.3️⃣ Lambda with Three Arguments

Lambda functions can also accept three or more arguments.

```python
maximum = lambda a, b, c: a if a > b and a > c else b if b > c else c

print(maximum(10, 25, 17))
```

Output:

```text
25
```

This uses a conditional expression.

However, if a lambda becomes complicated or difficult to read, a normal `def` function is usually better.

---

# 5.4️⃣ Lambda with Conditional Expression

Lambda functions cannot contain normal multi-line `if-else` statements.

However, they can use a conditional expression.

For example:

```python
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(4))
print(even_odd(7))
```

Output:

```text
Even
Odd
```

The general syntax is:

```python
value_if_true if condition else value_if_false
```

---

# 🧠 Understanding Conditional Lambda

Consider:

```python
lambda x: "Even" if x % 2 == 0 else "Odd"
```

The logic is:

```text
If x % 2 == 0
       ↓
     "Even"

Otherwise
       ↓
     "Odd"
```

---

# ⚠️ Lambda and print()

It is important to understand that `print()` does not return the printed value.

For example:

```python
result = lambda x: print("Even") if x % 2 == 0 else print("Odd")

print(result(4))
```

Output:

```text
Even
None
```

Why?

Because:

```python
print("Even")
```

prints `"Even"` but returns:

```python
None
```

Therefore, lambda functions should generally return values rather than use `print()` as their main purpose.

A better approach is:

```python
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(4))
```

---

# 5.5️⃣ Lambda with Built-in Functions

Lambda functions become particularly useful when passed to other functions.

For example:

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

Here, the lambda function defines what should happen to each element.

This becomes especially useful with:

- `map()`
- `filter()`
- `sorted()`
- `reduce()`

These concepts will be covered later in this chapter.

---

# 5.6️⃣ Lambda with `map()`

Example:

```python
numbers = [10, 20, 30, 40]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```text
[20, 40, 60, 80]
```

The lambda function:

```python
lambda x: x * 2
```

is applied to every element.

---

# 5.7️⃣ Lambda with `filter()`

Lambda functions can also be used to define filtering conditions.

```python
numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 20, numbers))

print(result)
```

Output:

```text
[25, 30]
```

Here, the lambda returns `True` only for values greater than `20`.

---

# 5.8️⃣ Lambda with `sorted()`

Lambda functions can define the sorting criteria.

For example:

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)
```

Output:

```text
[('Rahul', 78), ('Sonal', 85), ('Aman', 92)]
```

Here:

```python
lambda student: student[1]
```

tells `sorted()` to use the second element of each tuple as the sorting key.

---

# 5.9️⃣ Lambda Does Not Need to Be Assigned to a Variable

A lambda can be used directly.

For example:

```python
print((lambda x: x * x)(5))
```

Output:

```text
25
```

Here:

```python
lambda x: x * x
```

creates the function and:

```python
(5)
```

immediately calls it.

However, this style can sometimes reduce readability.

For simple repeated operations, assigning the lambda to a meaningful variable can be clearer:

```python
square = lambda x: x * x

print(square(5))
```

---

# 🔟 Lambda Functions and Readability

Lambda functions are useful, but they should not be used everywhere.

For example, this is simple and readable:

```python
square = lambda x: x * x
```

But a complicated nested lambda can become difficult to understand.

Instead of:

```python
result = lambda a, b, c: a if a > b and a > c else b if b > c else c
```

a normal function may be more readable:

```python
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
```

Therefore:

> Use lambda functions for short, simple operations. Use `def` when the logic becomes complex.

---

# ⚠️ Important Limitations of Lambda Functions

Lambda functions are intentionally limited.

A lambda:

- Contains a single expression.
- Automatically returns the result of that expression.
- Does not use a normal `return` statement.
- Is best suited for small operations.
- Should not be used for complex multi-step logic.
- Can accept multiple arguments.
- Can use conditional expressions.
- Is especially useful with functions such as `map()`, `filter()`, `reduce()`, and `sorted()`.

---

# 🤖 Lambda Functions in AI Engineering

Lambda functions are not an AI-specific feature, but they are frequently useful in AI/ML data-processing code.

For example:

### Transforming Data

```python
numbers = [10, 20, 30, 40]

result = list(map(lambda x: x / 10, numbers))

print(result)
```

Output:

```text
[1.0, 2.0, 3.0, 4.0]
```

### Filtering Data

```python
scores = [45, 72, 91, 38, 85]

result = list(filter(lambda score: score >= 70, scores))

print(result)
```

Output:

```text
[72, 91, 85]
```

### Sorting Data

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

result = sorted(students, key=lambda student: student[1], reverse=True)

print(result)
```

Lambda is therefore useful for short data transformation and sorting operations that commonly appear in Python data-processing workflows.

---

# 🧠 Lambda — Quick Revision

```text
Lambda Function
       ↓
Anonymous function
       ↓
lambda arguments: expression
       ↓
Automatically returns expression result
       ↓
Best for small operations
       ↓
Commonly used with:
map()
filter()
reduce()
sorted()
```

---

# 6️⃣ map()

## 📌 Definition

> `map()` is a built-in Python function that applies a function to every element of an iterable and returns a map object containing the transformed results.

It is mainly used when we want to **transform every element** of a collection.

---

# 📖 Why Do We Use map()?

Suppose we have:

```python
numbers = [10, 20, 30, 40]
```

and we want to multiply every number by `5`.

Using a loop:

```python
numbers = [10, 20, 30, 40]

result = []

for number in numbers:
    result.append(number * 5)

print(result)
```

Output:

```text
[50, 100, 150, 200]
```

The same transformation can be performed using `map()`:

```python
numbers = [10, 20, 30, 40]

result = map(lambda number: number * 5, numbers)

print(list(result))
```

Output:

```text
[50, 100, 150, 200]
```

---

# 🧩 Syntax of map()

The general syntax is:

```python
map(function, iterable)
```

For example:

```python
map(lambda x: x * 2, numbers)
```

Here:

```text
function
   ↓
Defines the transformation

iterable
   ↓
Provides the elements
```

---

# 🔍 Understanding map()

Consider:

```python
numbers = [10, 20, 30, 40]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

The process is:

```text
10 → 10 × 2 → 20
20 → 20 × 2 → 40
30 → 30 × 2 → 60
40 → 40 × 2 → 80
```

Final result:

```text
[20, 40, 60, 80]
```

---

# 6.1️⃣ map() Returns a map Object

`map()` does not directly return a list.

For example:

```python
numbers = [10, 20, 30]

result = map(lambda x: x * 2, numbers)

print(result)
```

The output will be something similar to:

```text
<map object at 0x...>
```

To obtain the actual values as a list:

```python
print(list(result))
```

Output:

```text
[20, 40, 60]
```

---

# 🧠 Why Do We Use list() with map()?

`map()` returns an iterable map object.

When we want to display or store all the transformed values as a list, we can convert it:

```python
list(result)
```

Therefore:

```python
result = map(...)
```

creates the map object, while:

```python
list(result)
```

materializes the results into a list.

---

# 6.2️⃣ map() with Lambda

One of the most common patterns is:

```python
map(lambda x: expression, iterable)
```

For example:

```python
numbers = [10, 20, 30, 40, 50]

result = map(lambda x: x + 10, numbers)

print(list(result))
```

Output:

```text
[20, 30, 40, 50, 60]
```

---

# 6.3️⃣ map() with Strings

`map()` can also transform strings.

For example:

```python
names = ["sonal", "rahul", "aman", "rohit"]

result = map(lambda name: name.upper(), names)

print(list(result))
```

Output:

```text
['SONAL', 'RAHUL', 'AMAN', 'ROHIT']
```

Every name is transformed into uppercase.

---

# 6.4️⃣ map() for Finding String Lengths

We can use `map()` to calculate the length of every string.

```python
words = ["Python", "AI", "Machine", "Learning"]

result = map(lambda word: len(word), words)

print(list(result))
```

Output:

```text
[6, 2, 7, 8]
```

The same operation can be written more simply because `len` itself is a function:

```python
words = ["Python", "AI", "Machine", "Learning"]

result = map(len, words)

print(list(result))
```

Output:

```text
[6, 2, 7, 8]
```

When an existing function already performs exactly what we need, using that function directly is often cleaner than creating a lambda.

---

# 6.5️⃣ map() with Multiple Iterables

`map()` can work with multiple iterables.

For example:

```python
numbers1 = [10, 20, 30]
numbers2 = [1, 2, 3]

result = map(lambda a, b: a + b, numbers1, numbers2)

print(list(result))
```

Output:

```text
[11, 22, 33]
```

The elements are processed pair by pair:

```text
10 + 1  → 11
20 + 2  → 22
30 + 3  → 33
```

---

# ⚠️ Different Lengths with Multiple Iterables

When multiple iterables are passed to `map()`, processing continues according to the shortest iterable in modern Python behavior.

For example:

```python
numbers1 = [10, 20, 30, 40]
numbers2 = [1, 2]

result = map(lambda a, b: a + b, numbers1, numbers2)

print(list(result))
```

Output:

```text
[11, 22]
```

Only the available pairs are processed.

---

# 🆚 map() vs for Loop

### Using a loop

```python
numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

### Using map()

```python
numbers = [1, 2, 3, 4]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

Both can produce:

```text
[2, 4, 6, 8]
```

The choice depends on readability and the complexity of the transformation.

---

# 📌 When Should We Use map()?

Use `map()` when:

- Every element needs the same transformation.
- The transformation can be clearly expressed as a function.
- We want concise data-processing code.
- We are working with collections of data.

Examples:

```text
Convert strings to uppercase
Convert strings to integers
Multiply numbers
Calculate lengths
Transform values
Apply a mathematical operation
```

---

# ⚠️ Important Points About map()

- `map()` is a built-in Python function.
- It applies a function to each element.
- It returns a `map` object.
- `list()` can be used to obtain the results as a list.
- Lambda functions are commonly used with `map()`.
- Existing functions such as `len`, `str`, or `int` can also be passed directly.
- `map()` is mainly used for transformation, not filtering.
- Multiple iterables can be passed to `map()`.

---

# 🤖 map() in AI Engineering

AI and ML workflows frequently involve transforming collections of values.

For example:

```python
data = ["10", "20", "30", "40"]

numbers = list(map(int, data))

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

This kind of transformation is common when preparing raw data for further processing.

Another example:

```python
scores = [0.75, 0.82, 0.91]

percentages = list(map(lambda score: score * 100, scores))

print(percentages)
```

Output:

```text
[75.0, 82.0, 91.0]
```

---

# 🧠 map() — Quick Revision

```text
map()
  ↓
Applies a function to every element
  ↓
Transforms data
  ↓
Returns a map object
  ↓
Use list() when a list is required
  ↓
Commonly used with lambda
```

---

# 7️⃣ filter()

## 📌 Definition

> `filter()` is a built-in Python function that selects elements from an iterable based on a condition and returns only the elements for which the condition is true.

The main purpose of `filter()` is **selection**, not transformation.

---

# 📖 Why Do We Use filter()?

Suppose we have:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]
```

and we want only numbers greater than `20`.

Using a loop:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

result = []

for number in numbers:
    if number > 20:
        result.append(number)

print(result)
```

Output:

```text
[25, 30, 35, 40]
```

Using `filter()`:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

result = filter(lambda x: x > 20, numbers)

print(list(result))
```

Output:

```text
[25, 30, 35, 40]
```

---

# 🧩 Syntax of filter()

The basic syntax is:

```python
filter(function, iterable)
```

For example:

```python
filter(lambda x: x > 20, numbers)
```

The function should return a truth value.

```text
True
```

means:

> Keep the element.

```text
False
```

means:

> Remove the element from the filtered result.

---

# 🔍 Understanding filter()

Consider:

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x > 20, numbers)

print(list(result))
```

The condition is:

```python
x > 20
```

Evaluation:

```text
10 > 20 → False → Remove
15 > 20 → False → Remove
20 > 20 → False → Remove
25 > 20 → True  → Keep
30 > 20 → True  → Keep
```

Final result:

```text
[25, 30]
```

---

# 7.1️⃣ filter() Returns a filter Object

Like `map()`, `filter()` returns a special object rather than directly returning a list.

For example:

```python
numbers = [10, 20, 30]

result = filter(lambda x: x > 15, numbers)

print(result)
```

The output will be similar to:

```text
<filter object at 0x...>
```

To get the values as a list:

```python
print(list(result))
```

Output:

```text
[20, 30]
```

---

# 7.2️⃣ filter() with Lambda

A common pattern is:

```python
filter(lambda x: condition, iterable)
```

Example:

```python
numbers = [5, 10, 15, 20, 25, 30]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[10, 20, 30]
```

The lambda returns `True` for even numbers.

---

# 7.3️⃣ Filtering Positive Numbers

```python
numbers = [-10, 5, -3, 8, -2, 12, -7]

positive_numbers = filter(lambda x: x > 0, numbers)

print(list(positive_numbers))
```

Output:

```text
[5, 8, 12]
```

---

# 7.4️⃣ filter() Without Lambda

We do not have to use lambda with `filter()`.

We can define a normal function:

```python
def name_length(name):
    return len(name) > 4
```

Then:

```python
names = ["Sonal", "Aman", "Raj", "Rahul", "Om"]

result = filter(name_length, names)

print(list(result))
```

Output:

```text
['Sonal', 'Rahul']
```

Here:

```python
name_length
```

is passed as the filtering function.

---

# 7.5️⃣ filter() with Strings

We can filter strings based on their properties.

For example:

```python
names = ["Sonal", "Aman", "Rahul", "Om", "Rohit"]

result = filter(lambda name: len(name) > 4, names)

print(list(result))
```

Output:

```text
['Sonal', 'Rahul', 'Rohit']
```

---

# 🆚 map() vs filter()

This is an important distinction.

## map()

`map()` **transforms** every element.

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

The number of elements remains the same.

---

## filter()

`filter()` **selects** elements based on a condition.

```python
numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4]
```

The number of elements may decrease.

---

# 🧠 Easy Way to Remember

```text
map()
 ↓
Transform

filter()
 ↓
Select
```

For example:

```text
[1, 2, 3, 4, 5]

map(x × 2)
        ↓
[2, 4, 6, 8, 10]
```

Whereas:

```text
[1, 2, 3, 4, 5]

filter(x is even)
        ↓
[2, 4]
```

---

# 📌 When Should We Use filter()?

Use `filter()` when:

- We want to select specific elements.
- We have a condition.
- Only elements satisfying the condition should remain.

Common examples:

```text
Find positive numbers
Find even numbers
Find students above a marks threshold
Find names longer than a specific length
Find valid records
Find values above/below a threshold
```

---

# ⚠️ Important Points About filter()

- `filter()` is a built-in Python function.
- It selects elements based on a condition.
- It returns a `filter` object.
- `list()` can be used to obtain the results as a list.
- The filtering function should produce a truth value.
- Lambda functions are commonly used with `filter()`.
- A normal function can also be passed.
- `filter()` is mainly used for selection.
- Unlike `map()`, the number of output elements can be smaller than the input.

---

# 🤖 filter() in AI Engineering

Filtering is very common in data-processing workflows.

For example, suppose we have model confidence scores:

```python
scores = [0.45, 0.82, 0.91, 0.38, 0.76]

high_confidence = filter(lambda score: score >= 0.80, scores)

print(list(high_confidence))
```

Output:

```text
[0.82, 0.91]
```

The same concept can be used when selecting:

- Valid records
- High-confidence predictions
- Data above a threshold
- Non-empty values
- Relevant text entries
- Valid input data

---

# 🧠 filter() — Quick Revision

```text
filter()
   ↓
Checks a condition
   ↓
True  → Keep element
False → Remove element
   ↓
Returns filter object
   ↓
Use list() to obtain list
```

---

# 8️⃣ reduce()

## 📌 Definition

> `reduce()` repeatedly applies a function to the elements of an iterable and reduces them to a single final value.

Unlike `map()` and `filter()`, which generally produce multiple results, `reduce()` combines multiple values into **one result**.

---

# 📦 Importing reduce()

Unlike `map()` and `filter()`, `reduce()` is not a built-in function directly available without importing it.

It is provided by the `functools` module.

We import it using:

```python
from functools import reduce
```

---

# 🧩 Basic Syntax

```python
reduce(function, iterable)
```

For example:

```python
from functools import reduce

result = reduce(lambda a, b: a + b, numbers)
```

---

# 📖 Why Do We Use reduce()?

Suppose we have:

```python
numbers = [1, 2, 3, 4, 5]
```

and want to calculate the total.

Using a loop:

```python
numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number

print(total)
```

Output:

```text
15
```

Using `reduce()`:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
15
```

---

# 🔍 How reduce() Works

Consider:

```python
numbers = [1, 2, 3, 4, 5]
```

and:

```python
reduce(lambda a, b: a + b, numbers)
```

The process is:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

Final result:

```text
15
```

The intermediate result becomes the input for the next step.

---

# 🧠 Understanding `a` and `b`

In:

```python
lambda a, b: a + b
```

`a` represents the accumulated result so far.

`b` represents the next element.

For:

```text
[1, 2, 3, 4, 5]
```

the process is:

```text
a = 1, b = 2 → 3
a = 3, b = 3 → 6
a = 6, b = 4 → 10
a = 10, b = 5 → 15
```

---

# 8.1️⃣ Multiplication Using reduce()

We can multiply all numbers.

```python
from functools import reduce

numbers = [2, 3, 4, 5, 6]

multiplication = reduce(lambda a, b: a * b, numbers)

print(multiplication)
```

Output:

```text
720
```

The calculation is:

```text
2 × 3 = 6
6 × 4 = 24
24 × 5 = 120
120 × 6 = 720
```

---

# 8.2️⃣ Finding Maximum Value Using reduce()

We can also use `reduce()` to find the maximum value.

```python
from functools import reduce

numbers = [10, 25, 7, 42, 18]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(maximum)
```

Output:

```text
42
```

---

# 🔍 Understanding Maximum Logic

Consider:

```python
lambda a, b: a if a > b else b
```

It means:

```text
If a > b
    ↓
return a

Otherwise
    ↓
return b
```

Therefore, the larger value continues as the accumulated result.

---

# 🆚 map() vs filter() vs reduce()

These three functions have different purposes.

| Function | Main Purpose | Result |
|---|---|---|
| `map()` | Transform elements | Transformed iterable |
| `filter()` | Select elements | Filtered iterable |
| `reduce()` | Combine elements | Single final value |

Example:

```text
Input:
[1, 2, 3, 4, 5]
```

### map()

```text
[1, 2, 3, 4, 5]
        ↓
multiply by 2
        ↓
[2, 4, 6, 8, 10]
```

### filter()

```text
[1, 2, 3, 4, 5]
        ↓
keep even
        ↓
[2, 4]
```

### reduce()

```text
[1, 2, 3, 4, 5]
        ↓
sum
        ↓
15
```

---

# 📌 When Should We Use reduce()?

`reduce()` can be useful when a sequence of values needs to be repeatedly combined into one result.

Examples include:

- Sum
- Product
- Maximum/minimum logic
- Combining values
- Cumulative operations

However, not every reduction problem requires `reduce()`.

For example, for a simple sum:

```python
sum(numbers)
```

is generally clearer than:

```python
reduce(lambda a, b: a + b, numbers)
```

Therefore, `reduce()` should be used when it makes the logic useful and understandable.

---

# ⚠️ Important Points About reduce()

- `reduce()` comes from the `functools` module.
- It must normally be imported using:

```python
from functools import reduce
```

- It repeatedly applies a function.
- The accumulated result is passed to the next iteration.
- It reduces an iterable to one final value.
- Lambda functions are commonly used with it.
- Built-in functions such as `sum()` may sometimes be clearer for simple operations.

---

# 🤖 reduce() in AI Engineering

`reduce()` is not one of the most frequently used tools in modern AI code, because libraries such as NumPy and Pandas provide specialized aggregation functions.

However, understanding `reduce()` is useful because it teaches the idea of **accumulation and reduction**, which is important in data processing.

For example:

```text
Multiple values
      ↓
Repeated combination
      ↓
Single result
```

This general idea appears throughout data processing and numerical computing.

---

# 🧠 reduce() — Quick Revision

```text
reduce()
    ↓
Repeatedly combines values
    ↓
Uses accumulated result
    ↓
Eventually produces
    ↓
One final value
```

---

# 9️⃣ Combining map(), filter() and lambda

## 📌 Definition

> `map()`, `filter()`, and `lambda` can be combined to first select required data and then transform the selected values using concise functional-style Python code.

This is an important practical pattern for data processing.

---

# 📖 Basic Flow

A common pattern is:

```text
Original Data
      ↓
filter()
      ↓
Select required elements
      ↓
map()
      ↓
Transform selected elements
      ↓
Final Result
```

Lambda functions are often used to define the filtering and transformation logic.

---

# 🧪 Example

Suppose we have:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]
```

We want:

1. Only even numbers.
2. Multiply those numbers by `2`.

First, filter the even numbers:

```python
even_numbers = filter(lambda x: x % 2 == 0, numbers)
```

Then transform them:

```python
result = map(lambda x: x * 2, even_numbers)
```

Finally:

```python
print(list(result))
```

Complete code:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

result = map(lambda x: x * 2, even_numbers)

print(list(result))
```

Output:

```text
[20, 40, 60, 80]
```

---

# 🔍 Step-by-Step Execution

Original:

```text
[10, 15, 20, 25, 30, 35, 40]
```

### Step 1 — filter()

Condition:

```python
x % 2 == 0
```

Result:

```text
[10, 20, 30, 40]
```

### Step 2 — map()

Transformation:

```python
x * 2
```

Result:

```text
[20, 40, 60, 80]
```

---

# 🧪 Another Example

Suppose:

```python
numbers = [5, 12, 18, 7, 25, 30, 9, 40]
```

We want:

- Numbers greater than `10`
- Then multiply them by `3`

Code:

```python
numbers = [5, 12, 18, 7, 25, 30, 9, 40]

filtered = filter(lambda x: x > 10, numbers)

result = map(lambda x: x * 3, filtered)

print(list(result))
```

Output:

```text
[36, 54, 75, 90, 120]
```

---

# 🧠 Important Order

The order matters.

If the requirement is:

> First select the required values, then transform them.

Use:

```text
filter()
   ↓
map()
```

For example:

```python
filter(...)
map(...)
```

Not every problem requires this exact order, but the logical requirement should determine the order.

---

# 🆚 map() + filter() + lambda

The roles are:

```text
lambda
   ↓
Defines small logic

filter()
   ↓
Selects elements

map()
   ↓
Transforms elements
```

Therefore:

```text
lambda + filter() + map()
            ↓
Concise data-processing pipeline
```

---

# 🤖 AI Engineer Relevance

This pattern is useful when preprocessing data before sending it to another stage.

For example, imagine a collection of values where:

```text
1. Invalid values need to be removed.
2. Valid values need to be transformed.
```

Conceptually:

```text
Raw Data
   ↓
filter()
   ↓
Valid Data
   ↓
map()
   ↓
Processed Data
```

The same general pipeline idea is extremely common in data-processing workflows, although real AI projects will often use tools such as **NumPy, Pandas, or PyTorch** for large-scale numerical operations.

---

# ⚠️ Important Points

- `filter()` is generally used for selection.
- `map()` is generally used for transformation.
- `lambda` can define short custom logic.
- Filtering can be performed before transformation when required.
- `list()` can be used to materialize the final result.
- For very complex logic, normal functions may be more readable than nested lambdas.
- In large-scale AI/data processing, specialized libraries may be more appropriate.

---

# 🧠 map() + filter() + lambda — Quick Revision

```text
Original Data
      ↓
   filter()
      ↓
Selected Data
      ↓
    map()
      ↓
Transformed Data
      ↓
 Final Result
```

---
# 🔟 join()

## 📌 Definition

> `join()` is a string method used to combine multiple strings from an iterable into a single string using a specified separator.

It is commonly used when we have multiple strings and want to combine them into one properly formatted string.

---

# 📖 Why Do We Use join()?

Suppose we have:

```python
words = ["Python", "is", "powerful"]
```

and we want:

```text
Python is powerful
```

We can use:

```python
result = " ".join(words)

print(result)
```

Output:

```text
Python is powerful
```

Here:

```text
" "
```

is the separator used between the strings.

---

# 🧩 Basic Syntax

The syntax is:

```python
separator.join(iterable)
```

For example:

```python
" ".join(words)
```

Here:

```text
" "
   ↓
Separator

words
   ↓
Iterable containing strings
```

---

# 🔍 How join() Works

Consider:

```python
words = ["Python", "is", "powerful"]

result = " ".join(words)

print(result)
```

The process is:

```text
Python
   +
" "
   +
is
   +
" "
   +
powerful
```

Final result:

```text
Python is powerful
```

The separator is inserted **between** the elements.

It is not added at the beginning or at the end.

---

# 10.1️⃣ Joining with a Space

```python
words = ["Python", "is", "powerful"]

result = " ".join(words)

print(result)
```

Output:

```text
Python is powerful
```

The separator is:

```python
" "
```

which represents one space.

---

# 10.2️⃣ Joining with a Comma

We can use:

```python
", "
```

as the separator.

Example:

```python
names = ["Sonal", "Aman", "Rahul", "Rohit"]

result = ", ".join(names)

print(result)
```

Output:

```text
Sonal, Aman, Rahul, Rohit
```

---

# 10.3️⃣ Joining with a Hyphen

```python
numbers = ["10", "20", "30", "40"]

result = " - ".join(numbers)

print(result)
```

Output:

```text
10 - 20 - 30 - 40
```

---

# 10.4️⃣ Joining Without a Separator

We can use an empty string:

```python
characters = ["P", "y", "t", "h", "o", "n"]

result = "".join(characters)

print(result)
```

Output:

```text
Python
```

Here:

```python
""
```

means no separator is inserted.

---

# 10.5️⃣ Joining with a New Line

The newline character:

```python
"\n"
```

can be used as the separator.

Example:

```python
names = ["Sonal", "Aman", "Rahul"]

result = "\n".join(names)

print(result)
```

Output:

```text
Sonal
Aman
Rahul
```

This is useful when creating multi-line text.

---

# 10.6️⃣ Joining with Tabs

We can also use:

```python
"\t"
```

which represents a tab.

Example:

```python
items = ["Python", "AI", "ML"]

result = "\t".join(items)

print(result)
```

Output will contain tab spacing between the values.

---

# 10.7️⃣ Joining Numbers

A very important point:

> `join()` works with strings, not directly with integers or other non-string objects.

For example, this will cause an error:

```python
numbers = [10, 20, 30, 40]

result = " - ".join(numbers)
```

The elements are integers, not strings.

---

# ✅ Converting Numbers to Strings

We can use `map()` with `str`:

```python
numbers = [10, 20, 30, 40, 50]

result = " - ".join(map(str, numbers))

print(result)
```

Output:

```text
10 - 20 - 30 - 40 - 50
```

The process is:

```text
numbers
   ↓
map(str, numbers)
   ↓
Convert every number to string
   ↓
join()
   ↓
Final string
```

This is a useful example of combining two concepts from this chapter.

---

# 10.8️⃣ Joining List of Strings

`join()` works naturally with a list of strings:

```python
languages = ["Python", "Java", "C++", "JavaScript"]

result = ", ".join(languages)

print(result)
```

Output:

```text
Python, Java, C++, JavaScript
```

---

# 10.9️⃣ Joining a Tuple

`join()` can work with other iterables containing strings, not only lists.

For example:

```python
languages = ("Python", "Java", "C++")

result = " | ".join(languages)

print(result)
```

Output:

```text
Python | Java | C++
```

---

# 10.🔟 Joining a Set

A set can also be passed to `join()` if it contains strings:

```python
skills = {"Python", "AI", "ML"}

result = ", ".join(skills)

print(result)
```

However, sets are unordered, so the output order should not be relied upon.

For predictable ordering, use a list or sort the values first.

---

# 10.1️⃣1️⃣ Joining Dictionary Values

When a dictionary is passed directly to `join()`, its keys are iterated over.

For example:

```python
student = {
    "name": "Sonal",
    "course": "Python",
    "level": "Beginner"
}

result = " | ".join(student)

print(result)
```

This joins the keys.

Output:

```text
name | course | level
```

If we want to join the values:

```python
result = " | ".join(student.values())

print(result)
```

Output:

```text
Sonal | Python | Beginner
```

---

# 10.1️⃣2️⃣ join() with split()

`split()` and `join()` are often used together.

`split()` separates a string into multiple parts.

Example:

```python
text = "Python is powerful"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'powerful']
```

Now we can join them again:

```python
result = "-".join(words)

print(result)
```

Output:

```text
Python-is-powerful
```

Therefore:

```text
String
  ↓
split()
  ↓
List of strings
  ↓
join()
  ↓
Combined string
```

---

# 🔄 split() vs join()

These operations are almost opposite in purpose.

### split()

```python
text = "Python is powerful"

result = text.split()

print(result)
```

Output:

```text
['Python', 'is', 'powerful']
```

It converts:

```text
String → List
```

### join()

```python
words = ["Python", "is", "powerful"]

result = " ".join(words)

print(result)
```

Output:

```text
Python is powerful
```

It converts:

```text
List of strings → String
```

---

# ⚠️ Important Point: join() is a String Method

The separator is the object on which `join()` is called.

For example:

```python
" ".join(words)
```

Here `" "` is the separator.

Another example:

```python
", ".join(words)
```

Here `", "` is the separator.

This is why we do not write:

```python
words.join(" ")
```

Instead, we write:

```python
" ".join(words)
```

---

# ❌ Common Mistake

This will fail if the list contains integers:

```python
numbers = [1, 2, 3, 4]

print(", ".join(numbers))
```

Why?

Because `join()` expects strings.

Correct:

```python
numbers = [1, 2, 3, 4]

print(", ".join(map(str, numbers)))
```

Output:

```text
1, 2, 3, 4
```

---

# 🧠 join() and Slicing — Important Difference

`join()` and slicing are completely different concepts.

For example:

```python
numbers[::2]
```

uses slicing.

The general slicing syntax is:

```python
sequence[start:stop:step]
```

For example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::2])
```

Output:

```text
[10, 30, 50]
```

Here:

```text
::2
```

means:

> Take every second element.

Similarly:

```python
numbers[::-1]
```

reverses the sequence.

This has nothing to do with the separator used by `join()`.

For example:

```python
"::".join(["Python", "AI", "ML"])
```

is a valid `join()` operation where `"::"` is simply the separator.

Output:

```text
Python::AI::ML
```

---

# 📌 When Should We Use join()?

Use `join()` when:

- Multiple strings need to be combined.
- A specific separator is required.
- We need clean text formatting.
- We need to construct multi-line text.
- We need to convert a collection of strings into one string.

Common examples:

```text
Creating CSV-like text
Creating sentences
Formatting names
Generating paths or identifiers
Creating multi-line output
Combining processed data
```

---

# 🤖 join() in AI Engineering

`join()` can be useful when processing text.

For example, suppose we have words:

```python
words = ["Artificial", "Intelligence", "Engineer"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Artificial Intelligence Engineer
```

This kind of string manipulation can appear during:

- Text preprocessing
- Data cleaning
- NLP pipelines
- Creating prompts
- Combining tokens or text fragments
- Preparing text for APIs or models

For example:

```python
sentences = [
    "Python is useful.",
    "AI is powerful.",
    "Practice is important."
]

text = "\n".join(sentences)

print(text)
```

Output:

```text
Python is useful.
AI is powerful.
Practice is important.
```

---

# ⚠️ Important Points About join()

- `join()` is a string method.
- It combines strings from an iterable.
- The separator is placed between elements.
- The elements normally need to be strings.
- `map(str, iterable)` can be used when the elements are numbers.
- It works with lists, tuples, and other iterables containing strings.
- `"\n".join()` can create multi-line text.
- `", ".join()` is useful for comma-separated values.
- `split()` and `join()` are frequently used together.
- `join()` is different from slicing.

---

# 🧠 join() — Quick Revision

```text
join()
  ↓
String method
  ↓
Combines multiple strings
  ↓
Uses a separator
  ↓
separator.join(iterable)
  ↓
Returns one string
```

---

# 1️⃣1️⃣ String Formatting

## 📌 Definition

> **String formatting** is the process of inserting values, variables, or expressions into strings in a readable and controlled way.

String formatting is commonly used for:

- Output messages
- Reports
- Logs
- User interfaces
- Error messages
- Data presentation
- Dynamic text generation

Python provides multiple ways to format strings.

The most important modern method is the **f-string**.

---

# 📖 Why Do We Need String Formatting?

Suppose:

```python
name = "Sonal"
age = 25
```

We want:

```text
My name is Sonal and I am 25 years old.
```

Instead of manually concatenating strings:

```python
print("My name is " + name + " and I am " + str(age) + " years old.")
```

we can use an f-string:

```python
print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Sonal and I am 25 years old.
```

F-strings are generally cleaner and easier to read.

---

# 1️⃣1️⃣.1️⃣ f-Strings

## 📌 Definition

> An **f-string** is a Python string prefixed with `f` that allows variables and expressions to be directly inserted inside `{}`.

Example:

```python
name = "Sonal"
course = "Python"

print(f"My name is {name} and I am learning {course}.")
```

Output:

```text
My name is Sonal and I am learning Python.
```

---

# 🧩 Basic Syntax

```python
f"Text {variable}"
```

For example:

```python
name = "Sonal"

print(f"Hello, {name}!")
```

Output:

```text
Hello, Sonal!
```

---

# 1️⃣1️⃣.2️⃣ Using Multiple Variables

```python
name = "Sonal"
age = 25
course = "Python"

print(f"My name is {name}, I am {age} years old, and I am learning {course}.")
```

Output:

```text
My name is Sonal, I am 25 years old, and I am learning Python.
```

---

# 1️⃣1️⃣.3️⃣ Expressions Inside f-Strings

We can place expressions inside `{}`.

For example:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

Another example:

```python
number = 5

print(f"Square = {number * number}")
```

Output:

```text
Square = 25
```

Therefore, the `{}` section does not have to contain only a variable.

It can contain a valid Python expression.

---

# 1️⃣1️⃣.4️⃣ Calling Functions Inside f-Strings

We can also call functions:

```python
name = "sonal"

print(f"Uppercase name: {name.upper()}")
```

Output:

```text
Uppercase name: SONAL
```

Another example:

```python
numbers = [10, 20, 30]

print(f"Number of elements: {len(numbers)}")
```

Output:

```text
Number of elements: 3
```

---

# 1️⃣1️⃣.5️⃣ Formatting Decimal Numbers

Suppose:

```python
price = 1499.786
```

If we want exactly two decimal places:

```python
print(f"Price: ₹{price:.2f}")
```

Output:

```text
Price: ₹1499.79
```

Here:

```text
.2f
```

means:

- `.2` → two decimal places
- `f` → floating-point formatting

---

# 1️⃣1️⃣.6️⃣ More Decimal Formatting

```python
number = 12.345678

print(f"{number:.2f}")
print(f"{number:.3f}")
print(f"{number:.1f}")
```

Output:

```text
12.35
12.346
12.3
```

---

# 1️⃣1️⃣.7️⃣ Percentage Formatting

We can use `%`.

For example:

```python
score = 0.8567

print(f"Score: {score:.2%}")
```

Output:

```text
Score: 85.67%
```

The value:

```text
0.8567
```

is converted to:

```text
85.67%
```

---

# 1️⃣1️⃣.8️⃣ Alignment

f-strings also support alignment.

### Left Alignment

```python
name = "Python"

print(f"{name:<10}")
```

`<10` means:

> Left-align within a field of width 10.

---

### Right Alignment

```python
name = "Python"

print(f"{name:>10}")
```

`>10` means:

> Right-align within a field of width 10.

---

### Center Alignment

```python
name = "Python"

print(f"{name:^10}")
```

`^10` means:

> Center-align within a field of width 10.

---

# 🧪 Creating a Simple Table

```python
name = "Python"
version = "3.14"

print(f"{name:<10} | {version}")
```

Output:

```text
Python     | 3.14
```

This is useful when creating formatted terminal output.

---

# 1️⃣1️⃣.9️⃣ f-Strings with Calculations

```python
price = 500
quantity = 3

print(f"Total = ₹{price * quantity}")
```

Output:

```text
Total = ₹1500
```

The expression:

```python
price * quantity
```

is evaluated before being inserted into the string.

---

# 1️⃣1️⃣.🔟 `.format()` Method

Before f-strings became common, Python frequently used the `.format()` method.

Example:

```python
name = "Sonal"
course = "Python"
chapter = 13

print(
    "My name is {}, I am learning {}, and I am on Chapter {}."
    .format(name, course, chapter)
)
```

Output:

```text
My name is Sonal, I am learning Python, and I am on Chapter 13.
```

---

# 🧩 `.format()` Syntax

The basic structure is:

```python
"Text {} {}".format(value1, value2)
```

The `{}` placeholders are replaced by the supplied values.

---

# 1️⃣1️⃣.1️⃣1️⃣ Positional Arguments in `.format()`

We can explicitly specify positions.

```python
name = "Sonal"
course = "Python"
chapter = 13

print(
    "I am learning {1}, my name is {0}, Chapter {2}."
    .format(name, course, chapter)
)
```

Output:

```text
I am learning Python, my name is Sonal, Chapter 13.
```

Here:

```text
{0} → name
{1} → course
{2} → chapter
```

Indexes start from `0`.

---

# 1️⃣1️⃣.1️⃣2️⃣ Named Arguments in `.format()`

We can also use named arguments:

```python
print(
    "My name is {name} and I am learning {course}."
    .format(name="Sonal", course="Python")
)
```

Output:

```text
My name is Sonal and I am learning Python.
```

This can improve readability when there are many values.

---

# 🆚 f-String vs `.format()`

### f-string

```python
name = "Sonal"

print(f"Hello {name}")
```

### `.format()`

```python
name = "Sonal"

print("Hello {}".format(name))
```

Both work.

For modern Python code:

> **f-strings are generally preferred because they are concise and readable.**

`.format()` is still useful when working with existing code or situations where its formatting behavior is convenient.

---

# ⚠️ Important Points About String Formatting

- f-strings are created by adding `f` before the string.
- Variables can be inserted using `{}`.
- Expressions can be written inside `{}`.
- Functions and methods can also be called inside expressions.
- Decimal precision can be controlled using formats such as `.2f`.
- Percentage formatting can use `%`.
- Alignment can be controlled using `<`, `>`, and `^`.
- `.format()` is another string formatting technique.
- Positional indexes in `.format()` start from `0`.
- f-strings are generally preferred for modern Python code.

---

# 🤖 String Formatting in AI Engineering

String formatting is frequently used in AI Engineering.

Examples include:

- Creating logs
- Displaying model predictions
- Formatting evaluation results
- Generating API responses
- Creating prompts
- Building reports
- Displaying metrics

For example:

```python
model_name = "MyModel"
accuracy = 0.9245

print(f"Model: {model_name}")
print(f"Accuracy: {accuracy:.2%}")
```

Output:

```text
Model: MyModel
Accuracy: 92.45%
```

This kind of formatting is useful when presenting machine-learning results.

---

# 🧠 String Formatting — Quick Revision

```text
String Formatting
       ↓
Insert values into strings
       ↓
Main modern method
       ↓
f-strings
       ↓
f"Hello {name}"
       ↓
Can also format:
numbers
decimals
percentages
alignment
expressions
```

---

# 1️⃣2️⃣ `*args` and `**kwargs`

## 📌 Definition

> `*args` allows a function to accept a variable number of positional arguments, while `**kwargs` allows a function to accept a variable number of keyword arguments.

These features are useful when we do not know in advance how many arguments a function will receive.

---

# 📖 Why Do We Need `*args` and `**kwargs`?

Normally, a function has a fixed number of parameters.

For example:

```python
def add(a, b):
    return a + b
```

This function expects two arguments:

```python
print(add(10, 20))
```

But what if we want to support:

```python
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)
```

We could create different functions, but that would be unnecessary.

Instead, we can use:

```python
*args
```

Similarly, when we want to accept a variable number of named arguments, we can use:

```python
**kwargs
```

---

# 1️⃣2️⃣.1️⃣ `*args`

## 📌 Definition

> `*args` allows a function to accept any number of positional arguments and stores them inside a tuple.

The name `args` is a convention. The important part is the `*`.

---

# 🧩 Basic Syntax

```python
def function_name(*args):
    # function body
    pass
```

Example:

```python
def show(*args):
    print(args)

show(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

The arguments are stored as a tuple.

---

# 🔍 Understanding `*args`

Consider:

```python
def student(*args):
    print(args)

student("Python", "AI", "ML")
```

Output:

```text
('Python', 'AI', 'ML')
```

Internally:

```text
args
 ↓
Tuple
 ↓
("Python", "AI", "ML")
```

Therefore, we can iterate over it like any other tuple.

---

# 1️⃣2️⃣.2️⃣ Looping Through `*args`

```python
def student(*subjects):
    for subject in subjects:
        print(subject)

student("Python", "AI", "ML")
```

Output:

```text
Python
AI
ML
```

Here, `subjects` is simply the name chosen for the variable.

The behavior comes from:

```python
*subjects
```

---

# 1️⃣2️⃣.3️⃣ Calculating Sum Using `*args`

One practical example is calculating the sum of any number of values.

```python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))
```

Output:

```text
60
150
```

The function can accept different numbers of arguments.

---

# 1️⃣2️⃣.4️⃣ Calculating Multiplication Using `*args`

```python
def multiply(*args):
    result = 1

    for number in args:
        result *= number

    return result

print(multiply(2, 3, 4))
print(multiply(2, 3, 4, 5))
```

Output:

```text
24
120
```

The same function works with different numbers of arguments.

---

# 1️⃣2️⃣.5️⃣ Normal Parameter with `*args`

We can have normal parameters before `*args`.

For example:

```python
def student(name, *subjects):
    print("Name:", name)
    print("Subjects:", subjects)

student("Sonal", "Python", "AI", "ML")
```

Output:

```text
Name: Sonal
Subjects: ('Python', 'AI', 'ML')
```

Here:

```text
name
 ↓
Receives the first positional argument

subjects
 ↓
Receives all remaining positional arguments
```

---

# 1️⃣2️⃣.6️⃣ Practical Example with Marks

```python
def student(name, *marks):
    print("Name:", name)
    print("Marks:", marks)

    total_marks = 0

    for mark in marks:
        total_marks += mark

    print("Total:", total_marks)

student("Sonal", 80, 75, 90)
```

Output:

```text
Name: Sonal
Marks: (80, 75, 90)
Total: 245
```

Here:

```text
"Sonal"
    ↓
name

80, 75, 90
    ↓
marks
```

---

# 1️⃣2️⃣.7️⃣ `*args` is a Tuple

Because `*args` stores values in a tuple, tuple operations can be used.

```python
def show(*args):
    print(type(args))
    print(len(args))

show(10, 20, 30, 40)
```

Output:

```text
<class 'tuple'>
4
```

Therefore:

```text
*args → tuple
```

---

# 1️⃣2️⃣.8️⃣ Unpacking with `*`

The `*` can also be used when calling a function to unpack an iterable.

For example:

```python
numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

print(add(*numbers))
```

Output:

```text
60
```

Here:

```python
*numbers
```

unpacks:

```text
[10, 20, 30]
```

into:

```text
10, 20, 30
```

---

# 1️⃣2️⃣.9️⃣ `**kwargs`

## 📌 Definition

> `**kwargs` allows a function to accept any number of keyword arguments and stores them inside a dictionary.

Again, `kwargs` is only a naming convention.

The important part is:

```text
**
```

---

# 🧩 Basic Syntax

```python
def function_name(**kwargs):
    # function body
    pass
```

Example:

```python
def student(**kwargs):
    print(kwargs)

student(name="Sonal", age=25, course="Python")
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'course': 'Python'}
```

---

# 🔍 Understanding `**kwargs`

Consider:

```python
student(
    name="Sonal",
    age=25,
    course="Python"
)
```

These are keyword arguments.

`**kwargs` collects them into a dictionary:

```python
{
    "name": "Sonal",
    "age": 25,
    "course": "Python"
}
```

Therefore:

```text
**kwargs
    ↓
Dictionary
```

---

# 1️⃣2️⃣.🔟 Looping Through `**kwargs`

Since `kwargs` is a dictionary, we can use `.items()`.

```python
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(
    name="Sonal",
    age=25,
    course="Python"
)
```

Output:

```text
name : Sonal
age : 25
course : Python
```

---

# 1️⃣2️⃣.1️⃣1️⃣ Practical Example with `**kwargs`

```python
def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(
    name="Sonal",
    age=25,
    city="Lucknow",
    skill="Python"
)
```

Output:

```text
name : Sonal
age : 25
city : Lucknow
skill : Python
```

The function can accept any number of keyword arguments.

---

# 1️⃣2️⃣.1️⃣2️⃣ Accessing Individual `kwargs`

Since `kwargs` is a dictionary, we can access values using keys.

```python
def student(**kwargs):
    print("Name:", kwargs["name"])
    print("Course:", kwargs["course"])

student(
    name="Sonal",
    course="Python"
)
```

Output:

```text
Name: Sonal
Course: Python
```

We can also use `.get()`:

```python
def student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

student(
    name="Sonal",
    course="Python"
)
```

Using `.get()` can be safer when a key may not exist.

---

# 1️⃣2️⃣.1️⃣3️⃣ `**kwargs` is a Dictionary

We can verify its type:

```python
def show(**kwargs):
    print(type(kwargs))

show(name="Sonal", age=25)
```

Output:

```text
<class 'dict'>
```

Therefore:

```text
*args
   ↓
tuple

**kwargs
   ↓
dictionary
```

This distinction is very important.

---

# 1️⃣2️⃣.1️⃣4️⃣ Unpacking with `**`

Just as `*` can unpack a list or tuple, `**` can unpack a dictionary into keyword arguments.

Example:

```python
details = {
    "name": "Sonal",
    "age": 25
}

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(**details)
```

Output:

```text
Name: Sonal
Age: 25
```

Here:

```python
**details
```

unpacks the dictionary into:

```python
name="Sonal"
age=25
```

---

# 1️⃣2️⃣.1️⃣5️⃣ Combining Normal Arguments, `*args`, and `**kwargs`

We can use all three together.

```python
def student(name, *marks, **details):
    print("Name:", name)
    print("Marks:", marks)

    for key, value in details.items():
        print(key, ":", value)

student(
    "Sonal",
    80, 75, 90,
    age=25,
    course="Python"
)
```

Output:

```text
Name: Sonal
Marks: (80, 75, 90)
age : 25
course : Python
```

---

# 🔢 Order of Parameters

When all types are used together, the usual order is:

```text
Normal positional parameters
        ↓
*args
        ↓
**kwargs
```

For example:

```python
def function(name, *args, **kwargs):
    pass
```

This is valid.

---

# 🧠 Understanding the Complete Flow

Consider:

```python
def student(name, *marks, **details):
    ...
```

and:

```python
student(
    "Sonal",
    80,
    75,
    90,
    age=25,
    course="Python"
)
```

The arguments are divided as:

```text
"Sonal"
   ↓
name

80, 75, 90
   ↓
marks → tuple

age=25
course="Python"
   ↓
details → dictionary
```

Therefore:

```text
name
 ↓
"Sonal"

marks
 ↓
(80, 75, 90)

details
 ↓
{
    "age": 25,
    "course": "Python"
}
```

---

# 🆚 `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Argument type | Positional | Keyword |
| Stores data in | Tuple | Dictionary |
| Symbol | `*` | `**` |
| Example | `10, 20, 30` | `name="Sonal"` |
| Useful for | Variable positional arguments | Variable named arguments |

---

# 🧠 Easy Way to Remember

```text
*args
   ↓
Positional arguments
   ↓
Tuple

**kwargs
   ↓
Keyword arguments
   ↓
Dictionary
```

---

# 1️⃣2️⃣.1️⃣6️⃣ `*args` and `**kwargs` with Existing Parameters

We can combine fixed parameters with flexible parameters.

Example:

```python
def introduce(name, age, *skills):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)

introduce(
    "Sonal",
    25,
    "Python",
    "AI",
    "ML"
)
```

Output:

```text
Name: Sonal
Age: 25
Skills: ('Python', 'AI', 'ML')
```

---

# 1️⃣2️⃣.1️⃣7️⃣ Passing Both `*args` and `**kwargs`

```python
def profile(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)

profile(
    "Sonal",
    "Python",
    "Git",
    "AI",
    age=25,
    course="B.Tech"
)
```

Output:

```text
Name: Sonal
Skills: ('Python', 'Git', 'AI')
Details: {'age': 25, 'course': 'B.Tech'}
```

---

# 📌 When Should We Use `*args`?

`*args` is useful when:

- The number of positional arguments is unknown.
- A function should accept a flexible number of values.
- We want to process multiple values using a loop.
- We are creating reusable functions.
- We are designing flexible APIs or utility functions.

Examples:

```text
Adding any number of numbers
Multiplying any number of values
Accepting multiple subjects
Accepting multiple scores
Passing variable data to a function
```

---

# 📌 When Should We Use `**kwargs`?

`**kwargs` is useful when:

- The number of keyword arguments is unknown.
- We want flexible named parameters.
- Configuration options need to be passed to a function.
- A function needs optional settings.
- We are building reusable utilities or APIs.

Examples:

```text
name="Sonal"
age=25
course="Python"
city="Lucknow"
```

---

# ⚠️ Important Points

- `*args` collects extra positional arguments.
- `*args` stores them as a tuple.
- `**kwargs` collects extra keyword arguments.
- `**kwargs` stores them as a dictionary.
- `args` and `kwargs` are conventional names, not reserved keywords.
- The `*` and `**` symbols provide the special behavior.
- Normal parameters can be combined with `*args` and `**kwargs`.
- When used together, the usual order is:

```text
normal parameters → *args → **kwargs
```

- `*` can unpack an iterable when calling a function.
- `**` can unpack a dictionary when calling a function.

---

# 🤖 `*args` and `**kwargs` in AI Engineering

These concepts are particularly useful when working with reusable Python libraries, APIs, configuration systems, and frameworks.

For example, an AI utility function may accept flexible options:

```python
def run_model(model_name, *inputs, **options):
    print("Model:", model_name)
    print("Inputs:", inputs)
    print("Options:", options)
```

It can then be called with different numbers of inputs and options:

```python
run_model(
    "MyModel",
    "image1",
    "image2",
    temperature=0.7,
    max_tokens=500
)
```

This kind of flexible function design appears frequently in larger Python codebases and frameworks.

---

# 🧠 `*args` and `**kwargs` — Quick Revision

```text
*args
  ↓
Variable positional arguments
  ↓
Stored as tuple

**kwargs
  ↓
Variable keyword arguments
  ↓
Stored as dictionary

Together:
normal args → *args → **kwargs
```

---

# 1️⃣3️⃣ zip()

## 📌 Definition

> `zip()` is a built-in Python function that combines elements from two or more iterables pair by pair and returns them as tuples.

It is useful when we want to process related data from multiple collections together.

---

# 📖 Why Do We Need zip()?

Suppose we have two lists:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]
```

The first name corresponds to the first mark:

```text
Sonal → 85
Aman  → 90
Rahul → 78
```

`zip()` makes it easy to combine these values.

```python
result = zip(names, marks)

print(list(result))
```

Output:

```text
[('Sonal', 85), ('Aman', 90), ('Rahul', 78)]
```

---

# 🧩 Basic Syntax

```python
zip(iterable1, iterable2, ...)
```

Example:

```python
zip(names, marks)
```

The elements are paired according to their positions.

---

# 🔍 Understanding zip()

Consider:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]
```

`zip()` creates:

```text
("Sonal", 85)
("Aman", 90)
("Rahul", 78)
```

Therefore:

```python
list(zip(names, marks))
```

produces:

```text
[('Sonal', 85), ('Aman', 90), ('Rahul', 78)]
```

---

# 1️⃣3️⃣.1️⃣ zip() Returns a zip Object

Like `map()` and `filter()`, `zip()` returns a special iterable object.

```python
names = ["Sonal", "Aman"]
marks = [85, 90]

result = zip(names, marks)

print(result)
```

The output will be similar to:

```text
<zip object at 0x...>
```

To see the paired values:

```python
print(list(result))
```

Output:

```text
[('Sonal', 85), ('Aman', 90)]
```

---

# 1️⃣3️⃣.2️⃣ zip() with Different Lengths

Suppose:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90]
```

Then:

```python
result = zip(names, marks)

print(list(result))
```

Output:

```text
[('Sonal', 85), ('Aman', 90)]
```

`zip()` stops when the shortest iterable is exhausted.

Therefore:

```text
names → 3 elements
marks → 2 elements

Result → 2 pairs
```

---

# 1️⃣3️⃣.3️⃣ zip() with Three Iterables

`zip()` can combine more than two iterables.

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]
courses = ["Python", "AI", "ML"]

result = zip(names, marks, courses)

print(list(result))
```

Output:

```text
[
    ('Sonal', 85, 'Python'),
    ('Aman', 90, 'AI'),
    ('Rahul', 78, 'ML')
]
```

Each position is combined together.

---

# 1️⃣3️⃣.4️⃣ zip() with a for Loop

We do not always need to convert the result into a list.

We can iterate directly:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, ":", mark)
```

Output:

```text
Sonal : 85
Aman : 90
Rahul : 78
```

This is often useful when we simply need to process paired values.

---

# 1️⃣3️⃣.5️⃣ Creating a Dictionary Using zip()

One very useful application of `zip()` is creating a dictionary from separate keys and values.

```python
keys = ["name", "age", "course"]
values = ["Sonal", 25, "Python"]

student = dict(zip(keys, values))

print(student)
```

Output:

```text
{'name': 'Sonal', 'age': 25, 'course': 'Python'}
```

The process is:

```text
keys
 ↓
["name", "age", "course"]

values
 ↓
["Sonal", 25, "Python"]

zip()
 ↓
("name", "Sonal")
("age", 25)
("course", "Python")

dict()
 ↓
Dictionary
```

---

# 1️⃣3️⃣.6️⃣ zip() and Unpacking

We can also reverse the process using unpacking.

Suppose:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

zipped = zip(names, marks)
```

We can unpack it:

```python
student_names, student_marks = zip(*zipped)

print(student_names)
print(student_marks)
```

Output:

```text
('Sonal', 'Aman', 'Rahul')
(85, 90, 78)
```

Here:

```python
*zipped
```

unpacks the zipped pairs.

---

# 1️⃣3️⃣.7️⃣ zip() with Strings

Strings are also iterable.

For example:

```python
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

result = zip(letters, numbers)

print(list(result))
```

Output:

```text
[('A', 1), ('B', 2), ('C', 3)]
```

---

# 🆚 zip() vs `enumerate()`

Both can be used to work with multiple pieces of information, but they serve different purposes.

### `enumerate()`

Provides:

```text
index + value
```

Example:

```python
names = ["Sonal", "Aman", "Rahul"]

for index, name in enumerate(names):
    print(index, name)
```

### `zip()`

Combines elements from multiple iterables:

```text
value1 + value2 + ...
```

Example:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, mark)
```

Easy distinction:

```text
enumerate()
    ↓
index + item

zip()
    ↓
item + item + item
```

---

# 📌 When Should We Use zip()?

Use `zip()` when:

- Related data is stored in separate iterables.
- We need to process multiple lists together.
- We need to create dictionaries from keys and values.
- We need to pair corresponding elements.
- We need to iterate over multiple sequences simultaneously.

Common examples:

```text
Names + Marks
Products + Prices
Keys + Values
Features + Labels
Names + IDs
```

---

# 🤖 zip() in AI Engineering

`zip()` is useful when working with related data.

For example:

```python
features = ["age", "salary", "experience"]
values = [25, 50000, 2]

data = dict(zip(features, values))

print(data)
```

Output:

```text
{
    'age': 25,
    'salary': 50000,
    'experience': 2
}
```

It can also be useful when working with:

- Input data and labels
- Predictions and actual values
- File names and predictions
- Features and metadata
- Dataset records

For example:

```python
predictions = ["cat", "dog", "car"]
actual = ["cat", "cat", "car"]

for prediction, true_label in zip(predictions, actual):
    print(prediction, true_label)
```

This allows related values to be processed together.

---

# ⚠️ Important Points About zip()

- `zip()` is a built-in Python function.
- It combines corresponding elements from multiple iterables.
- It returns a `zip` object.
- `list()` can be used to view all pairs at once.
- It stops at the shortest iterable.
- It can combine two or more iterables.
- `dict(zip(keys, values))` is a common pattern.
- `*` can be used to unpack zipped data.

---

# 🧠 zip() — Quick Revision

```text
zip()
  ↓
Combines multiple iterables
  ↓
Pairs elements by position
  ↓
Returns zip object
  ↓
Stops at shortest iterable
  ↓
Can be converted into:
list
tuple
dictionary
```

---

# 1️⃣4️⃣ sorted() and key=

## 📌 Definition

> `sorted()` is a built-in Python function that returns a new sorted list from an iterable without modifying the original iterable.

`sorted()` is useful when we need to arrange data in:

- Ascending order
- Descending order
- Alphabetical order
- Length-based order
- Custom order
- Order based on a particular value inside a data structure

---

# 📖 Why Do We Need sorted()?

Suppose we have:

```python
numbers = [40, 10, 30, 20, 50]
```

We can sort them using:

```python
result = sorted(numbers)

print(result)
```

Output:

```text
[10, 20, 30, 40, 50]
```

The original list remains unchanged:

```python
print(numbers)
```

Output:

```text
[40, 10, 30, 20, 50]
```

This is one of the important differences between `sorted()` and the list method `sort()`.

---

# 🧩 Basic Syntax

The basic syntax is:

```python
sorted(iterable)
```

For example:

```python
numbers = [40, 10, 30, 20, 50]

result = sorted(numbers)

print(result)
```

---

# 1️⃣4️⃣.1️⃣ sorted() with Numbers

```python
numbers = [50, 20, 80, 10, 40]

result = sorted(numbers)

print(result)
```

Output:

```text
[10, 20, 40, 50, 80]
```

By default, numbers are sorted in ascending order.

---

# 1️⃣4️⃣.2️⃣ Descending Order

We can use:

```python
reverse=True
```

Example:

```python
numbers = [50, 20, 80, 10, 40]

result = sorted(numbers, reverse=True)

print(result)
```

Output:

```text
[80, 50, 40, 20, 10]
```

Therefore:

```text
reverse=False
    ↓
Ascending order

reverse=True
    ↓
Descending order
```

`reverse=False` is the default behavior.

---

# 1️⃣4️⃣.3️⃣ sorted() with Strings

`sorted()` can also sort strings.

```python
names = ["Sonal", "Aman", "Rahul", "Om"]

result = sorted(names)

print(result)
```

Output:

```text
['Aman', 'Om', 'Rahul', 'Sonal']
```

The strings are sorted according to their ordering rules.

---

# 1️⃣4️⃣.4️⃣ Sorting Strings by Length

Suppose we want to sort strings according to their length rather than alphabetically.

We can use:

```python
key=len
```

Example:

```python
names = ["Sonal", "Aman", "Rahul", "Om"]

result = sorted(names, key=len)

print(result)
```

Output:

```text
['Om', 'Aman', 'Sonal', 'Rahul']
```

Here:

```python
key=len
```

means:

> Use the length of each string as the basis for sorting.

---

# 📌 What is key=?

## Definition

> The `key` parameter tells `sorted()` what value or property should be used to determine the sorting order.

This is extremely important when working with complex data.

---

# 🔍 Understanding key=

Consider:

```python
names = ["Sonal", "Aman", "Rahul", "Om"]

result = sorted(names, key=len)
```

Python effectively checks:

```text
Sonal → length 5
Aman  → length 4
Rahul → length 5
Om    → length 2
```

Then sorts according to those values:

```text
2 → Om
4 → Aman
5 → Sonal
5 → Rahul
```

Final result:

```text
['Om', 'Aman', 'Sonal', 'Rahul']
```

---

# 1️⃣4️⃣.5️⃣ key= with a Custom Function

The `key` parameter does not have to be a built-in function.

We can define our own function.

```python
def get_length(name):
    return len(name)

names = ["Sonal", "Aman", "Rahul", "Om"]

result = sorted(names, key=get_length)

print(result)
```

Output:

```text
['Om', 'Aman', 'Sonal', 'Rahul']
```

Here:

```python
get_length
```

is passed as the key function.

---

# 1️⃣4️⃣.6️⃣ key= with lambda

A lambda function is frequently used when the sorting logic is short.

```python
names = ["Sonal", "Aman", "Rahul", "Om"]

result = sorted(names, key=lambda name: len(name))

print(result)
```

Output:

```text
['Om', 'Aman', 'Sonal', 'Rahul']
```

This is equivalent to:

```python
def get_length(name):
    return len(name)

result = sorted(names, key=get_length)
```

The lambda version is shorter.

---

# 1️⃣4️⃣.7️⃣ Sorting Tuples

Suppose we have:

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]
```

Each tuple contains:

```text
(name, marks)
```

If we use:

```python
sorted(students)
```

Python will primarily sort according to the first element:

```text
Name
```

But suppose we want to sort according to marks.

We can use:

```python
result = sorted(students, key=lambda student: student[1])

print(result)
```

Output:

```text
[
    ('Rahul', 78),
    ('Sonal', 85),
    ('Aman', 92)
]
```

---

# 🔍 Understanding student[1]

Consider:

```python
student = ("Sonal", 85)
```

The indexes are:

```text
student[0] → "Sonal"
student[1] → 85
```

Therefore:

```python
lambda student: student[1]
```

means:

> For each student tuple, use the marks as the sorting key.

---

# 1️⃣4️⃣.8️⃣ Sorting Tuples in Descending Order

We can combine `key=` with `reverse=True`.

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)
```

Output:

```text
[
    ('Aman', 92),
    ('Sonal', 85),
    ('Rahul', 78)
]
```

---

# 1️⃣4️⃣.9️⃣ Using a Normal Function Instead of lambda

The same operation can be written using a normal function:

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]

def get_marks(student):
    return student[1]

result = sorted(students, key=get_marks)

print(result)
```

Output:

```text
[
    ('Rahul', 78),
    ('Sonal', 85),
    ('Aman', 92)
]
```

Both approaches are valid.

Use a lambda when the logic is simple and short.

Use a normal function when the logic becomes more complicated or needs to be reused.

---

# 1️⃣4️⃣.🔟 Sorting Dictionaries

Suppose we have a dictionary:

```python
students = {
    "Sonal": 85,
    "Aman": 92,
    "Rahul": 78
}
```

If we want to sort the dictionary items according to marks:

```python
result = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(result)
```

Output:

```text
[('Rahul', 78), ('Sonal', 85), ('Aman', 92)]
```

Here:

```python
students.items()
```

produces key-value pairs such as:

```text
("Sonal", 85)
("Aman", 92)
("Rahul", 78)
```

and:

```python
item[1]
```

refers to the value.

---

# 1️⃣4️⃣.1️⃣1️⃣ Sorting by Dictionary Values in Descending Order

```python
students = {
    "Sonal": 85,
    "Aman": 92,
    "Rahul": 78
}

result = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)

print(result)
```

Output:

```text
[('Aman', 92), ('Sonal', 85), ('Rahul', 78)]
```

---

# 1️⃣4️⃣.1️⃣2️⃣ Sorting by Dictionary Keys

If we want to sort dictionary items according to their keys:

```python
students = {
    "Sonal": 85,
    "Aman": 92,
    "Rahul": 78
}

result = sorted(
    students.items(),
    key=lambda item: item[0]
)

print(result)
```

Output:

```text
[('Aman', 92), ('Rahul', 78), ('Sonal', 85)]
```

Here:

```python
item[0]
```

represents the key.

---

# 1️⃣4️⃣.1️⃣3️⃣ Sorting Products by Price

A practical example:

```python
products = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]

result = sorted(
    products,
    key=lambda product: product[1]
)

print(result)
```

Output:

```text
[
    ('Mouse', 800),
    ('Keyboard', 1500),
    ('Monitor', 12000),
    ('Laptop', 55000)
]
```

The sorting key is the price.

---

# 1️⃣4️⃣.1️⃣4️⃣ Sorting Products from Highest Price to Lowest

```python
products = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]

result = sorted(
    products,
    key=lambda product: product[1],
    reverse=True
)

print(result)
```

Output:

```text
[
    ('Laptop', 55000),
    ('Monitor', 12000),
    ('Keyboard', 1500),
    ('Mouse', 800)
]
```

---

# 🆚 sorted() vs list.sort()

This distinction is very important.

## `sorted()`

`sorted()` returns a **new list**.

```python
numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
print(numbers)
```

Output:

```text
[10, 20, 30]
[30, 10, 20]
```

The original list is unchanged.

---

## `list.sort()`

`sort()` modifies the original list.

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30]
```

The original list has been changed.

---

# 📊 sorted() vs sort()

| Feature | `sorted()` | `.sort()` |
|---|---|---|
| Type | Built-in function | List method |
| Returns | New sorted list | `None` |
| Original list | Unchanged | Modified |
| Works with | Many iterables | Lists |
| Supports `key=` | Yes | Yes |
| Supports `reverse=` | Yes | Yes |

---

# 1️⃣4️⃣.1️⃣5️⃣ Sorting Without Modifying Original Data

This is one reason `sorted()` is useful.

```python
numbers = [50, 10, 30, 20, 40]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
```

Output:

```text
Original: [50, 10, 30, 20, 40]
Sorted: [10, 20, 30, 40, 50]
```

---

# 1️⃣4️⃣.1️⃣6️⃣ Sorting by Multiple Criteria

`key=` can also be used with multiple values.

Suppose:

```python
students = [
    ("Sonal", 85),
    ("Aman", 85),
    ("Rahul", 78),
    ("Rohit", 92)
]
```

We may want to sort by:

1. Marks
2. Then name

We can return a tuple from the key:

```python
result = sorted(
    students,
    key=lambda student: (student[1], student[0])
)

print(result)
```

The tuple returned by the key determines the sorting priority.

Conceptually:

```text
First → marks
Then  → name
```

---

# 1️⃣4️⃣.1️⃣7️⃣ Sorting with Case-Insensitive Strings

Normally, uppercase and lowercase letters can affect string ordering.

For case-insensitive sorting:

```python
names = ["sonal", "Aman", "rahul", "Rohit"]

result = sorted(names, key=str.lower)

print(result)
```

Output:

```text
['Aman', 'rahul', 'Rohit', 'sonal']
```

Here:

```python
str.lower
```

is used as the sorting key.

---

# 1️⃣4️⃣.1️⃣8️⃣ Sorting by Absolute Value

Suppose:

```python
numbers = [-10, 5, -3, 8, -2]
```

We want to sort based on absolute value.

We can use:

```python
result = sorted(numbers, key=abs)

print(result)
```

Output:

```text
[-2, -3, 5, 8, -10]
```

The sorting key is:

```text
abs(number)
```

---

# 🧠 Understanding key=

The most important idea is:

```python
sorted(data, key=function)
```

The `key` function does not change the original values.

Instead, it tells Python:

> "Use the result of this function to decide the sorting order."

For example:

```python
names = ["Python", "AI", "Machine", "ML"]

sorted(names, key=len)
```

Python effectively considers:

```text
Python   → 6
AI       → 2
Machine  → 7
ML       → 2
```

and sorts according to those key values.

---

# 📌 When Should We Use sorted()?

Use `sorted()` when:

- We need a new sorted list.
- We do not want to modify the original iterable.
- We need ascending or descending order.
- We need custom sorting.
- We need to sort complex data.
- We need to sort according to a specific field or property.

---

# ⚠️ Important Points About sorted()

- `sorted()` is a built-in Python function.
- It returns a new sorted list.
- It does not modify the original iterable.
- `reverse=True` gives descending order.
- `key=` specifies the basis of sorting.
- `key` can receive a built-in function.
- `key` can receive a custom function.
- Lambda functions are commonly used with `key=`.
- `sorted()` works with many iterable types.
- `sort()` modifies a list, while `sorted()` creates a new list.

---

# 🤖 sorted() in AI Engineering

Sorting is frequently used when processing AI/ML-related data.

Examples include:

- Sorting predictions by confidence
- Ranking search results
- Sorting scores
- Ranking recommendations
- Sorting datasets
- Ordering model outputs
- Selecting highest-scoring results

For example:

```python
predictions = [
    ("Cat", 0.82),
    ("Dog", 0.94),
    ("Car", 0.41)
]

result = sorted(
    predictions,
    key=lambda prediction: prediction[1],
    reverse=True
)

print(result)
```

Output:

```text
[
    ('Dog', 0.94),
    ('Cat', 0.82),
    ('Car', 0.41)
]
```

This pattern is useful for ranking predictions by confidence.

---

# 🧠 sorted() + key= — Quick Revision

```text
sorted()
    ↓
Returns new sorted list
    ↓
reverse=True
    ↓
Descending order

key=
    ↓
Defines sorting criteria

lambda
    ↓
Useful for short custom sorting logic
```

---

# 1️⃣5️⃣ any() and all()

## 📌 Definition

> `any()` returns `True` if at least one element in an iterable is truthy, while `all()` returns `True` only if every element in an iterable is truthy.

Both functions are useful for checking conditions across collections of values.

---

# 📖 Truthy and Falsy Values

Before understanding `any()` and `all()`, we need to understand truthy and falsy values.

Python treats some values as `False` in a Boolean context.

Common falsy values include:

```text
False
0
0.0
""
None
[]
{}
()
```

Most other values are generally truthy.

For example:

```text
True
1
-1
"Python"
[1, 2]
{"name": "Sonal"}
```

are truthy.

---

# 1️⃣5️⃣.1️⃣ any()

## 📌 Definition

> `any()` returns `True` if at least one element of an iterable is truthy. It returns `False` if all elements are falsy.

---

# 🧩 Basic Syntax

```python
any(iterable)
```

Example:

```python
values = [False, False, True, False]

result = any(values)

print(result)
```

Output:

```text
True
```

Because at least one value is `True`.

---

# 1️⃣5️⃣.2️⃣ any() with Numbers

```python
numbers = [0, 0, 5, 0]

print(any(numbers))
```

Output:

```text
True
```

Because `5` is truthy.

---

# 1️⃣5️⃣.3️⃣ any() When All Values Are False

```python
numbers = [0, 0, 0, 0]

print(any(numbers))
```

Output:

```text
False
```

Every value is falsy.

---

# 1️⃣5️⃣.4️⃣ any() with Conditions

A very useful pattern is:

```python
any(condition for item in iterable)
```

For example:

```python
numbers = [10, 20, 30, 40]

result = any(number > 25 for number in numbers)

print(result)
```

Output:

```text
True
```

Why?

Because:

```text
10 > 25 → False
20 > 25 → False
30 > 25 → True
40 > 25 → True
```

At least one condition is true.

Therefore:

```text
any() → True
```

---

# 1️⃣5️⃣.5️⃣ Checking for a Specific Condition

```python
numbers = [10, 20, 30, 40]

result = any(number == 30 for number in numbers)

print(result)
```

Output:

```text
True
```

Because one element is equal to `30`.

---

# 1️⃣5️⃣.6️⃣ all()

## 📌 Definition

> `all()` returns `True` only if every element of an iterable is truthy. If even one element is falsy, it returns `False`.

---

# 🧩 Basic Syntax

```python
all(iterable)
```

Example:

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

---

# 1️⃣5️⃣.7️⃣ all() with Numbers

```python
numbers = [1, 2, 3, 4]

print(all(numbers))
```

Output:

```text
True
```

All values are non-zero and therefore truthy.

---

# 1️⃣5️⃣.8️⃣ all() with a Zero

```python
numbers = [1, 2, 0, 4]

print(all(numbers))
```

Output:

```text
False
```

Because:

```text
0
```

is falsy.

---

# 1️⃣5️⃣.9️⃣ all() with Conditions

A common pattern is:

```python
all(condition for item in iterable)
```

Example:

```python
numbers = [10, 20, 30, 40]

result = all(number > 5 for number in numbers)

print(result)
```

Output:

```text
True
```

Every number is greater than `5`.

---

# 1️⃣5️⃣.🔟 all() with a Failing Condition

```python
numbers = [10, 20, 30, 4]

result = all(number > 5 for number in numbers)

print(result)
```

Output:

```text
False
```

Because:

```text
4 > 5
```

is false.

Only one false condition is enough for `all()` to return `False`.

---

# 🆚 any() vs all()

This distinction is extremely important.

| Function | Meaning |
|---|---|
| `any()` | At least one condition must be true |
| `all()` | Every condition must be true |

Easy way to remember:

```text
any()
 ↓
ANY ONE is enough

all()
 ↓
ALL must satisfy
```

---

# 🧪 Practical Example

Suppose we have marks:

```python
marks = [75, 82, 91, 68, 45]
```

We want to check:

1. Is at least one student scoring `90` or above?
2. Did every student score at least `50`?

We can write:

```python
marks = [75, 82, 91, 68, 45]

result1 = any(mark >= 90 for mark in marks)
result2 = all(mark >= 50 for mark in marks)

print(f"Output of any: {result1}")
print(f"Output of all: {result2}")
```

Output:

```text
Output of any: True
Output of all: False
```

Why?

For `any()`:

```text
91 >= 90
```

is true.

Therefore:

```text
any() → True
```

For `all()`:

```text
45 >= 50
```

is false.

Therefore:

```text
all() → False
```

---

# 1️⃣5️⃣.1️⃣1️⃣ any() with Strings

```python
names = ["", "", "Sonal", ""]

result = any(names)

print(result)
```

Output:

```text
True
```

Because `"Sonal"` is a non-empty string.

---

# 1️⃣5️⃣.1️⃣2️⃣ all() with Strings

```python
names = ["Sonal", "Aman", "Rahul"]

result = all(names)

print(result)
```

Output:

```text
True
```

All strings are non-empty.

If one is empty:

```python
names = ["Sonal", "", "Rahul"]

result = all(names)

print(result)
```

Output:

```text
False
```

---

# 1️⃣5️⃣.1️⃣3️⃣ any() and all() with Lists

```python
values = [[], [], [1, 2]]

print(any(values))
```

Output:

```text
True
```

Because `[1, 2]` is non-empty and therefore truthy.

For `all()`:

```python
values = [[1], [2], []]

print(all(values))
```

Output:

```text
False
```

Because the empty list is falsy.

---

# 🧠 Short-Circuit Behavior

`any()` and `all()` can stop evaluating as soon as the final result is known.

For `any()`:

```text
First True found
     ↓
Result is definitely True
     ↓
No need to check further
```

For `all()`:

```text
First False found
     ↓
Result is definitely False
     ↓
No need to check further
```

This behavior is called **short-circuit evaluation**.

---

# 📌 When Should We Use any()?

Use `any()` when the question is:

> "Is there at least one element that satisfies this condition?"

Examples:

```text
Is anyone above the age limit?
Is any prediction above a confidence threshold?
Does any value contain an error?
Is any file missing?
```

---

# 📌 When Should We Use all()?

Use `all()` when the question is:

> "Do all elements satisfy this condition?"

Examples:

```text
Are all marks passing?
Are all inputs valid?
Are all values positive?
Are all required fields present?
```

---

# ⚠️ Important Points About any() and all()

- Both are built-in Python functions.
- `any()` checks whether at least one value is truthy.
- `all()` checks whether every value is truthy.
- Both can be used with generators and comprehensions.
- `any()` can stop after finding a true value.
- `all()` can stop after finding a false value.
- Conditions are often written using generator expressions.
- Empty iterables have special behavior:
  - `any([])` → `False`
  - `all([])` → `True`

---

# 🤖 any() and all() in AI Engineering

These functions can be useful when validating data and model outputs.

For example, checking whether any prediction has high confidence:

```python
confidence_scores = [0.42, 0.51, 0.91, 0.63]

high_confidence = any(
    score >= 0.90
    for score in confidence_scores
)

print(high_confidence)
```

Output:

```text
True
```

Checking whether all input values are valid:

```python
values = [10, 20, 30, 40]

all_positive = all(
    value > 0
    for value in values
)

print(all_positive)
```

Output:

```text
True
```

These patterns can be useful in:

- Data validation
- Input validation
- Model result checking
- Threshold-based decisions
- Preprocessing pipelines

---

# 🧠 any() and all() — Quick Revision

```text
any()
  ↓
At least ONE must be truthy
  ↓
Any one True → True

all()
  ↓
EVERY value must be truthy
  ↓
One False → False
```

---

# 1️⃣6️⃣ pathlib

## 📌 Definition

> `pathlib` is a Python standard library module that provides an object-oriented way to work with files, folders, and filesystem paths.

`pathlib` is especially useful when a Python program needs to:

- Work with file paths
- Check whether files or folders exist
- Create files and directories
- Read and write text files
- Find files
- Navigate through directories
- Build paths safely
- Work with file extensions
- Handle relative and absolute paths

---

# 📖 Why Do We Need pathlib?

Python programs frequently need to interact with the filesystem.

For example, a program may need to:

```text
Find a file
Create a folder
Read a configuration file
Find all .py files
Check whether a file exists
Rename a file
Delete a file
Search through directories
```

Python provides modules such as `os` for filesystem operations, but `pathlib` provides a cleaner and more object-oriented interface for working specifically with paths.

Instead of treating paths only as strings:

```python
path = "C:/Users/Sonal/Documents/project/data.txt"
```

we can create a `Path` object:

```python
from pathlib import Path

path = Path("C:/Users/Sonal/Documents/project/data.txt")
```

Now the path can be manipulated using useful methods and properties.

---

# 1️⃣6️⃣.1️⃣ Importing pathlib

The most common approach is:

```python
from pathlib import Path
```

Then we can create a path:

```python
path = Path("example.txt")
```

---

# 1️⃣6️⃣.2️⃣ Path()

## 📌 Definition

> `Path()` creates a `Path` object representing a filesystem path.

Example:

```python
from pathlib import Path

path = Path("example.txt")

print(path)
```

Output:

```text
example.txt
```

The object represents the path to the file.

---

# 1️⃣6️⃣.3️⃣ Current Working Directory

We can find the current working directory using:

```python
from pathlib import Path

current_directory = Path.cwd()

print(current_directory)
```

Example output:

```text
C:\Users\Sonal\Desktop\Python-Learning\CodeWithHarry\CHAPTER 13
```

`cwd()` means:

```text
Current Working Directory
```

---

# 🧠 Why is the Current Working Directory Important?

Relative paths are interpreted with respect to the current working directory.

For example:

```python
path = Path("data.txt")
```

means:

> Look for `data.txt` relative to the current working directory.

Therefore, understanding the current working directory is important when working with files.

---

# 1️⃣6️⃣.4️⃣ Checking Whether a Path Exists

We can use:

```python
.exists()
```

Example:

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
```

Possible output:

```text
True
```

or:

```text
False
```

depending on whether the path exists.

---

# 1️⃣6️⃣.5️⃣ Checking Whether a Path is a File

We can use:

```python
.is_file()
```

Example:

```python
from pathlib import Path

path = Path("data.txt")

print(path.is_file())
```

If `data.txt` exists and is a file:

```text
True
```

If it does not exist or is not a file:

```text
False
```

---

# 1️⃣6️⃣.6️⃣ Checking Whether a Path is a Directory

We can use:

```python
.is_dir()
```

Example:

```python
from pathlib import Path

path = Path("project")

print(path.is_dir())
```

This checks whether the path represents a directory.

---

# 🆚 exists(), is_file(), and is_dir()

These methods answer different questions:

```text
.exists()
    ↓
Does this path exist?

.is_file()
    ↓
Does this path exist as a file?

.is_dir()
    ↓
Does this path exist as a directory?
```

Example:

```python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    print("Path exists.")

if path.is_file():
    print("It is a file.")

if path.is_dir():
    print("It is a directory.")
```

---

# 1️⃣6️⃣.7️⃣ Creating a Directory with mkdir()

`mkdir()` is used to create a directory.

Example:

```python
from pathlib import Path

folder = Path("data")
folder.mkdir()
```

This creates:

```text
data/
```

if it does not already exist.

---

# ⚠️ `exist_ok=True`

If the directory already exists, calling `mkdir()` normally raises an error.

We can avoid that using:

```python
folder.mkdir(exist_ok=True)
```

This means:

> Create the directory if it does not exist, but do not raise an error if it already exists.

Example:

```python
from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)
```

This is a safer pattern when the directory may already exist.

---

# 1️⃣6️⃣.8️⃣ Creating Nested Directories

Suppose we want:

```text
project/
└── data/
    └── raw/
```

We can use:

```python
from pathlib import Path

folder = Path("project/data/raw")

folder.mkdir(parents=True, exist_ok=True)
```

Here:

```text
parents=True
```

allows missing parent directories to be created.

And:

```text
exist_ok=True
```

prevents an error if the directories already exist.

---

# 🧠 mkdir() Important Parameters

```python
mkdir(
    mode=0o777,
    parents=False,
    exist_ok=False
)
```

The most practically useful parameters are:

### `parents=True`

Creates missing parent directories.

### `exist_ok=True`

Does not raise an error if the directory already exists.

A common practical pattern is:

```python
Path("project/data/raw").mkdir(
    parents=True,
    exist_ok=True
)
```

---

# 1️⃣6️⃣.9️⃣ Creating a File with touch()

`touch()` can be used to create an empty file.

Example:

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.touch()
```

This creates:

```text
example.txt
```

if it does not already exist.

---

# ⚠️ `touch(exist_ok=True)`

We can use:

```python
file_path.touch(exist_ok=True)
```

This avoids an error if the file already exists.

Example:

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.touch(exist_ok=True)
```

---

# 1️⃣6️⃣.🔟 Joining Paths Using `/`

One of the nicest features of `pathlib` is path joining.

Instead of manually writing:

```python
"data/" + "raw/" + "file.txt"
```

we can use:

```python
from pathlib import Path

path = Path("data") / "raw" / "file.txt"

print(path)
```

Output:

```text
data\raw\file.txt
```

on Windows.

The `/` operator automatically joins path components.

---

# 🧠 Why is Path Joining Useful?

Manually constructing paths using strings can become difficult because different operating systems use different path separators.

For example:

```text
Windows → \
Linux/macOS → /
```

`pathlib` handles the appropriate path representation.

Therefore:

```python
Path("data") / "raw" / "file.txt"
```

is generally safer and cleaner than manually concatenating path strings.

---

# 1️⃣6️⃣.1️⃣1️⃣ Listing Directory Contents with iterdir()

`iterdir()` returns the direct contents of a directory.

Example:

```python
from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    print(item)
```

Here:

```python
Path(".")
```

represents the current directory.

The program prints files and folders directly inside it.

---

# 🔍 Checking Each Item

We can combine `iterdir()` with other methods.

```python
from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    if item.is_file():
        print("File:", item)

    elif item.is_dir():
        print("Directory:", item)
```

This allows us to distinguish files from directories.

---

# 1️⃣6️⃣.1️⃣2️⃣ Finding Files with glob()

`glob()` is useful for finding paths that match a pattern.

For example, to find Python files in the current directory:

```python
from pathlib import Path

folder = Path(".")

for file in folder.glob("*.py"):
    print(file)
```

The pattern:

```text
*.py
```

means:

> Find files whose names end with `.py`.

---

# 🧩 Common glob Patterns

### All Python files

```python
folder.glob("*.py")
```

### All text files

```python
folder.glob("*.txt")
```

### All files beginning with `data`

```python
folder.glob("data*")
```

### Specific filename pattern

```python
folder.glob("practice*.py")
```

---

# 1️⃣6️⃣.1️⃣3️⃣ Recursive Search with rglob()

`glob()` normally searches the specified directory level.

If we want to search recursively through subdirectories, we can use:

```python
rglob()
```

Example:

```python
from pathlib import Path

folder = Path(".")

for file in folder.rglob("*.py"):
    print(file)
```

This searches:

```text
Current Directory
      ↓
Subdirectories
      ↓
Subdirectories inside them
      ↓
...
```

for Python files.

---

# 🆚 glob() vs rglob()

```text
glob()
  ↓
Searches according to the specified directory level/pattern

rglob()
  ↓
Recursive search through subdirectories
```

For example:

```python
folder.glob("*.py")
```

finds matching Python files in the current directory.

Whereas:

```python
folder.rglob("*.py")
```

can find matching Python files inside nested directories as well.

---

# 1️⃣6️⃣.1️⃣4️⃣ File Name with .name

The `.name` property gives the final name of the path.

Example:

```python
from pathlib import Path

path = Path("data/example.txt")

print(path.name)
```

Output:

```text
example.txt
```

---

# 1️⃣6️⃣.1️⃣5️⃣ File Name Without Extension with .stem

The `.stem` property gives the filename without its extension.

```python
from pathlib import Path

path = Path("data/example.txt")

print(path.stem)
```

Output:

```text
example
```

---

# 1️⃣6️⃣.1️⃣6️⃣ File Extension with .suffix

The `.suffix` property gives the file extension.

```python
from pathlib import Path

path = Path("data/example.txt")

print(path.suffix)
```

Output:

```text
.txt
```

For:

```text
model.py
```

we get:

```text
.py
```

---

# 🧠 name vs stem vs suffix

For:

```text
data/model.py
```

we have:

```text
path.name
    ↓
model.py

path.stem
    ↓
model

path.suffix
    ↓
.py
```

These properties are useful when processing files programmatically.

---

# 1️⃣6️⃣.1️⃣7️⃣ Parent Directory with .parent

The `.parent` property gives the immediate parent directory.

Example:

```python
from pathlib import Path

path = Path("data/raw/model.py")

print(path.parent)
```

Output:

```text
data\raw
```

---

# 1️⃣6️⃣.1️⃣8️⃣ All Parent Directories with .parents

`.parents` provides access to all parent paths.

Example:

```python
from pathlib import Path

path = Path("data/raw/model.py")

for parent in path.parents:
    print(parent)
```

It can provide:

```text
data\raw
data
.
```

The exact representation depends on the path and operating system.

---

# 🆚 parent vs parents

```text
.parent
    ↓
Immediate parent

.parents
    ↓
All parent levels
```

---

# 1️⃣6️⃣.1️⃣9️⃣ Reading Text with read_text()

`pathlib` provides a convenient method for reading text files.

Example:

```python
from pathlib import Path

file_path = Path("example.txt")

content = file_path.read_text()

print(content)
```

This reads the complete text content of the file.

---

# 📌 Specifying Encoding

For text files, specifying an encoding can be useful:

```python
from pathlib import Path

file_path = Path("example.txt")

content = file_path.read_text(encoding="utf-8")

print(content)
```

UTF-8 is a common encoding for text files.

---

# 1️⃣6️⃣.2️⃣0️⃣ Writing Text with write_text()

We can write text to a file using:

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.write_text("Hello Python!", encoding="utf-8")
```

This writes:

```text
Hello Python!
```

to the file.

---

# ⚠️ Important: write_text() Overwrites Existing Content

If the file already contains:

```text
Old content
```

and we execute:

```python
file_path.write_text("New content")
```

the old content is replaced.

Therefore:

```text
write_text()
    ↓
Writes/replaces file content
```

---

# 1️⃣6️⃣.2️⃣1️⃣ Appending Text

If we want to add content instead of replacing existing content, we can open the file in append mode.

```python
from pathlib import Path

file_path = Path("example.txt")

with file_path.open("a", encoding="utf-8") as file:
    file.write("New line\n")
```

Here:

```text
"a"
```

means append mode.

---

# 🆚 read_text() and write_text()

```text
read_text()
    ↓
Reads text from file

write_text()
    ↓
Writes/replaces text in file
```

For appending:

```python
file_path.open("a")
```

can be used.

---

# 1️⃣6️⃣.2️⃣2️⃣ Deleting a File with unlink()

A file can be deleted using:

```python
file_path.unlink()
```

Example:

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.unlink()
```

This removes the file.

---

# ⚠️ Safer Deletion

Before deleting, we can check whether the file exists:

```python
from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    file_path.unlink()
```

This avoids trying to delete a path that does not exist.

---

# 1️⃣6️⃣.2️⃣3️⃣ Removing an Empty Directory with rmdir()

An empty directory can be removed using:

```python
from pathlib import Path

folder = Path("data")

folder.rmdir()
```

Important:

> `rmdir()` works only when the directory is empty.

If the directory contains files or subdirectories, the operation will fail.

---

# ⚠️ Removing Non-Empty Directories

For recursively deleting a directory and its contents, Python's `shutil` module provides:

```python
shutil.rmtree()
```

Example:

```python
import shutil

shutil.rmtree("data")
```

This is a powerful and potentially dangerous operation because it can delete an entire directory tree.

Therefore, it should be used carefully.

---

# 1️⃣6️⃣.2️⃣4️⃣ Relative Paths

A relative path describes a location relative to the current working directory.

Example:

```python
from pathlib import Path

path = Path("data/example.txt")
```

This means:

```text
Current Directory
    ↓
data
    ↓
example.txt
```

---

# 1️⃣6️⃣.2️⃣5️⃣ Absolute Paths

An absolute path specifies the complete location.

For example, on Windows:

```python
from pathlib import Path

path = Path(
    r"C:\Users\Sonal\Desktop\Python-Learning\data\example.txt"
)
```

The `r` before the string creates a raw string, which is convenient for Windows paths.

---

# 🆚 Relative vs Absolute Paths

### Relative Path

```text
data/example.txt
```

It depends on the current working directory.

### Absolute Path

```text
C:\Users\Sonal\Desktop\Python-Learning\data\example.txt
```

It specifies the complete location.

---

# 1️⃣6️⃣.2️⃣6️⃣ Checking Whether a Path is Absolute

We can use:

```python
path.is_absolute()
```

Example:

```python
from pathlib import Path

path = Path("data/example.txt")

print(path.is_absolute())
```

A relative path will normally produce:

```text
False
```

An absolute path will produce:

```text
True
```

---

# 1️⃣6️⃣.2️⃣7️⃣ Resolving a Path with resolve()

The `.resolve()` method can convert a path into an absolute, resolved path.

Example:

```python
from pathlib import Path

path = Path("data/example.txt")

print(path.resolve())
```

This can produce an absolute path such as:

```text
C:\Users\Sonal\...\data\example.txt
```

It can also resolve path components such as:

```text
.
..
```

according to the operating system.

---

# 1️⃣6️⃣.2️⃣8️⃣ Path Parts with .parts

The `.parts` property breaks a path into its individual components.

Example:

```python
from pathlib import Path

path = Path("data/raw/model.py")

print(path.parts)
```

Possible output:

```text
('data', 'raw', 'model.py')
```

For an absolute Windows path, the drive component may also appear.

This can be useful when we need to inspect individual parts of a path.

---

# 1️⃣6️⃣.2️⃣9️⃣ Checking Whether a Path is Relative to Another Path

Modern versions of Python provide:

```python
is_relative_to()
```

Example:

```python
from pathlib import Path

path = Path("data/raw/model.py")

print(path.is_relative_to("data"))
```

Output:

```text
True
```

This checks whether the path is located under the specified path.

---

# 1️⃣6️⃣.3️⃣0️⃣ with_name()

`with_name()` creates a new path with a different filename.

Example:

```python
from pathlib import Path

path = Path("data/model.py")

new_path = path.with_name("model_v2.py")

print(new_path)
```

Output:

```text
data\model_v2.py
```

Important:

> `with_name()` creates a new `Path` object. It does not automatically rename the actual file.

---

# 1️⃣6️⃣.3️⃣1️⃣ with_suffix()

`with_suffix()` creates a new path with a different file extension.

Example:

```python
from pathlib import Path

path = Path("data/model.py")

new_path = path.with_suffix(".txt")

print(new_path)
```

Output:

```text
data\model.txt
```

Again:

> `with_suffix()` creates a new path. It does not automatically convert or rename the actual file.

---

# 1️⃣6️⃣.3️⃣2️⃣ pathlib and File Processing

`pathlib` becomes particularly useful when a program needs to process many files.

For example:

```python
from pathlib import Path

folder = Path(".")

for file in folder.glob("*.txt"):
    print(file.name)
```

This can be used as a starting point for tasks such as:

```text
Find all text files
Read each file
Process its contents
Save results
```

---

# 🧠 Common pathlib Operations

| Operation | Method / Property |
|---|---|
| Current directory | `Path.cwd()` |
| Create path | `Path()` |
| Check existence | `.exists()` |
| Check file | `.is_file()` |
| Check directory | `.is_dir()` |
| Create directory | `.mkdir()` |
| Create file | `.touch()` |
| List directory | `.iterdir()` |
| Find matching files | `.glob()` |
| Recursive search | `.rglob()` |
| Filename | `.name` |
| Filename without extension | `.stem` |
| Extension | `.suffix` |
| Parent directory | `.parent` |
| All parents | `.parents` |
| Read text | `.read_text()` |
| Write text | `.write_text()` |
| Delete file | `.unlink()` |
| Remove empty directory | `.rmdir()` |
| Absolute/resolved path | `.resolve()` |
| Path components | `.parts` |
| Change filename | `.with_name()` |
| Change extension | `.with_suffix()` |

---

# 🆚 pathlib and os

Both `pathlib` and `os` can be used for filesystem-related tasks.

However, their common use cases can be thought of as:

```text
pathlib
   ↓
Object-oriented path and file handling

os
   ↓
Operating-system interaction
Environment variables
System-level operations
```

For modern Python code, `pathlib` is often a clean choice when the main task is working with filesystem paths.

The `os` module remains very important and will be covered separately.

---

# 🤖 pathlib in AI Engineering

`pathlib` is highly useful in AI/ML projects because AI projects often work with many files and directories.

Examples include:

```text
Dataset files
CSV files
Images
Model files
Configuration files
Logs
Text documents
Training data
Output files
```

For example, an AI project may have:

```text
AI_Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── src/
│
└── outputs/
```

`pathlib` can be used to navigate and process these directories.

Example:

```python
from pathlib import Path

data_folder = Path("data/raw")

for file in data_folder.glob("*.csv"):
    print(file)
```

This finds CSV files inside the raw-data directory.

---

# 📌 pathlib — Important Points

- `pathlib` is part of Python's standard library.
- `Path` is the main class used for path handling.
- `Path.cwd()` returns the current working directory.
- `.exists()` checks whether a path exists.
- `.is_file()` checks for a file.
- `.is_dir()` checks for a directory.
- `.mkdir()` creates directories.
- `.touch()` creates files.
- `/` can be used to join paths.
- `.iterdir()` lists direct directory contents.
- `.glob()` searches according to a pattern.
- `.rglob()` performs recursive pattern searching.
- `.name`, `.stem`, and `.suffix` provide useful filename information.
- `.parent` and `.parents` provide parent paths.
- `.read_text()` reads text.
- `.write_text()` writes/replaces text.
- `.open("a")` can be used for appending.
- `.unlink()` deletes a file.
- `.rmdir()` removes an empty directory.
- Relative and absolute paths should be understood clearly.
- `.resolve()` can produce a resolved absolute path.
- `.with_name()` and `.with_suffix()` create modified path objects.
- `shutil.rmtree()` can recursively delete non-empty directories, but should be used carefully.

---

# 🧠 pathlib — Quick Revision

```text
Path
 ↓
Represents a filesystem path
 ↓
Check
 ├── exists()
 ├── is_file()
 └── is_dir()
 ↓
Create
 ├── mkdir()
 └── touch()
 ↓
Search
 ├── glob()
 └── rglob()
 ↓
Read / Write
 ├── read_text()
 └── write_text()
 ↓
Path Information
 ├── name
 ├── stem
 ├── suffix
 ├── parent
 └── parts
 ↓
Delete
 ├── unlink()
 └── rmdir()
```

---

# 1️⃣7️⃣ os Module and Environment Variables

## 📌 Definition

> The `os` module is a Python standard library module that provides functions for interacting with the operating system, including directories, environment variables, and system-level information.

The `os` module is useful when Python programs need to communicate with the operating system.

---

# 📖 Why Do We Need os?

A Python program may need to:

- Get the current working directory
- List files and folders
- Access environment variables
- Read operating-system configuration
- Work with paths and directories
- Access system-level information

For example:

```python
import os
```

allows us to access functionality provided by the operating system.

---

# 1️⃣7️⃣.1️⃣ Getting Current Working Directory

We can use:

```python
os.getcwd()
```

Example:

```python
import os

current_directory = os.getcwd()

print(current_directory)
```

Output may look like:

```text
C:\Users\Sonal\Desktop\Python-Learning\CodeWithHarry\CHAPTER 13
```

`getcwd()` means:

```text
Get Current Working Directory
```

---

# 1️⃣7️⃣.2️⃣ Listing Directory Contents

We can use:

```python
os.listdir()
```

Example:

```python
import os

files = os.listdir()

print(files)
```

This returns the names of files and directories in the current working directory.

---

# 1️⃣7️⃣.3️⃣ Listing a Specific Directory

We can provide a path:

```python
import os

files = os.listdir("data")

print(files)
```

This lists the contents of the `data` directory.

---

# 1️⃣7️⃣.4️⃣ Environment Variables

## 📌 Definition

> An **environment variable** is a value stored by the operating system that can provide configuration information to applications without placing that information directly inside source code.

Examples of environment variables include:

```text
API keys
Database URLs
Environment names
Configuration values
System paths
Application settings
```

Instead of writing sensitive information directly inside Python code:

```python
api_key = "my-secret-api-key"
```

we can store it outside the source code.

---

# 🔐 Why Are Environment Variables Important?

Hardcoding sensitive values inside source code can be dangerous.

For example:

```python
API_KEY = "secret-value"
```

If this file is pushed to GitHub, the secret could become exposed.

A better approach is:

```text
Environment Variable
        ↓
Python program reads it
        ↓
Secret/configuration stays outside source code
```

---

# 1️⃣7️⃣.5️⃣ os.environ

Python provides access to environment variables through:

```python
os.environ
```

Example:

```python
import os

print(os.environ)
```

This represents the environment variables available to the current process.

There can be many values, depending on the operating system and environment.

---

# 1️⃣7️⃣.6️⃣ Accessing a Specific Environment Variable

We can access a variable using:

```python
os.environ["VARIABLE_NAME"]
```

For example:

```python
import os

username = os.environ["USERNAME"]

print(username)
```

The exact value depends on the operating system.

---

# ⚠️ KeyError with os.environ

If the requested environment variable does not exist:

```python
os.environ["SOME_VARIABLE"]
```

can raise:

```text
KeyError
```

For example:

```python
import os

value = os.environ["DOES_NOT_EXIST"]
```

If the variable is missing, Python cannot find that key.

---

# 1️⃣7️⃣.7️⃣ os.getenv()

A safer and more flexible approach for optional environment variables is:

```python
os.getenv()
```

Example:

```python
import os

username = os.getenv("USERNAME")

print(username)
```

If the variable exists, its value is returned.

If it does not exist, `None` is returned by default.

---

# 🆚 os.environ vs os.getenv()

| Feature | `os.environ["NAME"]` | `os.getenv("NAME")` |
|---|---|---|
| Access environment variable | Yes | Yes |
| Missing variable | Raises `KeyError` | Returns `None` |
| Can provide default | Not directly in this form | Yes |
| Useful for required values | Yes | Yes |
| Useful for optional values | Less convenient | Yes |

---

# 1️⃣7️⃣.8️⃣ Providing a Default Value with getenv()

We can provide a default value:

```python
import os

environment = os.getenv("APP_ENV", "development")

print(environment)
```

If `APP_ENV` exists, its value is returned.

Otherwise:

```text
development
```

is returned.

---

# 1️⃣7️⃣.9️⃣ Environment Variables and API Keys

Suppose an application requires an API key.

Instead of:

```python
api_key = "secret-api-key"
```

we can use:

```python
import os

api_key = os.getenv("API_KEY")

print(api_key)
```

The actual value can be provided through the environment.

This keeps configuration separate from source code.

---

# ⚠️ Important Security Point

Environment variables are useful for keeping secrets out of source code, but simply using an environment variable does not automatically make a secret completely secure.

For example:

- Do not print secret values unnecessarily.
- Do not commit secret values to GitHub.
- Do not put real secrets directly inside `.env` files that are committed.
- Use appropriate secret-management solutions in production systems.

For local development, `.env` files are commonly used with tools such as `python-dotenv`.

---

# 🤖 Environment Variables in AI Engineering

Environment variables are extremely common in AI Engineering projects.

AI applications may require:

```text
LLM API keys
Database credentials
Cloud credentials
Vector database URLs
Model configuration
Application environment
Service endpoints
```

For example:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
database_url = os.getenv("DATABASE_URL")
environment = os.getenv("APP_ENV", "development")
```

This keeps configuration separate from the application code.

---

# 🧠 os Module — Quick Revision

```text
os
 ↓
Operating System Interaction
 ↓
Common operations
 ├── getcwd()
 ├── listdir()
 ├── environ
 └── getenv()
 ↓
Environment Variables
 ↓
Configuration outside source code
 ↓
Useful for APIs, databases and AI applications
```

---

# 1️⃣8️⃣ `.env` and python-dotenv

## 📌 Definition

> A **`.env` file** is a configuration file used to store environment variables outside the Python source code, while **`python-dotenv`** is a third-party package that loads variables from a `.env` file into the application's environment.

This concept is especially useful when working with:

- API keys
- Database credentials
- Application configuration
- Secret tokens
- Service URLs
- Development settings
- AI/LLM API credentials

---

# 📖 Why Do We Need `.env` Files?

Suppose an application uses an API key.

A beginner might write:

```python
API_KEY = "my-secret-api-key"
```

This creates a problem.

If the source code is uploaded to GitHub, the secret could accidentally become publicly visible.

A better approach is:

```text
.env
   ↓
Stores configuration/secrets
   ↓
Python application
   ↓
Reads values from environment
```

The Python source code does not need to contain the actual secret.

---

# 🔐 Example of the Problem

Avoid writing sensitive information directly in source code:

```python
API_KEY = "real-secret-key"
DATABASE_PASSWORD = "my-password"
```

If this code is committed to Git:

```text
Python Code
     ↓
Git
     ↓
GitHub
     ↓
Secret may become exposed
```

This is a serious security problem.

---

# ✅ Better Approach

Store configuration separately:

```text
.env
```

Example:

```text
API_KEY=demo_api_key_123
APP_USERNAME=sonal
PROJECT_NAME=AI Engineer
```

Then Python can read these values.

---

# 📂 Typical Project Structure

A project using `.env` may look like:

```text
MyProject/
│
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```

The `.env` file contains configuration values.

The Python source code reads them at runtime.

---

# ⚠️ Important `.env` Rule

A `.env` file is usually **not committed to GitHub** when it contains secrets.

Instead, it should normally be added to:

```text
.gitignore
```

For example:

```text
.env
```

This tells Git to ignore the `.env` file.

---

# 1️⃣8️⃣.1️⃣ What is python-dotenv?

## 📌 Definition

> `python-dotenv` is a Python package that loads variables from a `.env` file into the environment so that Python code can access them using environment-variable functions such as `os.getenv()`.

It is a third-party package, so it must be installed separately.

---

# 📦 Installing python-dotenv

Use:

```bash
pip install python-dotenv
```

After installation, we can import it:

```python
from dotenv import load_dotenv
```

---

# 1️⃣8️⃣.2️⃣ Creating a `.env` File

A `.env` file contains key-value pairs.

Example:

```text
API_KEY=demo_api_key_123
APP_USERNAME=sonal
PROJECT_NAME=AI Engineer
```

The basic structure is:

```text
KEY=VALUE
```

Each variable is normally placed on a separate line.

---

# 📌 `.env` Naming Convention

Environment variable names are commonly written in uppercase:

```text
API_KEY
DATABASE_URL
APP_ENV
SECRET_KEY
PROJECT_NAME
```

This is a convention that makes configuration variables easy to recognize.

---

# 1️⃣8️⃣.3️⃣ Loading `.env` Variables

Python code:

```python
from dotenv import load_dotenv

load_dotenv()
```

`load_dotenv()` searches for a `.env` file and loads the variables into the environment.

---

# 1️⃣8️⃣.4️⃣ Reading `.env` Variables

After loading the `.env` file, we can use `os.getenv()`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
username = os.getenv("APP_USERNAME")
project = os.getenv("PROJECT_NAME")

print(api_key)
print(username)
print(project)
```

If `.env` contains:

```text
API_KEY=demo_api_key_123
APP_USERNAME=sonal
PROJECT_NAME=AI Engineer
```

the values can be accessed by Python.

---

# 🔍 Complete Flow

The process is:

```text
.env
 ↓
API_KEY=...
APP_USERNAME=...
PROJECT_NAME=...
 ↓
load_dotenv()
 ↓
Environment Variables
 ↓
os.getenv()
 ↓
Python Application
```

---

# 1️⃣8️⃣.5️⃣ Why `load_dotenv()` is Needed

The `.env` file is not automatically treated as a normal operating-system environment variable source by Python.

We use:

```python
load_dotenv()
```

to load the values from the `.env` file.

Then:

```python
os.getenv("API_KEY")
```

can access the loaded value.

---

# 1️⃣8️⃣.6️⃣ Important Behavior of load_dotenv()

By default:

```python
load_dotenv()
```

does not normally override an environment variable that is already present in the environment.

For example, suppose the operating system already has:

```text
USERNAME=WindowsUser
```

and `.env` contains:

```text
USERNAME=sonal
```

Then:

```python
load_dotenv()
```

may continue using the already-existing environment variable rather than replacing it.

This behavior helps prevent an application's `.env` file from unexpectedly overriding existing environment configuration.

---

# 1️⃣8️⃣.7️⃣ Using override=True

If we explicitly want values from `.env` to override existing environment variables, we can use:

```python
from dotenv import load_dotenv

load_dotenv(override=True)
```

Now values from `.env` can replace existing environment variables with the same name.

---

# ⚠️ Why Generic Environment Variable Names Can Cause Problems

Using common names such as:

```text
USERNAME
PATH
HOME
USER
```

can be problematic because the operating system may already define variables with those names.

For application-specific configuration, it is often clearer to use names such as:

```text
APP_USERNAME
PROJECT_NAME
DATABASE_URL
API_KEY
MODEL_NAME
```

This reduces naming conflicts and makes the purpose of the variable clearer.

---

# 1️⃣8️⃣.8️⃣ `.env` and `os.getenv()` Together

A common pattern is:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

The responsibilities are:

```text
load_dotenv()
       ↓
Loads values from .env

os.getenv()
       ↓
Reads environment variables
```

---

# 1️⃣8️⃣.9️⃣ Providing Default Values

We can still use the default-value feature of `os.getenv()`.

For example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv("APP_ENV", "development")

print(environment)
```

If `APP_ENV` is not available:

```text
development
```

will be returned.

This can be useful for optional configuration.

---

# 1️⃣8️⃣.🔟 Checking Whether a Variable Exists

We can check whether a value was loaded:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key:
    print("API key is available.")
else:
    print("API key is missing.")
```

This is better than printing the actual secret.

---

# 🔐 Never Print Real Secrets Unnecessarily

Avoid:

```python
print(api_key)
```

in production code if `api_key` contains a real secret.

Instead:

```python
if api_key:
    print("API key loaded successfully.")
```

This confirms that the value exists without exposing it.

---

# 1️⃣8️⃣.1️⃣1️⃣ `.env` and GitHub

A common project structure is:

```text
MyProject/
│
├── .env
├── .env.example
├── .gitignore
├── main.py
└── requirements.txt
```

The roles are:

```text
.env
   ↓
Actual local configuration/secrets

.env.example
   ↓
Template containing placeholder values

.gitignore
   ↓
Prevents .env from being committed

requirements.txt
   ↓
Project dependencies
```

---

# 1️⃣8️⃣.1️⃣2️⃣ What is `.env.example`?

## 📌 Definition

> `.env.example` is a template file that documents which environment variables a project requires without containing the real secret values.

For example:

```text
API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
APP_ENV=development
```

This file can generally be committed to GitHub because it does not contain real secrets.

---

# 🆚 `.env` vs `.env.example`

| File | Purpose | Usually committed? |
|---|---|---|
| `.env` | Actual local configuration/secrets | Usually no |
| `.env.example` | Placeholder/template configuration | Usually yes |

---

# 1️⃣8️⃣.1️⃣3️⃣ `.gitignore`

A `.gitignore` file tells Git which files and folders should not be tracked.

For example:

```text
.env
```

can be added to `.gitignore`.

A common Python project `.gitignore` may also contain:

```text
.env
.venv/
__pycache__/
*.pyc
```

This prevents unnecessary or sensitive files from being committed.

---

# ⚠️ `.gitignore` Is Not a Security Mechanism

It is important to understand:

> `.gitignore` prevents Git from tracking a file, but it does not magically remove a secret that has already been committed.

For example, if a real API key was accidentally committed:

```text
Secret
  ↓
Git commit
  ↓
GitHub
```

Simply adding `.env` to `.gitignore` later does not make the previously exposed secret safe.

In such a situation, the secret should be **revoked or rotated** and the repository history may also need appropriate cleanup.

---

# 1️⃣8️⃣.1️⃣4️⃣ Environment Variables vs `.env`

There is an important distinction.

### Environment Variable

A value provided by the operating system or execution environment.

Example:

```text
API_KEY=some-value
```

### `.env` File

A convenient local-development file containing environment-variable-style values.

Example:

```text
API_KEY=some-value
```

### `python-dotenv`

A tool that loads values from `.env` into the application's environment.

Therefore:

```text
Operating System
       ↓
Environment Variables

OR

.env
       ↓
python-dotenv
       ↓
Environment Variables
```

---

# 1️⃣8️⃣.1️⃣5️⃣ `.env` Is Not Python Syntax

A `.env` file is not a Python file.

Do not write:

```text
API_KEY = "secret"
```

as if it were Python code.

A typical `.env` format is:

```text
API_KEY=secret
APP_ENV=development
MODEL_NAME=my-model
```

The exact parsing rules supported by `python-dotenv` allow some additional syntax, but the simple `KEY=VALUE` format is the most important pattern to remember.

---

# 1️⃣8️⃣.1️⃣6️⃣ Spaces and Variable Names

A clean convention is:

```text
API_KEY=value
DATABASE_URL=value
APP_ENV=development
```

Use descriptive names.

Prefer:

```text
APP_USERNAME=sonal
```

over a generic name such as:

```text
USERNAME=sonal
```

when there is a possibility of collision with an existing operating-system variable.

---

# 1️⃣8️⃣.1️⃣7️⃣ Using `.env` for AI APIs

Suppose an AI application uses an API service.

Instead of:

```python
api_key = "real-secret-key"
```

we can store:

```text
API_KEY=real-secret-key
```

inside `.env`.

Then:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

The application can use:

```python
api_key
```

without putting the actual secret directly into the source code.

---

# 1️⃣8️⃣.1️⃣8️⃣ Using `.env` for Database Configuration

An application may need:

```text
DATABASE_URL
DATABASE_USER
DATABASE_PASSWORD
```

These can be stored as configuration values:

```text
DATABASE_URL=...
DATABASE_USER=...
DATABASE_PASSWORD=...
```

Then Python can read them:

```python
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
```

The source code does not need to contain the actual credentials.

---

# 1️⃣8️⃣.1️⃣9️⃣ Using `.env` for Application Configuration

Not every environment variable has to be secret.

`.env` can also store normal configuration.

For example:

```text
APP_ENV=development
DEBUG=True
MODEL_NAME=my-model
PORT=8000
```

This allows configuration to change without modifying the Python source code.

---

# 1️⃣8️⃣.2️⃣0️⃣ Development vs Production

A `.env` file is especially convenient for local development.

In production systems, secrets are often provided using dedicated mechanisms such as:

```text
Cloud secret managers
Container environment variables
Deployment platform secrets
CI/CD secret stores
```

Therefore:

> `.env` is a convenient development technique, not a complete production secret-management system.

---

# 🤖 `.env` and python-dotenv in AI Engineering

This concept is extremely important for AI Engineers.

Modern AI applications may use:

```text
LLM API keys
Embedding API keys
Vector database credentials
Database URLs
Cloud credentials
Model configuration
Application environment
Service URLs
```

For example:

```text
LLM_API_KEY=...
VECTOR_DB_URL=...
DATABASE_URL=...
MODEL_NAME=...
APP_ENV=development
```

Python can load these values:

```python
from dotenv import load_dotenv
import os

load_dotenv()

llm_api_key = os.getenv("LLM_API_KEY")
vector_db_url = os.getenv("VECTOR_DB_URL")
model_name = os.getenv("MODEL_NAME")
```

This pattern is extremely common in:

- AI APIs
- LLM applications
- RAG systems
- FastAPI applications
- Database-backed AI applications
- Docker-based applications
- Cloud deployments

---

# ⚠️ Important Security Rules

When working with `.env` files:

### 1. Never hardcode real secrets unnecessarily

Avoid:

```python
API_KEY = "real-secret"
```

### 2. Do not commit `.env` containing real secrets

Add:

```text
.env
```

to `.gitignore`.

### 3. Use `.env.example`

Provide placeholders:

```text
API_KEY=your_api_key_here
```

### 4. Do not print secrets

Avoid:

```python
print(api_key)
```

### 5. Rotate exposed secrets

If a real secret is accidentally exposed, revoke or rotate it.

### 6. Use production secret-management tools

For deployed applications, use the secret-management capabilities provided by the hosting or infrastructure platform when appropriate.

---

# 🧠 `.env` + python-dotenv — Complete Flow

```text
.env
 │
 ├── API_KEY=...
 ├── DATABASE_URL=...
 └── MODEL_NAME=...
 │
 ↓
load_dotenv()
 │
 ↓
Environment Variables
 │
 ↓
os.getenv()
 │
 ↓
Python Application
```

---

# 🧠 `.env` vs os.getenv() vs python-dotenv

```text
.env
 ↓
Stores configuration values

python-dotenv
 ↓
Loads .env values

os.getenv()
 ↓
Reads environment variables

Python Application
 ↓
Uses configuration
```

---

# ⚠️ Important Points About `.env` and python-dotenv`

- `.env` stores environment-variable-style configuration.
- `python-dotenv` is a third-party package.
- Install it using:

```bash
pip install python-dotenv
```

- Load values using:

```python
from dotenv import load_dotenv

load_dotenv()
```

- Read values using:

```python
import os

os.getenv("VARIABLE_NAME")
```

- `load_dotenv()` normally does not override already-existing environment variables unless `override=True` is specified.
- Application-specific environment variable names are preferable to generic names.
- `.env` should normally not be committed when it contains secrets.
- `.env.example` can provide placeholders.
- `.gitignore` can be used to prevent `.env` from being tracked.
- `.gitignore` cannot protect a secret that has already been exposed.
- Real production applications may use dedicated secret-management systems.

---

# 🧠 `.env` — Quick Revision

```text
.env
 ↓
Stores configuration/secrets locally
 ↓
python-dotenv
 ↓
load_dotenv()
 ↓
Loads variables
 ↓
os.getenv()
 ↓
Reads variables
 ↓
Python Application
```

---

# 1️⃣9️⃣ Modules and Packages

## 📌 Definition

> A **module** is a Python file containing reusable code, while a **package** is a directory used to organize related Python modules into a structured collection.

Modules and packages are fundamental for organizing larger Python applications.

---

# 📖 Why Do We Need Modules?

Imagine putting an entire application into one Python file:

```text
main.py
│
├── 1000 lines
├── 2000 lines
├── 3000 lines
└── ...
```

As the project grows, maintaining one huge file becomes difficult.

Instead, we can divide functionality into separate modules.

For example:

```text
main.py
math_utils.py
file_utils.py
api_utils.py
```

Each file can contain related functionality.

---

# 1️⃣9️⃣.1️⃣ Module

A module is simply a Python file:

```text
filename.py
```

For example:

```text
math_utils.py
```

can contain:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

Another Python file can import these functions.

---

# 1️⃣9️⃣.2️⃣ import

We can import an entire module:

```python
import math_utils
```

Then access its functions using:

```python
math_utils.add(10, 20)
```

This makes the module name explicit.

---

# 1️⃣9️⃣.3️⃣ from ... import ...

We can import specific functionality:

```python
from math_utils import add

print(add(10, 20))
```

Now `add()` can be used directly.

---

# 1️⃣9️⃣.4️⃣ Importing Multiple Items

We can import multiple functions:

```python
from math_utils import add, subtract

print(add(10, 20))
print(subtract(20, 10))
```

---

# 1️⃣9️⃣.5️⃣ import ... as

We can create an alias:

```python
import math_utils as mu

print(mu.add(10, 20))
```

Here:

```text
math_utils
    ↓
mu
```

is the alias.

Aliases can make long module names more convenient.

---

# 1️⃣9️⃣.6️⃣ Standard Library Modules

Python provides many modules as part of its standard library.

Examples:

```python
import math
import random
import os
```

and:

```python
from pathlib import Path
```

These modules do not normally require installation through `pip`.

Examples include:

```text
math
random
os
pathlib
json
datetime
re
collections
```

---

# 1️⃣9️⃣.7️⃣ Third-Party Packages

Some Python libraries are not included in the standard library.

They are installed using tools such as `pip`.

Examples include:

```text
requests
numpy
pandas
matplotlib
scikit-learn
torch
```

For example:

```bash
pip install requests
```

Then:

```python
import requests
```

can be used in the Python program.

---

# 1️⃣9️⃣.8️⃣ Package

A package is a directory used to organize related Python modules.

Conceptually:

```text
utils/
│
├── math_utils.py
├── file_utils.py
└── text_utils.py
```

The modules are grouped according to related functionality.

---

# 1️⃣9️⃣.9️⃣ Package Import

Suppose:

```text
utils/
│
├── math_utils.py
└── file_utils.py
```

and `math_utils.py` contains:

```python
def add(a, b):
    return a + b
```

Another file can import it using:

```python
from utils.math_utils import add

print(add(10, 20))
```

This gives us a structured way to organize reusable code.

---

# 🧠 Module vs Package

| Feature | Module | Package |
|---|---|---|
| Basic unit | Python file | Directory of related modules |
| Example | `math_utils.py` | `utils/` |
| Purpose | Reusable code | Organize related modules |
| Extension | `.py` | Directory structure |

Easy way to remember:

```text
Module
 ↓
One Python file

Package
 ↓
Collection/organization of related modules
```

---

# 1️⃣9️⃣.🔟 Module vs Package vs Library

These terms are related but not identical.

### Module

A Python file containing reusable code.

```text
math_utils.py
```

### Package

A structured collection of related modules.

```text
utils/
```

### Library

A broader term for reusable software functionality provided for developers.

For example:

```text
NumPy
Pandas
Requests
Scikit-learn
PyTorch
```

A library may contain many modules and packages.

---

# 1️⃣9️⃣.1️⃣1️⃣ Why Modules and Packages Are Important

They help us:

- Organize code
- Reuse functionality
- Reduce duplication
- Improve readability
- Make large projects manageable
- Separate responsibilities
- Make testing easier
- Make maintenance easier

---

# 🤖 Modules and Packages in AI Engineering

AI projects can become large very quickly.

A project might eventually contain:

```text
AI_Project/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── preprocessing.py
│
├── models/
│   └── model.py
│
├── utils/
│   └── helpers.py
│
├── api/
│   └── routes.py
│
└── services/
    └── prediction.py
```

Each part has a specific responsibility.

For example:

```text
data/
   ↓
Data processing

models/
   ↓
Machine-learning/deep-learning models

api/
   ↓
API endpoints

services/
   ↓
Application logic

utils/
   ↓
Reusable helper functions
```

This type of organization becomes increasingly important as AI projects grow.

---

# 📌 Modules and Packages — Important Points

- A module is a Python file containing reusable code.
- Modules can contain functions, classes, variables, and other definitions.
- Modules can be imported using `import`.
- Specific functionality can be imported using `from ... import ...`.
- Aliases can be created using `as`.
- Packages organize related modules.
- Standard-library modules come with Python.
- Third-party packages are commonly installed using `pip`.
- Modular code improves organization and reusability.
- Large AI projects commonly use multiple modules and packages.

---

# 🧠 Modules and Packages — Quick Revision

```text
Module
   ↓
Python file
   ↓
Reusable code

Package
   ↓
Organized collection of modules
   ↓
Larger project structure

import
   ↓
Use reusable functionality
```

---

# 📚 Chapter 13 — Concepts Completed So Far

At this stage, the major concepts covered are:

```text
1. Virtual Environment
2. pip
3. requirements.txt
4. pip freeze
5. Lambda Functions
6. map()
7. filter()
8. reduce()
9. map() + filter() + lambda
10. join()
11. String Formatting
12. *args and **kwargs
13. zip()
14. sorted() + key=
15. any() and all()
16. pathlib
17. os & Environment Variables
18. .env & python-dotenv
19. Modules & Packages
```

# 🛠️ Practical Concepts

Chapter 13 introduced several Python features and utilities that are commonly used when building real-world applications.

The following practical concepts show how these features can work together in actual Python projects.

---

# 1️⃣ Working with Python Packages

Third-party packages are commonly installed using `pip`.

For example:

```bash
pip install requests
```

After installation:

```python
import requests
```

The package can then be used inside the application.

A project's dependencies can be stored in:

```text
requirements.txt
```

For example:

```text
requests==2.34.2
numpy==2.5.3
```

Another developer can install the same dependencies using:

```bash
pip install -r requirements.txt
```

This makes sharing and reproducing Python projects easier.

---

# 2️⃣ Using `lambda` with `map()`

`lambda` and `map()` are often used together for simple transformations.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x * x, numbers)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

Flow:

```text
numbers
   ↓
map()
   ↓
lambda transformation
   ↓
new values
```

---

# 3️⃣ Using `filter()` for Data Selection

`filter()` is useful when we need only the elements satisfying a condition.

Example:

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))
```

Output:

```text
[10, 20, 30]
```

This type of filtering is commonly needed when processing datasets or collections of objects.

---

# 4️⃣ Combining `filter()` and `map()`

Multiple operations can be combined.

Example:

```python
numbers = [5, 10, 15, 20, 25, 30]

result = filter(lambda x: x > 10, numbers)
result = map(lambda x: x * 2, result)

print(list(result))
```

Output:

```text
[30, 40, 50, 60]
```

The flow is:

```text
Original Data
     ↓
filter()
     ↓
Selected Data
     ↓
map()
     ↓
Transformed Data
```

This pattern is useful when processing data in multiple steps.

---

# 5️⃣ Using `zip()` to Combine Related Data

Suppose we have names and marks:

```python
names = ["Sonal", "Aman", "Rahul"]
marks = [85, 90, 78]
```

We can combine them:

```python
students = zip(names, marks)

print(list(students))
```

Output:

```text
[('Sonal', 85), ('Aman', 90), ('Rahul', 78)]
```

We can also create a dictionary:

```python
students = dict(zip(names, marks))

print(students)
```

Output:

```text
{'Sonal': 85, 'Aman': 90, 'Rahul': 78}
```

---

# 6️⃣ Sorting Data Using `sorted()` and `key=`

Suppose we have student records:

```python
students = [
    ("Sonal", 85),
    ("Aman", 92),
    ("Rahul", 78)
]
```

We can sort them according to marks:

```python
sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)
```

Output:

```text
[('Rahul', 78), ('Sonal', 85), ('Aman', 92)]
```

For descending order:

```python
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

---

# 7️⃣ Using `any()` and `all()` for Validation

Suppose we want to check whether any student scored 90 or more:

```python
marks = [75, 82, 91, 68, 45]

result = any(mark >= 90 for mark in marks)

print(result)
```

Output:

```text
True
```

To check whether every student passed:

```python
result = all(mark >= 40 for mark in marks)

print(result)
```

Output:

```text
True
```

These functions are useful for simple validation and condition checking.

---

# 8️⃣ Using `pathlib` for File Handling

Instead of manually constructing file paths as strings, we can use `Path`.

Example:

```python
from pathlib import Path

file_path = Path("data") / "students.txt"

print(file_path)
```

Output:

```text
data/students.txt
```

Check whether the file exists:

```python
if file_path.exists():
    print("File exists")
else:
    print("File does not exist")
```

This provides a cleaner and more platform-friendly way of working with paths.

---

# 9️⃣ Reading and Writing Text with `pathlib`

A text file can be read using:

```python
from pathlib import Path

file_path = Path("data.txt")

content = file_path.read_text()

print(content)
```

A file can be written using:

```python
file_path.write_text("Hello Python")
```

For more advanced file operations, the `open()` method can also be used:

```python
with file_path.open("a") as file:
    file.write("\nNew line")
```

---

# 🔟 Using Environment Variables for Configuration

Instead of hardcoding configuration values:

```python
API_KEY = "secret-key"
```

use environment variables:

```python
import os

api_key = os.getenv("API_KEY")
```

For local development, a `.env` file can be loaded:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

This keeps configuration separate from the application logic.

---

# 1️⃣1️⃣ Using `*args` for Flexible Functions

Suppose a function should accept any number of values:

```python
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Now we can provide different numbers of arguments:

```python
print(calculate_total(10, 20))
print(calculate_total(10, 20, 30, 40))
```

This makes the function flexible.

---

# 1️⃣2️⃣ Using `**kwargs` for Flexible Configuration

`**kwargs` is useful when a function may receive different named configuration values.

Example:

```python
def show_config(**config):
    for key, value in config.items():
        print(key, ":", value)


show_config(
    model="AI Model",
    temperature=0.7,
    max_tokens=500
)
```

Output:

```text
model : AI Model
temperature : 0.7
max_tokens : 500
```

This pattern is common in configurable applications.

---

# 1️⃣3️⃣ Using Modules to Organize Code

Instead of keeping everything inside `main.py`, functionality can be separated.

Example:

```text
project/
│
├── main.py
├── calculator.py
└── utils.py
```

`calculator.py`:

```python
def add(a, b):
    return a + b
```

`main.py`:

```python
from calculator import add

result = add(10, 20)

print(result)
```

This keeps the project organized.

---

# 1️⃣4️⃣ Practical Dependency Workflow

A common Python project workflow is:

```text
Create Project
      ↓
Create Virtual Environment
      ↓
Install Packages using pip
      ↓
Develop Application
      ↓
Save Dependencies
      ↓
requirements.txt
      ↓
Share Project
```

For example:

```bash
python -m venv .venv
```

Activate the environment and install packages:

```bash
pip install requests numpy
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Another developer can recreate the dependencies using:

```bash
pip install -r requirements.txt
```

---

# 1️⃣5️⃣ Practical Configuration Workflow

For an application that requires configuration:

```text
.env
   ↓
Environment Variables
   ↓
python-dotenv
   ↓
load_dotenv()
   ↓
os.getenv()
   ↓
Application
```

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

model_name = os.getenv("MODEL_NAME")
api_key = os.getenv("API_KEY")

print("Model:", model_name)

if api_key:
    print("API key loaded successfully.")
```

The actual API key does not need to be printed.

---

# 1️⃣6️⃣ Practical Data Processing Workflow

Several Chapter 13 concepts can work together:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

filtered = filter(lambda x: x >= 20, numbers)
transformed = map(lambda x: x * 2, filtered)

result = list(transformed)

print(result)
```

Output:

```text
[40, 50, 60, 70, 80]
```

Here:

```text
filter()
   ↓
Select data

map()
   ↓
Transform data

list()
   ↓
Convert result into a list
```

This type of processing pattern is useful when working with collections and datasets.

---

# 1️⃣7️⃣ Practical File Organization Workflow

`pathlib` and modules can work together in a real project.

For example:

```text
AI_Project/
│
├── main.py
├── requirements.txt
├── .env
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── utils/
│   └── file_utils.py
│
└── config/
    └── settings.py
```

This separates:

```text
Configuration
Data
Models
Utilities
Application Logic
Dependencies
```

As projects become larger, this type of organization becomes increasingly important.

---

# 1️⃣8️⃣ Practical Chapter 13 Workflow

The major concepts from this chapter can be connected like this:

```text
Python Project
      │
      ├── Virtual Environment
      │
      ├── pip
      │
      ├── requirements.txt
      │
      ├── Modules & Packages
      │
      ├── Configuration
      │      └── .env
      │
      ├── File Handling
      │      └── pathlib
      │
      └── Data Processing
             ├── map()
             ├── filter()
             ├── reduce()
             ├── zip()
             ├── sorted()
             ├── any()
             └── all()
```

---

# 📚 Chapter Summary

Chapter 13 introduced several practical Python tools and utilities that are useful for writing cleaner, reusable, and more maintainable programs.

## 🔹 Package Management

Learned:

```text
pip
requirements.txt
pip freeze
```

These tools help install, manage, record, and reproduce project dependencies.

---

## 🔹 Functional Programming Utilities

Learned:

```text
lambda
map()
filter()
reduce()
```

These allow us to write concise functions and process collections efficiently.

---

## 🔹 Collection Utilities

Learned:

```text
zip()
sorted()
any()
all()
```

These built-in functions are useful for combining, sorting, validating, and processing data.

---

## 🔹 String Utilities

Learned:

```text
join()
String Formatting
f-strings
.format()
```

These are useful when constructing readable and formatted output.

---

## 🔹 Flexible Function Arguments

Learned:

```text
*args
**kwargs
```

They allow functions to accept flexible numbers of positional and keyword arguments.

---

## 🔹 File and Path Management

Learned:

```text
pathlib
```

Important operations include:

```text
Path()
exists()
is_file()
is_dir()
iterdir()
glob()
rglob()
read_text()
write_text()
unlink()
resolve()
```

---

## 🔹 Operating System Interaction

Learned:

```text
os
os.getcwd()
os.listdir()
os.environ
os.getenv()
```

These provide interaction with the operating system and environment variables.

---

## 🔹 Environment Configuration

Learned:

```text
.env
python-dotenv
load_dotenv()
```

These are useful for keeping configuration and secrets outside the main source code.

---

## 🔹 Code Organization

Learned:

```text
Modules
Packages
Imports
Aliases
```

These concepts help organize larger Python applications.

---

# 🧠 Chapter 13 — Quick Revision

```text
Virtual Environment
        ↓
Isolated Python Environment

pip
        ↓
Package Management

requirements.txt
        ↓
Project Dependencies

pip freeze
        ↓
Installed Packages + Versions

lambda
        ↓
Small Anonymous Function

map()
        ↓
Transform Every Element

filter()
        ↓
Select Matching Elements

reduce()
        ↓
Reduce Elements to One Result

join()
        ↓
Combine Strings

String Formatting
        ↓
Create Formatted Output

*args
        ↓
Variable Positional Arguments

**kwargs
        ↓
Variable Keyword Arguments

zip()
        ↓
Combine Iterables

sorted()
        ↓
Sort Data

any()
        ↓
At Least One True

all()
        ↓
Every Element True

pathlib
        ↓
Modern Path/File Handling

os
        ↓
Operating System Interaction

.env
        ↓
Configuration / Secrets

python-dotenv
        ↓
Load .env Variables

Modules
        ↓
Reusable Python Files

Packages
        ↓
Organized Modules
```

---

# 🤖 AI Engineer Relevance

Chapter 13 is highly useful for moving from basic Python programming toward real-world AI development.

## 🔹 1. Package Management

AI development depends heavily on external libraries such as:

```text
NumPy
Pandas
Matplotlib
Scikit-learn
PyTorch
Transformers
FastAPI
Requests
```

`pip` and `requirements.txt` are therefore essential skills.

---

## 🔹 2. Environment Management

AI projects often require many dependencies.

For example:

```text
Project A
 ├── Python version
 ├── NumPy version
 └── PyTorch version

Project B
 ├── Python version
 ├── NumPy version
 └── Different PyTorch version
```

Virtual environments help isolate these dependencies.

---

## 🔹 3. Data Processing

Functions such as:

```text
map()
filter()
zip()
sorted()
any()
all()
```

are useful for processing and validating Python collections.

Later, similar ideas will appear when working with:

```text
NumPy
Pandas
Machine Learning datasets
```

---

## 🔹 4. File and Dataset Management

`pathlib` is useful when working with:

```text
Datasets
CSV files
JSON files
Images
Model files
Logs
Project directories
```

AI projects frequently involve large numbers of files and folders.

---

## 🔹 5. API Keys and Configuration

AI applications commonly communicate with external services.

For example:

```text
LLM APIs
Embedding APIs
Cloud Services
Vector Databases
Databases
```

Environment variables and `.env` files are commonly used for local development configuration.

---

## 🔹 6. Modules and Packages

As AI projects become larger, code needs to be divided into logical components:

```text
Data Processing
       ↓
Model
       ↓
Prediction
       ↓
API
       ↓
Application
```

Modules and packages allow these components to be organized properly.

---

## 🔹 7. Real-World AI Project Structure

A future AI project may look like:

```text
AI_Project/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│
├── models/
│
├── preprocessing/
│
├── services/
│
├── api/
│
└── utils/
```

The concepts learned in Chapter 13 provide several of the basic Python skills needed to understand this structure.

---

# 🎯 Chapter 13 — Final Takeaway

Chapter 13 moves Python learning from individual language features toward **real project development**.

The important idea is not only learning each function separately, but understanding how these tools work together:

```text
Python Code
     ↓
Organized into Modules
     ↓
Dependencies managed using pip
     ↓
Dependencies recorded in requirements.txt
     ↓
Configuration stored using Environment Variables
     ↓
Files managed using pathlib
     ↓
Data processed using Python utilities
     ↓
Complete Python Project
```

These concepts form an important bridge between **Python fundamentals** and the practical Python environment used in AI/ML development.

---

# 📚 Course Information

**Course:** CodeWithHarry — Python Programming  
**Chapter:** 13  
**Topic:** Python Tools & Advanced Utilities  
**Language:** Python

---

# 👨‍💻 Author

**Sonal Rai**