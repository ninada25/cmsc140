# This program says hello and asks for my name.

print('Hello, World!')
print('What is your name?') # ask for their name
myName = input() # the input func waits for the user to type some text on the keyboard and press ENTER.
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')