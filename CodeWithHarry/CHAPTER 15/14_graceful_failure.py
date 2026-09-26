# Graceful failure: It is the practice of handling errors or failures safely
# so that an application does not crash unexpectedly and 
# can provide a meaningful response or continue operating when possible.

def divide_numbers(a, b):
    try:
        # Division operation perform kar rahe hain.
        # Agar b = 0 hua, to ZeroDivisionError generate hoga.
        return a / b

    except ZeroDivisionError:
        # Error ko handle kar rahe hain taaki program
        # unexpected way mein crash na ho.
        print("Cannot divide by zero.")

        # None return karke caller ko signal de rahe hain
        # ki division successfully complete nahi hui.
        return None


# Function ko zero denominator ke saath call kar rahe hain.
result = divide_numbers(10, 0)


# Check kar rahe hain ki operation successful hua ya nahi.
if result is not None:
    print("Result:", result)

else:
    # Operation fail hone par meaningful response de rahe hain
    # instead of allowing the program to crash.
    print("Operation could not be completed.")

# Graceful Failure ka core idea
# Error occurs
#      ↓
# Detect the failure
#      ↓
# Handle it safely
#      ↓
# Give meaningful response
#      ↓
# Continue / fallback / stop safely

#Example:
def call_ai_api(prompt):
    try:
        # Real application mein yahan actual AI API request hoti.
        # Abhi API failure ko simulate kar rahe hain.
        raise ConnectionError("AI API is temporarily unavailable.")

    except ConnectionError as e:
        # API connection failure ko safely handle kar rahe hain.
        print("AI server error: ", e)

        # None return karke caller ko signal de rahe hain
        # ki AI response successfully receive nahi hua.
        return None

# User ka prompt AI service ko bhej rahe hain.
prompt = "Expalin Machine Learning."

response = call_ai_api(prompt)

# Check kar rahe hain ki AI response successfully mila ya nahi.
if response is not None:
    print("AI response: ", response)

else:
    # API fail hone par application crash karne ke bajay
    # user ko meaningful fallback message de rahe hain.
    print("Sorry, the AI service is currently unavailable.")
    print("Please try again later.")