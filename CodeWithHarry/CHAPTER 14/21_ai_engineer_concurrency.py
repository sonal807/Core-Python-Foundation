#Concurrency in AI engineering allows an application to handle multiple independent tasks efficiently,
#especially when those tasks involve waiting for APIs, databases, files, or other external services.

# AI Engineer ke liye final decision map
#              TASK
#                │
#        ┌───────┴────────┐
#        ↓                ↓
#    I/O-bound         CPU-bound
#        │                │
#    ┌───┴────┐           │
#    ↓        ↓           ↓
# asyncio   Threads    Processes
#    │        │           │
#    ↓        ↓           ↓
# Async    ThreadPool  ProcessPool

# Example:                    
# Situation                    	          Common approach
# Multiple API calls                        asyncio
# Async HTTP requests                       asyncio
# Database/network waiting                  asyncio / threads
# Blocking library                          ThreadPoolExecutor
# Heavy CPU computation                     ProcessPoolExecutor
# Multiple independent async operations	    asyncio.gather()

#Practical Example:
import asyncio

async def web_search():
    print("Web search started")
    await asyncio.sleep(2)
    return "Web search result"

async def database_search():
    print("Database search started")
    await asyncio.sleep(2)
    return "Database result"

async def llm_request():
    print("LLM request started")
    await asyncio.sleep(2)
    return "LLM response"

async def main():

    # Independent I/O-bound operations ko concurrently execute karta hai.
    results = await asyncio.gather(
        web_search(),
        database_search(),
        llm_request()
    )

    print("Results:", results)


asyncio.run(main())

#Example: Concurrent API calls
import asyncio


async def call_api(api_name, delay):
    print(f"{api_name} request started")

    # API response ka wait simulate kar raha hai
    await asyncio.sleep(delay)

    print(f"{api_name} response received")

    return f"{api_name} data"


async def main():

    results = await asyncio.gather(
        call_api("User API", 2),
        call_api("Weather API", 3),
        call_api("News API", 1)
    )

    print("\nAll API responses:")
    print(results)


asyncio.run(main())