# list unpacking **************

a, b, *c, d = [1, 2 ,3, 4, 5, 6]
print(f'from list to list {c}')
print(type(c))

# Set unpacking **************
e, f, *g, h = {7, 8 ,9, 10, 11, 12}
print(f'from set to list {g}')
print(type(g))

# Dictionary unpacking **************
i, j, *k, l = {13:10, 24:20 ,35:30, 46:40, 57:50, 68:60}
print(f'from dictionary to list {k}')
print(type(k))

# Tuple unpacking
(aa, *bb, cc) = (1, 2, 3, 4, 5)
print(bb)
print(type(bb))

# Using loops for unpacking
list1 = ['a', 'b', '1', 'd', 'e', ]
for i in list1:
  print(i)
print()
touple1 = ('a', 'b', 'c', 'd')
for i in touple1:
  print(i)
print()
dict1 = {'kmph': 45, 'reserve': 1.2, 'tank-capacity':12}
for (i,j) in dict1.items():
  print(i+ ' =>',j)
print()
for i in dict1.keys():
  print(i)
print()
for i in dict1.values():
  print(i)
print()
