# Scope of data-types

print('# Global scope')

val = 4
def changeTo(newVal):
    global val # Accesses 'val' in global scope
    val = newVal

print(val)
changeTo(10)
print(val)

print('# Local scope ')
data = 4
def changeTo(newVal):
    data = newVal # Creates a new variable, can't change 'data' in global scope outside the function

print(data)
changeTo(10)
print(data)

print('\n# nonlocal (Searches the variable named exactly same in parent scope [only one scope above])')

def outer():
  x = 'Outer'
  def inner():
    nonlocal x # Access the x in parent scope!
    x = 'Inner' 
    print('inner:', x)
  inner()
  print('outer:', x)

outer()