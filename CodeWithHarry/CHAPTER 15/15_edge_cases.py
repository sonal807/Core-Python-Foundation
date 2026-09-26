#An edge case is an unusual or extreme situation that occurs at the boundary of normal expected input or behavior 
#and can cause unexpected results if not handled properly.

#Simply Normal situation ke alawa jo unusual situations aa sakti hain,
#unhe pehle se identify karke handle karna = Edge Case Handling.

#Example — Empty List Edge Case
# Normal case: list mein numbers available hain.
numbers = [10, 20, 30, 40, 50]


# Edge case check:
# Agar list empty ([]) hui, to `not numbers` True hoga.
# Empty list hone par len(numbers) = 0 hota hai,
# isliye average calculate karne se ZeroDivisionError ho sakta hai.
if not numbers:

    # Edge case ko safely handle kar rahe hain.
    # Empty list hone par average calculate nahi karenge.
    print("Cannot calculate average. The list is empty.")

else:

    # Normal case:
    # List mein numbers available hain, isliye average calculate kar sakte hain.
    average = sum(numbers) / len(numbers)

    print("Average:", average)


#Example:
# User ka prompt receive kar rahe hain.
prompt = " "

# Edge case:
# Check kar rahe hain ki prompt empty ya sirf whitespace to nahi hai.
if not prompt.strip():

    # Invalid/empty prompt ko safely handle kar rahe hain.
    print("Cannot process an empty prompt.")

else:

    # Normal case:
    # Prompt available hai, isliye AI processing start kar sakte hain.
    print("Processing prompt:", prompt)
    