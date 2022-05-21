# String functions

str = ' Python is a Programming Language'
itemsStr = 'Box of apple __Banana   __  Oranges'
# str.strip('string')
print(str)
# str.strip() removes spaces from both ends
print(str.strip(' is ')) # not reliable

print(str.split())
# str.split() can split according to various characters
print(itemsStr.split('__'))

# str.replace() replaces the characters
print(str.replace('a', '##'))
print(str.replace('m', ''))

# str.lower, str.upper, str.capitalize 
# Does not convert the string
print('Upper() >\n'+str.upper())
print('Capitalize() >\n'+str.capitalize()) # First latter must not be space
print('lower() >\n'+str.lower())
print('Didn\'t change the original string >\n'+str)

# finds the index of first occurance, must exist in string
# case sensitive
print(str.index('o'))
print(str[6:].index('o')) # to get the original index must add start value
print(str.count('o'))
findStr = 'ython'
print(f'{findStr} is in index {str.find(findStr)}')