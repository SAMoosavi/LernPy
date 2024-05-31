# int ,float ,complex are types of numbers

a = 10
print(type(a))  # -> <class 'int'>

b = 10.0
print(type(b))  # -> <class 'float'>

b = 10.7
print(b, type(b))  # -> 10.7 <class 'float'>
b = int(b)
print(b, type(b))  # -> 10 <class 'int'>

c = a + b
print(c, type(c))  # -> 20.0 <class 'float'>

c = a + 10
print(c, type(c))  # -> 20 <class 'int'>

c = 5 + 10
print(c, type(c))  # -> 15 <class 'int'>

c = 5 * 10
print(c, type(c))  # -> 50 <class 'int'>

c = 10 / 6
print(c, type(c))  # -> 1.66667 <class 'float'>

c = 10 // 6
print(c, type(c))  # -> 1 <class 'int'>

c = 10 ** 5
print(c, type(c))  # -> 100000 <class 'int'>

c = 10 % 6
print(c, type(c))  # -> 4 <class 'int'>

x = 35e3
print(x, type(x))  # -> 35000.0 <class 'float'>
y = 12E4
print(y, type(y))  # -> 120000.0 <class 'float'>
z = -87.7e100
print(z, type(z))  # -> -8.77e+101 <class 'float'>

x = 3 + 5j
print(x, type(x))  # -> (3+5j) <class 'complex'>
y = 5j
print(y, type(y))  # -> 5j <class 'complex'>
z = -5j
print(z, type(z))  # -> (-0-5j) <class 'complex'>
