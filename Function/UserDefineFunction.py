# User defined functions

def my_func1(n1, n2): # type not defined
  return n1+n2

print(my_func1(3, 4)) # Type will be assigned as int
print(my_func1('9', '5')) # Type will be assigned as stirng

# Keyword arguments
print(my_func1(n2 = '9', n1 = '2')) 

# Default arguments 
def setRecord(score = 30):
    print(score)

print(f'Without passing params ',end='')
setRecord()
print(f'Without passing params ', end='')
setRecord(45)

# *args and **kwargs
def myFun1(*argv): 
    for arg in argv: 
        print (arg, end=', ')
 
def myFun2(**kwargs): 
    for key, value in kwargs.items():
        print (f"{key} : {value}", end=', ')

print("\nResult of * args: ")
myFun1('speed', 'gas', 'time', 'difficulty')
 
print("\nResult of **kwargs")
myFun2(speed ='100 km/h', gas ='40 Litre', finishTime ='5 minutes')