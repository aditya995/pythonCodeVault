# Call by reference

def callByref(collection):
    # Will not create a copy of the parameter, Will change the original collection 
    # collection.append(5) # for list example
    # collection.setdefault('cc', 3) # for dictionary example
    # collection.add(5) # for set example
    
    # Will create a new copy, Won't change the original collection
    collection = [8, 9]

myCollection = [1, 2, 4, 'z']
myCollection = {'aa': 1, 'bb': 2 }
myCollection = {1, 2, 3}
print(myCollection)

# collections(list, dictionary, set) (excluding tuple) gets call by ref, unless we reassign
callByref(myCollection)
print(myCollection) 


# Call by value

def my_func1(n1, n2):
  return n1+n2

print(my_func1(3, 4))