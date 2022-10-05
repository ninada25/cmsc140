# Lab 3 (9/29/22)

# Q1 - Adding Up:
# Write a function that calculates the sum of every number between two numbers. 
# When called, the function should return the sum. 

def my_sum(start, stop):
    sum = 0
    for num in range(start, (stop + 1)): # since the stop is exclusive, I set it to (stop + 1)
        sum = sum + num
    return sum

a = my_sum(10,15)
print(a)


# Q2 - Counting Down:

# Write a function that takes in two numbers. 
# The first number is the number to start from; the second number is the number to count down by. 
# When called, the function should print the countdown, and don’t output any numbers below 0. 

def countdown(start_from, count_down_by):
    for i in range(start_from, -1, -count_down_by): # the stop is exclusive, so I set it to -1
        print(i)

print("Countdown:")
countdown(18,3)

print("Countdown:")
countdown(18,4)


# Q3 - Putting it Together:

# Now, write a function that does the following:
# Asks the user which of the above two functions they would like to call.
# When they select their function, ask them for the appropriate input for each function.
# Run the functions with their inputs and print the result.

def function_chooser():
    print("Welcome to the function chooser. Please choose a function.") # prompt user to choose a function
    print("1 = Cumulative Sum")
    print("2 = Countdown")
    choice = int(input())
   # print("Your choice: {" + str(choice) + "}") # tell user which function they chose
    if choice == 1:
        print("Please enter first number: ") # prompt user to enter a first number
        start = int(input())
        print("Please enter final number: ") # prompt user to enter a final number
        stop = int(input())
        a = my_sum(start, stop)
        print(a)
    elif choice == 2:
        print("Please enter a start number: ") # prompt user to enter a start number
        start_from = int(input())
        print("Please enter a number to count by: ") # prompt user to enter a number to count by
        count_down_by = int(input())
        countdown(start_from, count_down_by)

function_chooser()

# Notes for revision:
# Remember for Mastery credit, you shouldn't print anything before the function chooser is called. 
# You should remove your earlier print statements and function calls for Mastery credit.