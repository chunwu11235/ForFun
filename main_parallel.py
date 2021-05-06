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
elapse, _ = run_sleepers(n)


# popen is non-blocking
@timer
def popen_sleepers(n):
    sleepers = []
    for _ in range(n):
        sleepers.append(subprocess.Popen(('sleep', '1')))

elapse2, _ = popen_sleepers(n)