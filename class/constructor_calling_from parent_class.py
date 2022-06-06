# calling all the constructors in multiple inheritance from base classes with arguments

class First:
    def __init__(self):
        print("First state")

class Second():
    def __init__(self, hello2):
        print("Second state")
        self.hello2 = hello2

class Third():
    def __init__(self, hello3):
        print("third state")
        self.hello3 = hello3

class Fourth(First, Second, Third):
    def __init__(self, a, b):
        print("Forth state")
        # Using name of the class
        # First.__init__()
        # Second.__init__(self, a)
        # Third.__init__(self, b)
        # Using super().__init__()
        super().__init__()
        super(First, self).__init__(a)
        super(Second, self).__init__(b)

forthObj = Fourth('some', 'one ')
print(forthObj.hello2, forthObj.hello3,'\n')

## if we use super in all of them will run, same happens for __init__ (constructor)
# the diamond inheritance
class Class1:
    def m(self):
        print("In Class1")
 
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
 
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
 
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")  
        super().m()

print('---')
obj = Class4()
obj.m()
print('---')
# calling all the constructors in multiple inheritance from base classes with Keyword-arguments

class FirstLine:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("First Line")

class SecondLine():
    def __init__(self, hello2, **kwargs):
        super().__init__(**kwargs)
        print("Second Line")
        self.hello2 = hello2

class ThirdLine():
    def __init__(self, hello3, **kwargs):
        super().__init__(**kwargs)
        print("third Line")
        self.hello3 = hello3

class FourthLine(FirstLine, SecondLine, ThirdLine):
    def __init__(self, a, b):
        super().__init__(hello2 = a, hello3 = b)
        print("Forth Line")
        # Using name of the class

line = FourthLine('D', 'J')
print(line.hello2, line.hello3,'\n')