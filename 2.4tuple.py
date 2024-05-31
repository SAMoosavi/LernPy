a = (1, 'hello')
print(a, type(a))  # -> (1, 'hello') <class 'tuple'>

b = (10)
print(b, type(b))  # -> 10 <class 'int'>

c = 1, 2
print(c, type(c))  # -> (1, 2) <class 'tuple'>

list_a = list(a)
print(list_a, type(list_a))  # -> [1, 'hello'] <class 'list'>

print(a[0])  # -> 1
# a[0] = 'hi' # TypeError: 'tuple' object does not support item assignment
