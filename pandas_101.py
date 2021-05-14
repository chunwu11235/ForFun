import pandas as pd
import numpy as np

s = pd.Series(np.arange(10), index=[ chr(i + ord('a')) for i in range(10)])
print(s)
print(s.index)

print(s[['a', 'd', 'e']])

d = { e: i for i, e in enumerate(['Andy', 'Bob', 'Calvin', 'Emma'])}
s2 = pd.Series(d) # from dict
print(s2)

s3 = pd.Series(d, index=list(d.keys()) + ['John'])
print(s3)
s3.isna()


# datafrom
name = ['Andy', 'Bob', 'Chris']
age = [10,20,30]
job = ['SDE', 'Quant', 'Trader']

e1 = pd.DataFrame({'name':name, 'age':age}) # dict for columns

e2 = pd.DataFrame({'age':age, 'job':job}, columns=['age', 'job'], index=name)
e2.head()

e2.columns
e2['age']
e2.loc['Andy']
e2['new column'] = 1
e2['new column 2'] = pd.Series([1,2], index=['Andy', 'Bob'])

e2.columns.name = 'field'
e2.index.name = 'name'
e2

arr = e2.values # np ndarray
print(type(arr))

assert pd.DataFrame(np.arange(10).reshape(2,5)).shape == (2,5) # row by row


# reordering with loc
e2_reordered = e2.loc[['Bob', 'Andy'], ['new column', 'age']]


e2.mean(axis=0)
e2.mean(axis='index')


e3 = pd.DataFrame(np.random.rand(*e2.shape), columns=e2.columns, index=e2.index)
new_index = ['Andy', 'Bob', 'Leo']

e3_copy = e3.copy()
e3_copy.index = new_index

e3 + e3_copy # pay attention to the result

e3_applied = e3.apply(lambda x : min(x), axis='index') # on rows or columns
np.round(e3, 2) # np ufuncs


e3_sorted = e3.sort_index(axis='columns', ascending=False)

e3.sort_values(by=['age', 'job'])

e3.describe()

e3.pct_change()