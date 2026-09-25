#Retry logic: Retry logic is a mechanism that automatically attempts an operation again when it temporarily fails.

#Maan lo API request temporarily fail ho rahi hai. Hum maximum 3 attempts denge.
import time

# Maximum number of times the operation can be attempted.
max_retries = 3

# Try the operation up to the maximum allowed attempts.
for attempt in range(1, max_retries + 1):

    print(f"Attempt {attempt}: Sending API request...")

    try:
        # Simulating a temporary network/API failure.
        # In a real application, this would be an actual API request.
        raise ConnectionError("Temporary network error")

    except ConnectionError as e:
        # Handle the temporary connection error.
        print("Request failed:", e)

        # Retry only if there are attempts remaining.
        if attempt < max_retries:
            print("Retrying...\n")

            # Wait for 2 seconds before making the next attempt.
            # This prevents immediate repeated requests.
            time.sleep(2)

        else:
            # No attempts are left, so stop retrying.
            print("Maximum retry attempts reached.")