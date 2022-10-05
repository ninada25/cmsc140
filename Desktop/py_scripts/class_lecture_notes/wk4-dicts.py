# Wednesday, October 5 Lecture Notes:

profs = ["Ackles", "Krebsbach", "Gregg"]

for prof in profs: # we can have anything instead of 'prof'
    print(prof + " is a CMSC professor.")

for i, prof in enumerate(profs): # one option for including both index and value in output: enumerate! prof prefers this
    print(str(i) + " " + prof + " is a CMCS professor.")

for i in range(len(profs)): # alternatively, using range of length AND index the list
    print(str(i) + " " + profs[i] + ' is a CMSC professor.')

profs.append("Sage")
print(profs)

profs.remove("Sage")
print(profs)

## Dictionaries

prof_offices = { # spacing doesn't change how it's run, but now code is more readable
    "Ackles" : "Steitz 131", 
    "Krebsbach" : "Briggs 411", 
    "Gregg" : "Briggs 413"
    }
print(prof_offices)
print(prof_offices["Ackles"])

print(prof_offices.keys()) # print all the keys in the dictionary, keys() is a func that works on dictionaries
print(prof_offices.values()) # print all the values in the dictionary, values() is a func that works on dictionaries

for name in prof_offices.keys():
    print(name)
    
for office in prof_offices.values():
    print(office)

for name, office in prof_offices.items(): # you need the .items() !!!
    print(name + " is in " + office)

########################################################
# In-class exercise 1

# Turn the following into key-value pairs in a dictionary called practice_dict. 
# Then, complete this for loop to print out the keys and the values.

practice_dict = {5 : 20 , 2 : "Hello" , "Hello" : 5}
for key, value in practice_dict.items():
    print("Key is:", key, " Value is:", value)

########################################################

prof_offices["Sage"] = "Briggs 417"
print(prof_offices)

# prof_offices["Ackles"] = "the moon"
# print(prof_offices)

# prof_offices[0] will give an error

# Key word "in" for seeing whether something is in a dictionary

print("Ackles" in prof_offices.keys())
print("Ackles" in prof_offices) # prof_offices is a shortcut for prof_offices.keys()
print("Steitz 131" in prof_offices) # false
print("Steitz 131" in prof_offices.values()) # true
print("Sattler" not in prof_offices)

if "Corry" in prof_offices:
    print("Already added.")
else:
    prof_offices["Corry"] = "needs an office"
print(prof_offices)

# alternatively:
if "Corry" not in prof_offices:
    prof_offices["Corry"] = "needs an office"

# Using Lists as Values
prof_classes = {
    "Ackles" : ["Intro Python", "Algorithms"], 
    "Krebsbach" : ["Intro Java", "First Year Studies"],
    "Gregg" : ["Web Development", "Algorithms"]
}

for name, classes in prof_classes.items():
    print("Name: ", name, "Classes: ", classes)

for name, classes in prof_classes.items():
    print("Name: ", name)
    for classname in classes:
        print(classname)

# Nesting Dictionaries

prof_info = {
    "Ackles" : {
        "classes":["Python", "Algorithms"],
        "office": "Steitz 131"
        },
    "Krebsbach" : {
        "classes":["Java", "FYS"],
        "office": "Briggs 411"
        },
    "Gregg" : {
        "classes":["Web Devel","Algorithms"],
        "office": "Briggs 413"
        }
    }

# access with nested indices
print(prof_info["Ackles"]["office"])

########################################################
# In-class exercise 2

# Write a program that iterates through the list shopping_needs and for every item does the following (iterate means go through each one):

# If the item in the dictionary fridge, print how many are in there (its value), for example, “You already have ITEMNUMBER ITEMNAME.”
# If the item is not in the dictionary fridge, print something like “ITEMNAME is not in the fridge.”

fridge = {
    "eggs" : 12,
    "milk" : 1,
    "cheese" : 2,
    "bread" : 3,
    "pizza" : 0.5
}

shopping_needs = ["eggs", "fruit", "milk", "juice"]

for item in shopping_needs:
    if item in fridge: # fridge is shorthand for fridge.keys()
        print("You already have ", fridge[item], item, ".") # fridge[item] grabs the value of item
    else:
        print(item, " is not in fridge.")