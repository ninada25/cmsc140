# Final Project: A Wordle Game! (11/2/2022)

import random
from pathlib import Path

filepath = Path("data") / "words.txt" # to ensure compatability for all devices

def choose_word(): # function for randomly choosing a word from the 'words.txt' file
    with open("words.txt") as f:
        word = f.read().splitlines()
        return random.choice(word) # return a random word from the file

def wordle_game():
    chosen_word = choose_word()
    # print(chosen_word) # used this line to test code
    number_guesses_remaining = 10 # give user 10 chances to guess the correct word
    number_correct_position = 0
    number_incorrect_position = 0
    total_number_guesses = 0
    previous_guesses = [] # create an empty list for storing user's guesses

    print("Welcome to Wordle! Please enter a 5-letter word.")

    while number_guesses_remaining != 1:
        guess = input().lower()

        previous_guesses.append(guess) # add guess to list of guesses
        number_guesses_remaining -= 1 # number_guesses_remaining = number_guesses_remaining - 1
        total_number_guesses += 1 # total_number_guesses = total_number_guesses + 1

        if guess.isalpha(): # if user enters a word (with only alphabet letters)
            if len(guess) == 5: # if user enters a word of length 5
                if guess != chosen_word: # if user guesses word incorrectly
                    for i in range(0,5):
                        if guess[i] == chosen_word[i]: # if letter is in the correct position
                            number_correct_position += 1
                        elif guess[i] in chosen_word: # if letter is in the word, but in the wrong position
                            number_incorrect_position += 1
                    print(f"Number of letters in the right position: {number_correct_position}\nNumber of letters in the wrong position: {number_incorrect_position}")
                    print(f"Guess again ({number_guesses_remaining} guesses left). You've already guessed the following: {previous_guesses}")
                    number_correct_position = 0 # reset to 0
                    number_incorrect_position = 0 # reset to 0
                else: # if user guesses word correctly
                    print(f"Good job -- {chosen_word} is the right word! It took you {total_number_guesses} guesses to get the word.")
                    exit()
            else: # if user enters a word that is not of length 5
                print(f"You have chosen a word that is not 5 letters. Guess again ({number_guesses_remaining} guesses left). You've already guessed the following: {previous_guesses}")
        else: # if user inputs characters other than alphabet letters
            print(f"Your input contains characters other than alphabet letters. Please enter a 5-letter word ({number_guesses_remaining} guesses left). You've already guessed the following: {previous_guesses}")

    if number_guesses_remaining == 1: # once the user is at their final guess, run this code
        guess = input().lower()

        total_number_guesses += 1 # total_number_guesses = total_number_guesses + 1

        if guess.isalpha(): # if user enters a word (with only alphabet letters)
            if len(guess) == 5: # if user enters a word of length 5
                if guess != chosen_word: # if user guesses word incorrectly
                    for i in range(0,5):
                        if guess[i] == chosen_word[i]: # if letter is in the correct position
                            number_correct_position += 1
                        elif guess[i] in chosen_word: # if letter is in the word, but in the wrong position
                            number_incorrect_position += 1
                    print(f"Number of letters in the right position: {number_correct_position}\nNumber of letters in the wrong position: {number_incorrect_position}")
                    print(f"Sorry, you lost. The correct word was {chosen_word}.")
                    exit()
                else: # if user guesses word correctly
                    print(f"Good job -- {chosen_word} is the right word! It took you {total_number_guesses} guesses to get the word.")
                    exit()
            else: # if user enters a word that is not of length 5
                print(f"Sorry, you lost. You entered a word that is not 5 letters. The correct word was {chosen_word}.")
                exit()
        else: # if user inputs characters other than alphabet letters
            print(f"Sorry, you lost. Your input contained characters other than alphabet letters. The correct word was {chosen_word}.")
            exit()

wordle_game()