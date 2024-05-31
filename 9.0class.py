from dataclasses import dataclass


class A:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


print(A.__doc__)
print(A.i)
# print(A.f()) # TypeError: A.f() missing 1 required positional argument: 'self'
a = A()
print(a.__doc__)
print(a.i)
print(a.f())
a.i = 1
print(A.i)
print(a.i)

print('-' * 20)


class AA:
    i = []


aa1 = AA()
aa2 = AA()

aa1.i.append(1)
aa2.i.append(2)

print(aa1.i)
print(aa2.i)

print('-' * 20)


class B:
    def __init__(self):
        print("Hi, i'm B!!!!")
        self.i = 1


# print(B.i) # AttributeError: type object 'B' has no attribute 'i'
b = B()
print(b.i)

print('-' * 20)


class C:
    def __init__(self, name):
        self.name = name

    def f(self):
        print(self.name)


c = C('S.Ali')
c.f()

print('-' * 20)


class D:
    pass


d = D()
d.i = 1
print(d.i)
del d.i
# print(d.i) # AttributeError: 'D' object has no attribute 'i'

print('-' * 20)


class EP:
    def __init__(self):
        print("I'm EP!!")
        self.i = 0

    def print_i(self):
        print(self.i)


class ECH(EP):
    def __init__(self):
        print("My parrent is EP!!!")
        self.i = 10


e = ECH()
e.print_i()

print('-' * 20)


class FP:
    def __init__(self):
        print("I'm FP!!")
        self.i = 0

    def print_i(self):
        print(self.i)


class FCH(FP):
    def __init__(self):
        # FP.__init__()  # TypeError: FP.__init__() missing 1 required positional argument: 'self'
        FP.__init__(self)
        # super().__init__()
        print("My parrent is FP!!!")
        self.i = 10


f = FCH()
f.print_i()

print('-' * 20)


class G:
    def __init__(self):
        self.__i = 10

    def get_i(self):
        return self.__i


g = G()
# print(g.i)  # AttributeError: 'G' object has no attribute 'i'
# print(g.__i)  # AttributeError: 'G' object has no attribute '__i'
print(g.get_i())

print('-'*20)


@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)

print(john)
print(john.salary)