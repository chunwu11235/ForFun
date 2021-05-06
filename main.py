import subprocess

from my_lib.utils.utils import timer

@timer
def sleep():
    subprocess.run(('sleep', '1'))


sleep()