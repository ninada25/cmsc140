# Monday, October 3 Lecture Notes:

### Imports! 

import math
import random # alt: import random as rand

print(len("class"))

def my_square(num):
    return num*num

a = my_square(5)
print(a)

# look up 'python math module' to know what mathematical functions it contains
b = math.ceil(2.4)
print(b)

pi = math.pi
print(pi)

random.seed(25) # if we don't use this, it uses our system's time as the seed and we get different numbers every time
num1 = random.randint(0,5) # unlike ranges, the stop is INCLUSIVE
num2 = random.randint(0,5)
print(num1, num2)