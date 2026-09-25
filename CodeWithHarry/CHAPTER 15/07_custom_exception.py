#A custom exception is a user-defined exception class created
#to represent a specific type of error in an application.

# Custom exception define kar rahe hain.
class InvalidAgeError(Exception):
    pass


def validate_age(age):
    # Age negative hone par custom exception raise karenge.
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    return age


try:
    age = validate_age(-5)

    print("Valid age:", age)

except InvalidAgeError as e:
    # Custom exception ko handle kar rahe hain.
    print("Validation Error:", e)


#AI example:
class TokenLimitError(Exception):
    pass

def validate_tokens(tokens):
    # AI model ki maximum token limit check kar rahe hain.
    if tokens > 4096:
        raise TokenLimitError(
            "Token limit exceeded. Maximum allowed tokens are 4096."
        )

    return tokens

try:
    tokens = validate_tokens(5000)
    print("Valid token count: ", tokens)

except TokenLimitError as e:
    print("AI error: ", e)


#Example:
class InvalidPromptError(Exception):
    pass

def validate_prompt(prompt):
    if not prompt.strip():
        raise InvalidPromptError(
            "The given prompt is invalid. Please enter prompt."
        )

    return prompt

try:
    prompt = validate_prompt(" ")

    print("Prompt: ", prompt)

except InvalidPromptError as e:
    print("Prompt error: ", e)