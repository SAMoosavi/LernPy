a = 20
b = 10

if a > b:  # -> T
    print("a is greater than b")

if a > b: print("a is greater than b")

if a < b:  # -> F
    print("a is less than b")
elif a == b:  # -> F
    print("a is equal to b")
else:  # -> so run it
    print("a is greater than b")

if a > 10:  # -> T
    print("a is greater than 10")
elif a > 5:  # -> not check
    print("a is greater than 5")
elif a > 0:  # -> not check
    print("a is greater than 0")
elif a == 0:  # -> not check
    print("a is equal to 0")
else:  # -> not check
    print("a is less than 0")

c = 0
if a > b:
    c = a
else:
    c = b
print(c)  # -> 20

c = a if a > b else b
print(c)  # -> 20

if a > 10:  # -> T
    if b < a:  # -> T
        print("b is less than a, and a is greater than 10")
    elif b > a:
        print("b is greater than a, and a is greater than 10")
    else:
        print("b is equal than a, and a is greater than 10")
else:
    if b < a:
        print("b is less than a, and a isn't greater than 10")
    elif b > a:
        print("b is greater than a, and a isn't greater than 10")
    else:
        print("b is equal than a, and a isn't greater than 10")
