# Homework 4 - Q3: Our Old Friend Random Number Guesser (10/13/22)

# Here is the new functionality you should add:

# Store the user’s past guesses in a list
# When the guessing game ends (either in failure or success), print out the average of all of their guesses.

import random

def random_number_guesser(number_guesses): # my function takes a single argument: the number of guesses a user has available
    all_guesses = [] # create an empty list that will store all the user's past guesses

    num = random.randint(1,100) # generate a random number in the range [1,100]
    print("Welcome to the random number guesser.")
    print("Please input a number between 1 and 100: ") # ask user to input a number

    while number_guesses != 1: # while number of guesses is not 1
        guess = input() 
        all_guesses.append(int(guess)) # add guess to list of all user's past guesses
        avg_guess = sum(all_guesses)/len(all_guesses) # calculate average of all guesses and store in avg_guess

        number_guesses -= 1 # number_guesses = number_guesses - 1
        
        if int(guess) > num: # if the number the user guesses is higher than the chosen number
            print(guess + " is too high. Try again (" + str(number_guesses) + " guesses left):")
        elif int(guess) < num: # if the number the user guesses is lower than the chosen number
            print(guess + " is too low. Try again (" + str(number_guesses) + " guesses left):")
        else: # if the user guesses correctly
            print("Yes! " + guess + " is the correct number.")
            print("The average of all your guesses was " + str(avg_guess) + ".")
            break

    if number_guesses == 1: # once the user is at their final guess, run this code
     #   print("Please input a number between 1 and 100: ") # ask user to input a number
        guess = input() 
        all_guesses.append(int(guess)) # add guess to list of all user's past guesses
        avg_guess = sum(all_guesses)/len(all_guesses) # calculate average of all guesses and store in avg_guess

        number_guesses -= 1
        
        if int(guess) > num: # if the number the user guesses is higher than the chosen number
            print("Sorry, you lost. The correct number was " + str(num) + ".")
            print("The average of all your guesses was " + str(avg_guess) + ".")
            exit()
        elif int(guess) < num: # if the number the user guesses is lower than the chosen number
            print("Sorry, you lost. The correct number was " + str(num) + ".")
            print("The average of all your guesses was " + str(avg_guess) + ".")
            exit()
        else: # if the user guesses correctly
            print("Yes! " + guess + " is the correct number.")
            print("The average of all your guesses was " + str(avg_guess) + ".")
            exit()

print("How many guesses?:") # ask user to input the number of guesses they want to take
input_number_guesses = int(input()) 
a = random_number_guesser(input_number_guesses)
print(a)