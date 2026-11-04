
import random


def get_feedback(target, guess, max_range):
    diff = abs(target - guess)

    if diff == 0:
        return "Correct!"

    if guess < target:
        direction = "Too low!"
    else:
        direction = "Too high!"

    if max_range <= 10:
        if diff == 1:
            distance = "Very close!"
        elif diff <= 3:
            distance = "Close!"
        elif diff <= 5:
            distance = "Far!"
        else:
            distance = "Very far!"
    else:
        if diff <= max(1, max_range * 0.05):
            distance = "Very close!"
        elif diff <= max(3, max_range * 0.15):
            distance = "Close!"
        elif diff <= max(5, max_range * 0.30):
            distance = "Far!"
        else:
            distance = "Very far!"

    return f"{direction} {distance}"


def play_level(level):
    levels = {
        1: (10, 5),
        2: (50, 7),
        3: (100, 10)
    }

    if level not in levels:
        print("Invalid level selected.")
        return

    max_val, max_attempts = levels[level]
    target = random.randint(1, max_val)
    attempts = 0

    print(f"\n--- Level {level} ---")
    print(f"Guess a number between 1 and {max_val}")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            user_input = input("Enter your guess: ").strip()

            if not user_input:
                print("Input cannot be empty.")
                continue

            guess = int(user_input)

            if guess < 1 or guess > max_val:
                print(f"Enter a number between 1 and {max_val}.")
                continue

            attempts += 1

            if guess == target:
                print(
                    f"\nCongratulations! You guessed {target} "
                    f"in {attempts} attempts."
                )
                return

            print(get_feedback(target, guess, max_val))
            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\nGame over! The correct number was {target}.")


def main():
    print("================================")
    print("   RANDOM NUMBER GUESSING GAME")
    print("================================")

    while True:
        print("\nSelect a Difficulty Level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        print("q. Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice in ("1", "2", "3"):
            play_level(int(choice))
        elif choice == "q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    while True:
        main()

        again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if again != "y":
            print("See you next time!")
            break
