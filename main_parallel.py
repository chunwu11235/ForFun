import subprocess
import math
from my_lib.utils.utils import timer

# run is blocking, i.e., run sequentially
@timer
def run_sleepers(n):
    sleepers = []
    for _ in range(n):
        sleepers.append(subprocess.run(('sleep', '1')))
    # return sleepers

n = 3
_, elapse = run_sleepers(n)
assert math.isclose(n, elapse, abs_tol=0.1)


