#Number Guessing Game 
import random

def random_number():
    secret_number=random.randint(1,100)
    attemp=0

    while True:
        
        user_guess=int(input('Guess a number between 1 to 100 : '))
        attemp +=1

        if user_guess >100 or user_guess<1:
            print('Enter A number in range .')
        elif user_guess > secret_number:
            print('Too high')
        elif user_guess <secret_number:
            print('Too low !')
        elif user_guess == secret_number:
            print(f'Congratulation you guessed the correct number in {attemp} . ')
        else:
            print('incorrect attempt ')
            break
#call the function
                
random_number()
