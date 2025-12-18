import random

print ("Welcome to Rock, Paper, Scissors!")

# Define possible choices
choices = ["rock", "paper", "scissors"]

#scores 

user_score = 0
computer_score = 0

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
            user_score += 1
    else:
            print("Computer wins!")
            computer_score += 1
    print(f"Score - You: {user_score} vs. Computer: {computer_score}")        
    play_again = input ("Play again? (y/n):").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        print (f"Final Score - You: {user_score} vs. Computer: {computer_score}")
        break