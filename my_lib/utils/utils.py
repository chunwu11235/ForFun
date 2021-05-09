import functools
import datetime
import time
from contextlib import contextmanager

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

class MyException(Exception):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class FileContextManager:
    """Old style context manager"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Prepareing resources')
        self.file = open(self.filename, self.mode)
        return self.file # return resources
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Realeasing resources')
        self.file.close() # release resource

@contextmanager
def file_context_manager(filename, mode):
    resource = open(filename, mode)
    try:
        yield resource # provide resource
    finally:
        resource.close()

# try:
#     with open('requirements.txt', 'rb') as f:
#         print(f'--- with ---')
#         print(f.readline())
#         raise MyException
# except MyException:
#     pass

# assert f.closed

# try:
#     with FileContextManager('rxt', 'rb') as f2:
#         print(f'--- old style manager ---')
#         print(f2.readline())
#         # raise MyException
# except MyException:
#     pass

# assert f2.closed # make sure the resource is released

