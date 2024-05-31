a = input('please input your name:')
print(a)

a = input('please input your age:')
# print(2024 - a) # -> TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(2024 - int(a))

a = input('please input your full name:').split()
print(a)

a = [int(i) for i in input('please input multi number:').split()]
print(a)

a = list(map(int, input('please input multi number:').split()))
print(a)

a = input()
print(a)
