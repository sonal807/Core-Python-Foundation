#Pydantic: Pydantic is a Python library used for data validation
#and structured data handling using Python type hints.

#First we have to install pydantic pip install pydantic

#In python we use pydantic generally to inherit BaseModel to make our data model

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

#Example:
from pydantic import BaseModel

# User ke expected data structure ko define kar rahe hain.
class User(BaseModel):
    name: str
    age: int


# User object create kar rahe hain.
user = User(
    name="Sonal",
    age=25
)


# Validated data access kar rahe hain.
print("Name:", user.name)
print("Age:", user.age)

#Example:
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    price: float
    quantity: int

customer = Customer(
    name = "Rahul",
    price = 99.9,
    quantity = "67"
)

print("Name: ", customer.name)
print("Price: ", customer.price)
print("Quantity: ", customer.quantity)

# Pydantic Validation:
#
# Pydantic checks incoming data according to the types defined
# in the BaseModel.
#
# If the value can be converted to the expected type,
# Pydantic may parse/coerce the value automatically.
#
# Example:
# quantity: int
#
# quantity="67" → Successfully converted to int → 67
# quantity="hello" → Cannot be converted to int → ValidationError
#
# Therefore, Pydantic provides both data validation
# and data parsing/coercion.


#Example: AI API request simulation
from pydantic import BaseModel


# AI chatbot request ka expected data structure define kar rahe hain.
class ChatRequest(BaseModel):
    question: str
    max_tokens: int
    temperature: float


# User/API se aayi request ko simulate kar rahe hain.
request = ChatRequest(
    question="What is Machine Learning?",
    max_tokens=200,
    temperature=0.7
)


# Validated data ko access kar rahe hain.
print("Question:", request.question)
print("Max Tokens:", request.max_tokens)
print("Temperature:", request.temperature)


#Required Fields: A required field is a field that must be provided when creating a Pydantic model object.

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

#Both fields are required
user = User(                #If user = User(name="Sonal"), then there will be ValidationError on missing age
    name= "Sonal",
    age= 25
)

print(user)
#name: str
#age: int  both are required
#If user = User(name="Sonal"), then there will be ValidationError on missing age

#Default Value: A default value is a predefined value that Pydantic uses when a field is not provided.

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    max_tokens: int = 200      #max_tokens should be integer, and if user doesn't give any value then 200 will be used

#max_tokens provide nhi mentioned hai,
#isliye default value 200 use hogi.
request = ChatRequest(
    question= "What is RAG?"
)

print("Question: ", request.question)
print("Max Tokens: ", request.max_tokens)


#AI related Full Example
from pydantic import BaseModel


class ChatRequest(BaseModel):
    # User ka question required hai.
    question: str

    # Agar user max_tokens nahi deta,
    # to 200 automatically use hoga.
    max_tokens: int = 200

    # AI response ki creativity control karne ke liye.
    # Default temperature 0.7 rakhi hai.
    temperature: float = 0.7

    # User ka model specify karna optional hai.
    # Default model use hoga.
    model: str = "default-model"


# User ne sirf question provide kiya.
request = ChatRequest(
    question="Explain RAG in simple words."
)

print("Question:", request.question)
print("Max Tokens:", request.max_tokens)
print("Temperature:", request.temperature)
print("Model:", request.model)