import random

secret_number = random.randint(1, 100)
guesses = 0

print("🎯 Number Guessing Game")

while True:
    try:
        guess = int(input("\nGuess the number between 1 and 100: "))

    except ValueError:
        print("Please enter valid number!")
        continue

    if guess < 1 or guess > 100:
        print("Please Enter a Number Between 1 and 100.")
        continue

    guesses += 1

    if guess < secret_number:
        print("Higher Number Please!")

    elif guess > secret_number:
        print("Lower Number Please!")

    else:
        print("\n🎉 Congratulations!")
        print(f"You Guessed the Correct Number: {secret_number}")
        print(f"It took {guesses} guesses to Guess The number")

        print()
        
        again = input("Play Again? (yes/no): ").lower()
        
        if again != "yes":
            break
        
