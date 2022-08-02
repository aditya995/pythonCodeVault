# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

# Extras:
# 1.Write two different functions to do this - one using a loop and 
# constructing a list, and another using sets.
# 2.Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def rDupByLoop(li):
    listUnique = []
    return [int(bool(listUnique.append(i)))+i  for i in li if i not in listUnique]

def rDupBySet(li):
    return list(set(li))

print(rDupByLoop(a))
print(rDupBySet(a))