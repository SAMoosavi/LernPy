a = {1, 2, 5, 5, 4}
print(a, type(a))  # -> {1, 2, 4, 5} <class 'set'>

a.add(3)
print(a)  # -> {1, 2, 3, 4, 5}

# print(a[0])  # -> TypeError: 'set' object is not subscriptable

b = {'hi', 5, False, True}
print(b)  # doesn't correct sort

# print(a + b)  # -> TypeError: unsupported operand type(s) for +: 'set' and 'set'

a.update({1, 2, 0})
print(a)  # -> {0, 1, 2, 3, 4, 5}

a.remove(5)
a.discard(4)
print(a)  # -> {0, 1, 2, 3}

# a.remove(6) # -> KeyError: 6
a.discard(6)
print(a)  # -> {0, 1, 2, 3}
