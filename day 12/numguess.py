import random  # Import the random module to generate random numbers

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
random_integer = random.randint(1, 100)

# Choose difficulty level
level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()  
# Convert input to lowercase to handle 'Easy' or 'HARD'

# Set number of attempts based on difficulty
if level == "easy":
    attempts = 10  # Easy mode has 10 attempts
elif level == "hard":
    attempts = 5   # Hard mode has 5 attempts
else:
    print("Invalid choice. Defaulting to easy mode.")
    attempts = 10  # Default to easy if input is invalid

# Initialize guess variable
guess = 0  # Start with 0 so the loop runs at least once

# Game loop: continues while the guess is incorrect and attempts remain
while guess != random_integer and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))  # Convert input to integer

    # Compare guess with the random number
    if guess > random_integer:
        print("Too high.")  # Guess is higher than the number
    elif guess < random_integer:
        print("Too low.")   # Guess is lower than the number
    else:
        print(f"Correct! The number was {random_integer}. You win!")
        break  # Exit the loop if the guess is correct

    # Decrement attempts after each wrong guess
    attempts -= 1

    # Check if attempts are over
    if attempts == 0:
        print(f"You've run out of guesses. The number was {random_integer}. Game over.")
