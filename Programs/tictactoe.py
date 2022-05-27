import os

board = [
  ['@', '@', '@', ],
  ['@', '@', '@', ],
  ['@', '@', '@', ],
        ]
a = 8
def draw():
  for j in board:
    for i in j:
      print(i,end = " ")
    print()
while(a):
  draw()
  if a%2 == 1:
    row = int(input('Player 1 give input row value\n'))
    column = int(input('Player 1 give input column value\n'))
    board[row-1][column-1] = 'O'
  else:
    row = int(input('Player 2 give input row value\n'))
    column = int(input('Player 2 give input column value\n'))
    board[row-1][column-1] = 'O'
  a-=1
  os.system('clear')

