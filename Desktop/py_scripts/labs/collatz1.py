# Lab 2: The Collatz Conjecture - Part 1 (9/22/22)

# Consider the following operations on any positive integer:
# If the number is even, divide it by two
# If the number is odd, multiply it by three and add one
# Repeat these steps by taking the output as the new input

# The conjecture states that no matter what integer you choose as your starting value, you will end up at 1.

print("Enter a number: ") # ask user to input a number
num = int(input())
counter = 0

while num > 1:
    if num % 2 == 0: # if the number is even, run this code
        num = num // 2 # bonus
        print("Div by 2: ", num)
        counter += 1
    elif num % 2 == 1: # if the number is odd, run this code
        num = (3 * num) + 1
        print("Times 3 Plus 1: ", num)
        counter += 1
print("Length of Chain: ", counter)