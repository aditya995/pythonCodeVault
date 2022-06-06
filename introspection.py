# Introspection is an ability to determine the type of an object at runtime.

# 1.type() : This function returns the type of an object.
print(type(1))
print(type("1"))

# 2.dir() :This function return list of methods and attributes associated with that object.
rk ={1, 2, 3, 4, 5}
class fly:
    def __init__(self):
        self.ability = 'fly'
bee = fly()
print(dir(bee))
print(dir(rk))

# 3.id() :This function returns a special id of an object.
print(id(bee))
print(id(rk))

# 4. Various other methods
# help()	It is used it to find what other functions do
# hasattr()	Checks if an object has an attribute
# getattr()	Returns the contents of an attribute if there are some.
# repr()	Return string representation of object
# callable()	Checks if an object is a callable object (a function)or not.
# issubclass()	Checks if a specific class is a derived class of another class.
# isinstance()	Checks if an objects is an instance of a specific class.
# sys()	Give access to system specific variables and functions
# __doc__	Return some documentation about an object
# __name__	Return the name of the object.