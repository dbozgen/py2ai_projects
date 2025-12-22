import random

# Build the full 52-card deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []
for suit in suits:
    for value in values:
        deck.append(f"{value} of {suit}")

# Pick 6 random cards
hand = random.choice(deck)
print(f"You drew: {hand}")