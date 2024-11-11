#Guess play

import random

def w_word():
    words = ['apple', 'banana', 'orange', 'grape', 'peach', 'lemon', 'strawberry', 'blueberry', 'watermelon', 'kiwi']
    word = random.choice(words)
    return word

def guess_play():
    print(f'Welcome to Guess Play! Guess the fruit! {w_word()}')
    number_of_guesses = 0
    
    while True:
        if number_of_guesses < 4:
            guess = input('Guess a fruit: ')
          
            if guess == w_word():
                print('Correct!')
                continue_play = input('Do you want to play again? (yes/no): ')
                if continue_play.lower() == 'yes':
                    word = random.choice(words)
                    print(word)
                    number_of_guesses = 0
                    continue
                else:
                    break   
            else:
                print('Incorrect. Try again!')
                number_of_guesses += 1   
        else:
            print('Game over!')
            break 

guess_play()