import os

board = [
  ['@', '@', '@', ],
  ['@', '@', '@', ],
  ['@', '@', '@', ],
        ]
turns = 9
player1 = input('Input player1 name\n')
player2 = input('Input player2 name\n')

def draw():
  for j in board:
    for i in j:
      print(f'| {i} ',end = "")
    print('|\n------------')

def validInput(a, b):
  a = int(a) if a.isdigit() else 0
  b = int(b) if b.isdigit() else 0
  if a > 0 and a < 4 and b > 0 and b < 4:
    if board[a-1][b-1] == '@':
      return True
    return False;
  return False

def isWinner():
  for i in [0,1,2]:
    if(board[i][0] == board[i][1] == board[i][2] and (board[i][2] == 'O' or board[i][2] == 'X')):
      # print('Rows')
      return 1 if board[i][0] == 'O' else 2
    if(board[0][i] == board[1][i] == board[2][i] and (board[2][i] == 'O' or board[2][i] == 'X')):
      # print('Columns')
      return 1 if board[0][i] == 'O' else 2
  
  # diagnal from leftupper to rightbottom
  if(board[0][0] == board[1][1] == board[2][2] and (board[2][2] == 'O' or board[2][2] == 'X')):
    # print('diagnal from leftupper to rightbottom')
    return 1 if board[2][2] == 'O' else 2
  # diagnal from leftbottom to rightupper
  if(board[0][2] == board[1][1] == board[0][2] and (board[0][2] == 'O' or board[0][2] == 'X')):
    # print('diagnal from leftbottom to rightupper')
    return 1 if board[0][2] == 'O' else 2
  return -1

while(turns):
  row = ''
  column = ''
  print('Remaining turns ',turns)
  draw()
  if isWinner() != -1: 
    break
  if turns%2 == 1:
    while not validInput(row, column):
      row = input(f'{player1} give input row value,range 1-3\n')
      column = input(f'{player1} give input column value,range 1-3\n')
    board[int(row)-1][int(column)-1] = 'O'
  else:
    while not validInput(row, column):
      row = input(f'{player2} give input row value,range 1-3\n')
      column = input(f'{player2} give input column value,range 1-3\n')
    board[int(row)-1][int(column)-1] = 'X'
  turns-=1
  os.system('cls')

winner = player1 if isWinner() == 1 else player2
print(f'Winner is player {winner}')
print ('Thanks for playing')