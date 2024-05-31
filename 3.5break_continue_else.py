a = "seyyed ali moosavi"
"""
s
e
y
y
e
d
a
l
i
m
o
o
s
a
v
i
"""
for i in a:
    if i == ' ':
        continue
    print(i)

"""
s
e
y
y
e
d
"""
for i in a:
    if i == ' ':
        break
    print(i)

"""
s
e
y
y
e
d
 
a
l
i
 
m
o
o
s
a
v
i
no break
"""
for i in a:
    if i == 'j':
        break
    print(i)
else:
    print("no break")

# s
for i in a:
    if i == 'e':
        break
    print(i)
else:
    print("no break")

"""
s
e
y
y
e
d
a
l
i
m
o
o
s
a
v
i
no break
"""
for i in a:
    if i == ' ':
        continue
    print(i)
else:
    print("no break")
