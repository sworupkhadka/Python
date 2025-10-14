from gamedata import data
import random

print("Welcome to the Higher or Lower game")

score = 0
game_should_continue = True

# Pick initial choices
choice_a, choice_b = random.sample(data, 2)
# another method:
# choice_a = random.choice(data)
# choice_b = random.choice([item for item in data if item != choice_a])

while game_should_continue:
    # Display choice A
    name = choice_a["name"]
    description = choice_a["description"]
    country = choice_a["country"]
    print(f"Compare A: {name}, a {description}, from {country}")

    # Display choice B
    name = choice_b["name"]
    description = choice_b["description"]
    country = choice_b["country"]
    print(f"Compare B: {name}, a {description}, from {country}")

    # Get user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Determine the correct answer
    if choice_a["follower_count"] > choice_b["follower_count"]:
        correct_answer = "A"
    elif choice_a["follower_count"] < choice_b["follower_count"]:
        correct_answer = "B"
    else:
        correct_answer = "Equal"  # Rare case

    # Check guess
    if guess == correct_answer:
        score += 1
        print(f"🎉 Correct guess! Your score: {score}")

        # Update choice_a to the winner
        if correct_answer == "B":
            choice_a = choice_b

        # Pick a new choice_b different from choice_a
        #choice_b = random.choice(data) 
        #this way might introduce error though it functions correctly if choice_a
        #and choice_b are same the follower might also be same so we can instead use 
        
        choice_b = random.choice([item for item in data if item != choice_a])
        
        #so that choice_a id not equal to choice_b
    else:
        print(f"❌ Incorrect guess! Final score: {score}")
        game_should_continue = False