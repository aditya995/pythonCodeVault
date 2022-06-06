from functools import reduce
listInt = [0]
fiboList = [0, 1]
n = 10
def fibb (acc, item):
    fiboList.append(acc+item)
    print(acc, item, acc+item)
    if(len(listInt) < n-2):listInt.append(acc)
    return acc + item

reduce(fibb, listInt, 1)
print(fiboList)
print(len(fiboList))

# explaination
# 1st iteration acc = 1, item = 0, acc+item = 1 and acc(1) got append in listInt
#                                             ^
#                     ------------------------|         ^
#                     |         |-----------------------|
#                     V         v
# 2nd iteration acc = 1, item = 1, acc+item = 2 and acc(1) got append in listInt
#                                             ^
#                     ------------------------|         ^
#                     |         |-----------------------|
#                     V         v
# 3rd iteration acc = 2, item = 1, acc+item = 3 and acc(2) got append in listInt
#                                             ^
#                     ------------------------|         ^
#                     |         |-----------------------|
#                     V         v
# 3rd iteration acc = 3, item = 2, acc+item = 5 and acc(3) got append in listInt
#                                             ^
#                     ------------------------|         ^
#                     |         |-----------------------|
#                     V         v
# 3rd iteration acc = 5, item = 3, acc+item = 8 and acc(5) got append in listInt