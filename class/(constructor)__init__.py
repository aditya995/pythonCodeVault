# class- __init__ works as a constructor

class animal:
  ability = None
  food = None
  animalType = ''

  def _findType(self, ability, food):
    if(ability == 'fly' and food == 'insects'):
      return 'bird'
    elif(ability == 'fly' and food == 'grass and leaves'):
      return 'insects'
    elif(ability == 'swim'):
      return 'fish'
    elif(ability == 'walk'):
      return 'land animals'
    return 'Not defined'

  def __init__(self, name, ability, food):
    self.name = name 
    self.ability = ability
    self.food = food
    self.animalType = self._findType(ability, food) # Method called in constructor

  
newAnimal1 = animal(food='insects', name='Pegion', ability='fly')
print(newAnimal1.name)
print(newAnimal1.ability)
print(newAnimal1.food)
print('This is a \'',newAnimal1.animalType, '\'\n')

newAnimal2 = animal(food='planktons', name='tuna', ability='swim')
print(newAnimal2.name)
print(newAnimal2.ability)
print(newAnimal2.food)
print('This is a \'',newAnimal2.animalType, '\'')