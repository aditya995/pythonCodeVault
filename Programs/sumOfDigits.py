# Sum of digits without loop

val = input('Give valid integer input\n')
len = len(val)
out = int(val[len-1])
if(len > 1):out = out + int(val[len-2])
if(len > 2):out = out + int(val[len-3])
if(len > 3):out = out + int(val[len-4])
if(len > 5):out = out + int(val[len-5])
print(out)