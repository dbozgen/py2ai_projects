# 1. Computer picks a random number (1-100)
# 2. User guesses
# 3. Computer says "too high" or "too low"
# 4. Repeat until user guesses correctly
# 5. Show how many tries it took
# 6. Ask if they want to play again

import random

while True:
        number_to_guess = random.randint(1, 100)
        tries = 0   
        while True:
                user_number = int(input ("Guess a number between 1 and 100: "))
                tries += 1
                if user_number < number_to_guess: 
                        print(f"Too low!")
                elif user_number > number_to_guess:
                        print(f"Too high!")
                else:
                        print(f"Amazing! You guessed it in {tries} tries.")
                        break    
        play_again = (input ('Play again? (y/n): ').lower())
        if play_again != 'y':
                print ("Thanks for playing!")
                break