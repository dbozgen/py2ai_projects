
# GAME PLAN 
# Step 1: Roll the dice (random 1-6) ✓
# Step 2: Create a deck of 52 cards
# Step 3: Pick that many random cards
# Step 4: Display them nicely


import random 

suit_meanings = {
    "Hearts ♥": "a community center",
    "Diamonds ♦": "a trading hub",
    "Clubs ♣": "a living ecosystem",
    "Spades ♠": "an energy system"
}

rank_meanings = {
    "A": "among solar-grown field towers",
    "2": "beneath orbital light collectors",
    "3": "along a managed riverway",
    "4": "within a canyon energy corridor",
    "5": "nested in a canopy habitat",
    "6": "atop a cryothermal summit station",
    "7": "adjacent to a geothermal regulation zone",
    "8": "upon a monitored ice shelf",
    "9": "inside the subterranean commons",
    "10": "embedded in a vertical bioscaffold",
    "J": "within an arid water-harvesting basin",
    "Q": "inside a deep-sea habitat array",
    "K": "moored to an aerial energy grid"
}

dice_meanings = {
    "1": "Far away in the distance.",
    "2": "Far away in the distance.",
    "3": "Appears next to you suddenly.",
    "4": "Appears next to you suddenly.",
    "5": "You see it as you are resting.",
    "6": "You see it as you are resting.",        
}

# Create a deck of 52 cards

suits = ["Hearts ♥", "Diamonds ♦", "Clubs ♣", "Spades ♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []   

# Create the deck by combining each rank with each suit
for suit in suits:
    for rank in ranks:
        card = f"{rank} of {suit}"
        deck.append(card)       
        
# Create a dice
dice_ranks = ["1","2", "3", "4", "5", "6"]


#1. Roll the dice
start_game = input("You wanna roll the dice? (y/n): ").lower()


if start_game == 'y':
    while True:
        #2. Roll the dice
        dice_roll = random.choice(dice_ranks)
        print(f"\nYou rolled a {dice_roll} 🎲 \n")
        
        #3. Pick a random cards
        card = random.choice(deck)
        print(f"You picked {card}")

        #4. Example of displaying meanings for each card picked   
        
        rank, _, suit = card.partition(" of ")
        suit_meaning = suit_meanings[suit]
        rank_meaning = rank_meanings[rank]
        dice_meaning = dice_meanings[dice_roll]
        
        print(f"WRITING PROMPT:\n{dice_meaning} - {suit_meaning} {rank_meaning} \n ")

    
        play_again = input ("Draw a card? (y/n):").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
else:
    print("Maybe next time!")
