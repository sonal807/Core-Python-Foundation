#Timeout: A timeout is a limit placed on how long a program will wait for an operation to complete before stopping
#or handling the delay as an error.

import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def api_request():
    # Simulating an API request that takes 5 seconds.
    # In a real application, this would be an actual API call.
    time.sleep(5)

    return "API response received"


with ThreadPoolExecutor() as executor:

    # Start the API request in a separate thread.
    future = executor.submit(api_request)

    try:
        # Wait for the API response for a maximum of 2 seconds.
        result = future.result(timeout=2)

        print(result)

    except TimeoutError:
        # The API did not respond within the allowed time.
        print("Request timed out.")