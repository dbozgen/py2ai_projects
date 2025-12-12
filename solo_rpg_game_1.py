
# GAME PLAN 
# Step 1: Roll the dice (random 1-6) ✓
# Step 2: Create a deck of 52 cards
# Step 3: Pick that many random cards
# Step 4: Display them nicely


import random 

suit_meanings = {
    "Hearts ♥": "Infrastructure & Habitats: Hearts are places built for living: solar villages, cliff dwellings, canopy homes, underground commons, floating neighborhoods, repurposed old cities grown over with green systems.",
    "Diamonds ♦": "Communities & Beings: Diamonds are people and other thinking or semi-thinking beings shaped by solarpunk life: neighbors, engineers, farmers, children, elders, augmented humans, uplifted animals, sentient machines, hybrid collectives.",
    "Clubs ♣": "Living Systems: Clubs are biological systems that support life but don’t act like individuals: food forests, algae farms, fungal networks, pollinator corridors, river ecologies, soil systems, floating gardens.", 
    "Spades ♠": "Energy, Tools & Knowledge: Spades are the systems that make everything work: solar grids, wind relays, water engines, seed libraries, repair tools, data archives, climate monitors, shared machines."
}

rank_meanings = {
    "A": "among solar-grown field towers, a wind-woven pollination tower that spreads seeds and makes power",
    "2": "beneath orbital light collectors, a lunar-charged night lens that stores and releases moonlight",
    "3": "along a managed riverway, a living ribbon that generates power while cleaning water",
    "4": "within a canyon energy corridor, a bridge that turns wind and vibration into energy",
    "5": "nested in a canopy habitat, a solar nest that shelters birds and powers life below",
    "6": "atop a cryothermal summit station, a beacon that draws energy from extreme cold and warmth",
    "7": "adjacent to a geothermal regulation zone, an engine that safely converts underground heat",
    "8": "upon a monitored ice shelf, an archive that records ice change and sends warnings",
    "9": "inside the subterranean commons, a network that moves energy, water, and information",
    "10": "embedded in a vertical bioscaffold, a garden system that passes light, water, and energy",
    "J": "within an arid water-harvesting basin, a tower that gathers night moisture and cools by day",
    "Q": "inside a deep-sea habitat array, an engine that learns tides to produce steady power",
    "K": "moored to an aerial energy grid, a floating orchard that grows food and sends energy downward"
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
        # Example of displaying meanings for each card picked   
        print("\nMeanings of your cards:")
        for card in hand:
            rank, _, suit = card.partition(" of ")
            suit_meaning = suit_meanings[suit]
            rank_meaning = rank_meanings[rank]
            print(f"{card}: {suit_meaning} - {rank_meaning}")
    
        play_again = input ("Roll again? (y/n):").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
else:
    print("Maybe next time!")
