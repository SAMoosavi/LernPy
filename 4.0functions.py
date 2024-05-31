def summation(a, b):
    return a + b


print(summation(1, 2))  # -> 3


def summation2(a: int, b: int) -> int:
    return a + b


print(summation2(1, 2.2))  # -> warning: Expected type 'int', got 'float' instead # -> 3.2


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 1 1 2 3 5
print(fib(4))  # -> 3
f = fib
print(f(5))  # -> 5


def logger(msg, file_name="log.txt"):
    print(f"the msg written to {file_name}: {msg}")


logger("Hello World")  # -> the msg written to log.txt: Hello World
logger("Hello World", "my_log.txt")  # -> the msg written to my_log.txt: Hello World

logger(msg="hi")  # -> the msg written to log.txt: hi

print("Hello", "world", sep=" ", end=" bye bye\n")  # -> Hello world bye bye


def summation3(*numbers):  # -> sum
    ans = 0
    for number in numbers:
        ans += number
    return ans

print(summation3(1, 2, 3))  # -> 6


def logger2(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}", end=" ** ")
    print()


logger2(error="err", warning="warn")  # -> error: err ** warning: warn **


def my_function():
    """my doc"""
    pass


print(my_function.__doc__)  # -> my doc

"""
Prints the values to a stream, or to sys.stdout by default.

  sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout.
  flush
    whether to forcibly flush the stream.
"""
print(print.__doc__)


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print(power(5, 6))  # -> 15625
