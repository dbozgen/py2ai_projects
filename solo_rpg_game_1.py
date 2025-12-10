
# GAME PLAN 
# Step 1: Roll the dice (random 1-6) ✓
# Step 2: Create a deck of 52 cards
# Step 3: Pick that many random cards
# Step 4: Display them nicely


import random 

# Create a deck of 52 cards

suits = ["Hearts ♥", "Diamonds ♦", "Clubs ♣", "Spades ♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []   

# Create the deck by combining each rank with each suit
for suit in suits:
    for rank in ranks:
        card = f"{rank} of {suit}"
        deck.append(card)       

start_game = input("You wanna roll the dice? (y/n): ").lower()

if start_game == 'y':
    while True:
        #1. Dice roll
        rolled_dice = random.randint(1, 6)
        print(f"You rolled a {rolled_dice}")

        #3. Pick that many random cards
        hand = random.sample(deck, rolled_dice)

        #4. Display them nicely
        print("You picked the following cards:")
        for card in hand:
            print(card)
        play_again = input ("Roll again? (y/n):").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
else:
    print("Maybe next time!")