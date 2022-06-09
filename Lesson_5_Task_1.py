def num_gen(n, start = 0, step = 2):
    current = start-1
    n = n-1
    while current < n:
        current += step
        yield current

for i in num_gen(50):
    print(i)