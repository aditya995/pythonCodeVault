# String
name = 'Mentis'
print(name)
print('# Access character using index \n\n   ## [start : stop : step]\n')
print(f'name[0] => {name[0]}')
print('\n# Access substring using [starting index : ending index]')
print(f'name[0:2] => {name[0:2]}')
print(
    f'name[3:10] => {name[3:10]} # Can take out of bound index as ending index'
)
print(f'name[3:] => {name[3:]} # from index 3 to end')
print(f'name[:3] => {name[:3]} # from start to index 3')
print('\nStep is used to hop to every n-th value in the string')
print(f'name[::2] => {name[::1]}')
print(f'name[::2] => {name[::2]}')
print(f'name[::2] => {name[::3]}')

print('\n# Using negative values in index')
print(f'name[-3] => {name[-3]}')
print(f'name[-2] => {name[-2]}')
print(f'name[-1] => {name[-1]}')
print('\n# Using negative in stop value, takes out characters from the end')
print(name[:-2])
print(
    '\n# Using negative in step value reverses the string\n# and also hop to every n-th value in the string'
)
print(f'name[::-1] => {name[::-1]}')
print(f'name[::-2] => {name[::-2]}')
