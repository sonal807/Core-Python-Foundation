#os: The os module provides functions for interacting with the operating system, 
#including working with directories, environment variables, and system-level information.

#os.getcwd()- Current Working Directory
import os

current_path = os.getcwd()  #it will give the path of current working folder, and it is similar to pathlib Path.cwd()

print(current_path)

#os.listdir()- Contents of Folder
import os

items = os.listdir(".")  #. represents current directory
print(items)

#Environment Variable: An environment variable is a key-value pair provided by the operating system or 
#environment that stores configuration information used by applications.

#For example: API_KEY = abc123
#API_KEY -> key
#abc123 -> value

#os.environ: It is used to access environment variables in python
# import os

# print(os.environ)

#os.getenv(): os.getenv() retrieves the value of an environment variable and returns None if the variable does not exist.

#Example:
import os

username = os.getenv("USERNAME")

print(username)

#os.environ vs os.getenv()
#Both can access value but os.environ will give KeyError if variable doesn't exist while os.getenv() will return none
