import random

print ("Welcome to Rock, Paper, Scissors!")

# Define possible choices
wins = {
    "rock": "scissors",      # rock beats scissors
    "paper": "rock",         # paper beats rock
    "scissors": "paper"      # scissors beats paper
}

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
    elif wins[player] == computer:
            print("You win!")
            user_score += 1
    else:
            print("Computer wins!")
            computer_score += 1
    print(f"Score - You: {user_score} vs. Computer: {computer_score}") 
    
    # Check if someone won best of 5
    if user_score == 3:
            print ("You won the best of 5 series!")
            print (f"Final Score - You: {user_score} vs. Computer: {computer_score}")
            break 
    elif computer_score == 3:
            print ("Computer won the best of 5 series!")
            print (f"Final Score - You: {user_score} vs. Computer: {computer_score}")
            break
    play_again = input ("Play again? (y/n):").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break