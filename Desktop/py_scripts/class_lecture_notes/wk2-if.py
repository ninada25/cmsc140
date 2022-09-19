""" # Monday, Sept. 19, 2022

my_number = 7
my_string = "CMSC 140"
my_bool = True

#and
print(True and True)
print(True and False)
print(False and False)

#or
print("T or T", True or True)
print("T or F", True or False)

#not
print("not T", not True)
print("not F", not False)

print(True and not (True or False))

## Comparison Operators 

# equals / not equals
print("7 == 7", 7 == 7)
print("7 != 7", 7 != 7)
print("hello" == "hello") # true
print(True == False)
print(7 == "7") # will not throw an error, but it will evaluate to false
print(1 + 2 == 3)
print("hi" + "hi" == "hihi")

# greater than/geq
print(7 > 5)
print(4 + 1 >= 5)
print("a" < "b") # true
print("cow" < "cat") # false

# less than/leq
print(7 <= 5)

# print(my_number,my_string,my_bool) """

# If Statements!

# if this statement is true:
#   do something

if True:
    print("Hello") # will always print hello

if False:
    print("Secret message that will never run") # will never run / print

i = 0
if i == 0:
    print("i is 0")

i = 7
if i < 10:
    i = 10
    print(i)
    y = 25
    print(y)
    if 7 == 7:
        print("7 is 7")
    print(2+2)

# Python runs top-to-bottom. It doesn't save any information about variables. It just runs the code. 
# (You can change this by writing functions, will get to this later.)

# Python does, however, remember the statements inside the if statements:
print ("i =",i)

example = 10
if example < 10:
    print("Small number.")
elif example == 10:
    print("It's 10!")
else:
    print("Big number.")

class_code = 140
if class_code == 140:
    print("This is Python")
elif class_code == 150:
    print("This is Java")
elif class_code == 270:
    print("This is Data Structures")
# elif example == 10: 
#    print("Example is 10 but I don't know the class code") # won't print because we have already evaluated the statement after the if
else:
    print("I don't know this class")

# MATCH CASE

case_key = 140

match case_key:
    case 140:
        print("Python is cool")
    case 270:
        print("I love data structures")
    case 205 | 255:
        print("This is a stats class")