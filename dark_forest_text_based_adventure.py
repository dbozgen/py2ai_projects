
# A simple text-based adventure game set in a dark forest

# your arsenal 

arsenal = []

# Define the rooms in the dark forest
rooms = {
    "forest": {
        "name": "Dark Forest",
        "description": "You're in a dark forest. Paths lead left and right.",
        "choices": ["left", "right", "search"],
        "art": """
        🌲🌲🌲
        🌲 YOU 🌲
        🌲🌲🌲
        """
    },
    "cave": {
        "name": "Mysterious Cave",
        "description": "You entered a dark cave. You see a treasure chest!",
        "choices": ["open", "leave"],
        "art": """
        /\\_/\\
       /     \\
       | 💎📦 |
        \\_____/
        """
    },
    "dragon": {
        "name": "Dragon's Lair",
        "description": "A dragon appears! It's angry!",
        "choices": ["fight", "run"],
        "art": """
      /\\___/\\
     ( o   o )
     (  =^=  )
     (        )
     (         ))
    (          ))
   ((         )))
        """        
    },
    "hidden_path": {
        "name": "Hidden Path",
        "description": "You found a magic sword.",
        "choices": ["go back to forest", "fight dragon"],
        "art": """
        |
       /|\\
      / | \\
     /  |  \\
    ⚔️ SWORD ⚔️
        """        
    }
}


# Start the game 

current_location = "forest"
game_over = False

while not game_over:
    room = rooms[current_location]
    if arsenal:
        print(f"\n🎒 Arsenal: {', '.join(arsenal)}")

    print("\n" + room["art"])
    print("\n" + room["name"])
    print(room["description"])
    choice = input("What do you do? " + "/".join(room["choices"]) + ": ").strip().lower()

#Forest logic
    if current_location == "forest":
        if choice == "left":
            current_location = "cave"
        elif choice == "right":
            current_location = "dragon"
        elif choice == "search":
            current_location = "hidden_path"
        else:
            print("Invalid choice. Try again.")
#Cave logic
    elif current_location == "cave":
        if choice == "open":
            print("You found the treasure! You win!")
            game_over = True
        elif choice == "leave":
            current_location = "forest"
        else:
            print("Invalid choice. Try again.")
#Dragon logic
    elif current_location == "dragon":
        if choice == "fight":
            if "magic sword" in arsenal:
                print("With the magic sword, you defeated the dragon! You win!")
                game_over = True
            else:
                print("\n💀 You tried to fight barehanded. The dragon defeated you! Game over.")
                game_over = True
        elif choice == "run":
            current_location = "forest"
        else:
            print("Invalid choice. Try again.")
#Hidden path logic
    elif current_location == "hidden_path":
        if "magic sword" not in arsenal:
            arsenal.append("magic sword")
            print("You picked up the magic sword!")
        if choice == "go back to forest":
            current_location = "forest"
        elif choice == "fight dragon":
            print("With the magic sword, you defeated the dragon! You win!")
            game_over = True
        else:
            print("Invalid choice. Try again.")