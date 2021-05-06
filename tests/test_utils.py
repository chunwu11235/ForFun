import time
from my_lib.utils.utils import timer

def test_timer():

    @timer
    def sleep(t):
        time.sleep(t)

    sleep(0.1)
    assert (1+1) == 2