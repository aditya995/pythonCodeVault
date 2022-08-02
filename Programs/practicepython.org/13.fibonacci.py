# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use functions. 

# Using generators *
def fibonacci(n):
    x, y = 1, 1
    if n >= 1:yield x
    if n >= 2:yield y
    for z in range(2, n):
        yield x + y
        x, y = y, x + y

n = int(input('how many fibonacci you need? '))
print([x for x in fibonacci(n)])