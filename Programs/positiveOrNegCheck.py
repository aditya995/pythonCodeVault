# Check negative or positive from input

inp = int(input("Give an integer number\n"))
if(inp > 0):
  print('Positive number')
elif(inp == 0):
  print('The number 0 is neither positive nor negative, and is usually displayed as the central number in a number line.')
else:
  print('Negative number')