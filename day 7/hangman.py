# hangman.py
# Simple terminal Hangman game

import random
from pics import HANGMAN_PICS


# List of possible words to guess
WORDS = ["python", "hangman", "developer", "programming", "keyboard", "algorithm"]

def play():  # Main game function
    word = random.choice(WORDS)         # Pick a random word from the list
    guessed = set()                     # Store correctly guessed letters
    wrong = 0                           # Count wrong guesses
    max_wrong = len(HANGMAN_PICS) - 1   # Max allowed wrong guesses

    print("Let's play Hangman!")        # Game start message

    while True:
        print(HANGMAN_PICS[wrong])      # Show hangman stage
        display = " ".join([c if c in guessed else "_" for c in word])  # Show word progress
        print("Word:", display)         # Display current word state

        # Win or lose checks
        if all(c in guessed for c in word):  # All letters guessed
            print("\n You won! The word was:", word)
            break
        if wrong == max_wrong:               # Used all chances
            print("\n💀 You lost! The word was:", word)
            break

        guess = input("Guess a letter: ").lower()  # Ask user for a letter
        if not guess.isalpha() or len(guess) != 1: # Check for valid input
            print("Enter a single letter!")        
            continue
        if guess in guessed:                       # Already guessed this letter
            print("You already tried that!")       
            continue

        if guess in word:              # Correct guess
            guessed.add(guess)
            print("Correct!")
        else:                          # Wrong guess
            wrong += 1
            print("Wrong!")

# Run the game only when file is executed directly
if __name__ == "__main__":
    play()