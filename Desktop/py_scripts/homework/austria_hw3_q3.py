def silly_program():
    x = 0
    # Q2 MARKER
    while x < 2:
        for i in range(3):
            print(i)
            if i == 2:
                print(i, "is my favorite number")
        x += 1
x = 5 
# Q1 MARKER
print("This is my program.")
print(silly_program())