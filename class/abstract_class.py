# abstract class cannot
# be an instantiation
# If class inherits ABC and atleast one method is mentioned abstruct
from abc import ABC,abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def kill(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
    def move(self):
        print("I can bark")
 
class Lion(Animal):
    def move(self):
        print("I can roar")
 
c=Animal() # will return error
a = Lion()
a.move()