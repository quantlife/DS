
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('abcd'))
print df
df1 = pd.DataFrame([[0.25,0.25,0.5,0.5]])
print df1
df1 = df1.T.iloc[:, 0]
print df1
df = df.mul(df1.values, axis=1)
print df
portfolio = df.sum()
print type(portfolio)
