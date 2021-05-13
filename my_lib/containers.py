import abc
from collections.abc import Iterator

def generator(n):
    for i in range(n):
        yield i

class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        while self.items:
            try:
                yield self.items.pop()
            except IndexError:
                raise StopIteration

     

class MyIterableBase(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        pass


class MyIterable(MyIterableBase):
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return MyIterator(self.n)

class MyIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a1 = 0
        self.a2 = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            self.a1, self.a2 = self.a2, self.a1 + self.a2
            return self.a1
        else:
            raise StopIteration




def playground():
    s = Stack()
    for i in range(10):
        s.add(i)

    for i in iter(s):
        print(i)

    print('----')
    my_iterable = MyIterable(10)
    print(*my_iterable)
    print(*my_iterable)
    assert not isinstance(my_iterable, Iterator)

    it1 = iter(my_iterable)
    print(*it1)
    assert isinstance(it1, Iterator) # duck typing
    
    it2 = iter(my_iterable)
    assert isinstance(it1, Iterator)
    
    try:
        print(next(it1))
    except StopIteration:
        print('--- Expected. Iterator can only be used once! ---')
    else:
        print('Should Not Come Here!')
    
    fibonacci = [i for i in it2]
    print(*fibonacci)


if __name__ == "__main__":
    playground()