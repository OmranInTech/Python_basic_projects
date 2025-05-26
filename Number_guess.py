import random


def number_guessing_game() -> None:
    """
    Starts a number guessing game where the user tries to guess
    a randomly generated number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            user_guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("❗ Please enter a number within the range of 1 to 100.\n")
            elif user_guess > secret_number:
                print("📈 Too high! Try again.\n")
            elif user_guess < secret_number:
                print("📉 Too low! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.\n")
                break
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number.\n")


# Start the game
if __name__ == "__main__":
    number_guessing_game()
