# Wednesday, September 28 Lecture Notes:

# Call Stack 

print("Start of Script")

def outer_function():
    print("Outer Function Called.")
    inner_function()
    print("Outer Function Ends.")

def inner_function():
    print("Inner function called.")
    print("Inner function ends.")

print("After function declaration")

outer_function()

print("After function call")
print("End of Script")

# Nested loops and the call stack

for i in range (5): # useful for when we are filling out a matrix or a grid of values by row 
    for j in range (5):
        print("i =", i, "j = ", j)

        # if you wanted an inner while loop, you could add one:
        # k = 0
        # while < 2:
        #    k += 1
         #   print(k)
        # indentation matters

# Scope

# Local variables cannot be used in global scope

def add_num(num1, num2): # num1 and num2 are NOT variables. They are arguments! They're even more temporary. 
    new_sum = num1 + num2
    return new_sum

add_num(5,8)
# print(new_sum) # will give a NameError

# To actually print new_sum, you could do:


def add_num(num1, num2): # num1 and num2 are NOT variables. They are arguments! They're even more temporary. 
    new_sum = num1 + num2
    return new_sum

print(add_num(5,8))
# alternatively, assign add_num(5,8) to a variable and then print that variable (all outside function definition)
# alternatively, could put the print statement within the function definition

def file_reader():
    filename_fr = "my_thoughts.pdf"
    print(filename_fr)

def file_namer():
    filename_fn = "my_program.py"
    file_reader()
    print(filename_fn)

file_reader() 
file_namer()

# Reading variables from global scope (try not to do this, more proper way would be to pass the local variable into the function as an argument (in the call))

num = 0

def incrementer(number):
    number = number + 1
    return number

print(num)
print(incrementer(num))
num = incrementer(num)
print(num)