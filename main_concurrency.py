from threading import Thread, Lock
from my_lib.utils.utils import *

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


def main():
    demo_thread101()
    print('----')
    demo_race_condition()


if __name__ == '__main__':
    main()

