# Homework 3 - Q2: A Functional Random Number Guesser (10/06/22)

# Add the following functionality to last week's random number guesser:
# 1. The number guesser script should generate its own random number. (Hint: use the random module.)
# 2. The number guesser should be a function, random_number_guesser(), which takes a single argument: the number of guesses a user has available.
# 3. The user should input the number of guesses they want to take.
# 4. The number guesser should tell the user how many guesses are left each time they guess a new number.
# 5. If the user runs out of guesses, the number generator should stop and tell them sorry, but they lost, and print the correct number.

import random

def random_number_guesser(number_guesses):
    num = random.randint(1,100) # generate a random number in the range [1,100]
    print("How many guesses?:") # ask user to input the number of guesses they want to take
    number_guesses = int(input())

    print("Please input a number between 1 and 100: ") # ask user to input a number

    while number_guesses != 1: # while number of guesses is not 1
        guess = input() 

        number_guesses -= 1 # number_guesses = number_guesses - 1
        
        if int(guess) > num: # if the number the user guesses is higher than the chosen number
            print(guess + " is too high. Try again (" + str(number_guesses) + " guesses left):")
        elif int(guess) < num: # if the number the user guesses is lower than the chosen number
            print(guess + " is too low. Try again (" + str(number_guesses) + " guesses left):")
        else: # if the user guesses correctly
            print("Yes! " + guess + " is the correct number.")
            break

    if number_guesses == 1: # once the user is at their final guess, run this code
     #   print("Please input a number between 1 and 100: ") # ask user to input a number
        guess = input() 

        number_guesses -= 1
        
        if int(guess) > num: # if the number the user guesses is higher than the chosen number
            print("Sorry, you lost. The correct number was " + str(num) + ".")
        elif int(guess) < num: # if the number the user guesses is lower than the chosen number
            print("Sorry, you lost. The correct number was " + str(num) + ".")
        else: # if the user guesses correctly
            print("Yes! " + guess + " is the correct number.")
            exit()

random_number_guesser(3) # question for Dr. Ackles: isn't it redundant to have the function take in an argument that is the number of guesses a user has 