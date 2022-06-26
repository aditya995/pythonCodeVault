import math

intVal = 14
floatVal = 7.02
strVal = 'ff'
# Not an integer division
print(f'29 / 14 => {29 / 14}')
print(f'intVal / floatVal => {intVal / floatVal}')
# Integer division
print(f'30 // 2 => {30//2}')

# round, math.floor, math.ceil
print(f'\nround(14.6) => {round(14.6)}')
print(f'round(14.2) => {round(14.2)}')
print(f'math.ceil(14.5) => {math.ceil(14.5)}')
print(f'math.ceil(14.2) => {math.ceil(14.2)}')
print(f'math.floor(14.5) => {math.floor(14.5)}')
print(f'math.floor(14.2) => {math.floor(14.2)}\n')

# sqrt, cuberoot, **, pow, absolute, factorial, isfinite, e^x, log(Base e), log2(Base 2), log10(Base 10)
print (f'2**3 => {2**3}')
print (f'pow(2,3) => {pow(2,3)}\n')

print (f'8**(1/3) => {8**(1/3)} # Must use () in the power part!') 
print (f'pow(8,1/3) => {pow(8,1/3)}')
print (f'math.pow(2,3) => {math.pow(2,3)}\n')
print (f'math.sqrt(64) => {math.sqrt(64)}\n')
print (f'math.fabs(-64) => {math.fabs(-64)}\n') # absolute value
print (f'math.factorial(4) => {math.factorial(4)}\n')
print (f'math.isfinite(-451654648452135468131874131543184354316836541687543168486) => {math.isfinite(-451654648452135468131874131543184354316836541687543168486)}\n')
print (f'math.exp(4) => {math.exp(1)}') # e^x
print('math.log(2.718281828459045) => ', {math.log(2.718281828459045)})
print('math.log2(2) => ', {math.log2(2)})
print('math.log10(10) => ', {math.log10(10)})

# Degree and Radians
print(f'math.degrees(1.5707963267948966) => {math.degrees(1.5707963267948966)}')
print(f'math.radians(90) => {math.radians(90)}')

print(f'math.sin(1.5707963267948966) => {math.sin(1.5707963267948966)}')
print(f'math.cos(0) => {math.cos(0)}')
print(f'math.tan(0.7853981633974483) => {round(math.tan(0.7853981633974483))}')

print(f'PI {math.pi}')
print(f'tau {math.tau}')
print(f'e {math.e}')
