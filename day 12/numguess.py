import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_integer = random.randint(1, 100)

# Choose difficulty level
level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid choice. Defaulting to easy mode.")
    attempts = 10

# Game loop
guess = 0
while guess != random_integer and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > random_integer:
        print("Too high.")
    elif guess < random_integer:
        print("Too low.")
    else:
        print(f"Correct! The number was {random_integer}. You win!")
        break

    attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses. The number was {random_integer}. Game over.")
