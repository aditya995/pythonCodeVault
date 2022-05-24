# set and it's finctions

# union, intersection, difference won't change the original set, returns set
a = {1, 1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {6, 7, 8, 9}
d = a.copy()
e = {45, 21}
print(d)
print(a.union(b))
print( a.intersection(b))
print(a.difference(b))

# difference_update() removes the unwanted items from the original set
a.difference_update(b) 
print(a) # set a changed!
# intersection_update() Remove the items from the original set that is not present in both
b.intersection_update(c)
print(b);print() # set b changed!

# isdisjoint() finds if they have no common elements (if they intersect)
a = {1, 1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {6, 7, 8, 9}
print(a.isdisjoint(c))
print(a.isdisjoint(b))

print(a.pop())
a.remove(3)
print(a)

# update() Insert the items from set y into set x
c.update(b)
print(c)
c.add(44)
print(c)
c.clear()
print(c)