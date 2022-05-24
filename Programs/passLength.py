# Take input of username and password, 
# print username and password as "***" (obscured text) that has the same length as the password length
# example:
# Hi UserWarning
# Your *** is 3 charecters long.

uname = input("Give your username\n")
pword = input("Give your password\n")
str = '*' * len(pword)
print(f'Hi {uname}')
print(f'Your {str} is {len(pword)} characters long.')