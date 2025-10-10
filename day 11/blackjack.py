import random  # Import the random module for random card selection

# ------------------ Deal a random card ------------------
def deal_card():
    """Returns a random card from the deck."""
    # List of possible card values (Ace = 11, face cards = 10)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)  # Randomly pick one card from the deck


# ------------------ Calculate the score ------------------
def calculate_score(cards):
    """Takes a list of cards and returns the score."""
    # Check for a Blackjack (Ace + 10 as the first two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represent Blackjack as 0

    # If there's an Ace (11) and total > 21, convert Ace to 1 to prevent bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  # Return the final score


# ------------------ Compare final scores ------------------
def compare(user_score, computer_score):
    """Compares user and computer scores and returns the result message."""
    if user_score == computer_score:
        return "It's a draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over 21! You lose "
    elif computer_score > 21:
        return "Opponent went over 21! You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "


# ------------------ Main Game Function ------------------
def play_game():
    user_cards = []        # Stores player's cards
    computer_cards = []    # Stores computer's cards
    is_game_over = False   # Game control flag

    # Deal 2 initial cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Main game loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show current hands and scores
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if someone already won or busted
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Give player another card
            else:
                is_game_over = True  # Player passes, round ends

    # Computer keeps drawing cards until it reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show both players' final hands and scores
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Announce the result


# ------------------ Run the Game ------------------
# Loop the game so the player can choose to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
