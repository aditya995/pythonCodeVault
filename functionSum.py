# Using sum in list
num1 = list(range(1,3))
sum1 = sum(num1)
print(sum1)
# Using sum in tuple
num2 = (1, 2, 3)
sum2 = sum(num2)
print(sum2)
# Using sum in set
num3 = {1, 2, 3}
sum3 = sum(num3)
print(sum3)
# Using sum in dictionary
dict = {1:'01', 2:'02'}
num1 = list(dict.values())
num = []
for i in num1:
  num.extend([int(i)])
print(num)
sum = sum(num)
print(sum)
