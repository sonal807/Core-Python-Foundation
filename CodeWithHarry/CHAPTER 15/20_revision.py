#Type hinting is a Python feature that allows us to specify the expected data type of
# variables, function parameters, and return values.

# AI response generate karne wale function ko define kar rahe hain.
# Type hints ke through hum bata rahe hain ki function ko
# kis type ka data chahiye aur ye kya return karega.
def generate_response(
    prompt: str,          # User ka question/message string ke form mein hoga.
    temperature: float,   # AI generation parameter ke liye float value expected hai.
    max_tokens: int,      # Maximum tokens ki limit integer mein hogi.
    stream: bool          # Streaming enable hai ya nahi, True/False hoga.
) -> str:                 # Function ek string response return karega.

    # Received prompt ko display kar rahe hain.
    print("Prompt:", prompt)

    # AI generation ke temperature value ko display kar rahe hain.
    print("Temperature:", temperature)

    # Maximum allowed tokens ko display kar rahe hain.
    print("Max Tokens:", max_tokens)

    # Streaming ka status display kar rahe hain.
    print("Streaming:", stream)

    # Abhi actual AI API call nahi kar rahe hain.
    # Sirf AI response ko simulate karne ke liye string return kar rahe hain.
    return "AI response generated."


# Function ko required values ke saath call kar rahe hain.
response = generate_response(
    "Explain AI.",   # prompt: str
    0.7,             # temperature: float
    200,             # max_tokens: int
    False            # stream: bool
)

# Function se returned AI response ko display kar rahe hain.
print("Response:", response)

#List
from typing import List

def get_languages() -> List[str]:
    # AI model ki supported languages return kar rahe hain.
    return ["English", "Hindi", "French"]


languages = get_languages()

print(languages)

#Dict
from typing import Dict

def get_model_config() -> Dict[str, float]:
    # AI model ki configuration return kar rahe hain.
    return {
        "temperature": 0.7,
        "top_p": 0.9
    }


config = get_model_config()

print(config)

#Optional: It is used when a value can either contain specific type or be None.
from typing import Optional

def get_user_email(email: Optional[str]) -> str:

    # Check kar rahe hain ki email provide kiya gaya hai ya nahi.
    if email is None:
        return "Email not provided."

    return email


print(get_user_email("sonal@example.com"))
print(get_user_email(None))

#AI use:
from typing import Optional

def chat(
    prompt: str,
    model: Optional[str] = None
) -> str:

    # Agar model provide nahi hua,
    # to default model use kar sakte hain.
    if model is None:
        model = "default-model"

    return f"Using {model} for: {prompt}"


print(chat("Explain AI."))
print(chat("Explain AI.", "my-model"))

#Pydantic:Pydantic is a Python library used for data validation and structured data handling using Python type hints.

#BaseModel
from pydantic import BaseModel


# Chat request ke liye structured data model define kar rahe hain.
class ChatRequest(BaseModel):

    # User ka prompt string hona chahiye.
    prompt: str

    # Temperature ek floating-point value honi chahiye.
    temperature: float

    # Maximum tokens integer hone chahiye.
    max_tokens: int


# User/API request ka data create kar rahe hain.
request = ChatRequest(
    prompt="Explain Machine Learning.",
    temperature=0.7,
    max_tokens=200
)


# Validated data ko access kar rahe hain.
print("Prompt:", request.prompt)
print("Temperature:", request.temperature)
print("Max Tokens:", request.max_tokens)


#Pydantic conversion:
from pydantic import BaseModel


class ChatRequest(BaseModel):

    prompt: str
    temperature: float
    max_tokens: int


request = ChatRequest(
    prompt="Explain AI.",
    temperature=0.7,
    max_tokens="200"
)

print("Max Tokens:", request.max_tokens)
print("Type:", type(request.max_tokens))


#An AI Engineer practical example combines Python concepts to build reliable, structured, and maintainable AI application components.

#We are creating AI chat request simulator:
#We will use:
# Type Hints
#     ↓
# Pydantic
#     ↓
# Input Validation
#     ↓
# Custom Exception
#     ↓
# Logging
#     ↓
# Error Handling
#     ↓
# Graceful Failure
#     ↓
# AI Response Simulation

import logging
from pydantic import BaseModel, Field, ValidationError


# Application ke logs configure kar rahe hain.
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    force=True
)


# Invalid AI request ko represent karne ke liye
# custom exception define kar rahe hain.
class InvalidAIRequestError(Exception):
    pass


# AI chat request ka structured data model define kar rahe hain.
class ChatRequest(BaseModel):

    # User ka prompt required hai aur empty nahi ho sakta.
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


# AI response generate karne ka function.
def generate_response(request: ChatRequest) -> str:

    # AI request receive hone ka log record kar rahe hain.
    logging.info("AI request received.")

    # Abhi actual AI API call nahi kar rahe.
    # AI response ko simulate kar rahe hain.
    response = f"AI response for: {request.prompt}"

    # Generated response return kar rahe hain.
    return response


def process_chat_request(
    prompt: str,
    max_tokens: int = 200,
    temperature: float = 0.7
) -> str:

    # User request ko validate karne ki koshish kar rahe hain.
    try:
        request = ChatRequest(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )

    except ValidationError as e:
        # Pydantic validation failure ko log kar rahe hain.
        logging.error("AI request validation failed.")

        # Validation error ko application-specific
        # custom exception mein convert kar rahe hain.
        raise InvalidAIRequestError(
            "Invalid AI request. "
            "Please check prompt, max_tokens, and temperature."
        ) from e

    # Validated request ko AI response function mein bhej rahe hain.
    return generate_response(request)


# User request ko safely process kar rahe hain.
try:

    # Valid AI request provide kar rahe hain.
    response = process_chat_request(
        prompt="Explain Machine Learning.",
        max_tokens=200,
        temperature=0.7
    )

    # Successful AI response display kar rahe hain.
    print("Response:", response)

except InvalidAIRequestError as e:

    # Custom exception ko safely handle kar rahe hain.
    logging.error("Request failed: %s", e)

    # User ko clear aur meaningful error message de rahe hain.
    print("Request failed:", e)