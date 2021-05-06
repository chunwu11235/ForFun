import functools
import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print(f'--- Calling {func.__name__} ---')
        start = datetime.datetime.now()
        res = func(*args, **kargs)
        elapse = (datetime.datetime.now() - start)
        print(f'---- Took {elapse} ---')
        return res
    return wrapper

