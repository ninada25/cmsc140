# Lab 2: The Collatz Conjecture - Part 2 (9/22/22)

# Part 2a: Set Range

# create a list to store all lengths of chains:
lengths = [] # https://www.freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python/

counter = 0

for num in range(2, 1001):
    while num > 1:
        if num % 2 == 0: # if the number is even, run this code
            num = num // 2 # bonus
            counter += 1
        elif num % 2 == 1: # if the number is odd, run this code
            num = (3 * num) + 1
            counter += 1
    lengths.append(counter) # add the length of the chain to the list
    counter = 0 # reset counter to 0
print(lengths)

max_value = max(lengths) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
max_index = lengths.index(max_value) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
print("Longest Chain: ", max_index + 2) 
print("Length of Chain: ", max(lengths))

# Part 2b: User-Defined Range

print("Enter a start: ") # ask user to enter a start number
start = int(input())
print("Enter a stop: ") # ask user to enter a stop number
stop = int(input())

# create a list to store all lengths of chains:
lengths_b = []

counter_b = 0

for i in range(start, (stop + 1)): # want to include the number indicated for the stop
    while i > 1:
        if i % 2 == 0: # if i is even, run this code
            i = i // 2 # bonus
            counter_b += 1
        elif i % 2 == 1: # if i is odd, run this code
            i = (3 * i) + 1
            counter_b += 1
    lengths_b.append(counter_b) # add the length of the chain to the list
    counter_b = 0
print(lengths_b) # oops I don't actually need this line?

max_value_b = max(lengths_b) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
max_index_b = lengths_b.index(max_value_b) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
print("Longest Chain: ", max_index_b + 2) 
print("Length of Chain: ", max(lengths_b))