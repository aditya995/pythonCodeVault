import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print('This will not show')
clearConsole() # Call it to clear

#or
os.system('clear') # Call it for specific os
print('This is visible')
