# Create a program that asks the user to enter their name and their age. Print 
# out a message addressed to them that tells them the year that they will turn 
# 100 years old.

# Extras:
# 1. Add on to the previous program by asking the user for another number and 
# printing out that many copies of the previous message.
# 2. Print out that many copies of the previous message on separate lines.

from datetime import date 

current_year = date.today().year
name = input("Give me your name: ")
print("Your name is " + name)
age = int(input("Enter your age: "))
n_times = int(input('How many times to print? input int number.'))
when100 = current_year + 100 - age if age < 100 else current_year - age + 100
for i in range(n_times):
    if when100 < current_year:
        print(f'You already became 100 at year {when100}')
    else :
        print(f'You will become 100 years old in {when100} ')