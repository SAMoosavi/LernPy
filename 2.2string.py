a = 'hello world'
print(a, type(a))  # -> hello world <class 'str'>

b = "hello world"
print(b, type(b))  # -> hello world <class 'str'>

c = "hello \"world\""
print(c, type(c))  # -> hello "world" <class 'str'>

d = "hello\tworld"
print(d, type(d))  # -> hello   "world" <class 'str'>

e = """hello
world"""
print(e, type(e))  # -> hello
# world <class 'str'>

f = "hello world" * 2
print(f, type(f))  # -> hello worldhello world <class 'str'>

g = "hello" + "world"
print(g, type(g))  # -> helloworld <class 'str'>

h = "0123456789"
print(h[0])  # -> 0
print(h[1])  # -> 1
print(h[-1])  # -> 9
print(h[-2])  # -> 8

print(h[2:6])  # -> 2345
print(h[:6])  # -> 012345
print(h[2:])  # -> 23456789
print(h[2:6:2])  # -> 24
print(h[:6:2])  # -> 024
print(h[2::2])  # -> 2468
print(h[8:2:-1])  # -> 876543
print(h[:2:-1])  # -> 9876543
print(h[8::-1])  # -> 876543210
print(h[::-1])  # -> 9876543210

# h[1] = 'a'    # -> TypeError: 'str' object does not support item assignment

print(len(h))  # -> 10

n = 1
i = "my number:"
# print(i + n)  # -> TypeError: can only concatenate str (not "int") to str
print(i + str(n))  # -> my number:1

j = "my number:{}".format(n)
print(j)  # -> my number:1

j = f"my number:{n}"
print(j)  # -> my number:1

k = "seyyed ali moosavi"
print(k.capitalize())  # -> Seyyed ali moosavi
print(k.upper())  # -> SEYYED ALI MOOSAVI
print(k.find('o'))  # -> 12
print(k.count('o'))  # -> 2
print(k.rfind('o'))  # -> 13
print(k.replace('oo', 'ou'))  # -> seyyed ali mousavi
print(k.split())  # -> ['seyyed', 'ali', 'moosavi']
