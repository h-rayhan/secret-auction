import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print the auction logo
print(logo)
print("Welcome to the secret auction program.")

bidders = {}

# Main loop to gather bids
while True:
    name = input("What is your name?: ")

    while True:
        try:
            amount = int(input("What's your bid?: £"))
            break
        except ValueError:
            print("Enter a valid number for the bid.")

    bidders[name] = amount

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bidders not in ["yes", "y"]:
        break
    clear()

clear()

# Determine the winner
highest_bid = 0
winner = ""

for bidder_name, bid_amount in bidders.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder_name

print(f"The winner is {winner} with a bid of £{highest_bid}.")
