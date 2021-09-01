from game_data import data
from art import logo,vs
import random


def format_account(account):
    return (f"{account['name']}, {account['description']}, from {account['country']}")


def check(guess, a_follows, b_follows):

    if a_follows > b_follows:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    a = format_account(account_a)
    b = format_account(account_b)
    print(f'Account A: {a}')
    print(vs)
    print(f'Account B: {b}')
    a_follows = account_a['follower_count']
    b_follows = account_b['follower_count']
    guess = input("Who was more follows? Type 'a' or 'b'\n").lower()
    is_correct = check(guess,a_follows,b_follows)

    if is_correct == True:
        score += 1
        print(f"You're right! current score {score}")
    else:
        game_should_continue = False
        print(f"Wrong! final score {score}")

