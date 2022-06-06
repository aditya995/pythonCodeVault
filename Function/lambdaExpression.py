# lambda functions/expressions 
# also known as anonymous functions

from functools import reduce
listG = [1, 2, 3, 4, 5, -6]
# def addTwo(item):
#     return item+2
# print(list(map(addTwo, listG)))

# above 3 lines outputs the same as the line below
print(list(map(lambda item: item+2, listG))) # adds 2 to each items

print(list(filter(lambda x: x<0, listG))) # filters the negative numbers
# Making sum of all the elements
print(reduce(lambda x, y: (x+y),listG[:4]))

listN = [(8, 2), (5, 3), (4, 1), (-10, 6)]
listN.sort(key=lambda x: x[1]) # sorted using second element of tuple
print(listN)


charList = [char for char in 'dizzy']
numList1 = [n if(n%2!=0) else 'Even' for n in range(5)] # works as map, else is expected
numList2 = [n for n in range(10) if(n%2==0)] # works as filter, else is not excepted
print(charList)
print(numList1)
print(numList2)

dictThings = {
    'a':1,
    'b':2,
    'c':3
}
NewDict1 = {k:v if(v%2==0) else 'Odd' for k, v in dictThings.items()}
NewDict2 = {k:v for k, v in dictThings.items() if(v%2!=0)}
print(NewDict1)
print(NewDict2)