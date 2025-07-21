
#text based adventure Game 
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room with two doors.")
    print("One door leads to a dungeon, and the other leads to a treasure room.")
    print("What would you like to do?")
    print("Type 'dungeon' to enter the dungeon or 'treasure' to enter the treasure room.")

def dungeon():
    print("You are in the dungeon. It’s dark, and you can barely see anything.")
    print("There’s a chest in the corner. Do you want to open it? (yes or no)")
    
    choice = input("> ").lower()
    
    if choice == 'yes':
        print("The chest opens, and you find a magical sword!")
        print("Now you can fight the dragon guarding the treasure!")
        fight()
    elif choice == 'no':
        print("You decide not to open the chest and leave the dungeon.")
        main()
    else:
        print("I don't understand that. Please choose 'yes' or 'no'.")
        dungeon()

def treasure_room():
    print("You’re in a room full of glittering gold and jewels.")
    print("A dragon stands guard over the treasure. What do you do?")
    print("You can either fight the dragon with your sword or run away.")
    
    choice = input("> ").lower()
    
    if choice == 'fight':
        print("You fight the dragon and win! You take the treasure and become rich!")
        end_game()
    elif choice == 'run':
        print("You run away from the dragon and escape safely, but you leave the treasure behind.")
        end_game()
    else:
        print("I don't understand that. Please choose 'fight' or 'run'.")
        treasure_room()

def fight():
    print("The dragon approaches. What will you do?")
    print("Type 'attack' to fight or 'defend' to block the attack.")
    
    choice = input("> ").lower()
    
    if choice == 'attack':
        print("You attack the dragon with your sword and defeat it!")
        treasure_room()
    elif choice == 'defend':
        print("You defend yourself, but the dragon overpowers you. You lose the fight.")
        end_game()
    else:
        print("I don't understand that. Please choose 'attack' or 'defend'.")
        fight()

def end_game():
    print("Game over! Would you like to play again? (yes or no)")
    
    choice = input("> ").lower()
    
    if choice == 'yes':
        main()
    elif choice == 'no':
        print("Thanks for playing! Goodbye.")
    else:
        print("I don't understand that. Please choose 'yes' or 'no'.")
        end_game()

def main():
    intro()
    
    while True:
        choice = input("> ").lower()
        
        if choice == 'dungeon':
            dungeon()
            break
        elif choice == 'treasure':
            treasure_room()
            break
        else:
            print("I don't understand that. Please choose 'dungeon' or 'treasure'.")
            main()

if __name__ == "__main__":
    main()
