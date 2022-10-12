# Homework 4 - Q1: Indexing (10/13/22)

# Write a function that takes in both of the following lists and returns a list of all the indices where the lists differ:

a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))

def listdiff(list1, list2):
    diff_indexes = [] # create an empty list to store indices where the lists differ
    for i in range(len(list1)):
        if list1[i] != list2[i]: # if at index i, the two lists differ
            diff_indexes.append(i) # add index i to our list called 'diff_indexes'
    return diff_indexes

diff = listdiff(a,b)
print(diff)