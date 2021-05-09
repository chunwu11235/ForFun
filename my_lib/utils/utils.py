import functools
import datetime
import time

def sleep(n):
    time.sleep(n)

def hello():
    print(f'Hello!')

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print(f'--- Calling {func.__name__} ---')
        start = datetime.datetime.now()
        res = func(*args, **kargs)
        elapse = (datetime.datetime.now() - start)
        print(f'---- Took {elapse} ---')
        return elapse.total_seconds(), res
    return wrapper

def counter(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        nonlocal count
        count += 1
        return count, func(*args, **kargs)
    return wrapper

# decorator with args
# decorator_factory
def delay(second: float):
    """return a decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            print(f'--- calling {func.__name__} with delay {second} second ---')
            time.sleep(second)
            
            return second, func(*args, **kargs)
        return wrapper
    return decorator
        

def repeat(n: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            res = [func(*args, **kargs) for _ in range(n)]
            return res
        return wrapper
    return decorator    