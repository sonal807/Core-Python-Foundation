#.env: A .env file stores configuration values and sensitive environment variables outside the Python source code,
#while python-dotenv loads those values into the environment.

#python-dotenv: to read key-value configuration pairs from a local .env file into your application's environment.
#installing python-dotenv: pip install python-dotenv

from dotenv import load_dotenv   #python-dotenv se load_dotenv() import karta hai
import os

load_dotenv()  #.env file ke variables environment mein load karta hai.

api_key = os.getenv("API_KEY")  #Loaded variable ki value retrieve karta hai.
username = os.getenv("APP_USERNAME")
project = os.getenv("PROJECT")

print("API Key:", api_key)
print("Username:", username)
print("Project:", project)

#.gitignore: .gitignore is a Git configuration file that tells Git which files and folders should be ignored and not tracked in a repository.

#we just create a .gitignore file and in that file we mention the name which we dont want to commit on github