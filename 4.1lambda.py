def add(a, b):
    return a + b


f = lambda a, b: a + b

print(f(1, 2))  # -> 3

"""
1
4
27
256
3125
46656
823543
16777216
387420489
"""
for i in map(lambda num: num ** num, range(10)):
    print(i)
