# Monday, October 3 Lecture Notes:

### Lists!

a = 4
b = 5
c = 2
d = 100
e = 29485020

my_list = [4,5,2,100,29485020]
print(my_list)

pet_names = ["Peanut", "Napoleon", "Llewyn", "Juniper", "Spike"]
mixed_list = [2, "string_ex", True, 2.4958]
print(pet_names)
print(mixed_list)

# Indexing
a = pet_names[0] # strings start at 0, just like ranges!
b = pet_names[3]
print(a, b)

c = pet_names[-1] # going backwards, it's not zero indexed since -0 is still 0
print(c) 

# Slices of a list
cats = pet_names[0:3] # slices are not inclusive, just like ranges
other_animals = pet_names[3:] # from some index to the end
print(cats)
print(other_animals)

############################################################################################################

# In-class exercise 1: Write a list that contains the names of all the classes you're taking this term. Print the second value in the list (not index 2!).

fall_classes = ["CMSC 140", "MATH 340", "ENG 180"]
print(fall_classes[1])

# In-class exercise 2: Take the same list from above, and replace intro Python with a fake class name. Any class you like. Maybe "Advanced Sleeping".
fall_classes[0] = "Piano for Athletes"
print(fall_classes)

############################################################################################################

a = "Hello"
print(a)
a = "Goodbye"
print(a)

pet_names[0] = "Baby"
print(pet_names)
pet_names[1] = pet_names[0] # changing one part of the list to another part of the list
print(pet_names)

list_a = [1,2,3]
list_b = ['x','y','z']
final_list = list_b + list_a
print(final_list)

numbers = []
for i in range(5): # this only goes up to 4
    numbers = numbers + [i] # can only concatenate lists to lists, not strings to lists
    print(numbers)

for item in final_list:
    print(item)

nums = [1,2,3,4,5]
for i in nums:
    print("Square of", i, "is", i**2)

############################################################################################################

# In-class exercise 3:
# 1. Create a list of 20 random numbers between 1 and 100 using the random module. (Hint: You will also need a loop.) 
# 2. Using that list, create a new list which consists of the square root of each of those numbers from the first list.

# Part 1
import random, math

list_3 = []
for i in range(20):
    list_3 += [random.randint(1,100)]

print(list_3)  

# Part 2
sq_root_list_3 = [] # create empty list
for i in range(len(list_3)):
    sq_root_list_3 += [math.sqrt(list_3[i])]

print(sq_root_list_3)

############################################################################################################

numbers = []
example_list = []
for _ in range(20): # since I'm not going to use this iterator, I don't need to have one
    # numbers = numbers + [random.randint(0,100)]
    numbers.append(random.randint(0,100)) # changes the list itself in place. lists are mutable! 
    example_list.append(i)
print(numbers)
print(example_list)

# Sorting a list
numbers.sort()
print(numbers)

# If you want a list of a certain size (say 20):
list_size = [0] * 20
print(list_size)

# Enumerating each element of your list
print(pet_names)

for i, name in enumerate(pet_names):
    print(i, name)