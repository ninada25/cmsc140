# Wednesday, October 12 Lecture Notes:

### Regular Expressions

import re # regular expressions models is called re

# check if valid Lawrence email
emails = ['acacia.ackles@lawrence.edu',
'scott.corry@lawrence.edu',
'deanna.donohue@lawrence.edu',
'mmore500@msu.edu',
'elizabeth.k.sattler@lawrenc.edu']

# Idea 1:
for email in emails:
    e = email.split('@')
    if (e[1] == "lawrence.edu"):
        print(email, "is Valid")

# Idea 2 
for email in emails:
    if "@lawrence.edu" in email:
        print(email, "is Valid")

# Idea 3
for email in emails:
    if email.endswith("@lawrence.edu"):
        print(email, "is Valid")

############################################################################################################
### In-Class Exercise 1

def isValidFile():
    print("Please enter file name: ")
    file = input()
    if file.endswith(".py") or file.endswith(".pdf"):
        return True
    else:
        return False

print(isValidFile())

# to make more concise: 
def isValidFile(string):
    return string.endswith(".py") or string.endswith(".pdf")

print(isValidFile("hw.ap"))

# In general...

# def newfunction(condition):
#     if condition:
#         return True
#     else:
#         return False

# def newfunction(condition): # return true when condition is true (makes code above more concise!)
#     return condition

# def newfunction(condition): # return false when condition is true
#     return not condition
############################################################################################################

# Website to find regular expressions
# https://regex101.com/

def check_app(string):
    return "app" in string and not string.startswith("app")

# With regular expressions,

# . = any character
# + = plus 1 or more (+ = 1 or more time)
# * = matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (* = 0 or more time)

# So .* basically matches the entire input 

# example: ^[A-Za-z]+app 
# \d will match any digits
# ? means a character is option

# tell python what regex we want
print("regex: ")
email_regex = re.compile(r'[a-z]+\.([a-z]+)?[a-z]+@lawrence.edu$') # the r is a raw string so we can put any esc character we want
for email in emails:
    if re.search(email_regex, email):
        print(f"{email} is a valid address.")

############################################################################################################
### In-Class Exercise 3: Revise your isValidFile() function to use regex instead.

def isValidFile_regex(string):
    regex = re.compile(r'[A-za-z0-9]+\.(py|pdf)$')
    return re.search(regex, string)

print(isValidFile_regex("hello.py")) # she will revise this lol
print(isValidFile_regex("hello.py.cpp")) # she will revise this lol
############################################################################################################