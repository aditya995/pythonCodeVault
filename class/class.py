# class- properties, method

class animal:
  # First argument of the method will be self (could be anyother word)
  # We create properties of the class using self.propertyName in methods !!
  def create(self, name, ability='', food=''):
    # must use self as a reference
    self.name = name 
    self.ability = ability
    self.food = food
  

newAnimal = animal()
newAnimal.create(food='insects', name='Pegion', ability='fly')
# newAnimal.create(name='Pegion')
# newAnimal.create()
print(newAnimal.name)
print(newAnimal.ability)
print(newAnimal.food)