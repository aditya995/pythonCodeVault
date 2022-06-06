# Static method and class method

## static method ***
# 1 Using staticmethod decorator
class Dates:
    def __init__(self, date):
        self.date = date       
    def getDate(self):
        return self.date
    @staticmethod # Using staticmethod decorator
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")
print(date.getDate(), dateFromDB.getDate())

# 2 staticmethod() is considered a un-Pythonic way of creating a static function. 
# Hence, in newer versions of Python, you can use the @staticmethod decorator.
class Calculator:
  def add_numbers(num1, num2):
    return num1 + num2
# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)
sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)
# Output: Sum: 12

## class method ***
# 1 Using classmethod decorator
# Factory methods are those methods that return a class object (like constructor) for different use cases. here fromFathersAge, fromBirthYear both are Factory methods
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))
man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))

# Output 
# True
# False

# Here, using a static method to create a class instance wants us to hardcode the instance type during creation.
# This clearly causes a problem when inheriting Person to Man.
# fromFathersAge method doesn't return a Man object but its base class Person's object.
# This violates the OOP paradigm. Using a class method as fromBirthYear can ensure the OOP-ness of the code since it takes the first parameter as the class itself and calls its factory method.

# 2 classmethod() is considered un-Pythonic so in newer Python versions, you can use the @classmethod decorator for classmethod definition.

class Student:
  marks = 0
  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)
# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

# Output: Obtained Marks: 88