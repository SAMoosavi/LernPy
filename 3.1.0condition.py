print(2 == 2)  # -> T
print(2 != 2)  # -> F
print(2 > 2)  # -> F
print(2 >= 2)  # -> T
print(2 < 2)  # -> F
print(2 <= 2)  # -> T

print(5 in [1, 2, 3])  # -> F
print(5 not in [1, 2, 3])  # -> T
print('a' in {'b': 5})  # -> F

print(2 > 4 and 3 == 5)  # -> F
print(0 > 5 and 5 >= 20)  # -> T
print(0 > 5 >= 20)  # -> T
print(2 > 4 or 3 != 5)  # -> T
print(not (2 > 4 and 3 == 5))  # -> T

print([1] is [1])  # -> F
a = [1]
b = a
print(a is b)  # -> T

print("" and "world")  # ->
print("hello" and "world")  # -> world
print("" or "world")  # -> world
print("hello" or "world")  # -> hello
