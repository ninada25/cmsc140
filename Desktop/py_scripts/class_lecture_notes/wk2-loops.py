# Wednesday, September 21 Lecture Notes:

# while loops

classcode = "CMSC 140"
if classcode == "CMSC 140":
    print("Welcome to class!")

# this is basically an if statement
while classcode == "CMSC 140":
    print("Welcome to class!")
    classcode = "CMSC 150" # change the code so the loop ends

print("The while loop is over.")
print(classcode)

times_through = 0
if times_through < 5:
    times_through = times_through + 1
    print("This has executed " + str(times_through) + " times.")
print("times_through:", times_through)

times_through = 0
while times_through < 5:
    times_through = times_through + 1
    print("This has executed " + str(times_through) + " times.")
print("times_through:", times_through)

print("New while loop: ")

num = 1120
# How many times can you cut this num in half and get a number bigger than 1?
while num > 1:
    num = num//2 # double division is integer division. This is not automatic in Python.
    print("Number: ", num)


# In-class exercise 1 (Log Base 2 Algorithm, expanding on the loop above (extremely common in CS))):

print("Please enter a number: ")
num = int(input())
counter = 0
# run loop until num is no longer > 1
while num > 1:
    num = num//2
    counter = counter + 1 # alternatively: counter += 1
    print("Number: ", num, "Counter: ", counter)

# for loops
print("For Loop: ")
for times_through_for in range(5): # notice we didn't even need to initialize / declare our variable outside the for statement
    print("This has executed " + str(times_through_for) + " times.")
print("times_through:", times_through_for) # notice that range(5) means the range from 0 to 4, python is 0-indexed, R is 1-indexed

for i in range(10):
    print(str(i) + " squared is " + str(i**2))

i = 0
while i < 10:
    print(str(i) + " squared is " + str(i**2))
    i += 1 # shorthand for i = i + 1

# In-class exercise 2: Write a loop that prints every even number from 0 to 1000. (Can use a for or while loop!)

# using while loop:
i = 0
while i <= 1000:
    print(i)
    i = i + 2

# using step in range:
for even_num in range(0,1001,2):
    print(even_num)

# using modulo:
for i in range(1001):
    if i % 2 == 0: # checks if the number is even
        print(i)