import numpy as np
import tensorflow as tf
from ForFun.lib_playground import myAdd



def main():
    print("tensorflow:", tf.__version__)
    print("numpy:", np.__version__)
    print(myAdd(10, 2))


if __name__ == "__main__":
    print("---main.py---")
    main()

