# def my_func(n1, n2):
#   return n1+n2;

# print(my_func(3, 4))


### Class 27/5/2022

# help()

# args and kwargs in python

# when we dont know how many number of arguments

# clean code rules

# readibility
# clean
# perdictable
# Keep It Simple S (KISS)
# Dont Repeat Your code (DRY)

# functional scope

# global keyword
# nonlocal

# pass keyword

# r1 = 5

# def outer():
#   r1 = 10
#   x = 'local'
#   def inner():
#     nonlocal x
#     # global r1 # will use r1 from the parent function
#     # r1 = 2 # comment to see magic global r1 manupulated
#     x = 'non local' # comment to see diff
#     print('inner:', x, r1 )
#   inner()
#   print('outer:', x)

# outer()
# print(r1)


# 

# class gg:
#   def __init__(s, name):
#     s.name = name

# gg1 = gg('GoodGame')
# print(gg1.name)