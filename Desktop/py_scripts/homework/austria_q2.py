# Homework 1 - Q2: A Terrible Number Guesser (9/22/22)

# This program has a variable set to a number. It asks a user for a number between 1 and 10, and prints both numbers. 
# It then asks the user to compare the numbers and see if they guessed correctly.

num = 3 
print("Welcome to the random number guesser.")
print("Please input a number between 1 and 10: ") # ask user to input a number
guess = input() 
print("You chose " + guess + ". The number I chose was " + str(num) + ". Did you guess it?")