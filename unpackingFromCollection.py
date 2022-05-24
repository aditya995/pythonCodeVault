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