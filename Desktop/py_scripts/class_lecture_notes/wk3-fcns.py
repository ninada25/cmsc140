# Monday, September 26 Lecture Notes:

# functions!!!

print("Hello")
num = input("Enter a number: ")
print("Your number was:", num)

name_length = len("Nina")
print(name_length)

print(len("Nina"))

my_sum = 0
for i in range(1,21):
    my_sum += i
print(my_sum)

# Need to duplicate code in order to do the same from [1,100]
my_sum = 0
for i in range(1,101):
    my_sum += i
print(my_sum)

def our_first_function():
    print("This is a function")

print("This is before the function.")
our_first_function() # runs when it is called, not when it is defined.
print("This is after the function.")

def excited_print(my_string):
    print(my_string + "!!!!!!")

excited_print("Hello")
# print(my_string) # will throw an error, will talk about scope on wed. if we want to use the var outside the func, can use a return. but it is a local var. 

def number_add_2(num):
    print(num + 2)
number_add_2(73)

def exc_print(my_string):
    return my_string + "!!!!!" # return does not require parentheses or anything
string1 = exc_print("Hello")
string2 = exc_print("This is a function")
print(string1)
print(string2)

def adder(num1, num2):
    my_sum = num1 + num2
    return my_sum
new_sum = adder(1,4)
number_add_2(73)

# In-class exercise 1:

# Write a function exponent() that takes two numbers, called n1 and n2 as inputs, and returns n1 raised to the power of n2.

def exponent(n1, n2):
    my_power = int(n1 ** n2)
    return my_power
ex1 = exponent(7,3)
ex2 = exponent(4,2)
ex3 = exponent(25,0.5)
print(ex1)
print(ex2)
print(ex3)

def number_add_2(num):
    return num + 2
print(number_add_2(73))

def is_equal(num1, num2):
    if num1 == num2:
        print("This is equal") # or return "This is equal"
    else:
        print("This is not equal") # or return "This is not equal"
is_equal(7,8)
is_equal(1,1)
is_equal(4,2+2)

def new_adder(start, stop):
    my_sum = 0
    for i in range(start, stop + 1):
        my_sum += i
    return my_sum
print(new_adder(1000,2500))

# Collatz Pt 1 Expansion (done together in class):

def approx_log(num, divisor):
    counter = 0
    while num > 1:
        num = num // divisor
        counter += 1
    return counter

ex1 = approx_log(25, 2)
ex2 = approx_log(16, 2)
print(ex1)
print(ex2)