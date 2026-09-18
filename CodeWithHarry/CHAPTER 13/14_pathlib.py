#pathlib: pathlib is a Python standard library module used to work with files and directories using 
#an object-oriented and platform-independent approach.

#Importing path
# from pathlib import Path

#To get current folder path
from pathlib import Path

current_path = Path.cwd()  #it will return current working directory

print(current_path) 

#Creating file path
from pathlib import Path

file_path = Path("data.txt") #Now it only represent path, with it file doesn't create automatically
print(file_path)

#For checking that file exists or not
from pathlib import Path

file_path = Path("data.txt")

print(file_path.exists())

#for checking that it is file: .is_file()
#for checking it is directory: .is_dir()

# ============================================================
# pathlib — Working with Files, Folders & Paths
# ============================================================

# 📝 Definition:
# pathlib is a Python standard library module used to work with
# files, folders and paths in a clean, object-oriented way.
#
# Import:
#
# from pathlib import Path


# ============================================================
# 1. Path() and Path.cwd()
# ============================================================

# Path() is used to create a Path object.
#
# Example:
#
# from pathlib import Path
#
# file_path = Path("data/students.csv")
# print(file_path)
#
# Output:
# data/students.csv
#
# Path() only represents the path.
# It does NOT create the actual file or folder.


# Path.cwd() returns the Current Working Directory.
#
# Example:
#
# current_path = Path.cwd()
# print(current_path)
#
# It tells us the directory from which the Python program
# is currently running.


# ============================================================
# 2. exists(), is_file() and is_dir()
# ============================================================

# exists() checks whether a path exists or not.
#
# Example:
#
# path = Path("data.txt")
# print(path.exists())
#
# True  → Path exists
# False → Path does not exist


# is_file() checks whether the path represents a file.
#
# Example:
#
# path = Path("data.txt")
# print(path.is_file())
#
# True → It is a file
# False → It is not a file / doesn't exist


# is_dir() checks whether the path represents a directory.
#
# Example:
#
# folder = Path("data")
# print(folder.is_dir())
#
# True → It is a directory
# False → It is not a directory / doesn't exist


# ============================================================
# 3. mkdir() and touch()
# ============================================================

# mkdir() is used to create a directory/folder.
#
# Example:
#
# folder = Path("data")
# folder.mkdir()
#
# If the folder already exists, an error can occur.
#
# To avoid that:
#
# folder.mkdir(exist_ok=True)
#
# exist_ok=True means:
# If the folder already exists, don't raise an error.


# touch() is used to create an empty file.
#
# Example:
#
# file_path = Path("data.txt")
# file_path.touch()
#
# It creates data.txt if it doesn't exist.
# It does not delete the existing file contents.


# ============================================================
# 4. Path Joining using /
# ============================================================

# The / operator is used to combine Path objects and path parts.
#
# Example:
#
# folder = Path("data")
# file_path = folder / "students.csv"
#
# print(file_path)
#
# Output:
# data/students.csv
#
# NOTE:
# Here / is NOT mathematical division.
# With Path objects, / means "join these paths".
#
# This is better than manually writing:
#
# "data/" + "students.csv"


# ============================================================
# 5. parents=True
# ============================================================

# parents=True allows pathlib to create missing parent
# directories while using mkdir().
#
# Example:
#
# folder = Path("data/students/marks")
# folder.mkdir(parents=True, exist_ok=True)
#
# This can create:
#
# data/
# └── students/
#     └── marks/
#
# parents=True:
# Creates missing parent directories.
#
# exist_ok=True:
# Does not raise an error if the directory already exists.


# ============================================================
# 6. iterdir()
# ============================================================

# iterdir() returns the files and directories directly inside
# a directory.
#
# Example:
#
# folder = Path(".")
#
# for item in folder.iterdir():
#     print(item)
#
# Path(".") means the current directory.
#
# iterdir() does NOT search recursively.
# It only checks the direct contents of the directory.


# Only files:
#
# for item in folder.iterdir():
#     if item.is_file():
#         print(item)
#
#
# Only directories:
#
# for item in folder.iterdir():
#     if item.is_dir():
#         print(item)


# ============================================================
# 7. glob() and rglob()
# ============================================================

# glob() searches for paths matching a particular pattern
# in the current directory.
#
# Example:
#
# folder = Path(".")
#
# for file in folder.glob("*.py"):
#     print(file)
#
# "*.py" means:
# *  → any filename
# .py → Python file extension
#
# So this finds Python files in the current directory.


# Other examples:
#
# folder.glob("*.txt")   → Find .txt files
# folder.glob("*.csv")   → Find .csv files
# folder.glob("*.json")  → Find .json files


# rglob() performs a recursive search.
# It searches the current directory AND its subdirectories.
#
# Example:
#
# folder = Path("Project")
#
# for file in folder.rglob("*.csv"):
#     print(file)
#
# This finds all CSV files inside Project and its
# subdirectories.


# Difference:
#
# iterdir()
# → All direct contents
#
# glob("*.py")
# → Matching files in the current directory
#
# rglob("*.py")
# → Matching files in the current directory
#   + all subdirectories


# ============================================================
# 8. name, stem and suffix
# ============================================================

# These attributes help us extract information from a file path.
#
# Example:
#
# file_path = Path("data/students.csv")
#
# print(file_path.name)
# print(file_path.stem)
# print(file_path.suffix)
#
# Output:
#
# students.csv
# students
# .csv
#
# name:
# → Complete filename
#
# stem:
# → Filename without extension
#
# suffix:
# → File extension


# Example:
#
# Path("images/cat.jpg")
#
# name   → cat.jpg
# stem   → cat
# suffix → .jpg


# ============================================================
# 9. parent and parents
# ============================================================

# parent returns the immediate parent directory.
#
# Example:
#
# file_path = Path("project/data/train/images/cat.jpg")
#
# print(file_path.parent)
#
# Output:
# project/data/train/images


# parent.parent can be used to move multiple levels upward.
#
# print(file_path.parent.parent)
#
# Output:
# project/data/train


# parents provides all parent directories as a sequence.
#
# Example:
#
# for parent in file_path.parents:
#     print(parent)
#
# It gives the different parent levels one by one.


# ============================================================
# 10. read_text() and write_text()
# ============================================================

# read_text() reads the complete text content of a file
# and returns it as a string.
#
# Example:
#
# file_path = Path("data.txt")
# content = file_path.read_text()
# print(content)


# write_text() writes text into a file.
#
# Example:
#
# file_path = Path("data.txt")
# file_path.write_text("Hello, Python!")
#
# If the file doesn't exist, it can create it.
#
# ⚠️ Important:
# write_text() overwrites/replaces existing file content.


# For append mode, use open():
#
# with file_path.open("a") as file:
#     file.write("\nNew content")
#
# "a" → append mode


# ============================================================
# 11. unlink() and rmdir()
# ============================================================

# unlink() removes a file.
#
# Example:
#
# file_path = Path("data.txt")
# file_path.unlink()
#
# ⚠️ If the file doesn't exist, FileNotFoundError can occur.


# rmdir() removes an EMPTY directory.
#
# Example:
#
# folder = Path("data")
# folder.rmdir()
#
# ⚠️ rmdir() cannot normally remove a non-empty directory.


# For recursively deleting a non-empty directory,
# shutil.rmtree() can be used:
#
# import shutil
# shutil.rmtree("data")
#
# ⚠️ Be very careful with rmtree() because it can delete
# the entire directory and its contents.


# ============================================================
# 12. Relative Path vs Absolute Path
# ============================================================

# Relative Path:
# A path specified relative to the current working directory.
#
# Example:
#
# file_path = Path("data/students.csv")
#
# If the current directory is:
#
# C:/Projects/Python
#
# then the path refers to:
#
# C:/Projects/Python/data/students.csv


# Absolute Path:
# A complete path that specifies the exact location.
#
# Example (Windows):
#
# file_path = Path(r"C:\Projects\Python\data\students.csv")
#
# The complete location is specified here.


# Generally, project code should prefer relative paths
# instead of hard-coded machine-specific absolute paths
# whenever practical.


# ============================================================
# 13. resolve()
# ============================================================

# resolve() converts a path into a resolved absolute path.
#
# Example:
#
# file_path = Path("data/students.csv")
#
# print(file_path.resolve())
#
# This gives the complete path according to the current
# environment.


# ============================================================
# 14. parts
# ============================================================

# parts returns individual components of a path as a tuple.
#
# Example:
#
# file_path = Path("project/data/train/images/cat.jpg")
#
# print(file_path.parts)
#
# Output:
#
# ('project', 'data', 'train', 'images', 'cat.jpg')
#
# Useful when we need to inspect individual parts of a path.


# ============================================================
# 15. with_name()
# ============================================================

# with_name() creates a NEW Path with a different filename.
# It does NOT rename the actual file automatically.
#
# Example:
#
# file_path = Path("data/students.csv")
#
# new_path = file_path.with_name("teachers.csv")
#
# print(new_path)
#
# Output:
# data/teachers.csv
#
# Original:
# data/students.csv
#
# New Path:
# data/teachers.csv


# ============================================================
# 16. with_suffix()
# ============================================================

# with_suffix() creates a NEW Path with a different file extension.
#
# Example:
#
# file_path = Path("data/students.csv")
#
# new_path = file_path.with_suffix(".json")
#
# print(new_path)
#
# Output:
# data/students.json
#
# It changes the suffix in the Path object.
# It does NOT convert the actual file from CSV to JSON.


# Difference:
#
# with_name()
# → Changes the complete filename
#
# with_suffix()
# → Changes only the extension


# ============================================================
# 17. Useful Path Checks & Properties
# ============================================================

# Some additional useful Path methods/properties:
#
# path.is_absolute()
# → Checks whether the path is absolute.
#
# path.is_relative_to(other)
# → Checks whether the path is relative to another path.
#   (Available in modern Python versions.)
#
# path.anchor
# → Returns the anchor/root part of the path.
#
# path.drive
# → On Windows, returns the drive such as C:.
#
# path.root
# → Returns the root part of the path.


# Example:
#
# path = Path(r"C:\Projects\Python\data.txt")
#
# print(path.is_absolute())
# print(path.drive)
# print(path.root)
#
# These properties are mainly useful when you need to inspect
# or validate paths.


# ============================================================
# 18. pathlib + os — When to Use Which?
# ============================================================

# pathlib:
# → Modern and object-oriented way to work with paths.
# → Preferred for most new Python code involving files/paths.
#
# Example:
#
# from pathlib import Path
#
# path = Path("data") / "students.csv"
#
# if path.exists():
#     print(path)


# os:
# → Older/general-purpose module containing many operating
#   system related utilities.
#
# Examples:
#
# import os
#
# os.getcwd()       → Current working directory
# os.environ        → Environment variables
# os.listdir()      → List directory contents
# os.makedirs()     → Create directories
#
#
# pathlib and os are NOT competitors.
# They can be used together when required.


# Example:
#
# from pathlib import Path
# import os
#
# path = Path("data")
#
# print(path.exists())
# print(os.environ.get("API_KEY"))
#
# Here:
# pathlib → File/path handling
# os      → Environment variable handling


# General Rule:
#
# Path/file/directory operations
# → Prefer pathlib
#
# Environment variables / some OS-level operations
# → os can still be useful
#
# Both can work together in real-world projects.


# ============================================================
# 🔥 QUICK REVISION
# ============================================================

# Path("file.txt")       → Create a Path object
# Path.cwd()             → Current working directory
# exists()               → Check if path exists
# is_file()              → Check if it is a file
# is_dir()               → Check if it is a directory
# mkdir()                → Create directory
# touch()                → Create empty file
# /                      → Join paths
# parents=True           → Create missing parent directories
# iterdir()              → Iterate direct contents
# glob()                 → Search using a pattern
# rglob()                → Recursive pattern search
# name                   → Complete filename
# stem                   → Filename without extension
# suffix                 → File extension
# parent                 → Immediate parent directory
# parents                → All parent directories
# read_text()            → Read text file
# write_text()           → Write/overwrite text file
# unlink()                → Delete a file
# rmdir()                 → Delete an empty directory
# resolve()              → Resolved absolute path
# parts                  → Path components
# with_name()             → Create path with new filename
# with_suffix()           → Create path with new extension
#
# ============================================================
# pathlib is especially useful in AI/ML projects for handling
# datasets, model files, configuration files, uploaded files,
# output directories, logs and project folder structures.
# ============================================================