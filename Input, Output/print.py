# Printing output
print('Something')
print('No new line will be added',end = " ") # print without new line
print('Something' + ' ' + 'is on the screen')
# Printing values from variables
name = 'Aditya'
age = 85
# String concatenation
# Must convert the number to string format!!
print(name + ' is not ' + str(age) + ' years old')
# String interpolation
print(f'{name} is not {age} years old')
# Using format
print('{} is not {} years old'.format(name, age))
print('{1} is not {0} years old'.format(name, age))