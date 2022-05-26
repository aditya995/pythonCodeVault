# Dictionary and it's functions, Un ordered!!

record = {
  'apple': 14.5,
  'list': ['gg','nvm'],
  False: 'wrong',
  True: 'great'
}
rec = record.copy() # copies the whole dictionary
print(record[False])
print(rec[False])
print(record['list'][1]);print()

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
rec.setdefault('new', 124)
print(f'rec.setdefault("new", 124) => {rec}\n')

# get() To get the value, if non-existent returns given specified value 
output = rec.get('apple', 'Not found!')
print(output)
output = rec.get('ss', 'Not found!')
print(output);print ()

# keys() Returns all the keys
print(rec.keys())
print(True in record.keys())

# values() Returns all the values
print(record.values())
print('wrong' in record.values());print()

# update() Updates the dictionary with the specified key-value pairs
rec.update({True: 'Yes'})
print(rec)

# clear(), pop(), popitem () Removes the last inserted key-value pair
rec.pop('apple')
print(rec)
rec.popitem()
print(rec)
rec.popitem()
print(rec)
rec.clear()
print(f'{rec}\n');