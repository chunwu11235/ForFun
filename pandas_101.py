import pandas as pd
import numpy as np

s = pd.Series(np.arange(10), index=[ chr(i + ord('a')) for i in range(10)])
print(s)
print(s.index)

print(s[['a', 'd', 'e']])
