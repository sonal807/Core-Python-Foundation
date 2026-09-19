# ============================================================
# MODULES & PACKAGES — QUICK NOTES
# ============================================================

# 📝 Definition:
# A module is a Python file containing reusable code,
# while a package is a collection of related Python modules
# organized in a directory.
#
# Simple:
# Module  → Usually one .py file
# Package → Collection of related modules


# ============================================================
# 1. MODULE
# ============================================================

# A module is a Python (.py) file containing reusable code
# such as functions, classes, and variables.
#
# Example:
#
# math_utils.py
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# math_utils.py is a module.


# ============================================================
# 2. import
# ============================================================

# import is used to make a module available in another
# Python file.
#
# Example:
#
# import math_utils
#
# print(math_utils.add(10, 20))
#
# Syntax:
#
# import module_name
# module_name.function_name()


# ============================================================
# 3. from ... import ...
# ============================================================

# Used to import specific functions, classes or variables
# from a module.
#
# Example:
#
# from math_utils import add
#
# print(add(10, 20))
#
# Multiple imports:
#
# from math_utils import add, multiply


# ============================================================
# 4. import ... as ...
# ============================================================

# 'as' creates an alias (short name) for a module.
#
# Example:
#
# import math_utils as mu
#
# print(mu.add(10, 20))
#
# math_utils → mu


# ============================================================
# 5. BUILT-IN / STANDARD LIBRARY MODULES
# ============================================================

# Python provides many modules in its Standard Library.
# They can generally be used without installing them separately.
#
# Examples:
#
# import math
# import random
# import os
# import pathlib
#
# Example:
#
# import math
# print(math.sqrt(25))


# ============================================================
# 6. THIRD-PARTY PACKAGES
# ============================================================

# Third-party packages are created by the Python community
# and are usually installed using pip.
#
# Example:
#
# pip install requests
#
# Then:
#
# import requests
#
# Other examples used in AI/ML:
#
# numpy
# pandas
# matplotlib
# scikit-learn
# torch
#
# These packages are generally installed separately.


# ============================================================
# 7. PACKAGE
# ============================================================

# A package is a directory that organizes related Python
# modules together.
#
# Example structure:
#
# my_project/
# │
# ├── main.py
# │
# └── utils/
#     ├── math_utils.py
#     ├── file_utils.py
#     └── text_utils.py
#
# math_utils.py   → Module
# file_utils.py   → Module
# text_utils.py   → Module
# utils/          → Package


# ============================================================
# 8. IMPORTING FROM A PACKAGE
# ============================================================

# A module inside a package can be imported using:
#
# from package.module import function
#
# Example:
#
# from utils.math_utils import add
#
# print(add(10, 20))
#
# Flow:
#
# utils
#   ↓
# math_utils
#   ↓
# add()


# ============================================================
# 9. MODULE vs PACKAGE vs LIBRARY
# ============================================================

# Module:
# → Usually a single .py file containing reusable code.
#
# Package:
# → A collection of related modules organized in a directory.
#
# Library:
# → A broader collection of reusable code that may contain
#   modules and/or packages.
#
# Simple:
#
# Module  → One reusable Python file
# Package → Collection of related modules
# Library → Broader reusable code collection


# ============================================================
# 10. WHY MODULES & PACKAGES ARE IMPORTANT
# ============================================================

# They help make code:
#
# → Organized
# → Reusable
# → Maintainable
# → Easier to debug
# → Easier to scale
#
# Instead of putting the entire project into one large
# Python file, code can be divided into logical modules
# and packages.


# ============================================================
# 11. AI ENGINEER RELEVANCE
# ============================================================

# Real AI/ML projects are usually divided into multiple
# modules and packages.
#
# Example:
#
# AI_Project/
# │
# ├── main.py
# ├── config.py
# │
# ├── data/
# │
# ├── models/
# │
# ├── utils/
# │   ├── preprocessing.py
# │   └── helpers.py
# │
# └── api/
#     └── routes.py
#
# This keeps different responsibilities separated and makes
# the project easier to maintain and expand.


# ============================================================
# 🔥 QUICK REVISION
# ============================================================

# import module
# → Import an entire module
#
# from module import function
# → Import a specific function/class/variable
#
# import module as alias
# → Give a module a shorter name
#
# Module
# → Reusable .py file
#
# Package
# → Collection of related modules
#
# pip install package
# → Install third-party package
#
# ============================================================
# NOTE:
# Modules and Packages are fundamental for organizing
# real-world Python and AI/ML projects.
# ============================================================