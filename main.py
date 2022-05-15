# int('number string with correct format', corresponding base of the string)
print('# Converts any number to decimal')

print(int('0x19', 16))
print(int("0o15", 8))
print(int("0b10100", 2))

print('\n# From decimal to hex(), oct(), bin()')
print(hex(25))
print(oct(15))
print(bin(20))

print('\n# Converting any number system to other')
binNum = bin(int('0x19', 16))
print(f'Hexadecimal(0x19) to Binary => {binNum}')

hexNum = hex(int('0b1010', 2))
print(f'Binary(0b1010) to Hexadecimal => {hexNum}')
