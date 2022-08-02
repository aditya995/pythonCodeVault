# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 

# Extras:
# 1.If the number is a multiple of 4, print out a different message.
# 2.Ask the user for two numbers: one number to check (call it num) and one 
# number to divide by (check). If check divides evenly into num, tell that to 
# the user. If not, print a different appropriate message.

num = int(input('Give an integer number'))
check = int(input('Give a integer number to divide the first integer'))
if num%2 == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

if num%4 == 0:
    print(f'{num} is divisible by {4}')
else:
    print(f'{num} is not divisible by {4}')

if num%check == 0:
    print(f'{num} is divisible by {check}')
else:
    print(f'{num} is not divisible by {check}')
