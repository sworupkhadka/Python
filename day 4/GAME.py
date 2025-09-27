import random

print("Welcome to Rock-Paper-Scissors!")
print("Type 'q' to quit.")

choices = ['rock', 'paper', 'scissors']
while True:
    user_choice = input("Choose rock, paper or scissors: ").strip().lower()
    if user_choice == 'q' or user_choice == 'quit':
        print("Goodbye!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
    (user_choice == 'paper' and computer_choice == 'rock') or \
    (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
        
        







#  1️⃣ .strip()

# Removes leading and trailing whitespace (spaces, tabs, newlines) from a string.

# Example:

# user_input = "   rock   "
# cleaned = user_input.strip()
# print(cleaned)  # Output: "rock"


# Without .strip(), " rock " would not match "rock" in comparisons.

# 2️⃣ .lower()

# Converts all characters in the string to lowercase.

# Example:

# user_input = "RoCk"
# cleaned = user_input.lower()
# print(cleaned)  # Output: "rock"


# Without .lower(), "RoCk" would not match "rock" in comparisons.

# Combined: .strip().lower()

# Removes extra spaces and makes the string lowercase.

# Very common when taking user input so comparisons are case-insensitive and space-insensitive.

# user_input = "   RoCk  "
# cleaned = user_input.strip().lower()
# print(cleaned)  # Output: "rock"


# ✅ This ensures your input matches 'rock', 'paper', or 'scissors' regardless of how the user types it.



# to keep count of games and win use 


# import random

# print("Welcome to Rock-Paper-Scissors!")
# print("Type 'q' to quit.")

# choices = ['rock', 'paper', 'scissors']
# scores = {'You': 0, 'Computer': 0, 'Ties': 0}

# while True:
#     user_choice = input("Choose rock, paper or scissors: ").strip().lower()
#     if user_choice == 'q' or user_choice == 'quit':
#         print("Goodbye!")
#         print(f"Final Score -> You: {scores['You']} | Computer: {scores['Computer']} | Ties: {scores['Ties']}")
#         break
#     if user_choice not in choices:
#         print("Invalid choice. Try again.")
#         continue

#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#         scores['Ties'] += 1
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         print("You win!")
#         scores['You'] += 1
#     else:
#         print("Computer wins!")
#         scores['Computer'] += 1

#     print(f"Current Score -> You: {scores['You']} | Computer: {scores['Computer']} | Ties: {scores['Ties']}")
