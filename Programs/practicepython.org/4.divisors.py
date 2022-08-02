# Create a program that asks the user for a number and then prints out a list 
# of all the divisors of that number.
import math
num = int(input('Give an integer'))
divisor_list = []
for i in range(1, int(math.sqrt(num))+1):
    if(num%i == 0):
        divisor_list.append(i)
        divisor_list.append(num//i)
print(divisor_list)