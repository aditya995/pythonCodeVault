numList = [1, 2, 3]  # Iterable 'numList'

numList_iterator = iter(numList)  # Iterator 'numList_iterator'

print(next(numList_iterator))  # Iteration
print(next(numList_iterator))  # Iteration
print(next(numList_iterator))  # Iteration

for item in numList:
    # prints every iteration
    print(f'item {item}')  # Iterator 'item'
