# Homework 3 - Q2: A Functional Random Number Guesser (10/06/22)

# Add the following functionality to last week's random number guesser:
# 1. The number guesser script should generate its own random number. (Hint: use the random module.)
# 2. The number guesser should be a function, random_number_guesser(), which takes a single argument: the number of guesses a user has available.
# 3. The user should input the number of guesses they want to take.
# 4. The number guesser should tell the user how many guesses are left each time they guess a new number.
# 5. If the user runs out of guesses, the number generator should stop and tell them sorry, but they lost, and print the correct number.

import random

num = random.randint(1, 100) # assign a random int in the range [1,100] to the variable 'num'

def random_number_guesser(number_guesses):
        print("How many guesses?:")
        number_guesses = int(input())
        print("Welcome to the random number guesser.")

        while True:
            if(number_guesses >= 1):
                print("Please input a number between 1 and 100: ") # ask user to input a number
                guess = input()
            
                if int(guess) > num:
                    number_guesses -= 1
                    print(guess + " is too high. Try again (" + str(number_guesses) + " guesses left):")
                elif int(guess) < num:
                    number_guesses -= 1
                    print(guess + " is too low. Try again (" + str(number_guesses) + " guesses left):")
                else:
                    print("Yes! " + guess + " is the correct number.")
                    #break
                    exit()
            else:
                print("Sorry, you lost. The correct number was " + str(num) + ".")
                break

random_number_guesser(7)
