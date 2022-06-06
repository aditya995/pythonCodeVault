## multiple inheritance in python

# the diamond problem
#    Class1
#     /  \
# Class2 Class3
#     \  /
#    Class4
# method “m” which is an overridden method in one of Class2 and Class3 or both then the ambiguity arises which of the method “m” Class4 should inherit.
class Class1:
    def m(self):
        print("In Class1")
 
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3")
 
class Class4(Class3, Class2):  
    pass
      
obj = Class4()
obj.m() # if overriden in both base classes, order matters, Class4 definition says Class3 comes first!
print(Class4.mro())         #This will print list
# print(Class4.__mro__)        #This will print tuple
