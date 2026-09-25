#Configuration handling is the practice of storing and
#managing application settings separately from the main program code.

#Approach 1: Every code in hard-code
model = "my-ai-model"
temperature = 0.7
max_tokens = 500
api_key = "my-secret-key"
debug = True

print("Model: ", model)
print("Temperature: ", temperature)
print("Max Tokens: ", max_tokens)

#Approach 2: we just make 2 files seperatly for application settings and in another about acessing it and modifying it
#config.py
# MODEL = "my-ai-model"
# TEMPERATURE = 0.7
# MAX_TOKENS = 500
# DEBUG = True

#main.py
# from config import MODEL, TEMPERATURE, MAX_TOKENS, DEBUG

# print("Model:", MODEL)
# print("Temperature:", TEMPERATURE)
# print("Max Tokens:", MAX_TOKENS)
# print("Debug Mode:", DEBUG)


# main.py
# → "AI request kaise bhejni hai?"

# config.py
# → "Kaunsa model use karna hai?"
# → "Temperature kitna hai?"
# → "Max tokens kitne hain?"

# Environment
# → "Secret API key kya hai?"

#Environment variable: An environment variable is a value stored outside the Python source code that an application can read while it is running.

import os 

api_key = os.getenv("API_KEY")  #Suppose we have API_KEY = abc123-secret

print(api_key)    #If no key then it will give none

#In real project its not better choice to print API key
import os

api_key = os.getenv("API_KEY")

if api_key:
    print("API key loaded successfully.")
else:
    print("API key is missing.")