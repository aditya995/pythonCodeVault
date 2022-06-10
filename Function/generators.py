def gen(n):
    for i in (1, 2, 3, 4, 5, 6):
        yield i * n


for i in gen(5):
    print(i)
print(gen(2))
