# Lists and Its' functions

mycart = [1,2,'Hello', ] # Type is dymanic just like dynamic in dart
mycart.append('gg') # Adds element to last
print(f'mycart > {mycart}')

print('# Access elements using index \n\n   ## [start : stop : step]\n')
# [start : stop : step] Works same as string ***
# can reverse elements, show in between ranges, etc.
newcart1 = mycart[:1] 
print(f'newcart1 =>{newcart1}')

# Copy list elements
newcart2 = mycart
print(f'newcart2 =>{newcart2}')
newcart3 = mycart.copy()
print(f'newcart3 =>{newcart3}')
newcart4 = mycart[0:3] # Can use range of elements
print(f'newcart4 =>{newcart4}\n')

# Copy elements multiple times
print(f'newcart4 * 2 => {newcart4 * 2}') 
print(f'newcart1 + [2] => {newcart1 + [2]}') # does not append
newcart1.extend([100, 's']) # appends
print(f'newcart1.extend([100, \'s\']) => {newcart1}') 
newcart1.insert(1, 'G') # inserts value and shifts all elements ro right
print(f'newcart1.insert([1, \'G\']) => {newcart1}') 

# find existing or non existing, pop, remove, clear
print(f'\n100 in newcart1 =>{100 in newcart1}') # returns index, doesn't through error if not found
print(f'newcart1.index(\'s\') => {newcart1.index("s")}') # element must be inside
print(f'newcart1 =>{newcart1}')
print(newcart1.pop(2)) # Uses index # returns element's value
print(f'newcart1.pop(2) =>{newcart1}')
print(newcart1.remove('G')) # Uses element value # returns None
print(f'newcart1.remove(\'G\') =>{newcart1}')
newcart1.clear() # clears off all
print(f'newcart1.clear() => {newcart1}')
# Count repeated elements
basket = ["Banana", "Banana", "Banana", "Apples", "Oranges", "Blueberries"]
print(f'\nbasket.count(\'Banana\') => {basket.count("Banana")}')