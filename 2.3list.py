# list is a container

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, type(a))  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

b = list([0, 1, 2, 3, 4])
print(b, type(b))  # -> [0, 1, 2, 3, 4] <class 'list'>

print(b[0])  # -> 0
print(b[-1])  # -> 4
print(b[2:])  # -> [2, 3, 4]
b[0] = -1
print(b)  # -> [-1, 1, 2, 3, 4]
b[0] = 0
print(len(b))  # -> 5

c = b + [5, 6, 7, 8, 9]
print(c)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

d = b * 2
print(d)  # -> [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

b.append(5)
print(b)  # -> [0, 1, 2, 3, 4, 5]

e = b
print(id(e), id(b))  # -> it prints two same number
e.append(6)
print(e, b)  # -> [0, 1, 2, 3, 4, 5, 6] [0, 1, 2, 3, 4, 5, 6]

f = b.copy()  # you can write f = b[:]
print(id(f), id(b))  # -> it prints two different number
f.append(7)
print(f, b)  # -> [0, 1, 2, 3, 4, 5, 6, 7] [0, 1, 2, 3, 4, 5, 6]

f.append('hi')  # warning: Expected type 'int' (matched generic type '_T'), got 'str' instead
print(f)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 'hi']

g = [a, b]
print(g)  # -> [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6]]
print(g[0])  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(g[1][2])  # -> 2
g[1][2] = 10
print(b)  # -> [0, 1, 10, 3, 4, 5, 6]
g[1][2] = 2

print(a.pop())  # -> 9
print(a)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(a.pop(3))  # -> 3
print(a)  # -> [0, 1, 2, 4, 5, 6, 7, 8]

a.insert(3, 3)
print(a)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8]

a.remove(8)
print(a)  # -> [0, 1, 2, 3, 4, 5, 6, 7]

del a[3]
print(a)  # -> [0, 1, 2, 4, 5, 6, 7]

a.clear()
print(a)  # -> []

a = [1, 5, 0, 6, 9, 2, 1, 3]
print(a)  # -> [1, 5, 0, 6, 9, 2, 1, 3]
a.sort()
print(a)  # -> [0, 1, 1, 2, 3, 5, 6, 9]
