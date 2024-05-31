"""
1
2
3
4
5
6
7
8
9
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    print(i)

"""
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
"""
for i, j in enumerate(a):
    print(i, j)

"""
a
b
c
d
"""
b = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in b:
    print(i)

"""
1
2
3
4
"""
for i in b.values():
    print(i)

"""
a 1
b 2
c 3
d 4
"""
for i, j in b.items():
    print(i, j)

"""
1 10
2 20
3 30
4 40
5 50
6 60
7 70
8 80
9 90
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for i, j in zip(a, b):
    print(i, j)

c = []
for i in range(10):
    c.append(i ** 2)
print(c)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

c = [i ** 2 for i in range(10)]
print(c)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
