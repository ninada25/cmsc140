# Homework 3 - Q1: Collatz Conjecture (Redux) (10/06/22)

# Write function called longest_collatz() that:
# Takes in two numbers, start and stop from the user.
# Returns (NOT prints) the number that the longest chain in that range started from
# Note that you are not printing the length of the longest chain, only the number it originated from.

def longest_collatz(start, stop):
    lengths = [] # create a list to store all lengths of chains
    counter = 0
    for i in range(start, (stop + 1)): # want to include the number indicated for the stop
        while i > 1:
            if i % 2 == 0: # if i is even, run this code
                i = i // 2 # bonus
                counter += 1
            elif i % 2 == 1: # if i is odd, run this code
                i = (3 * i) + 1
                counter += 1
        lengths.append(counter) # add the length of the chain to the list
        counter = 0
    max_value = max(lengths) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
    max_index = lengths.index(max_value) # https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
    chain_from = max_index + start # add 'start' to 'max_index_b' to reflect proper index
    return "Longest Chain is from: " + str(chain_from) 
    
print(longest_collatz(1,100))