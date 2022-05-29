# tuple items are ordered, unchangeable, and allow duplicate values.

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# access elements [start:stop:step] same as string
print(tuple1[::-1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. 
# convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple2 = list(tuple1)
tuple2[1] = "kiwi"
tuple1 = tuple(tuple2)
print(tuple1)

# Add tuple to a tuple, multiply, addition allowed like string manipulation
y = ("orange",)
tuple1 += y * 2 
tuple1 = tuple1 + (8, 9)
print(tuple1)

# count() index()
print(tuple1.count('orange'))
print(tuple1.index('orange'))