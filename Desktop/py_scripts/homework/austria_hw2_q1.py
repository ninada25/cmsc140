# Homework 2 - Q1: Adding Up (9/29/22)

# Write a while loop that calculates the sum of every number from 1 to 1000. Write a for loop that does the same.

# while loop
num = 1
sum = 0
while num <= 1000:
    sum = sum + num
    num += 1
print(sum)

# for loop
sum = 0
for num in range(1, 1001):
    sum = sum + num
print(sum)