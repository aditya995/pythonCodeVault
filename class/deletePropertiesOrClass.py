# class- delete properties/class

class animal:
  def setVal(self, name='n-_-', ability='a-_-'):
    self.name = name 
    self.ability = ability
  
  def __init__(self):
    self.setVal()

newAnimal = animal()
print(newAnimal.__dict__)
newAnimal.setVal(name='Pegion', ability='fly')
print(newAnimal.__dict__)
# animal.__run(newAnimal)
del newAnimal.ability
# print(newAnimal) # Will give error
print('ability' in newAnimal.__dir__())

del newAnimal
# print(newAnimal) # Will give error