# ternary Operator

# msg if condition else msg
val = 6
flag = 3
print('val is 3') if val==3 else print('val is not 3')
print('val is 3') if not val!=3 else print('val is not 3')

str = f'range(1-10), not {flag}' if  val>1 and val<10 and not val==flag else 'False'
print(str)
