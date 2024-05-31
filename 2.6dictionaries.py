a = {'a': 1, 'b': 2, 'c': 3}
print(a, type(a))  # -> {'a': 1, 'b': 2, 'c': 3} <class 'dict'>

print(a['a'])  # -> 1

b = {'a': 1, 'b': 2, 'c': 3, 'c': 4}  # warning: Dictionary contains duplicate keys 'c'
print(b)  # -> {'a': 1, 'b': 2, 'c': 4}

c = dict(a=1, b=2, c=3, d=4)
print(c)  # -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys = c.keys()
print(keys)  # -> dict_keys(['a', 'b', 'c', 'd'])

values = c.values()
print(values)  # -> dict_values([1, 2, 3, 4])

items = c.items()
print(items)  # -> dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

c['e'] = 5
print(c)
print(keys)  # -> dict_keys(['a', 'b', 'c', 'd', 'e])
print(values)  # -> dict_values([1, 2, 3, 4, 5])
print(items)  # -> dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

c.pop('a')
print(c) # -> {'b': 2, 'c': 3, 'd': 4, 'e': 5}
