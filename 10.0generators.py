def my_range(start, end, step=1):
    i = start
    while i < end:
        yield i
        i += step


for i in my_range(1, 100, 5):
    print(i)
