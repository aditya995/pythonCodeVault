import os.path

path1 = 'C:/Users/adity'
path2 = 'C:/Users/adity/Desktop/ipid.txt'

print('Returns file-name ->', os.path.basename(path2))
print('Returns dir-name ->', os.path.dirname(path2))
print('Splits the path into a tuple(dir, filename) ->', os.path.split(path2))
print('Splits the file-ext. ->', os.path.splitext(path2))
print('Splits the drive name ->', os.path.splitdrive(path2))
print('Joins the ->', os.path.join(path1, path2))

print('\n# conditionals')
print('If this exists (file or dir) ->',os.path.exists(path2))
print('Checks if it is a dir->', os.path.isdir(path1))
print('Checks if it is a file->', os.path.isfile(path2))
