# Homework 4 - Q2: Schedule Saver (10/13/22)

my_schedule = {
    'CMSC 140' : {
        '- Course Name' : 'Intro to Python',
        '- Professor' : 'Ackles',
        '- Units' : 6, 
        '- Meets' : ["M 9:50 - 11:00",
        "W 9:50 - 11:00",
        "R 10:25 - 12:10"]
    },
    'MATH 340' : {
        '- Course Name' : 'Probability',
        '- Professor' : 'Sage',
        '- Units' : 6, 
        '- Meets' : ["M 1:50-3:00",
        "W 1:50-3:00",
        "F 1:50-3:00"]
    },
    'ENG 180' : {
        '- Course Name' : 'Intro to Creative Writing',
        '- Professor' : 'Segrest',
        '- Units' : 6, 
        '- Meets' : ["T 2:35-4:20",
        "R 2:35-4:20"]
    }
}

for code,v in my_schedule.items():
    print("Course Code:",code)
    for key,val in v.items(): # now iterating through the values which are themselves dictionaries
        if isinstance(val, list): # if the value of the value is a list
            print(key,":")
            for i in val:
                print(i)
        else:
            print(key,":",val)
    print("----") # include ---- between each individual course
