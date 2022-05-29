# break to stop the loop

for i in range(10):
    if(i == 3): break
    print(i, end=', ')
print()

# continue jump to the end of the block
for i in range(10):
    if(i == 3): continue
    print(i, end=', ')
print()

# pass to fill up empty block
for i in range(10):
    if(i%2 == 0): 
        pass
    else:
        print(i, end=', ')
print()
