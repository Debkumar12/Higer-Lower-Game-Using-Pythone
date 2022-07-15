"""My self Deb Kumar Das a small devoloper just starting learning pythone and currently exploring stuffs and making small projects,Hope you all enjoy this very well known game"""

import os
from data import data
from logo import logo, versus
import random

def clear():
   
    os.system('clear')


def game():
    print(logo)
    score = 0
    first_acc = random.choice(data)

    game_over = False
    while not game_over:
        print(f'Current score: {score}\n')
        print('Which social media account has more followers?')

        second_acc = random.choice(data)

        if first_acc == second_acc:
            second_acc = random.choice(data)
        else:
            print(f"{first_acc['name']}, a {first_acc['description']}, from {first_acc['country']}")
            print(versus)
            print(f"{second_acc['name']}, a {second_acc['description']}, from {second_acc['country']}")

       
        guess = input('Is it "A" or "B"? ').upper()
        clear()
        print(logo)

       
        A = first_acc["follower_count"]
        B = second_acc["follower_count"]
          
              
   
        if guess == 'A' and A > B:
            print(f'Correct, {first_acc["name"]} has more followers.')
            score += 1
            guess_data = first_acc
            first_acc = guess_data
        elif guess == 'A' and B > A:
            print(f'Wrong, {second_acc["name"]} has more followers.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        elif guess == 'B' and A < B:
            print(f'Correct, {second_acc["name"]} has more followers.')
            score += 1
         
            guess_data = second_acc
            first_acc = guess_data
        elif guess == 'B' and A > B:
            print(f'Wrong, {first_acc["name"]} has more followers.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        else:
            print('OOps! Invalid guess. Restart the game...')
            score = 0


game()