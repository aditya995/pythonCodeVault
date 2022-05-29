# Useful Built-in methods and properties class

class animal:
  __privateVar = 'PrivateVar'
  def setVal(self, name='n-_-', ability='a-_-', food='f-_-'):
    self.name = name 
    self.ability = ability
    self.food = food


# __dir__() returns a list of current-properties and methods in the class
newAnimal = animal()
print(newAnimal.__dir__())
print('food' in newAnimal.__dir__())
# Will add 3 more properties in the class
newAnimal.setVal(food='insects', name='Pegion', ability='fly')
print('New 3 properties added after calling setVal() method: **\n', newAnimal.__dir__())
print('food' in newAnimal.__dir__(),'\n')


# __dict__ returns a set of current-properties in the class 
# Be aware that in some rare cases there's a __slots__ property, such classes often have no __dict__. ***
newAnimal02 = animal()
print(newAnimal02.__dict__)
newAnimal02.setVal(food='insects', name='Pegion', ability='fly')
print(newAnimal02.__dict__)