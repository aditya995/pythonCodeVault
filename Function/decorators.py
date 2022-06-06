# Decorators allow us to wrap another function in order to extend the behaviour 
# of the wrapped function, without permanently modifying it

def decorator(func):
    #  The inner function takes the argument as *args and **kwargs 
    # which means that a tuple of positional arguments 
    # or a dictionary of keyword arguments can be passed of any length. 
    # This makes it a general decorator that can decorate a function 
    # having any number of arguments.
    def inner(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value
    return inner
# adding decorator to the function
@decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))

# code for testing decorator chaining

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner
@decor1
@decor2
def num():
    return 10

print(num())
# decor1(decor2(num)) It works like this
# first decor2(num) returns 2*10 = 20
# then decor1(20) returns 20*20 = 400