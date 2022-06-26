import os

# os.system('command')
cmd = 'systeminfo |find "Available Physical Memory"'
os.system(cmd)
# Opens ms-paint
cmd = 'mspaint'
os.system(cmd)

# Other methods of os
currentDir = os.getcwd()
print('Current dir->', currentDir)
print('Username: ', os.getlogin())
dirFileFolderList = os.listdir()
print('Listings-> ')
for i in dirFileFolderList:
    print(i)
# listing everything in the Directory **
for directory, dirnames, files in os.walk(currentDir+'/Programs'):
    print('Directory :', directory)
    print('Dirnames :', dirnames)
    print('Files :', files)

# Change, make, delete Directory
os.chdir('D:/')
# os.mkdir(currentDir+'/TestDir') # if exists then throughs error
os.rmdir(currentDir+'/TestDir')
print('Available cpu/cores',os.cpu_count())

# # Clear screen
# clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
# clearConsole() # Call it to clear
# #or
# os.system('clear') # Call it for specific os
