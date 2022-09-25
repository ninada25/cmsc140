def hello(): # define a function named hello()
    print('Howdy!') # body of the func, executed when func is called not when it is first defined
    print('Howdy!!!')
    print('Hello there.')

hello() # call the function
hello()
hello()

# want to avoid duplicating code in case you end up having a bug in the code

def hello(name):
    print("Hello, " + name)

hello("Alice")
hello("Bob")

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

# alternatively, print(getAnswer(random.randint(1,9)))

# the print() function automatically adds a newline character to the end of the string it is passed. to change this, use the end keyword arg:
print('Hello', end = '')
print('World')

#the print() func automatically separates string values with a single space. to change this, could pass sep keyword.
print('cats','dogs','mice')
print('cats', 'dogs', 'mice', sep=',')