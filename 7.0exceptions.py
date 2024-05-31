try:
    a = 10 / 1
    print('no error')
except ZeroDivisionError:
    print("hi")
except (RuntimeError, TypeError, NameError):
    pass

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
    

try:
    raise ValueError
except ValueError:
    print("valuse error")

print('-'*20)
try:
    a = 10 / 0
except ZeroDivisionError as err:
    print("err: ",err)

try:
    raise NameError('HiThere')
except NameError as err:
    print('An exception flew by!',err.args)

print('-'*20)
try:
    print('hi')
except:
    print('err')
else:
    print('no err')


try:
    a = 10 / 0
except:
    print('err')
else:
    print('no err')

print('-'*20)
try:
    print('hi')
except:
    print('err')
finally:
    print('finally')

try:
    a = 10 / 0
except:
    print('err')
finally:
    print('finally')

print('-'*20)

try:
    try:
        a = 10 / 0
    except:
        print("error in nested!")
    
    b = 10 / 0
except:
    print("error in parent!")

print('-'*20)

class A(Exception):
    pass

try:
    raise A
except A:
    print("custom")