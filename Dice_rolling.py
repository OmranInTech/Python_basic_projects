#Dice_rolling Game
import random

def roll_dice():
    # Generate a random number between 1 and 6 (representing a die roll)
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")

def main():
    while True:
        user_input = input("Press Enter to roll the dice, or type 'exit' to quit: ").strip().lower()
        
        if user_input == "exit":
            print("Thanks for playing!")
            break
        elif user_input == "":
            roll_dice()
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
