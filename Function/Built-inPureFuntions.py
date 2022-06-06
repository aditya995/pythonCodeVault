# map, filter, zip, reduce are pure functions

my_list = [1, 2, 3]
his_list = [6, 7, 8, 9, 10, 11, 12, 13]
def multiply(li):
    return li*3

print(list(map(multiply, my_list)),'\n')

def only_even(listItem):
    return listItem % 2 == 0

def only_odd(listItem):
    return listItem % 2 != 0

# map calls the function on each element, and returns all the processed-elements 
# filter keeps those who returns true, keeps those original unprocessed elements
print(list(filter(only_even, my_list)), '*')
print(list(map(only_even, my_list)),'\n')

print(tuple(filter(only_odd, my_list)), '#')
print(tuple(map(only_odd, my_list)))
# zip creates tuples
print(list(zip(my_list, his_list, my_list, his_list))) 

# reduce takes a function which must have 2 arguments
from functools import reduce
# dont use from cv2 library **
listInt = [0]
fiboList = [0, 1]
def accumulat (acc, item):
    # print(acc, item, acc+item)
    fiboList.append(acc+item)
    if(len(listInt) < 10-2):
        listInt.append(acc)
    return acc + item

reduce(accumulat, listInt, 1)
print(fiboList)