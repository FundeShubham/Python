# It is simple Guess The Number game devlop using python.
# I created this game when i was learning Python at my collage.

import random
import sys

def get_feedback(target, guess, max_range):
    diff = abs(target - guess)
    
    if diff == 0:
        return "Correct!"
    
    # Adjust thresholds based on range size for better playability
    if max_range <= 10:
        if diff == 1:
            return "Very Close!"
        elif diff <= 3:
            return "Close"
        elif diff <= 5:
            return "Far"
        else:
            return "Very Far"
    else:
        # Percentage based for larger ranges
        if diff <= max(1, max_range * 0.05): # Within 5%
            return "Very Close!"
        elif diff <= max(3, max_range * 0.15): # Within 15%
            return "Close"
        elif diff <= max(5, max_range * 0.30): # Within 30%
            return "Far"
        else:
            return "Very Far"

def play_level(level):
    if level == 1:
        max_val = 10
    elif level == 2:
        max_val = 50
    elif level == 3:
        max_val = 100
    else:
        print("Invalid level selected.")
        return

    print(f"\n--- Level {level} ---")
    print(f"Guess a number between 1 and {max_val}")
    
    target = random.randint(1, max_val)
    attempts = 0
    
    while True:
        try:
            user_input = input("Enter your guess: ")
            if not user_input.strip(): # Handle empty input
                continue
                
            guess = int(user_input)
            attempts += 1
            
            if guess < 1 or guess > max_val:
                print(f"Please enter a number between 1 and {max_val}.")
                continue
            
            if guess == target:
                print(f"Congratulations! You guessed the number {target} in {attempts} attempts.")
                break
            else:
                feedback = get_feedback(target, guess, max_val)
        
                print(f"{feedback}")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Random Number Guessing Game!")
    
    while True:
        print("\nSelect a Difficulty Level:")
        print("1. Level 1 (1-10)")
        print("2. Level 2 (1-50)")
        print("3. Level 3 (1-100)")
        print("q. Quit")
        
        choice = input("Enter choice (1/2/3/q): ").strip().lower()
        
        if choice == '1':
            play_level(1)
        elif choice == '2':
            play_level(2)
        elif choice == '3':
            play_level(3)
        elif choice == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
