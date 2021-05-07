
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
                return
            
def playground():
    s = Stack()
    for i in range(10):
        s.add(i)

    for i in iter(s):
        print(i)
