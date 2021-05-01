
a = [i for i in range(10)]
b = a # reference
assert a is b

c = a[:] # deep copy
assert c is not a
assert c == a

a[2:3] = list("something")
assert b == a
print(a)
print(b)

print(c)

#stride
n = [i for i in range(10)]
print(n[::2])
print(n[::-1])
print(n[3:7:3])
print(n[-3:1:1])
print(n[-3:1:-1])

n1 = n[::-1]
n1[0] = "test"
print(n1)
print(n)

# catch-all unpacking (*)
zero, *m, nine = tuple(n)
print(zero, m, nine)
first, second, *others = n
print(first, second, others)
# *all = n # error


names = ["Lisa", "Jane", "Annie", "Elizabeth"]
print(sorted(names, key=lambda name: (len(name), name.lower()), reverse=True))

print("\n")

def func(a, b=[]): # bad, the default argument only evaluate once when the function is defined
    return b

assert func(10) is func(20)
b_ref = func(1)
b_ref2 = func(1)
b_ref.append(1000)
print(b_ref2) # [1000]


# function decorator
import time
from functools import wraps

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kargs):
        print(f'calling {fn.__name__}({args!r}, {kargs!r}')
        start = time.time()
        res = fn(*args, **kargs)
        print(f'function call end')
        print(f'spent {start-time.time():.6f}\n')
        return res
    return wrapper


@timer
def factorial(n: int) -> int:
    """
    this is to test docstring
    """
    if n < 0:
        raise ValueError(f'input cannot be negative')
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(4))
# print(factorial(-1))

print(factorial)
print(help(factorial))
# help(factorial)
    

