# Take user's first and last name, print them in reversed order

str = input('Give your first and last name:\n')
strArr = str.split()
print(strArr[len(strArr)-1]+' '+strArr[len(strArr)-2])
