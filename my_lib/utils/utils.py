import functools
import datetime
import time

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

# decorator with args
# decorator_factory
def delay(second: float):
    """return a decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            print(f'--- delay {second} second ---')
            time.sleep(second)
            print(f'--- calling {func.__name__} ---')
            return second, func(*args, **kargs)
        return wrapper
    return decorator
        
        
def sleep(n):
    time.sleep(n)