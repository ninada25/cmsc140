# Homework 2 - Q2: Counting Down (9/29/22)

# Write a program that asks the user to input a number to start with. 
# Then ask them to input a second number to count down by. 
# Output the countdown, and don’t output any numbers below 0. 

print("Please enter a number to start from: ")
start_from = int(input())
print("Please enter how much to count down by: ")
count_down_by = int(input())

# for loop
for i in range(start_from, -1, -count_down_by):
    print(i)