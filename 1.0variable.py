"""
definition:
    name: type = value

type is optional

name must be:
    1. just created by alphanumeric characters and underscores (A-Z a-z 0-9 _)
    2. can't start with number (0-9)
    3. can't be any of the Python keywords

name is case-sensitive

Legal:
    myvar
    my_var
    _my_var
    myVar
    MYVAR
    myvar2

Illegal:
    2myvar
    my-var
    my var
"""

x: int = 10
y = 10  # If we don't specify the type, Python guesses the type

# the print shows in to terminal
print(x, y)  # -> 10 10

# the type returns type of var
print(type(x), type(y))  # -> <class 'int'> <class 'int'>

# when many variables have the same value, you can simply write it once
x = y = 11
print(x, y)  # -> 11 11

"""
When there are many values stored in a container (list, tuple, ...),
and you want to assign each value to a variable, you can do so simply by writing it once
"""
x, y = (10, 11)
print(x, y)  # -> 10 11
