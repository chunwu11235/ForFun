from threading import Thread, Lock
from my_lib.utils.utils import *
import time

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
        self.put(MyQueue.END)

class Job:
    id = 0
    lock = Lock()
    def __init__(self):
        with Job.lock:
            self._id = Job.id
            Job.id += 1
        self.done = False
    
    def work(self):
        self.done = True
    
    def is_done(self):
        return self.done == True

    def __repr__(self):
        return f'Job {self._id} done? {self.done}'

class Producer(Thread):
    def __init__(self, q: queue, n_jobs, **kargs):
        super().__init__(**kargs)
        self.q = q
        self.n_jobs = n_jobs
    
    def run(self):
        for i in range(self.n_jobs):
            if i % 3 == 0:
                time.sleep(1)
            j = Job()
            # print(f'{self} is producing job {j}')
            self.q.put(j)
            print(f'{self} pushed {j}')

class Consumer(Thread):
    def __init__(self, q, ls,**kargs):
        super().__init__(**kargs)
        self.q = q
        self.ls = ls
    
    def run(self):
        i = 0
        while True:
            i += 1
            if i % 5 == 0:
                time.sleep(1)
            job = self.q.get()
            if job == MyQueue.END:
                self.q.task_done()
                break
            else:
                job.work()
                print(f'{self} finished {job}')
                self.ls.append(job)
                self.q.task_done()
        return
                
 
def demo_threading_with_queue():
    """the consumer producer pattern"""

    q = MyQueue(10)
    ls = []
    producers = [Producer(q, 50) for _ in range(3)]
    for p in producers:
        p.start()
    
    consumers = [Consumer(q, ls) for _ in range(3)]
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    
    # for _ in consumers:
    #     q.end()
    q.join()

    assert len(ls) == 150
    # ls.sort(key=lambda j: j.id)
    seen = set()
    for j in ls:
        assert j._id not in seen
        seen.add(j._id)
        assert j.is_done
        print(f'{j}')
    
    print(f'---- END ----')


def main():
    # demo_thread101()
    # print('----')
    # demo_race_condition()
    print('----')
    demo_threading_with_queue()


if __name__ == '__main__':
    main()

