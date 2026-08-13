# It is simple rock paper sissor game devlop using python.
# I created this game when i was learning Python at my collage.

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")
    
    choices = ['rock', 'paper', 'scissors']
    
    # Track scores
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("\nYour choice: ").lower().strip()
        
        if user_choice == 'quit':
            print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        if user_choice not in choices:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 🤖")
            computer_score += 1
            
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
