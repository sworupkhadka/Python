# Ask for name and bid
# Save data to a dictionary {name: price}
# Check if new bids are to be added
# Compare bids in the dictionary

def find_highest_bidder(bidding_dictionary):
    # Initialize variables to track the highest bidder
    winner = ""
    highest_bid = 0

    # Loop through each bidder in the dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        # Check if the current bid is higher than the previous highest
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder  # store the bidder's name

    # Announce the winner
    print(f"The winner is {winner} with the highest bid of Rs {highest_bid}")


# Create an empty dictionary to store bids
bids = {}
continue_bidding = True

# Loop to allow multiple bidders
while continue_bidding:
    # Ask for user name and bid amount
    name = input("Enter your name:\n")
    price = int(input("What is your bid (in Rs):\n"))
    bids[name] = price

    # Ask if there are any new bidders
    should_continue = input("Are there any new bidders? Type 'yes' or 'no':\n").lower()

    # If no new bidders, stop the loop and find the winner
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    # If yes, clear the screen (simulate by printing blank lines)
    elif should_continue == "yes":
        print("\n" * 20)
