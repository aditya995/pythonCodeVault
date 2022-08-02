# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that 
# are common between the lists (without duplicates). Make sure your program 
# works on two lists of different sizes. Write this in one line of Python using
# at least one list comprehension.

import random
# a = [random.randint(1,100) for i in range(1,50)]
# b = [random.randint(1,100) for u in range(1,55)]
a = [13, 1, 1, 2, 2, 21, 34, 55, 89, 3, 5, 8]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([i for i in list(set(a)) if i in b])