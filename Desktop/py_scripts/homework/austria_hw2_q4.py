# Homework 2 - Q4: A Better Random Number Guesser (9/29/22)

# Update your random number guesser from last week to do the following:
# 1. The number you chose should be between 1 and 100.
# 2. If the number the user guesses is higher than the chosen number, say "Too high."
# 3. If the number the user guesses is lower than the chosen number, say "Too low."
# 4. If the user does guess the number, it should say congrats, and end the program. 
# 5. If the user doesn't guess the number, it should prompt them to guess again. 

import random

num = random.randint(1, 100) # assign a random int in the range [1,100] to the variable 'num'
print("Welcome to the random number guesser.")

while True:
    print("Please input a number between 1 and 100: ") # ask user to input a number
    guess = input() 

    if int(guess) > num:
        print(guess + " is too high. Try again:")
    elif int(guess) < num:
        print(guess + " is too low. Try again:")
    else:
        print("Yes! " + guess + " is the correct number.")
        break