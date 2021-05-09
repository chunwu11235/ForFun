import pytest
import time
import math
from my_lib.utils.utils import *
from unittest.mock import Mock

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

    
def test_counter():
    f = counter(hello)
    for i in range(1, 10):
        c, _ = f()
        assert c == i 
    

def test_repeat():
    mock = Mock(side_effect=lambda : None)
    f = repeat(5)(mock)
    f()

    assert mock.call_count == 5
    

def test_file_context_manager():
    try:
        with file_context_manager('requirements.txt', 'rb') as f:
            print(f'--- contextmanager decorator ---')
            # print(f1.readline())
            raise MyException
    except MyException:
        pass
    assert f.closed