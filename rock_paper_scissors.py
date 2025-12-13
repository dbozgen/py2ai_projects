import random

print ("Welcome to Rock, Paper, Scissors!")

# Define possible choices
choices = ["rock", "paper", "scissors"]

while True:
    player = input ("Enter your choice (rock, paper, scissors): ").lower()
    if player not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer = random.choice(choices)   

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
            print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"): 
            print("You win!")
    else:
            print("Computer wins!")
    
    play_again = input ("Play again? (y/n):").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break