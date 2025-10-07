from hangman_art import HANGMANPICS
from hangman_words import words
from logo import logo

import random

def check_guess_present_and_update_states(secret_word: str, placeholder: list):
    is_present = False
    
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            placeholder[i] = guess
            is_present = True
            
    return is_present
            

secret_word = random.choice(words)

placeholder = ['_' for _ in range(len(secret_word))]


is_game_over = False
count_errors = 0

max_errors = len(HANGMANPICS)

print(logo)

while not is_game_over:
    print(f"****************** {max_errors - count_errors - 1} LIVES LEFT **************************")
    print(HANGMANPICS[count_errors])
    
    print(" ".join(placeholder))

    guess = input("Guess a letter: ").lower()

    hint = check_guess_present_and_update_states(secret_word, placeholder)
    
    if not hint:
        count_errors += 1
    
    print(' '.join(placeholder))
    
    word_formed = ''.join(placeholder)
        
    if count_errors == max_errors - 1:
        print(HANGMANPICS[count_errors])
        print(f"SECRET WORD WAS: {secret_word}")
        print("*****************YOU LOSE*****************")
        is_game_over = True
    
    if word_formed == secret_word:
        print("*****************YOU WIN*****************")
        is_game_over = True