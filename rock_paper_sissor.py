#rock paper sissor

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()
