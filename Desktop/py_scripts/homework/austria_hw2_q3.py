# Homework 2 - Q3: Your Age (9/29/22)

# Write a program that asks the user what year they were born. 
# Then, ask them if they have already had their birthday this year.
# Use this information to calculate their age. 

print("Hello. What year were you born?: ") # ask user what year they were born
birth_year = int(input())
print("Have you already had a birthday this year?:" ) # ask user if they have already had their birthday this year
bday_passed = input()

if bday_passed == "Yes" or bday_passed == "Y" or bday_passed == "yes" or bday_passed == "y":
    cur_age = 2022 - birth_year
    print("You are " + str(cur_age) + " years old.")
elif bday_passed == "No" or bday_passed == "N" or bday_passed == "no" or bday_passed == "n":
    cur_age = 2022 - birth_year - 1
    print("You are " + str(cur_age) + " years old.")