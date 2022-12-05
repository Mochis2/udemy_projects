from game_data import data
from art import logo, vs
import random
import os
# Takes account data returns printable format


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_origin = account['country']
    return (f'{account_name}, a {account_description}, from {account_origin}.')


# take users guess and followercount and returns if correct.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Diplay art
print(logo)
# score keeping
score = 0
# making account at pos b the next account at pos a
account_b = random.choice(data)
# make game repeatable
game_keeps_running = True
while game_keeps_running:

    # Generate random acount from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f'A: {format_data(account_a)}')
    print(vs)
    print(f'B: {format_data(account_b)}')

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Not dumb after all! Current Score: {score}.")
    else:
        game_keeps_running = False
        print(f"WRONG! Oh no! A dumb person! Final Score: {score}.")
