# public, private, protected

# public is accessed outside of the class
# protected is the same as public in terms of accessibility! but we use naming convention to prevent programmers from using it outside of the class or sub-classes

# private is only available in the class, still there is a way of using it outside of class by python name mangling, "_className__privateVarName". Should be prohibited.
class animal():
    def __init__(self, public, private, protected):
        self.public = public
        self.__private = private
        self._protected = protected
        print(f'"animal" created\n')

class mammal(animal):
    def __init__(self, a, b, c):
        super().__init__(private= b, public= a, protected= c)
        print(f"mammal created\npublic = {self.public}, _protected = {self._protected}")


human = mammal('publicVal', 'privateVal', 'protectedVal')
# name mangling used to access the private variable in aminal class
print(human.public, human._protected, human._animal__private)