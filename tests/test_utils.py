import pytest
import time
import math
from my_lib.utils.utils import *

@pytest.mark.parametrize("t,", [
    1,
    2,
])
def test_timer(t,):

    @timer
    def sleep(t):
        time.sleep(t)
        return t

    measured_elapse, elapse, = sleep(t)
    print(measured_elapse, elapse)
    assert math.isclose(elapse, measured_elapse, abs_tol=0.01)

@pytest.mark.parametrize("t,", [0.5,1,])
def test_delay(t):

    @delay(second=t)
    def hello():
        print('Hello!')

    second, _ = hello()
    assert math.isclose(second, t, abs_tol=0.01)

    
