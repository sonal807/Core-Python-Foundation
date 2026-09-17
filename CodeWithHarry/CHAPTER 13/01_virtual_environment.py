#Virtual Environment: A virtual environment is an isolated Python environment that allows a project to have its own Python packages
#and dependencies without affecting other projects or the system-wide Python installation.

#Craeting virtual environment:
# '''Terminal command:
#      python -m venv .venv   #it will create a folder name .venv with will contain some folders and files
#      .venv\Scrpits\Activate.ps1    #it will activate virtual environment successfully.
#      pip install .....         #it will install any package/library
#      deactivate               #it will deactivate virtual environment''' 

# import requests  #It is useful for working with APIs
# print("Requests package is working")

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array: ", arr)
print("First element: ", arr[0])
print("Array sum: ", arr.sum())
print("Mean: ", np.mean(arr))