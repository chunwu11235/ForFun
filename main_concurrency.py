from threading import Thread, Lock
from my_lib.utils.utils import *

import queue

class MyThread(Thread):
    def __init__(self, callable, n_calls, *args, **kargs):
        super().__init__(*args, **kargs)
        self.callable = callable
        self.n_calls = n_calls
    
    def run(self):
        print(f'--- Calling {self.callable.__name__} {self.n_calls} times ---')
        for _ in range(self.n_calls):
            self.callable()

def demo_thread101():
    @delay(second=1)
    def say_hello_to(name):
        print(f'What\'s up! {name}')
    
    thread = Thread(target=say_hello_to, args=('Bro', ))
    thread.start()
    print(f'Yoyoyo!') # not blocking by say_hello_to
    thread.join() # block or not
    print(f'this is line is blocked by join()')



def demo_race_condition(n_thread=10, n_counts=1000000):
    f = counter(lambda: None)
    threads = [MyThread(f, n_counts) for i in range(n_thread)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    
    print(f'Actually called {f.__closure__[0].cell_contents}') # probably != n_thread * n_counts


class MyQueue(queue.Queue):
    END = object()
    
    def end(self):
        self.add(MyQueue.END)
    
    def __iter__(self):
        while self.qsize():
            item = self.get()
            if item is MyQueue.END:
                raise StopIteration
            else:
                yield item

class Job:
    id = 0
    def __init__(self):
        self._id = Job.id
        Job.id += 1
        self.done = False
    
    def work(self):
        self.done = True
    
    def is_done(self):
        return self.done == True

    def __repr__(self):
        return f'Job {self.id} done? {self.done}'


class Producer(Thread):
    def __init__(self, q: queue, n_jobs, **kargs):
        super().__init__(**kargs)
        self.q = q
        self.n_jobs = n_jobs
    
    def run(self):
        for _ in range(self.n_jobs):
            j = Job()
            # print(f'{self} is producing job {j}')
            self.q.put(j)
            print(f'{self} pushed job {j}')
            print(f'size of {self.q} is {self.q.qsize()}')


def demo_threading_with_queue():
    """the consumer producer pattern"""

    q = MyQueue(10)
    producers = [Producer(q, 100) for _ in range(5)]
    for p in producers:
        p.start()


    for p in producers:
        p.join()


def main():
    # demo_thread101()
    # print('----')
    # demo_race_condition()
    print('----')
    demo_threading_with_queue()


if __name__ == '__main__':
    main()

