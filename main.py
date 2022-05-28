# def my_func(n1, n2):
#   return n1+n2;

# print(my_func(3, 4))


# import os

# board = [
#   ['@', '@', '@', ],
#   ['@', '@', '@', ],
#   ['@', '@', '@', ],
#         ]
# a = 9
# def draw():
#   for j in board:
#     for i in j:
#       print(i,end = " ") # print without new line
#     print()

# def inputCheck(a, b):
#   if a+b > 6:
#     return False
#   return True
# row = 5
# column = 5

# while(a):
#   draw()
#   if a%2 == 1:
#     row = int(input('Player 1 give input row value,range 1-3\n'))
#     column = int(input('Player 1 give input column value,range 1-3\n'))
#     while not inputCheck(row, column):
#       row = int(input('Player 1 give input row value,range 1-3\n'))
#       column = int(input('Player 1 give input column value,range 1-3\n'))
#     board[row-1][column-1] = 'O'
#   else:
#     row = int(input('Player 2 give input row value,range 1-3\n'))
#     column = int(input('Player 2 give input column value,range 1-3\n'))
#     while not inputCheck(row, column):
#       row = int(input('Player 2 give input row value,range 1-3\n'))
#       column = int(input('Player 2 give input column value,range 1-3\n'))
#     board[row-1][column-1] = 'X'
#   a-=1
#   os.system('clear')

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