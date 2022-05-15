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

# sqrt, cuberoot, **, pow
print (f'2**3 => {2**3}')
print (f'pow(2,3) => {pow(2,3)}\n')

print (f'8**(1/3) => {8**(1/3)} # Must use () in the power part!') 
print (f'pow(8,1/3) => {pow(8,1/3)}')
print (f'math.sqrt(64) => {math.sqrt(64)}\n')