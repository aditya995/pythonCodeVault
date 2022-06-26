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
dirFileFolderList = os.listdir()
print('Listings-> ')
for i in dirFileFolderList:
    print(i)
os.mkdir(currentDir+'/TestDir') # if exists then throughs error
os.rmdir(currentDir+'/TestDir')
print('Available cpu/cores',os.cpu_count())
