# Monday, October 10 Lecture Notes:

### Strings!

# Escape characters

# ex_string = 'This won't work'

double_quote = "This 'string' is okay"
single_quote = 'This "string" is okay'
print(double_quote, single_quote)
 
esc_double = "This is \"fine\" now." # put backslash before your character to say I do want this printed.
esc_single = "This string\'s formatting is okay."
print(esc_double)
print(esc_single)

# to print a \, you would need 2 backslashes: \\

rawstring = r'This prints \' exactly \" what I type.' # r followed by a quote tells the computer it is a rawstring.
print(rawstring)

# Printing on new lines:
print("hello")
print("this is a new line")

# Printing on new lines with triple quotation marks
trip_quote = """This is a string
across multiple lines."""
print(trip_quote)

# Alternatively, use \n with no spaces
newline = "This is a string\nwith a newline"
print(newline)

#############################################

### In-Class Exercise 1: Literal

print("Here's a string for you! \nThis \\n is a newline command \nthat didn't actually do anything.")

# Alternatively:
print("""Here's a string for you!
This \\n is a newline command
that didn't actually do anything.""")

#############################################

# String slicing and indexing
name = "Nina Austria"
print(name[0])
print(name[0:4]) # slicing does not alter the original string. strings are immutable!
print(name)

firstname = name[0:4]
print(firstname)

# name[0] = "K" <- will produce an error
# name.append("hello") <- will also produce an error

# You can use in and not in with strings
print(firstname in name)
print("Hello" in "Hello")
print("j" in "fox")
print("j" not in "fox")

splitname = name.split() # automatically splits on whitespace 
print(splitname)
# for key,val in dict.items()

first,last = name.split()
print(first)
print(last)

newname = name.split('a') # can pass in a chr, used as a delimiter
print(newname)

# Joining Strings (opposite of splitting):

my_list = ["hello", "python", "class"]
nospace = "".join(my_list)
space = " ".join(my_list)
print(nospace)
print(space)

#############################################

### In-Class Exercise 2: Split and Join

# Replace all the whitespaces with dashes (using the python functions we just learned) then print the result. 
# Make sure to properly deal with the backslashes in the string.

string = "C:\MyDocuments\Classes\Intro to Python\Week 5"
splitname = string.split() 
# print(splitname)
dashes = "-".join(splitname)
print(dashes)

#############################################

space_string = "This is a string with    a lot of    spaces!"
splitstring = space_string.split() # will strip all spaces no matter how many there were
print(splitstring)
print(splitstring[4])
print(splitstring[4][0])

a,b,c = ["hello", 2, True]
print(a)
print(b)
print(c)

print("-".join(["a","b","c"]))

print("-".join("These are spaces".split()))


# Strings in Strings!!!
fruit = "apples"
num = 7
print("I have " + str(num) + " " + fruit + ".")

# string interpolation
print("I have %s %s." % (num, fruit)) # %s is a stand-in for our strings

# f-strings
print(f'I have {num} {fruit}.') # the f is for format. can perform operations within the brackets i.e. {num + 1}


# Formatting
newname = name.upper()
print(newname)
newname2 = name.lower()
print(newname2)

print(newname.isupper())
print(name.isupper())

# capitalization techniques = useful for user input to make sure capitalization isn't causing any differences in outcome

age = int(input("How old are you?: "))
birthday = input("Did you have a birthday this year?: ")
birthyear = 2022 - age

if birthday.lower() == "yes" or birthday.lower() == "y":
    print(f"You were born in {birthyear}.")
else:
    print(f"You were born in {birthyear-1}.")

# Whitespace Stripping
space_string = "        Hello!   "
left = space_string.lstrip()
right = space_string.rstrip()
both = space_string.strip()
print(left)
print(right)
print(both)
print(left == both)

cool_string = "oooo Hello this is my string oooooo"
print(cool_string.strip('o')) # will not strip the o in Hello since there are characters surrounding it. will only strip from the ends.

# Checking alphanumeric
print("abc".isalpha())
print("abc123".isalpha()) # will print false since it's not just alphabetical
print("abc123".isalnum())
print("abc!!123".isalnum())

# Other things (int, lists)
print(isinstance(7,int))
print(isinstance("hello", int))
print(isinstance(name, str))
my_list = [7,8,"list",[1,2]]
print(isinstance(my_list, list))

if isinstance(my_list, list): # print if 'my_list' is a list
    print(my_list)