import pytest
import time
import math
from my_lib.utils.utils import timer

@pytest.mark.parametrize("t,", [
    1,
    2,
])
def test_timer(t,):

    @timer
    def sleep(t):
        time.sleep(t)
        return t

    elapse, measured_elapse = sleep(t)
    print(elapse, measured_elapse)
    assert math.isclose(elapse, measured_elapse, abs_tol=0.01)