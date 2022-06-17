list1 = ['✔', '✔', '✔', ]
list2 = ['✔', '✔', '✔', ]
list3 = ['✔', '✔', '✔', ]


def printli(li: list):
    for i in li:
        print(i)


printli([list1, list2, list3])

col = int(input('Give column number 1-3\n'))
row = int(input('Give row number 1-3\n'))
col -= 1
row -= 1
if row == 0:
    list1[col] = '🎁'
elif row == 1:
    list2[col] = '🎁'
elif row == 2:
    list3[col] = '🎁'

printli([list1, list2, list3])

str = 'sdf'
str.join()
