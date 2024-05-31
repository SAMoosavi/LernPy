x = 10
print(type(x))  # -> <class 'int'>

x = 10.1
print(type(x))  # -> <class 'float'>

x = "hi"
print(type(x))  # -> <class 'str'>

x = True
print(type(x))  # -> <class 'bool'>

"""
somtime we want to change the type of var. like it:
    x = '10' we have a number but type of it is str
    for change the type of it to int use casting
    x = int(x) 
"""
x = '10'
print(type(x))  # -> <class 'str'>
x = int(x)
print(type(x))  # -> <class 'int'>

y: str = '10'
y = int(y)  # warning: Expected type 'str', got 'int' instead
print(type(y))  # -> <class 'int'>
