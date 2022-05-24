# Given input of a one digit number 'x', print sum of x + xx + xxx
# example: Input 5, Output 5+55+555 = 615

val = input('give integer value\n')
intV1 = int(val) # 5
intV2 = int(val*2) # 55
intV3 = int(val*3) #555
print(f'The sum of {intV1} + {intV2} + {intV3} = {intV1+intV2+intV3}')