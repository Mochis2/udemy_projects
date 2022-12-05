from art1 import logo
import random

print(logo)
# need a number between 1- 100
print('Welcome to the Guessing Game!')
print('Im thinking of a number between 1 and 100.')
RANDOM_NUMBER = random.randint(1, 100)

DIFF_OPERATOR = input('Choose a difficulty. Type "easy" or "hard": ').lower()
if DIFF_OPERATOR == 'hard':
    print('You have 5 attempts remaining to guess the number')
elif DIFF_OPERATOR == 'easy':
    print('You have 10 attempts remaining to guess the number')
else:
    print('Invalid input')
    quit()
# input where i can guess
USER_GUESS = int(input('Make a guess: '))






# check if the answer is correct
def check_answer(guess, correct_number, difficulty):
    attempts = 0
# a difficulty easy = 10 attemps, hard = 5 attemps
## difficulty setting
    if difficulty == 'hard':
        attempts = 5
    if difficulty == 'easy':
        attempts = 10
    
# while attempts are above 1 you can guess 
    while attempts > 1:
    
        if guess > correct_number:
            attempts -= 1
            print('Too high.')
            print('Guess again')
            print(f'You have {attempts} attempts remaining to guess the number')
            next_guess = int(input('Make a guess: '))
            guess = next_guess
            
        elif guess < correct_number:
            attempts -= 1
            print('Too low.')
            print('Guess again')
            print(f'You have {attempts} attempts remaining to guess the number')
            next_guess = int(input('Make a guess: '))
            guess = next_guess
            
        elif guess == correct_number:
            print('You got it! Lucky mfer. Here have a cookie: 🍪 ')
            quit()
            
    print('NO! LOSER!')
    print("You've run out of guesses, you lose.")

check_answer(USER_GUESS, RANDOM_NUMBER, DIFF_OPERATOR)


    
## check if it is too high or too low