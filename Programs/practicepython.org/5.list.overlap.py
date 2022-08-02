# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that 
# are common between the lists (without duplicates). Make sure your program 
# works on two lists of different sizes.

# Extras:
# 1.Randomly generate two lists to test this
# 2.Write this in one line of Python 
import random
a = [random.randint(1,100) for i in range(1,10)]
b = [random.randint(1,100) for u in range(1,15)]
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
setA = set(a)
setB = set(b)
overlap_list = list(setA&setB)
print (overlap_list)