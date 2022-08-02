# Ask the user for a number and determine whether the number is prime or not. 
import math
def isPrime(num:int):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0 : return False
    return True
num = int(input('Give a number to check prime\n'))
print(f'{num} is {"not" if not isPrime(num) else ""} Prime')